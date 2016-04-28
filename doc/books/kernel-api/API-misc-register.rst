.. -*- coding: utf-8; mode: rst -*-

.. _API-misc-register:

=============
misc_register
=============

*man misc_register(9)*

*4.6.0-rc5*

register a miscellaneous device


Synopsis
========

.. c:function:: int misc_register( struct miscdevice * misc )

Arguments
=========

``misc``
    device structure


Description
===========

Register a miscellaneous device with the kernel. If the minor number is
set to ``MISC_DYNAMIC_MINOR`` a minor number is assigned and placed in
the minor field of the structure. For other cases the minor number
requested is used.

The structure passed is linked into the kernel and may not be destroyed
until it has been unregistered. By default, an ``open`` syscall to the
device sets file->private_data to point to the structure. Drivers don't
need open in fops for this.

A zero is returned on success and a negative errno code for failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
