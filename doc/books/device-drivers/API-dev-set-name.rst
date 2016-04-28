.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-set-name:

============
dev_set_name
============

*man dev_set_name(9)*

*4.6.0-rc5*

set a device name


Synopsis
========

.. c:function:: int dev_set_name( struct device * dev, const char * fmt, ... )

Arguments
=========

``dev``
    device

``fmt``
    format string for the device's name

``...``
    variable arguments


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
