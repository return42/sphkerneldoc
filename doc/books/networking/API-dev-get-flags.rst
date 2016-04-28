.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-get-flags:

=============
dev_get_flags
=============

*man dev_get_flags(9)*

*4.6.0-rc5*

get flags reported to userspace


Synopsis
========

.. c:function:: unsigned int dev_get_flags( const struct net_device * dev )

Arguments
=========

``dev``
    device


Description
===========

Get the combination of flag bits exported through APIs to userspace.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
