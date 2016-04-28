.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-get-iflink:

==============
dev_get_iflink
==============

*man dev_get_iflink(9)*

*4.6.0-rc5*

get 'iflink' value of a interface


Synopsis
========

.. c:function:: int dev_get_iflink( const struct net_device * dev )

Arguments
=========

``dev``
    targeted interface


Description
===========

Indicates the ifindex the interface is linked to. Physical interfaces
have the same 'ifindex' and 'iflink' values.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
