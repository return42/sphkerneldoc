
.. _API-blk-alloc-devt:

==============
blk_alloc_devt
==============

*man blk_alloc_devt(9)*

*4.6.0-rc1*

allocate a dev_t for a partition


Synopsis
========

.. c:function:: int blk_alloc_devt( struct hd_struct * part, dev_t * devt )

Arguments
=========

``part``
    partition to allocate dev_t for

``devt``
    out parameter for resulting dev_t


Description
===========

Allocate a dev_t for block device.


RETURNS
=======

0 on success, allocated dev_t is returned in ⋆ ``devt``. -errno on failure.


CONTEXT
=======

Might sleep.
