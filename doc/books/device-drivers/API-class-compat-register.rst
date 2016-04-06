
.. _API-class-compat-register:

=====================
class_compat_register
=====================

*man class_compat_register(9)*

*4.6.0-rc1*

register a compatibility class


Synopsis
========

.. c:function:: struct class_compat ⋆ class_compat_register( const char * name )

Arguments
=========

``name``
    the name of the class


Description
===========

Compatibility class are meant as a temporary user-space compatibility workaround when converting a family of class devices to a bus devices.
