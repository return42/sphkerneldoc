
.. _API-register-chrdev-region:

======================
register_chrdev_region
======================

*man register_chrdev_region(9)*

*4.6.0-rc1*

register a range of device numbers


Synopsis
========

.. c:function:: int register_chrdev_region( dev_t from, unsigned count, const char * name )

Arguments
=========

``from``
    the first in the desired range of device numbers; must include the major number.

``count``
    the number of consecutive device numbers required

``name``
    the name of the device or driver.


Description
===========

Return value is zero on success, a negative error code on failure.
