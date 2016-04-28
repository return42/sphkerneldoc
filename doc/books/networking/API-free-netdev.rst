.. -*- coding: utf-8; mode: rst -*-

.. _API-free-netdev:

===========
free_netdev
===========

*man free_netdev(9)*

*4.6.0-rc5*

free network device


Synopsis
========

.. c:function:: void free_netdev( struct net_device * dev )

Arguments
=========

``dev``
    device


Description
===========

This function does the last stage of destroying an allocated device
interface. The reference to the device object is released. If this is
the last reference then it will be freed. Must be called in process
context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
