
.. _API-bdget-disk:

==========
bdget_disk
==========

*man bdget_disk(9)*

*4.6.0-rc1*

do ``bdget`` by gendisk and partition number


Synopsis
========

.. c:function:: struct block_device ⋆ bdget_disk( struct gendisk * disk, int partno )

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
