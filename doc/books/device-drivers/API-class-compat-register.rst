.. -*- coding: utf-8; mode: rst -*-

.. _API-class-compat-register:

=====================
class_compat_register
=====================

*man class_compat_register(9)*

*4.6.0-rc5*

register a compatibility class


Synopsis
========

.. c:function:: struct class_compat * class_compat_register( const char * name )

Arguments
=========

``name``
    the name of the class


Description
===========

Compatibility class are meant as a temporary user-space compatibility
workaround when converting a family of class devices to a bus devices.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
