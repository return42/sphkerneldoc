
.. _API-edd-dev-is-type:

===============
edd_dev_is_type
===============

*man edd_dev_is_type(9)*

*4.6.0-rc1*

is this EDD device a 'type' device?


Synopsis
========

.. c:function:: int edd_dev_is_type( struct edd_device * edev, const char * type )

Arguments
=========

``edev``
    target edd_device

``type``
    a host bus or interface identifier string per the EDD spec


Description
===========

Returns 1 (TRUE) if it is a 'type' device, 0 otherwise.
