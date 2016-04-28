.. -*- coding: utf-8; mode: rst -*-

.. _API-add-disk:

========
add_disk
========

*man add_disk(9)*

*4.6.0-rc5*

add partitioning information to kernel list


Synopsis
========

.. c:function:: void add_disk( struct gendisk * disk )

Arguments
=========

``disk``
    per-device partitioning information


Description
===========

This function registers the partitioning information in ``disk`` with
the kernel.


FIXME
=====

error handling


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
