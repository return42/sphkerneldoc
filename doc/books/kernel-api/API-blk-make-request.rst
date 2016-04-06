
.. _API-blk-make-request:

================
blk_make_request
================

*man blk_make_request(9)*

*4.6.0-rc1*

given a bio, allocate a corresponding struct request.


Synopsis
========

.. c:function:: struct request ⋆ blk_make_request( struct request_queue * q, struct bio * bio, gfp_t gfp_mask )

Arguments
=========

``q``
    target request queue

``bio``
    The bio describing the memory mappings that will be submitted for IO. It may be a chained-bio properly constructed by block/bio layer.

``gfp_mask``
    gfp flags to be used for memory allocation


Description
===========

blk_make_request is the parallel of generic_make_request for BLOCK_PC type commands. Where the struct request needs to be farther initialized by the caller. It is passed a
``struct bio``, which describes the memory info of the I/O transfer.

The caller of blk_make_request must make sure that bi_io_vec are set to describe the memory buffers. That ``bio_data_dir`` will return the needed direction of the request. (And
all bio's in the passed bio-chain are properly set accordingly)

If called under none-sleepable conditions, mapped bio buffers must not need bouncing, by calling the appropriate masked or flagged allocator, suitable for the target device.
Otherwise the call to blk_queue_bounce will BUG.


WARNING
=======

When allocating/cloning a bio-chain, careful consideration should be given to how you allocate bios. In particular, you cannot use __GFP_DIRECT_RECLAIM for anything but the
first bio in the chain. Otherwise you risk waiting for IO completion of a bio that hasn't been submitted yet, thus resulting in a deadlock. Alternatively bios should be allocated
using ``bio_kmalloc`` instead of ``bio_alloc``, as that avoids the mempool deadlock. If possible a big IO should be split into smaller parts when allocation fails. Partial
allocation should not be an error, or you risk a live-lock.
