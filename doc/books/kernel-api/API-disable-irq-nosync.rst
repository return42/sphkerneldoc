
.. _API-disable-irq-nosync:

==================
disable_irq_nosync
==================

*man disable_irq_nosync(9)*

*4.6.0-rc1*

disable an irq without waiting


Synopsis
========

.. c:function:: void disable_irq_nosync( unsigned int irq )

Arguments
=========

``irq``
    Interrupt to disable


Description
===========

Disable the selected interrupt line. Disables and Enables are nested. Unlike ``disable_irq``, this function does not ensure existing instances of the IRQ handler have completed
before returning.

This function may be called from IRQ context.
