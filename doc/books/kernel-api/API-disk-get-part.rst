.. -*- coding: utf-8; mode: rst -*-

.. _API-disk-get-part:

=============
disk_get_part
=============

*man disk_get_part(9)*

*4.6.0-rc5*

get partition


Synopsis
========

.. c:function:: struct hd_struct * disk_get_part( struct gendisk * disk, int partno )

Arguments
=========

``disk``
    disk to look partition from

``partno``
    partition number


Description
===========

Look for partition ``partno`` from ``disk``. If found, increment
reference count and return it.


CONTEXT
=======

Don't care.


RETURNS
=======

Pointer to the found partition on success, NULL if not found.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
