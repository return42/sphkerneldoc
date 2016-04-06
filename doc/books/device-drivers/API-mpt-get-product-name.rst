
.. _API-mpt-get-product-name:

====================
mpt_get_product_name
====================

*man mpt_get_product_name(9)*

*4.6.0-rc1*

returns product string


Synopsis
========

.. c:function:: const char⋆ mpt_get_product_name( u16 vendor, u16 device, u8 revision )

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

Returns product string displayed when driver loads, in /proc/mpt/summary and /sysfs/class/scsi_host/host<X>/version_product
