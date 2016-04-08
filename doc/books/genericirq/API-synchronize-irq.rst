
.. _API-synchronize-irq:

===============
synchronize_irq
===============

*man synchronize_irq(9)*

*4.6.0-rc1*

wait for pending IRQ handlers (on other CPUs)


Synopsis
========

.. c:function:: void synchronize_irq( unsigned int irq )

Arguments
=========

``irq``
    interrupt number to wait for


Description
===========

This function waits for any pending IRQ handlers for this interrupt to complete before returning. If you use this function while holding a resource the IRQ handler may need you
will deadlock.

This function may be called - with care - from IRQ context.
