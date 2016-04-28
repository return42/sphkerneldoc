.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-get-product-name:

====================
mpt_get_product_name
====================

*man mpt_get_product_name(9)*

*4.6.0-rc5*

returns product string


Synopsis
========

.. c:function:: const char* mpt_get_product_name( u16 vendor, u16 device, u8 revision )

Arguments
=========

``vendor``
    pci vendor id

``device``
    pci device id

``revision``
    pci revision id


Description
===========

Returns product string displayed when driver loads, in /proc/mpt/summary
and /sysfs/class/scsi_host/host<X>/version_product


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
