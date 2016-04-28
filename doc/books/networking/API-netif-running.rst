.. -*- coding: utf-8; mode: rst -*-

.. _API-netif-running:

=============
netif_running
=============

*man netif_running(9)*

*4.6.0-rc5*

test if up


Synopsis
========

.. c:function:: bool netif_running( const struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Test if the device has been brought up.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
