.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-probe:

=========
phy_probe
=========

*man phy_probe(9)*

*4.6.0-rc5*

probe and init a PHY device


Synopsis
========

.. c:function:: int phy_probe( struct device * dev )

Arguments
=========

``dev``
    device to probe and init


Description
===========

Take care of setting up the phy_device structure, set the state to
READY (the driver's init function should set it to STARTING if needed).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
