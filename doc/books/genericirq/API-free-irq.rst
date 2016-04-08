
.. _API-free-irq:

========
free_irq
========

*man free_irq(9)*

*4.6.0-rc1*

free an interrupt allocated with request_irq


Synopsis
========

.. c:function:: void free_irq( unsigned int irq, void * dev_id )

Arguments
=========

``irq``
    Interrupt line to free

``dev_id``
    Device identity to free


Description
===========

Remove an interrupt handler. The handler is removed and if the interrupt line is no longer in use by any driver it is disabled. On a shared IRQ the caller must ensure the interrupt
is disabled on the card it drives before calling this function. The function does not return until any executing interrupts for this IRQ have completed.

This function must not be called from interrupt context.
