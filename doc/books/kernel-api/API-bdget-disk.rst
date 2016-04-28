.. -*- coding: utf-8; mode: rst -*-

.. _API-bdget-disk:

==========
bdget_disk
==========

*man bdget_disk(9)*

*4.6.0-rc5*

do ``bdget`` by gendisk and partition number


Synopsis
========

.. c:function:: struct block_device * bdget_disk( struct gendisk * disk, int partno )

Arguments
=========

``disk``
    gendisk of interest

``partno``
    partition number


Description
===========

Find partition ``partno`` from ``disk``, do ``bdget`` on it.


CONTEXT
=======

Don't care.


RETURNS
=======

Resulting block_device on success, NULL on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
