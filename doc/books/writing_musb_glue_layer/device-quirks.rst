
.. _device-quirks:

=============
Device Quirks
=============

Completing the platform data specific to your device, you may also need to write some code in the glue layer to work around some device specific limitations. These quirks may be
due to some hardware bugs, or simply be the result of an incomplete implementation of the USB On-the-Go specification.

The JZ4740 UDC exhibits such quirks, some of which we will discuss here for the sake of insight even though these might not be found in the controller hardware you are working on.

Let's get back to the init function first:


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

Instruction on line 12 helps the MUSB controller driver to work around the fact that the controller hardware is missing registers that are used for USB endpoints configuration.

Without these registers, the controller driver is unable to read the endpoints configuration from the hardware, so we use line 12 instruction to bypass reading the configuration
from silicon, and rely on a hard-coded table that describes the endpoints configuration instead:


.. code-block:: c

    static struct musb_fifo_cfg jz4740_musb_fifo_cfg[] = {
    { .hw_ep_num = 1, .style = FIFO_TX, .maxpacket = 512, },
    { .hw_ep_num = 1, .style = FIFO_RX, .maxpacket = 512, },
    { .hw_ep_num = 2, .style = FIFO_TX, .maxpacket = 64, },
    };

Looking at the configuration table above, we see that each endpoints is described by three fields: hw_ep_num is the endpoint number, style is its direction (either FIFO_TX for
the controller driver to send packets in the controller hardware, or FIFO_RX to receive packets from hardware), and maxpacket defines the maximum size of each data packet that can
be transmitted over that endpoint. Reading from the table, the controller driver knows that endpoint 1 can be used to send and receive USB data packets of 512 bytes at once (this
is in fact a bulk in/out endpoint), and endpoint 2 can be used to send data packets of 64 bytes at once (this is in fact an interrupt endpoint).

Note that there is no information about endpoint 0 here: that one is implemented by default in every silicon design, with a predefined configuration according to the USB
specification. For more examples of endpoint configuration tables, see musb_core.c.

Let's now get back to the interrupt handler function:


.. code-block:: c

    static irqreturn_t jz4740_musb_interrupt(int irq, void *__hci)
    {
        unsigned long   flags;
        irqreturn_t     retval = IRQ_NONE;
        struct musb     *musb = __hci;

        spin_lock_irqsave(&musb->lock, flags);

        musb->int_usb = musb_readb(musb->mregs, MUSB_INTRUSB);
        musb->int_tx = musb_readw(musb->mregs, MUSB_INTRTX);
        musb->int_rx = musb_readw(musb->mregs, MUSB_INTRRX);

        /*
         * The controller is gadget only, the state of the host mode IRQ bits is
         * undefined. Mask them to make sure that the musb driver core will
         * never see them set
         */
        musb->int_usb &= MUSB_INTR_SUSPEND | MUSB_INTR_RESUME |
            MUSB_INTR_RESET | MUSB_INTR_SOF;

        if (musb->int_usb || musb->int_tx || musb->int_rx)
            retval = musb_interrupt(musb);

        spin_unlock_irqrestore(&musb->lock, flags);

        return retval;
    }

Instruction on line 18 above is a way for the controller driver to work around the fact that some interrupt bits used for USB host mode operation are missing in the MUSB_INTRUSB
register, thus left in an undefined hardware state, since this MUSB controller hardware is used in peripheral mode only. As a consequence, the glue layer masks these missing bits
out to avoid parasite interrupts by doing a logical AND operation between the value read from MUSB_INTRUSB and the bits that are actually implemented in the register.

These are only a couple of the quirks found in the JZ4740 USB device controller. Some others were directly addressed in the MUSB core since the fixes were generic enough to provide
a better handling of the issues for others controller hardware eventually.
