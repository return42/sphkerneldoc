
.. _API-class-compat-create-link:

========================
class_compat_create_link
========================

*man class_compat_create_link(9)*

*4.6.0-rc1*

create a compatibility class device link to a bus device


Synopsis
========

.. c:function:: int class_compat_create_link( struct class_compat * cls, struct device * dev, struct device * device_link )

Arguments
=========

``cls``
    the compatibility class

``dev``
    the target bus device

``device_link``
    an optional device to which a “device” link should be created
