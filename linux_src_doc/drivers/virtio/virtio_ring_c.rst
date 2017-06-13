.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/virtio/virtio_ring.c

.. _`virtqueue_add_sgs`:

virtqueue_add_sgs
=================

.. c:function:: int virtqueue_add_sgs(struct virtqueue *_vq, struct scatterlist  *sgs, unsigned int out_sgs, unsigned int in_sgs, void *data, gfp_t gfp)

    expose buffers to other end

    :param struct virtqueue \*_vq:
        *undescribed*

    :param struct scatterlist  \*sgs:
        array of terminated scatterlists.

    :param unsigned int out_sgs:
        *undescribed*

    :param unsigned int in_sgs:
        *undescribed*

    :param void \*data:
        the token identifying the buffer.

    :param gfp_t gfp:
        how to do memory allocations (if necessary).

.. _`virtqueue_add_sgs.description`:

Description
-----------

Caller must ensure we don't call this with other virtqueue operations
at the same time (except where noted).

Returns zero or a negative error (ie. ENOSPC, ENOMEM, EIO).

.. _`virtqueue_add_outbuf`:

virtqueue_add_outbuf
====================

.. c:function:: int virtqueue_add_outbuf(struct virtqueue *vq, struct scatterlist *sg, unsigned int num, void *data, gfp_t gfp)

    expose output buffers to other end

    :param struct virtqueue \*vq:
        the struct virtqueue we're talking about.

    :param struct scatterlist \*sg:
        scatterlist (must be well-formed and terminated!)

    :param unsigned int num:
        the number of entries in \ ``sg``\  readable by other side

    :param void \*data:
        the token identifying the buffer.

    :param gfp_t gfp:
        how to do memory allocations (if necessary).

.. _`virtqueue_add_outbuf.description`:

Description
-----------

Caller must ensure we don't call this with other virtqueue operations
at the same time (except where noted).

Returns zero or a negative error (ie. ENOSPC, ENOMEM, EIO).

.. _`virtqueue_add_inbuf`:

virtqueue_add_inbuf
===================

.. c:function:: int virtqueue_add_inbuf(struct virtqueue *vq, struct scatterlist *sg, unsigned int num, void *data, gfp_t gfp)

    expose input buffers to other end

    :param struct virtqueue \*vq:
        the struct virtqueue we're talking about.

    :param struct scatterlist \*sg:
        scatterlist (must be well-formed and terminated!)

    :param unsigned int num:
        the number of entries in \ ``sg``\  writable by other side

    :param void \*data:
        the token identifying the buffer.

    :param gfp_t gfp:
        how to do memory allocations (if necessary).

.. _`virtqueue_add_inbuf.description`:

Description
-----------

Caller must ensure we don't call this with other virtqueue operations
at the same time (except where noted).

Returns zero or a negative error (ie. ENOSPC, ENOMEM, EIO).

.. _`virtqueue_add_inbuf_ctx`:

virtqueue_add_inbuf_ctx
=======================

.. c:function:: int virtqueue_add_inbuf_ctx(struct virtqueue *vq, struct scatterlist *sg, unsigned int num, void *data, void *ctx, gfp_t gfp)

    expose input buffers to other end

    :param struct virtqueue \*vq:
        the struct virtqueue we're talking about.

    :param struct scatterlist \*sg:
        scatterlist (must be well-formed and terminated!)

    :param unsigned int num:
        the number of entries in \ ``sg``\  writable by other side

    :param void \*data:
        the token identifying the buffer.

    :param void \*ctx:
        extra context for the token

    :param gfp_t gfp:
        how to do memory allocations (if necessary).

.. _`virtqueue_add_inbuf_ctx.description`:

Description
-----------

Caller must ensure we don't call this with other virtqueue operations
at the same time (except where noted).

Returns zero or a negative error (ie. ENOSPC, ENOMEM, EIO).

.. _`virtqueue_kick_prepare`:

virtqueue_kick_prepare
======================

.. c:function:: bool virtqueue_kick_prepare(struct virtqueue *_vq)

    first half of split virtqueue_kick call.

    :param struct virtqueue \*_vq:
        *undescribed*

.. _`virtqueue_kick_prepare.description`:

Description
-----------

Instead of \ :c:func:`virtqueue_kick`\ , you can do:
if (virtqueue_kick_prepare(vq))
virtqueue_notify(vq);

This is sometimes useful because the \ :c:func:`virtqueue_kick_prepare`\  needs
to be serialized, but the actual \ :c:func:`virtqueue_notify`\  call does not.

.. _`virtqueue_notify`:

virtqueue_notify
================

.. c:function:: bool virtqueue_notify(struct virtqueue *_vq)

    second half of split virtqueue_kick call.

    :param struct virtqueue \*_vq:
        *undescribed*

.. _`virtqueue_notify.description`:

Description
-----------

This does not need to be serialized.

Returns false if host notify failed or queue is broken, otherwise true.

.. _`virtqueue_kick`:

virtqueue_kick
==============

.. c:function:: bool virtqueue_kick(struct virtqueue *vq)

    update after add_buf

    :param struct virtqueue \*vq:
        the struct virtqueue

.. _`virtqueue_kick.description`:

Description
-----------

After one or more virtqueue_add\_\* calls, invoke this to kick
the other side.

Caller must ensure we don't call this with other virtqueue
operations at the same time (except where noted).

Returns false if kick failed, otherwise true.

.. _`virtqueue_get_buf_ctx`:

virtqueue_get_buf_ctx
=====================

.. c:function:: void *virtqueue_get_buf_ctx(struct virtqueue *_vq, unsigned int *len, void **ctx)

    get the next used buffer

    :param struct virtqueue \*_vq:
        *undescribed*

    :param unsigned int \*len:
        the length written into the buffer

    :param void \*\*ctx:
        *undescribed*

.. _`virtqueue_get_buf_ctx.description`:

Description
-----------

If the device wrote data into the buffer, \ ``len``\  will be set to the
amount written.  This means you don't need to clear the buffer
beforehand to ensure there's no data leakage in the case of short
writes.

Caller must ensure we don't call this with other virtqueue
operations at the same time (except where noted).

Returns NULL if there are no used buffers, or the "data" token
handed to virtqueue_add\_\*().

.. _`virtqueue_disable_cb`:

virtqueue_disable_cb
====================

.. c:function:: void virtqueue_disable_cb(struct virtqueue *_vq)

    disable callbacks

    :param struct virtqueue \*_vq:
        *undescribed*

.. _`virtqueue_disable_cb.description`:

Description
-----------

Note that this is not necessarily synchronous, hence unreliable and only
useful as an optimization.

Unlike other operations, this need not be serialized.

.. _`virtqueue_enable_cb_prepare`:

virtqueue_enable_cb_prepare
===========================

.. c:function:: unsigned virtqueue_enable_cb_prepare(struct virtqueue *_vq)

    restart callbacks after disable_cb

    :param struct virtqueue \*_vq:
        *undescribed*

.. _`virtqueue_enable_cb_prepare.description`:

Description
-----------

This re-enables callbacks; it returns current queue state
in an opaque unsigned value. This value should be later tested by
virtqueue_poll, to detect a possible race between the driver checking for
more work, and enabling callbacks.

Caller must ensure we don't call this with other virtqueue
operations at the same time (except where noted).

.. _`virtqueue_poll`:

virtqueue_poll
==============

.. c:function:: bool virtqueue_poll(struct virtqueue *_vq, unsigned last_used_idx)

    query pending used buffers

    :param struct virtqueue \*_vq:
        *undescribed*

    :param unsigned last_used_idx:
        virtqueue state (from call to virtqueue_enable_cb_prepare).

.. _`virtqueue_poll.description`:

Description
-----------

Returns "true" if there are pending used buffers in the queue.

This does not need to be serialized.

.. _`virtqueue_enable_cb`:

virtqueue_enable_cb
===================

.. c:function:: bool virtqueue_enable_cb(struct virtqueue *_vq)

    restart callbacks after disable_cb.

    :param struct virtqueue \*_vq:
        *undescribed*

.. _`virtqueue_enable_cb.description`:

Description
-----------

This re-enables callbacks; it returns "false" if there are pending
buffers in the queue, to detect a possible race between the driver
checking for more work, and enabling callbacks.

Caller must ensure we don't call this with other virtqueue
operations at the same time (except where noted).

.. _`virtqueue_enable_cb_delayed`:

virtqueue_enable_cb_delayed
===========================

.. c:function:: bool virtqueue_enable_cb_delayed(struct virtqueue *_vq)

    restart callbacks after disable_cb.

    :param struct virtqueue \*_vq:
        *undescribed*

.. _`virtqueue_enable_cb_delayed.description`:

Description
-----------

This re-enables callbacks but hints to the other side to delay
interrupts until most of the available buffers have been processed;
it returns "false" if there are many pending buffers in the queue,
to detect a possible race between the driver checking for more work,
and enabling callbacks.

Caller must ensure we don't call this with other virtqueue
operations at the same time (except where noted).

.. _`virtqueue_detach_unused_buf`:

virtqueue_detach_unused_buf
===========================

.. c:function:: void *virtqueue_detach_unused_buf(struct virtqueue *_vq)

    detach first unused buffer

    :param struct virtqueue \*_vq:
        *undescribed*

.. _`virtqueue_detach_unused_buf.description`:

Description
-----------

Returns NULL or the "data" token handed to virtqueue_add\_\*().
This is not valid on an active queue; it is useful only for device
shutdown.

.. _`virtqueue_get_vring_size`:

virtqueue_get_vring_size
========================

.. c:function:: unsigned int virtqueue_get_vring_size(struct virtqueue *_vq)

    return the size of the virtqueue's vring

    :param struct virtqueue \*_vq:
        *undescribed*

.. _`virtqueue_get_vring_size.description`:

Description
-----------

Returns the size of the vring.  This is mainly used for boasting to
userspace.  Unlike other operations, this need not be serialized.

.. This file was automatic generated / don't edit.

