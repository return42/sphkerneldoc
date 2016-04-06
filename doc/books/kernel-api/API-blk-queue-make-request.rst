
.. _API-blk-queue-make-request:

======================
blk_queue_make_request
======================

*man blk_queue_make_request(9)*

*4.6.0-rc1*

define an alternate make_request function for a device


Synopsis
========

.. c:function:: void blk_queue_make_request( struct request_queue * q, make_request_fn * mfn )

Arguments
=========

``q``
    the request queue for the device to be affected

``mfn``
    the alternate make_request function


Description
===========

The normal way for ``struct bios`` to be passed to a device driver is for them to be collected into requests on a request queue, and then to allow the device driver to select
requests off that queue when it is ready. This works well for many block devices. However some block devices (typically virtual devices such as md or lvm) do not benefit from the
processing on the request queue, and are served best by having the requests passed directly to them. This can be achieved by providing a function to ``blk_queue_make_request``.


Caveat
======

The driver that does this ⋆must⋆ be able to deal appropriately with buffers in “highmemory”. This can be accomplished by either calling ``__bio_kmap_atomic`` to get a temporary
kernel mapping, or by calling ``blk_queue_bounce`` to create a buffer in normal memory.
