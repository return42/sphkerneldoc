
.. _API-usb-add-hcd:

===========
usb_add_hcd
===========

*man usb_add_hcd(9)*

*4.6.0-rc1*

finish generic HCD structure initialization and register


Synopsis
========

.. c:function:: int usb_add_hcd( struct usb_hcd * hcd, unsigned int irqnum, unsigned long irqflags )

Arguments
=========

``hcd``
    the usb_hcd structure to initialize

``irqnum``
    Interrupt line to allocate

``irqflags``
    Interrupt type flags


Finish the remaining parts of generic HCD initialization
========================================================

allocate the buffers of consistent memory, register the bus, request the IRQ line, and call the driver's ``reset`` and ``start`` routines.
