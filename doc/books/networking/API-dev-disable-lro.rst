.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-disable-lro:

===============
dev_disable_lro
===============

*man dev_disable_lro(9)*

*4.6.0-rc5*

disable Large Receive Offload on a device


Synopsis
========

.. c:function:: void dev_disable_lro( struct net_device * dev )

Arguments
=========

``dev``
    device


Description
===========

Disable Large Receive Offload (LRO) on a net device. Must be called
under RTNL. This is needed if received packets may be forwarded to
another interface.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
