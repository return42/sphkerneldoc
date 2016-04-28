.. -*- coding: utf-8; mode: rst -*-

.. _API-class-destroy:

=============
class_destroy
=============

*man class_destroy(9)*

*4.6.0-rc5*

destroys a struct class structure


Synopsis
========

.. c:function:: void class_destroy( struct class * cls )

Arguments
=========

``cls``
    pointer to the struct class that is to be destroyed


Description
===========

Note, the pointer to be destroyed must have been created with a call to
``class_create``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
