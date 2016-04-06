
.. _API-class-compat-remove-link:

========================
class_compat_remove_link
========================

*man class_compat_remove_link(9)*

*4.6.0-rc1*

remove a compatibility class device link to a bus device


Synopsis
========

.. c:function:: void class_compat_remove_link( struct class_compat * cls, struct device * dev, struct device * device_link )

Arguments
=========

``cls``
    the compatibility class

``dev``
    the target bus device

``device_link``
    an optional device to which a “device” link was previously created
