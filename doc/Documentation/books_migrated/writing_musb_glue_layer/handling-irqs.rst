.. -*- coding: utf-8; mode: rst -*-

.. _handling-irqs:

*************
Handling IRQs
*************

Additionally to the MUSB controller hardware basic setup and
registration, the glue layer is also responsible for handling the IRQs:


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

Here the glue layer mostly has to read the relevant hardware registers
and pass their values on to the controller driver which will handle the
actual event that triggered the IRQ.

The interrupt handler critical section is protected by the
spin_lock_irqsave() and counterpart spin_unlock_irqrestore()
functions (line 7 and 24 respectively), which prevent the interrupt
handler code to be run by two different threads at the same time.

Then the relevant interrupt registers are read (line 9 to 11):

-  MUSB_INTRUSB: indicates which USB interrupts are currently active,

-  MUSB_INTRTX: indicates which of the interrupts for TX endpoints are
   currently active,

-  MUSB_INTRRX: indicates which of the interrupts for TX endpoints are
   currently active.

Note that musb_readb() is used to read 8-bit registers at most, while
musb_readw() allows us to read at most 16-bit registers. There are
other functions that can be used depending on the size of your device
registers. See musb_io.h for more information.

Instruction on line 18 is another quirk specific to the JZ4740 USB
device controller, which will be discussed later in
:ref:`Chapter 5 <device-quirks>`.

The glue layer still needs to register the IRQ handler though. Remember
the instruction on line 14 of the init function:


.. code-block:: c

    static int jz4740_musb_init(struct musb *musb)
    {
        musb->isr = jz4740_musb_interrupt;

        return 0;
    }

This instruction sets a pointer to the glue layer IRQ handler function,
in order for the controller hardware to call the handler back when an
IRQ comes from the controller hardware. The interrupt handler is now
implemented and registered.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
