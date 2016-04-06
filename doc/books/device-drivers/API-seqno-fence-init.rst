
.. _API-seqno-fence-init:

================
seqno_fence_init
================

*man seqno_fence_init(9)*

*4.6.0-rc1*

initialize a seqno fence


Synopsis
========

.. c:function:: void seqno_fence_init( struct seqno_fence * fence, spinlock_t * lock, struct dma_buf * sync_buf, uint32_t context, uint32_t seqno_ofs, uint32_t seqno, enum seqno_fence_condition cond, const struct fence_ops * ops )

Arguments
=========

``fence``
    seqno_fence to initialize

``lock``
    pointer to spinlock to use for fence

``sync_buf``
    buffer containing the memory location to signal on

``context``
    the execution context this fence is a part of

``seqno_ofs``
    the offset within ``sync_buf``

``seqno``
    the sequence # to signal on

``cond``
    fence wait condition

``ops``
    the fence_ops for operations on this seqno fence


Description
===========

This function initializes a struct seqno_fence with passed parameters, and takes a reference on sync_buf which is released on fence destruction.

A seqno_fence is a dma_fence which can complete in software when enable_signaling is called, but it also completes when (s32)((sync_buf)[seqno_ofs] - seqno) >= 0 is true

The seqno_fence will take a refcount on the sync_buf until it's destroyed, but actual lifetime of sync_buf may be longer if one of the callers take a reference to it.

Certain hardware have instructions to insert this type of wait condition in the command stream, so no intervention from software would be needed. This type of fence can be
destroyed before completed, however a reference on the sync_buf dma-buf can be taken. It is encouraged to re-use the same dma-buf for sync_buf, since mapping or unmapping the
sync_buf to the device's vm can be expensive.

It is recommended for creators of seqno_fence to call fence_signal before destruction. This will prevent possible issues from wraparound at time of issue vs time of check, since
users can check fence_is_signaled before submitting instructions for the hardware to wait on the fence. However, when ops.enable_signaling is not called, it doesn't have to be
done as soon as possible, just before there's any real danger of seqno wraparound.
