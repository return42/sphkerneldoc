.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-start-interrupts:

====================
phy_start_interrupts
====================

*man phy_start_interrupts(9)*

*4.6.0-rc5*

request and enable interrupts for a PHY device


Synopsis
========

.. c:function:: int phy_start_interrupts( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct


Description
===========

Request the interrupt for the given PHY. If this fails, then we set irq
to PHY_POLL. Otherwise, we enable the interrupts in the PHY. This
should only be called with a valid IRQ number. Returns 0 on success or <
0 on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
