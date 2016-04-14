.. -*- coding: utf-8; mode: rst -*-

=============
seqno-fence.h
=============

.. _`to_seqno_fence`:

to_seqno_fence
==============

.. c:function:: struct seqno_fence *to_seqno_fence (struct fence *fence)

    cast a fence to a seqno_fence

    :param struct fence \*fence:
        fence to cast to a seqno_fence


.. _`to_seqno_fence.description`:

Description
-----------

Returns NULL if the fence is not a seqno_fence,
or the seqno_fence otherwise.


.. _`seqno_fence_init`:

seqno_fence_init
================

.. c:function:: void seqno_fence_init (struct seqno_fence *fence, spinlock_t *lock, struct dma_buf *sync_buf, uint32_t context, uint32_t seqno_ofs, uint32_t seqno, enum seqno_fence_condition cond, const struct fence_ops *ops)

    initialize a seqno fence

    :param struct seqno_fence \*fence:
        seqno_fence to initialize

    :param spinlock_t \*lock:
        pointer to spinlock to use for fence

    :param struct dma_buf \*sync_buf:
        buffer containing the memory location to signal on

    :param uint32_t context:
        the execution context this fence is a part of

    :param uint32_t seqno_ofs:
        the offset within ``sync_buf``

    :param uint32_t seqno:
        the sequence # to signal on

    :param enum seqno_fence_condition cond:
        fence wait condition

    :param const struct fence_ops \*ops:
        the fence_ops for operations on this seqno fence


.. _`seqno_fence_init.description`:

Description
-----------

This function initializes a struct seqno_fence with passed parameters,
and takes a reference on sync_buf which is released on fence destruction.

A seqno_fence is a dma_fence which can complete in software when
enable_signaling is called, but it also completes when
(s32)((sync_buf)[seqno_ofs] - seqno) >= 0 is true

The seqno_fence will take a refcount on the sync_buf until it's
destroyed, but actual lifetime of sync_buf may be longer if one of the
callers take a reference to it.

Certain hardware have instructions to insert this type of wait condition
in the command stream, so no intervention from software would be needed.
This type of fence can be destroyed before completed, however a reference
on the sync_buf dma-buf can be taken. It is encouraged to re-use the same
dma-buf for sync_buf, since mapping or unmapping the sync_buf to the
device's vm can be expensive.

It is recommended for creators of seqno_fence to call fence_signal
before destruction. This will prevent possible issues from wraparound at
time of issue vs time of check, since users can check fence_is_signaled
before submitting instructions for the hardware to wait on the fence.
However, when ops.enable_signaling is not called, it doesn't have to be
done as soon as possible, just before there's any real danger of seqno
wraparound.

