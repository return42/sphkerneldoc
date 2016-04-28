.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-aneg-done:

=============
phy_aneg_done
=============

*man phy_aneg_done(9)*

*4.6.0-rc5*

return auto-negotiation status


Synopsis
========

.. c:function:: int phy_aneg_done( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct


Description
===========

Return the auto-negotiation status from this ``phydev`` Returns > 0 on
success or < 0 on error. 0 means that auto-negotiation is still pending.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
