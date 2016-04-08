
.. _API-phy-interrupt:

=============
phy_interrupt
=============

*man phy_interrupt(9)*

*4.6.0-rc1*

PHY interrupt handler


Synopsis
========

.. c:function:: irqreturn_t phy_interrupt( int irq, void * phy_dat )

Arguments
=========

``irq``
    interrupt line

``phy_dat``
    phy_device pointer


Description
===========

When a PHY interrupt occurs, the handler disables interrupts, and schedules a work task to clear the interrupt.
