
.. _API---unregister-chrdev:

===================
__unregister_chrdev
===================

*man __unregister_chrdev(9)*

*4.6.0-rc1*

unregister and destroy a cdev


Synopsis
========

.. c:function:: void __unregister_chrdev( unsigned int major, unsigned int baseminor, unsigned int count, const char * name )

Arguments
=========

``major``
    major device number

``baseminor``
    first of the range of minor numbers

``count``
    the number of minor numbers this cdev is occupying

``name``
    name of this range of devices


Description
===========

Unregister and destroy the cdev occupying the region described by ``major``, ``baseminor`` and ``count``. This function undoes what ``__register_chrdev`` did.
