.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-detach:

==========
phy_detach
==========

*man phy_detach(9)*

*4.6.0-rc5*

detach a PHY device from its network device


Synopsis
========

.. c:function:: void phy_detach( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct


Description
===========

This detaches the phy device from its network device and the phy driver,
and drops the reference count taken in ``phy_attach_direct``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
