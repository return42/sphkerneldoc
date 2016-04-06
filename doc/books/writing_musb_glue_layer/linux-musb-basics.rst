
.. _linux-musb-basics:

=================
Linux MUSB Basics
=================

To get started on the topic, please read USB On-the-Go Basics (see Resources) which provides an introduction of USB OTG operation at the hardware level. A couple of wiki pages by
Texas Instruments and Analog Devices also provide an overview of the Linux kernel MUSB configuration, albeit focused on some specific devices provided by these companies. Finally,
getting acquainted with the USB specification at USB home page may come in handy, with practical instance provided through the Writing USB Device Drivers documentation (again, see
Resources).

Linux USB stack is a layered architecture in which the MUSB controller hardware sits at the lowest. The MUSB controller driver abstract the MUSB controller hardware to the Linux
USB stack.


.. code-block:: c

          ------------------------
          |                      | <------- drivers/usb/gadget
          | Linux USB Core Stack | <------- drivers/usb/host
          |                      | <------- drivers/usb/core
          ------------------------
                     ⬍
         --------------------------
         |                        | <------ drivers/usb/musb/musb_gadget.c
         | MUSB Controller driver | <------ drivers/usb/musb/musb_host.c
         |                        | <------ drivers/usb/musb/musb_core.c
         --------------------------
                     ⬍
      ---------------------------------
      | MUSB Platform Specific Driver |
      |                               | <-- drivers/usb/musb/jz4740.c
      |       aka "Glue Layer"        |
      ---------------------------------
                     ⬍
      ---------------------------------
      |   MUSB Controller Hardware    |
      ---------------------------------

As outlined above, the glue layer is actually the platform specific code sitting in between the controller driver and the controller hardware.

Just like a Linux USB driver needs to register itself with the Linux USB subsystem, the MUSB glue layer needs first to register itself with the MUSB controller driver. This will
allow the controller driver to know about which device the glue layer supports and which functions to call when a supported device is detected or released; remember we are talking
about an embedded controller chip here, so no insertion or removal at run-time.

All of this information is passed to the MUSB controller driver through a platform_driver structure defined in the glue layer as:


.. code-block:: c

    static struct platform_driver jz4740_driver = {
        .probe      = jz4740_probe,
        .remove     = jz4740_remove,
        .driver     = {
            .name   = "musb-jz4740",
        },
    };

The probe and remove function pointers are called when a matching device is detected and, respectively, released. The name string describes the device supported by this glue layer.
In the current case it matches a platform_device structure declared in arch/mips/jz4740/platform.c. Note that we are not using device tree bindings here.

In order to register itself to the controller driver, the glue layer goes through a few steps, basically allocating the controller hardware resources and initialising a couple of
circuits. To do so, it needs to keep track of the information used throughout these steps. This is done by defining a private jz4740_glue structure:


.. code-block:: c

    struct jz4740_glue {
        struct device           *dev;
        struct platform_device  *musb;
        struct clk      *clk;
    };

The dev and musb members are both device structure variables. The first one holds generic information about the device, since it's the basic device structure, and the latter holds
information more closely related to the subsystem the device is registered to. The clk variable keeps information related to the device clock operation.

Let's go through the steps of the probe function that leads the glue layer to register itself to the controller driver.

N.B.: For the sake of readability each function will be split in logical parts, each part being shown as if it was independent from the others.


.. code-block:: c

    static int jz4740_probe(struct platform_device *pdev)
    {
        struct platform_device      *musb;
        struct jz4740_glue      *glue;
        struct clk                      *clk;
        int             ret;

        glue = devm_kzalloc(&pdev->dev, sizeof(*glue), GFP_KERNEL);
        if (!glue)
            return -ENOMEM;

        musb = platform_device_alloc("musb-hdrc", PLATFORM_DEVID_AUTO);
        if (!musb) {
            dev_err(&pdev->dev, "failed to allocate musb devicen");
            return -ENOMEM;
        }

        clk = devm_clk_get(&pdev->dev, "udc");
        if (IS_ERR(clk)) {
            dev_err(&pdev->dev, "failed to get clockn");
            ret = PTR_ERR(clk);
            goto err_platform_device_put;
        }

        ret = clk_prepare_enable(clk);
        if (ret) {
            dev_err(&pdev->dev, "failed to enable clockn");
            goto err_platform_device_put;
        }

        musb->dev.parent     = &pdev->dev;

        glue->dev            = &pdev->dev;
        glue->musb           = musb;
        glue->clk            = clk;

        return 0;

    err_platform_device_put:
        platform_device_put(musb);
        return ret;
    }

The first few lines of the probe function allocate and assign the glue, musb and clk variables. The GFP_KERNEL flag (line 8) allows the allocation process to sleep and wait for
memory, thus being usable in a blocking situation. The PLATFORM_DEVID_AUTO flag (line 12) allows automatic allocation and management of device IDs in order to avoid device
namespace collisions with explicit IDs. With devm_clk_get() (line 18) the glue layer allocates the clock -- the ``devm_`` prefix indicates that clk_get() is managed: it
automatically frees the allocated clock resource data when the device is released -- and enable it.

Then comes the registration steps:


.. code-block:: c

    static int jz4740_probe(struct platform_device *pdev)
    {
        struct musb_hdrc_platform_data  *pdata = &jz4740_musb_platform_data;

        pdata->platform_ops      = &jz4740_musb_ops;

        platform_set_drvdata(pdev, glue);

        ret = platform_device_add_resources(musb, pdev->resource,
                            pdev->num_resources);
        if (ret) {
            dev_err(&pdev->dev, "failed to add resourcesn");
            goto err_clk_disable;
        }

        ret = platform_device_add_data(musb, pdata, sizeof(*pdata));
        if (ret) {
            dev_err(&pdev->dev, "failed to add platform_datan");
            goto err_clk_disable;
        }

        return 0;

    err_clk_disable:
        clk_disable_unprepare(clk);
    err_platform_device_put:
        platform_device_put(musb);
        return ret;
    }

The first step is to pass the device data privately held by the glue layer on to the controller driver through platform_set_drvdata() (line 7). Next is passing on the device
resources information, also privately held at that point, through platform_device_add_resources() (line 9).

Finally comes passing on the platform specific data to the controller driver (line 16). Platform data will be discussed in :ref:`Chapter 4 <device-platform-data>`, but here we
are looking at the platform_ops function pointer (line 5) in musb_hdrc_platform_data structure (line 3). This function pointer allows the MUSB controller driver to know which
function to call for device operation:


.. code-block:: c

    static const struct musb_platform_ops jz4740_musb_ops = {
        .init       = jz4740_musb_init,
        .exit       = jz4740_musb_exit,
    };

Here we have the minimal case where only init and exit functions are called by the controller driver when needed. Fact is the JZ4740 MUSB controller is a basic controller, lacking
some features found in other controllers, otherwise we may also have pointers to a few other functions like a power management function or a function to switch between OTG and
non-OTG modes, for instance.

At that point of the registration process, the controller driver actually calls the init function:


.. code-block:: c

    static int jz4740_musb_init(struct musb *musb)
    {
        musb->xceiv = usb_get_phy(USB_PHY_TYPE_USB2);
        if (!musb->xceiv) {
            pr_err("HS UDC: no transceiver configuredn");
            return -ENODEV;
        }

        /* Silicon does not implement ConfigData register.
         * Set dyn_fifo to avoid reading EP config from hardware.
         */
        musb->dyn_fifo = true;

        musb->isr = jz4740_musb_interrupt;

        return 0;
    }

The goal of jz4740_musb_init() is to get hold of the transceiver driver data of the MUSB controller hardware and pass it on to the MUSB controller driver, as usual. The
transceiver is the circuitry inside the controller hardware responsible for sending/receiving the USB data. Since it is an implementation of the physical layer of the OSI model,
the transceiver is also referred to as PHY.

Getting hold of the MUSB PHY driver data is done with usb_get_phy() which returns a pointer to the structure containing the driver instance data. The next couple of instructions
(line 12 and 14) are used as a quirk and to setup IRQ handling respectively. Quirks and IRQ handling will be discussed later in :ref:`Chapter 5 <device-quirks>` and
:ref:`Chapter 3 <handling-irqs>`.


.. code-block:: c

    static int jz4740_musb_exit(struct musb *musb)
    {
        usb_put_phy(musb->xceiv);

        return 0;
    }

Acting as the counterpart of init, the exit function releases the MUSB PHY driver when the controller hardware itself is about to be released.

Again, note that init and exit are fairly simple in this case due to the basic set of features of the JZ4740 controller hardware. When writing an musb glue layer for a more complex
controller hardware, you might need to take care of more processing in those two functions.

Returning from the init function, the MUSB controller driver jumps back into the probe function:


.. code-block:: c

    static int jz4740_probe(struct platform_device *pdev)
    {
        ret = platform_device_add(musb);
        if (ret) {
            dev_err(&pdev->dev, "failed to register musb devicen");
            goto err_clk_disable;
        }

        return 0;

    err_clk_disable:
        clk_disable_unprepare(clk);
    err_platform_device_put:
        platform_device_put(musb);
        return ret;
    }

This is the last part of the device registration process where the glue layer adds the controller hardware device to Linux kernel device hierarchy: at this stage, all known
information about the device is passed on to the Linux USB core stack.


.. code-block:: c

    static int jz4740_remove(struct platform_device *pdev)
    {
        struct jz4740_glue  *glue = platform_get_drvdata(pdev);

        platform_device_unregister(glue->musb);
        clk_disable_unprepare(glue->clk);

        return 0;
    }

Acting as the counterpart of probe, the remove function unregister the MUSB controller hardware (line 5) and disable the clock (line 6), allowing it to be gated.
