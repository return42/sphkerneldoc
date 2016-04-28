.. -*- coding: utf-8; mode: rst -*-

.. _API-edd-dev-is-type:

===============
edd_dev_is_type
===============

*man edd_dev_is_type(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
