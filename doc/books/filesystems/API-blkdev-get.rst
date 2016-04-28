.. -*- coding: utf-8; mode: rst -*-

.. _API-blkdev-get:

==========
blkdev_get
==========

*man blkdev_get(9)*

*4.6.0-rc5*

open a block device


Synopsis
========

.. c:function:: int blkdev_get( struct block_device * bdev, fmode_t mode, void * holder )

Arguments
=========

``bdev``
    block_device to open

``mode``
    FMODE_* mask

``holder``
    exclusive holder identifier


Description
===========

Open ``bdev`` with ``mode``. If ``mode`` includes ``FMODE_EXCL``,
``bdev`` is open with exclusive access. Specifying ``FMODE_EXCL`` with
``NULL`` ``holder`` is invalid. Exclusive opens may nest for the same
``holder``.

On success, the reference count of ``bdev`` is unchanged. On failure,
``bdev`` is put.


CONTEXT
=======

Might sleep.


RETURNS
=======

0 on success, -errno on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
