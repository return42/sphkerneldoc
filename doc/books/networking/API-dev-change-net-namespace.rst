.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-change-net-namespace:

========================
dev_change_net_namespace
========================

*man dev_change_net_namespace(9)*

*4.6.0-rc5*

move device to different nethost namespace


Synopsis
========

.. c:function:: int dev_change_net_namespace( struct net_device * dev, struct net * net, const char * pat )

Arguments
=========

``dev``
    device

``net``
    network namespace

``pat``
    If not NULL name pattern to try if the current device name is
    already taken in the destination network namespace.


Description
===========

This function shuts down a device interface and moves it to a new
network namespace. On success 0 is returned, on a failure a netagive
errno code is returned.

Callers must hold the rtnl semaphore.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
