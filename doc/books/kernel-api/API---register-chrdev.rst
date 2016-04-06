
.. _API---register-chrdev:

=================
__register_chrdev
=================

*man __register_chrdev(9)*

*4.6.0-rc1*

create and register a cdev occupying a range of minors


Synopsis
========

.. c:function:: int __register_chrdev( unsigned int major, unsigned int baseminor, unsigned int count, const char * name, const struct file_operations * fops )

Arguments
=========

``major``
    major device number or 0 for dynamic allocation

``baseminor``
    first of the requested range of minor numbers

``count``
    the number of minor numbers required

``name``
    name of this range of devices

``fops``
    file operations associated with this devices


Description
===========

If ``major`` == 0 this functions will dynamically allocate a major and return its number.

If ``major`` > 0 this function will attempt to reserve a device with the given major number and will return zero on success.

Returns a -ve errno on failure.

The name of this device has nothing to do with the name of the device in /dev. It only helps to keep track of the different owners of devices. If your module name has only one type
of devices it's ok to use e.g. the name of the module here.
