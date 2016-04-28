.. -*- coding: utf-8; mode: rst -*-

.. _API-request-threaded-irq:

====================
request_threaded_irq
====================

*man request_threaded_irq(9)*

*4.6.0-rc5*

allocate an interrupt line


Synopsis
========

.. c:function:: int request_threaded_irq( unsigned int irq, irq_handler_t handler, irq_handler_t thread_fn, unsigned long irqflags, const char * devname, void * dev_id )

Arguments
=========

``irq``
    Interrupt line to allocate

``handler``
    Function to be called when the IRQ occurs. Primary handler for
    threaded interrupts If NULL and thread_fn != NULL the default
    primary handler is installed

``thread_fn``
    Function called from the irq handler thread If NULL, no irq thread
    is created

``irqflags``
    Interrupt type flags

``devname``
    An ascii name for the claiming device

``dev_id``
    A cookie passed back to the handler function


Description
===========

This call allocates interrupt resources and enables the interrupt line
and IRQ handling. From the point this call is made your handler function
may be invoked. Since your handler function must clear any interrupt the
board raises, you must take care both to initialise your hardware and to
set up the interrupt handler in the right order.

If you want to set up a threaded irq handler for your device then you
need to supply ``handler`` and ``thread_fn``. ``handler`` is still
called in hard interrupt context and has to check whether the interrupt
originates from the device. If yes it needs to disable the interrupt on
the device and return IRQ_WAKE_THREAD which will wake up the handler
thread and run ``thread_fn``. This split handler design is necessary to
support shared interrupts.

Dev_id must be globally unique. Normally the address of the device data
structure is used as the cookie. Since the handler receives this value
it makes sense to use it.

If your interrupt is shared you must pass a non NULL dev_id as this is
required when freeing the interrupt.


Flags
=====

IRQF_SHARED Interrupt is shared IRQF_TRIGGER_* Specify active edge(s)
or level


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
