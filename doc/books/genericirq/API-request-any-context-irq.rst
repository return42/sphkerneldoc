
.. _API-request-any-context-irq:

=======================
request_any_context_irq
=======================

*man request_any_context_irq(9)*

*4.6.0-rc1*

allocate an interrupt line


Synopsis
========

.. c:function:: int request_any_context_irq( unsigned int irq, irq_handler_t handler, unsigned long flags, const char * name, void * dev_id )

Arguments
=========

``irq``
    Interrupt line to allocate

``handler``
    Function to be called when the IRQ occurs. Threaded handler for threaded interrupts.

``flags``
    Interrupt type flags

``name``
    An ascii name for the claiming device

``dev_id``
    A cookie passed back to the handler function


Description
===========

This call allocates interrupt resources and enables the interrupt line and IRQ handling. It selects either a hardirq or threaded handling method depending on the context.

On failure, it returns a negative value. On success, it returns either IRQC_IS_HARDIRQ or IRQC_IS_NESTED.
