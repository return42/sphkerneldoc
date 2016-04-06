
.. _API-usb-hcd-irq:

===========
usb_hcd_irq
===========

*man usb_hcd_irq(9)*

*4.6.0-rc1*

hook IRQs to HCD framework (bus glue)


Synopsis
========

.. c:function:: irqreturn_t usb_hcd_irq( int irq, void * __hcd )

Arguments
=========

``irq``
    the IRQ being raised

``__hcd``
    pointer to the HCD whose IRQ is being signaled


Description
===========

If the controller isn't HALTed, calls the driver's irq handler. Checks whether the controller is now dead.


Return
======

``IRQ_HANDLED`` if the IRQ was handled. ``IRQ_NONE`` otherwise.
