
.. _API-add-disk:

========
add_disk
========

*man add_disk(9)*

*4.6.0-rc1*

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

This function registers the partitioning information in ``disk`` with the kernel.


FIXME
=====

error handling
