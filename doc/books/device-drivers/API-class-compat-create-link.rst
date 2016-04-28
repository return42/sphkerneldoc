.. -*- coding: utf-8; mode: rst -*-

.. _API-class-compat-create-link:

========================
class_compat_create_link
========================

*man class_compat_create_link(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
