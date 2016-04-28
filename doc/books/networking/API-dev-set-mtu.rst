.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-set-mtu:

===========
dev_set_mtu
===========

*man dev_set_mtu(9)*

*4.6.0-rc5*

Change maximum transfer unit


Synopsis
========

.. c:function:: int dev_set_mtu( struct net_device * dev, int new_mtu )

Arguments
=========

``dev``
    device

``new_mtu``
    new transfer unit


Description
===========

Change the maximum transfer size of the network device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
