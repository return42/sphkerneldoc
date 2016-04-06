
.. _API-blkdev-get-by-dev:

=================
blkdev_get_by_dev
=================

*man blkdev_get_by_dev(9)*

*4.6.0-rc1*

open a block device by device number


Synopsis
========

.. c:function:: struct block_device ⋆ blkdev_get_by_dev( dev_t dev, fmode_t mode, void * holder )

Arguments
=========

``dev``
    device number of block device to open

``mode``
    FMODE_⋆ mask

``holder``
    exclusive holder identifier


Description
===========

Open the blockdevice described by device number ``dev``. ``mode`` and ``holder`` are identical to ``blkdev_get``.

Use it ONLY if you really do not have anything better - i.e. when you are behind a truly sucky interface and all you are given is a device number. _Never_ to be used for internal
purposes. If you ever need it - reconsider your API.

On success, the returned block_device has reference count of one.


CONTEXT
=======

Might sleep.


RETURNS
=======

Pointer to block_device on success, ERR_PTR(-errno) on failure.
