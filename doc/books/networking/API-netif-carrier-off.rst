.. -*- coding: utf-8; mode: rst -*-

.. _API-netif-carrier-off:

=================
netif_carrier_off
=================

*man netif_carrier_off(9)*

*4.6.0-rc5*

clear carrier


Synopsis
========

.. c:function:: void netif_carrier_off( struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Device has detected loss of carrier.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
