
.. _API-disable-irq:

===========
disable_irq
===========

*man disable_irq(9)*

*4.6.0-rc1*

disable an irq and wait for completion


Synopsis
========

.. c:function:: void disable_irq( unsigned int irq )

Arguments
=========

``irq``
    Interrupt to disable


Description
===========

Disable the selected interrupt line. Enables and Disables are nested. This function waits for any pending IRQ handlers for this interrupt to complete before returning. If you use
this function while holding a resource the IRQ handler may need you will deadlock.

This function may be called - with care - from IRQ context.
