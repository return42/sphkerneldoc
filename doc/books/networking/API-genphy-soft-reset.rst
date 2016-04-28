.. -*- coding: utf-8; mode: rst -*-

.. _API-genphy-soft-reset:

=================
genphy_soft_reset
=================

*man genphy_soft_reset(9)*

*4.6.0-rc5*

software reset the PHY via BMCR_RESET bit


Synopsis
========

.. c:function:: int genphy_soft_reset( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct


Description
===========

Perform a software PHY reset using the standard BMCR_RESET bit and poll
for the reset bit to be cleared.


Returns
=======

0 on success, < 0 on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
