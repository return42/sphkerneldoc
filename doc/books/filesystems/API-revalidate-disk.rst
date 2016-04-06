
.. _API-revalidate-disk:

===============
revalidate_disk
===============

*man revalidate_disk(9)*

*4.6.0-rc1*

wrapper for lower-level driver's revalidate_disk call-back


Synopsis
========

.. c:function:: int revalidate_disk( struct gendisk * disk )

Arguments
=========

``disk``
    struct gendisk to be revalidated


Description
===========

This routine is a wrapper for lower-level driver's revalidate_disk call-backs. It is used to do common pre and post operations needed for all revalidate_disk operations.
