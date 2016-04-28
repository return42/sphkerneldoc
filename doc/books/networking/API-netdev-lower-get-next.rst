.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-lower-get-next:

=====================
netdev_lower_get_next
=====================

*man netdev_lower_get_next(9)*

*4.6.0-rc5*

Get the next device from the lower neighbour list


Synopsis
========

.. c:function:: void * netdev_lower_get_next( struct net_device * dev, struct list_head ** iter )

Arguments
=========

``dev``
    device

``iter``
    list_head ** of the current position


Description
===========

Gets the next netdev_adjacent from the dev's lower neighbour list,
starting from iter position. The caller must hold RTNL lock or its own
locking that guarantees that the neighbour lower list will remain
unchanged.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
