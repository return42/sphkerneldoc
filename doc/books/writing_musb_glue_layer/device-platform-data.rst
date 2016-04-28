.. -*- coding: utf-8; mode: rst -*-

.. _device-platform-data:

====================
Device Platform Data
====================

In order to write an MUSB glue layer, you need to have some data
describing the hardware capabilities of your controller hardware, which
is called the platform data.

Platform data is specific to your hardware, though it may cover a broad
range of devices, and is generally found somewhere in the arch/
directory, depending on your device architecture.

For instance, platform data for the JZ4740 SoC is found in
arch/mips/jz4740/platform.c. In the platform.c file each device of the
JZ4740 SoC is described through a set of structures.

Here is the part of arch/mips/jz4740/platform.c that covers the USB
Device Controller (UDC):


.. code-block:: c

    /* USB Device Controller */
    struct platform_device jz4740_udc_xceiv_device = {
        .name = "usb_phy_gen_xceiv",
        .id   = 0,
    };

    static struct resource jz4740_udc_resources[] = {
        [0] = {
            .start = JZ4740_UDC_BASE_ADDR,
            .end   = JZ4740_UDC_BASE_ADDR + 0x10000 - 1,
            .flags = IORESOURCE_MEM,
        },
        [1] = {
            .start = JZ4740_IRQ_UDC,
            .end   = JZ4740_IRQ_UDC,
            .flags = IORESOURCE_IRQ,
            .name  = "mc",
        },
    };

    struct platform_device jz4740_udc_device = {
        .name = "musb-jz4740",
        .id   = -1,
        .dev  = {
            .dma_mask          = &jz4740_udc_device.dev.coherent_dma_mask,
            .coherent_dma_mask = DMA_BIT_MASK(32),
        },
        .num_resources = ARRAY_SIZE(jz4740_udc_resources),
        .resource      = jz4740_udc_resources,
    };

The jz4740_udc_xceiv_device platform device structure (line 2)
describes the UDC transceiver with a name and id number.

At the time of this writing, note that "usb_phy_gen_xceiv" is the
specific name to be used for all transceivers that are either built-in
with reference USB IP or autonomous and doesn't require any PHY
programming. You will need to set CONFIG_NOP_USB_XCEIV=y in the
kernel configuration to make use of the corresponding transceiver
driver. The id field could be set to -1 (equivalent to
PLATFORM_DEVID_NONE), -2 (equivalent to PLATFORM_DEVID_AUTO) or
start with 0 for the first device of this kind if we want a specific id
number.

The jz4740_udc_resources resource structure (line 7) defines the UDC
registers base addresses.

The first array (line 9 to 11) defines the UDC registers base memory
addresses: start points to the first register memory address, end points
to the last register memory address and the flags member defines the
type of resource we are dealing with. So IORESOURCE_MEM is used to
define the registers memory addresses. The second array (line 14 to 17)
defines the UDC IRQ registers addresses. Since there is only one IRQ
register available for the JZ4740 UDC, start and end point at the same
address. The IORESOURCE_IRQ flag tells that we are dealing with IRQ
resources, and the name "mc" is in fact hard-coded in the MUSB core in
order for the controller driver to retrieve this IRQ resource by
querying it by its name.

Finally, the jz4740_udc_device platform device structure (line 21)
describes the UDC itself.

The "musb-jz4740" name (line 22) defines the MUSB driver that is used
for this device; remember this is in fact the name that we used in the
jz4740_driver platform driver structure in
:ref:`Chapter 2 <linux-musb-basics>`. The id field (line 23) is set to
-1 (equivalent to PLATFORM_DEVID_NONE) since we do not need an id for
the device: the MUSB controller driver was already set to allocate an
automatic id in :ref:`Chapter 2 <linux-musb-basics>`. In the dev field
we care for DMA related information here. The dma_mask field (line 25)
defines the width of the DMA mask that is going to be used, and
coherent_dma_mask (line 26) has the same purpose but for the
alloc_coherent DMA mappings: in both cases we are using a 32 bits mask.
Then the resource field (line 29) is simply a pointer to the resource
structure defined before, while the num_resources field (line 28) keeps
track of the number of arrays defined in the resource structure (in this
case there were two resource arrays defined before).

With this quick overview of the UDC platform data at the arch/ level now
done, let's get back to the MUSB glue layer specific platform data in
drivers/usb/musb/jz4740.c:


.. code-block:: c

    static struct musb_hdrc_config jz4740_musb_config = {
        /* Silicon does not implement USB OTG. */
        .multipoint = 0,
        /* Max EPs scanned, driver will decide which EP can be used. */
        .num_eps    = 4,
        /* RAMbits needed to configure EPs from table */
        .ram_bits   = 9,
        .fifo_cfg = jz4740_musb_fifo_cfg,
        .fifo_cfg_size = ARRAY_SIZE(jz4740_musb_fifo_cfg),
    };

    static struct musb_hdrc_platform_data jz4740_musb_platform_data = {
        .mode   = MUSB_PERIPHERAL,
        .config = &jz4740_musb_config,
    };

First the glue layer configures some aspects of the controller driver
operation related to the controller hardware specifics. This is done
through the jz4740_musb_config musb_hdrc_config structure.

Defining the OTG capability of the controller hardware, the multipoint
member (line 3) is set to 0 (equivalent to false) since the JZ4740 UDC
is not OTG compatible. Then num_eps (line 5) defines the number of USB
endpoints of the controller hardware, including endpoint 0: here we have
3 endpoints + endpoint 0. Next is ram_bits (line 7) which is the width
of the RAM address bus for the MUSB controller hardware. This
information is needed when the controller driver cannot automatically
configure endpoints by reading the relevant controller hardware
registers. This issue will be discussed when we get to device quirks in
:ref:`Chapter 5 <device-quirks>`. Last two fields (line 8 and 9) are
also about device quirks: fifo_cfg points to the USB endpoints
configuration table and fifo_cfg_size keeps track of the size of the
number of entries in that configuration table. More on that later in
:ref:`Chapter 5 <device-quirks>`.

Then this configuration is embedded inside jz4740_musb_platform_data
musb_hdrc_platform_data structure (line 11): config is a pointer to
the configuration structure itself, and mode tells the controller driver
if the controller hardware may be used as MUSB_HOST only,
MUSB_PERIPHERAL only or MUSB_OTG which is a dual mode.

Remember that jz4740_musb_platform_data is then used to convey
platform data information as we have seen in the probe function in
:ref:`Chapter 2 <linux-musb-basics>`


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
