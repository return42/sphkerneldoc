.. -*- coding: utf-8; mode: rst -*-

.. _API-netif-dormant:

=============
netif_dormant
=============

*man netif_dormant(9)*

*4.6.0-rc5*

test if carrier present


Synopsis
========

.. c:function:: bool netif_dormant( const struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Check if carrier is present on device


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
