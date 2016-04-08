
.. _API-dev-get-flags:

=============
dev_get_flags
=============

*man dev_get_flags(9)*

*4.6.0-rc1*

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
