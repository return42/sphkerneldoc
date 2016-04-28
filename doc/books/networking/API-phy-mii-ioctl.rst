.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-mii-ioctl:

=============
phy_mii_ioctl
=============

*man phy_mii_ioctl(9)*

*4.6.0-rc5*

generic PHY MII ioctl interface


Synopsis
========

.. c:function:: int phy_mii_ioctl( struct phy_device * phydev, struct ifreq * ifr, int cmd )

Arguments
=========

``phydev``
    the phy_device struct

``ifr``
    ``struct ifreq`` for socket ioctl's

``cmd``
    ioctl cmd to execute


Description
===========

Note that this function is currently incompatible with the PHYCONTROL
layer. It changes registers without regard to current state. Use at own
risk.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
