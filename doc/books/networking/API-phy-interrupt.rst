.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-interrupt:

=============
phy_interrupt
=============

*man phy_interrupt(9)*

*4.6.0-rc5*

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

When a PHY interrupt occurs, the handler disables interrupts, and
schedules a work task to clear the interrupt.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
