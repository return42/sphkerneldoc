.. -*- coding: utf-8; mode: rst -*-

.. _API-alloc-chrdev-region:

===================
alloc_chrdev_region
===================

*man alloc_chrdev_region(9)*

*4.6.0-rc5*

register a range of char device numbers


Synopsis
========

.. c:function:: int alloc_chrdev_region( dev_t * dev, unsigned baseminor, unsigned count, const char * name )

Arguments
=========

``dev``
    output parameter for first assigned number

``baseminor``
    first of the requested range of minor numbers

``count``
    the number of minor numbers required

``name``
    the name of the associated device or driver


Description
===========

Allocates a range of char device numbers. The major number will be
chosen dynamically, and returned (along with the first minor number) in
``dev``. Returns zero or a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
