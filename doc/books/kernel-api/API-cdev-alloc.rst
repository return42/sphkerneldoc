
.. _API-cdev-alloc:

==========
cdev_alloc
==========

*man cdev_alloc(9)*

*4.6.0-rc1*

allocate a cdev structure


Synopsis
========

.. c:function:: struct cdev ⋆ cdev_alloc( void )

Arguments
=========

``void``
    no arguments


Description
===========

Allocates and returns a cdev structure, or NULL on failure.
