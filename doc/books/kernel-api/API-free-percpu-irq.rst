
.. _API-free-percpu-irq:

===============
free_percpu_irq
===============

*man free_percpu_irq(9)*

*4.6.0-rc1*

free an interrupt allocated with request_percpu_irq


Synopsis
========

.. c:function:: void free_percpu_irq( unsigned int irq, void __percpu * dev_id )

Arguments
=========

``irq``
    Interrupt line to free

``dev_id``
    Device identity to free


Description
===========

Remove a percpu interrupt handler. The handler is removed, but the interrupt line is not disabled. This must be done on each CPU before calling this function. The function does not
return until any executing interrupts for this IRQ have completed.

This function must not be called from interrupt context.
