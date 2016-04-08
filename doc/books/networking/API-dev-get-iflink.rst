
.. _API-dev-get-iflink:

==============
dev_get_iflink
==============

*man dev_get_iflink(9)*

*4.6.0-rc1*

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

Indicates the ifindex the interface is linked to. Physical interfaces have the same 'ifindex' and 'iflink' values.
