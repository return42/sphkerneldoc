
.. _API-class-destroy:

=============
class_destroy
=============

*man class_destroy(9)*

*4.6.0-rc1*

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

Note, the pointer to be destroyed must have been created with a call to ``class_create``.
