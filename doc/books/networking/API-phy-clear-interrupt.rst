.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-clear-interrupt:

===================
phy_clear_interrupt
===================

*man phy_clear_interrupt(9)*

*4.6.0-rc5*

Ack the phy device's interrupt


Synopsis
========

.. c:function:: int phy_clear_interrupt( struct phy_device * phydev )

Arguments
=========

``phydev``
    the phy_device struct


Description
===========

If the ``phydev`` driver has an ack_interrupt function, call it to ack
and clear the phy device's interrupt.

Returns 0 on success or < 0 on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
