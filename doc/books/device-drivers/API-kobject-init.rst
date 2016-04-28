.. -*- coding: utf-8; mode: rst -*-

.. _API-kobject-init:

============
kobject_init
============

*man kobject_init(9)*

*4.6.0-rc5*

initialize a kobject structure


Synopsis
========

.. c:function:: void kobject_init( struct kobject * kobj, struct kobj_type * ktype )

Arguments
=========

``kobj``
    pointer to the kobject to initialize

``ktype``
    pointer to the ktype for this kobject.


Description
===========

This function will properly initialize a kobject such that it can then
be passed to the ``kobject_add`` call.

After this function is called, the kobject MUST be cleaned up by a call
to ``kobject_put``, not by a call to kfree directly to ensure that all
of the memory is cleaned up properly.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
