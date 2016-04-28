.. -*- coding: utf-8; mode: rst -*-

.. _API-kobject-get-path:

================
kobject_get_path
================

*man kobject_get_path(9)*

*4.6.0-rc5*

generate and return the path associated with a given kobj and kset pair.


Synopsis
========

.. c:function:: char * kobject_get_path( struct kobject * kobj, gfp_t gfp_mask )

Arguments
=========

``kobj``
    kobject in question, with which to build the path

``gfp_mask``
    the allocation type used to allocate the path


Description
===========

The result must be freed by the caller with ``kfree``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
