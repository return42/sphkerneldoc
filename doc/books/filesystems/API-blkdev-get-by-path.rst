
.. _API-blkdev-get-by-path:

==================
blkdev_get_by_path
==================

*man blkdev_get_by_path(9)*

*4.6.0-rc1*

open a block device by name


Synopsis
========

.. c:function:: struct block_device ⋆ blkdev_get_by_path( const char * path, fmode_t mode, void * holder )

Arguments
=========

``path``
    path to the block device to open

``mode``
    FMODE_⋆ mask

``holder``
    exclusive holder identifier


Description
===========

Open the blockdevice described by the device file at ``path``. ``mode`` and ``holder`` are identical to ``blkdev_get``.

On success, the returned block_device has reference count of one.


CONTEXT
=======

Might sleep.


RETURNS
=======

Pointer to block_device on success, ERR_PTR(-errno) on failure.
