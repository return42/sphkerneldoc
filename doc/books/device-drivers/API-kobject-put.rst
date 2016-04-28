.. -*- coding: utf-8; mode: rst -*-

.. _API-kobject-put:

===========
kobject_put
===========

*man kobject_put(9)*

*4.6.0-rc5*

decrement refcount for object.


Synopsis
========

.. c:function:: void kobject_put( struct kobject * kobj )

Arguments
=========

``kobj``
    object.


Description
===========

Decrement the refcount, and if 0, call ``kobject_cleanup``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
