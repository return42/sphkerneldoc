.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/bus/dpio/dpio-service.c

.. _`dpaa2_io_create`:

dpaa2_io_create
===============

.. c:function:: struct dpaa2_io *dpaa2_io_create(const struct dpaa2_io_desc *desc)

    create a dpaa2_io object.

    :param const struct dpaa2_io_desc \*desc:
        the dpaa2_io descriptor

.. _`dpaa2_io_create.description`:

Description
-----------

Activates a "struct dpaa2_io" corresponding to the given config of an actual
DPIO object.

Return a valid dpaa2_io object for success, or NULL for failure.

.. _`dpaa2_io_down`:

dpaa2_io_down
=============

.. c:function:: void dpaa2_io_down(struct dpaa2_io *d)

    release the dpaa2_io object.

    :param struct dpaa2_io \*d:
        the dpaa2_io object to be released.

.. _`dpaa2_io_down.description`:

Description
-----------

The "struct dpaa2_io" type can represent an individual DPIO object (as
described by "struct dpaa2_io_desc") or an instance of a "DPIO service",
which can be used to group/encapsulate multiple DPIO objects. In all cases,
each handle obtained should be released using this function.

.. _`dpaa2_io_irq`:

dpaa2_io_irq
============

.. c:function:: irqreturn_t dpaa2_io_irq(struct dpaa2_io *obj)

    ISR for DPIO interrupts

    :param struct dpaa2_io \*obj:
        the given DPIO object.

.. _`dpaa2_io_irq.description`:

Description
-----------

Return IRQ_HANDLED for success or IRQ_NONE if there
were no pending interrupts.

.. _`dpaa2_io_service_register`:

dpaa2_io_service_register
=========================

.. c:function:: int dpaa2_io_service_register(struct dpaa2_io *d, struct dpaa2_io_notification_ctx *ctx)

    Prepare for servicing of FQDAN or CDAN notifications on the given DPIO service.

    :param struct dpaa2_io \*d:
        the given DPIO service.

    :param struct dpaa2_io_notification_ctx \*ctx:
        the notification context.

.. _`dpaa2_io_service_register.description`:

Description
-----------

The caller should make the MC command to attach a DPAA2 object to
a DPIO after this function completes successfully.  In that way:
(a) The DPIO service is "ready" to handle a notification arrival
(which might happen before the "attach" command to MC has
returned control of execution back to the caller)
(b) The DPIO service can provide back to the caller the 'dpio_id' and
'qman64' parameters that it should pass along in the MC command
in order for the object to be configured to produce the right
notification fields to the DPIO service.

Return 0 for success, or -ENODEV for failure.

.. _`dpaa2_io_service_deregister`:

dpaa2_io_service_deregister
===========================

.. c:function:: void dpaa2_io_service_deregister(struct dpaa2_io *service, struct dpaa2_io_notification_ctx *ctx)

    The opposite of 'register'.

    :param struct dpaa2_io \*service:
        the given DPIO service.

    :param struct dpaa2_io_notification_ctx \*ctx:
        the notification context.

.. _`dpaa2_io_service_deregister.description`:

Description
-----------

This function should be called only after sending the MC command to
to detach the notification-producing device from the DPIO.

.. _`dpaa2_io_service_rearm`:

dpaa2_io_service_rearm
======================

.. c:function:: int dpaa2_io_service_rearm(struct dpaa2_io *d, struct dpaa2_io_notification_ctx *ctx)

    Rearm the notification for the given DPIO service.

    :param struct dpaa2_io \*d:
        the given DPIO service.

    :param struct dpaa2_io_notification_ctx \*ctx:
        the notification context.

.. _`dpaa2_io_service_rearm.description`:

Description
-----------

Once a FQDAN/CDAN has been produced, the corresponding FQ/channel is
considered "disarmed". Ie. the user can issue pull dequeue operations on that
traffic source for as long as it likes. Eventually it may wish to "rearm"
that source to allow it to produce another FQDAN/CDAN, that's what this
function achieves.

Return 0 for success.

.. _`dpaa2_io_service_pull_fq`:

dpaa2_io_service_pull_fq
========================

.. c:function:: int dpaa2_io_service_pull_fq(struct dpaa2_io *d, u32 fqid, struct dpaa2_io_store *s)

    pull dequeue functions from a fq.

    :param struct dpaa2_io \*d:
        the given DPIO service.

    :param u32 fqid:
        the given frame queue id.

    :param struct dpaa2_io_store \*s:
        the dpaa2_io_store object for the result.

.. _`dpaa2_io_service_pull_fq.description`:

Description
-----------

Return 0 for success, or error code for failure.

.. _`dpaa2_io_service_pull_channel`:

dpaa2_io_service_pull_channel
=============================

.. c:function:: int dpaa2_io_service_pull_channel(struct dpaa2_io *d, u32 channelid, struct dpaa2_io_store *s)

    pull dequeue functions from a channel.

    :param struct dpaa2_io \*d:
        the given DPIO service.

    :param u32 channelid:
        the given channel id.

    :param struct dpaa2_io_store \*s:
        the dpaa2_io_store object for the result.

.. _`dpaa2_io_service_pull_channel.description`:

Description
-----------

Return 0 for success, or error code for failure.

.. _`dpaa2_io_service_enqueue_fq`:

dpaa2_io_service_enqueue_fq
===========================

.. c:function:: int dpaa2_io_service_enqueue_fq(struct dpaa2_io *d, u32 fqid, const struct dpaa2_fd *fd)

    Enqueue a frame to a frame queue.

    :param struct dpaa2_io \*d:
        the given DPIO service.

    :param u32 fqid:
        the given frame queue id.

    :param const struct dpaa2_fd \*fd:
        the frame descriptor which is enqueued.

.. _`dpaa2_io_service_enqueue_fq.description`:

Description
-----------

Return 0 for successful enqueue, -EBUSY if the enqueue ring is not ready,
or -ENODEV if there is no dpio service.

.. _`dpaa2_io_service_enqueue_qd`:

dpaa2_io_service_enqueue_qd
===========================

.. c:function:: int dpaa2_io_service_enqueue_qd(struct dpaa2_io *d, u32 qdid, u8 prio, u16 qdbin, const struct dpaa2_fd *fd)

    Enqueue a frame to a QD.

    :param struct dpaa2_io \*d:
        the given DPIO service.

    :param u32 qdid:
        the given queuing destination id.

    :param u8 prio:
        the given queuing priority.

    :param u16 qdbin:
        the given queuing destination bin.

    :param const struct dpaa2_fd \*fd:
        the frame descriptor which is enqueued.

.. _`dpaa2_io_service_enqueue_qd.description`:

Description
-----------

Return 0 for successful enqueue, or -EBUSY if the enqueue ring is not ready,
or -ENODEV if there is no dpio service.

.. _`dpaa2_io_service_release`:

dpaa2_io_service_release
========================

.. c:function:: int dpaa2_io_service_release(struct dpaa2_io *d, u32 bpid, const u64 *buffers, unsigned int num_buffers)

    Release buffers to a buffer pool.

    :param struct dpaa2_io \*d:
        the given DPIO object.

    :param u32 bpid:
        the buffer pool id.

    :param const u64 \*buffers:
        the buffers to be released.

    :param unsigned int num_buffers:
        the number of the buffers to be released.

.. _`dpaa2_io_service_release.description`:

Description
-----------

Return 0 for success, and negative error code for failure.

.. _`dpaa2_io_service_acquire`:

dpaa2_io_service_acquire
========================

.. c:function:: int dpaa2_io_service_acquire(struct dpaa2_io *d, u32 bpid, u64 *buffers, unsigned int num_buffers)

    Acquire buffers from a buffer pool.

    :param struct dpaa2_io \*d:
        the given DPIO object.

    :param u32 bpid:
        the buffer pool id.

    :param u64 \*buffers:
        the buffer addresses for acquired buffers.

    :param unsigned int num_buffers:
        the expected number of the buffers to acquire.

.. _`dpaa2_io_service_acquire.description`:

Description
-----------

Return a negative error code if the command failed, otherwise it returns
the number of buffers acquired, which may be less than the number requested.
Eg. if the buffer pool is empty, this will return zero.

.. _`dpaa2_io_store_create`:

dpaa2_io_store_create
=====================

.. c:function:: struct dpaa2_io_store *dpaa2_io_store_create(unsigned int max_frames, struct device *dev)

    Create the dma memory storage for dequeue result.

    :param unsigned int max_frames:
        the maximum number of dequeued result for frames, must be <= 16.

    :param struct device \*dev:
        the device to allow mapping/unmapping the DMAable region.

.. _`dpaa2_io_store_create.description`:

Description
-----------

The size of the storage is "max_frames\*sizeof(struct dpaa2_dq)".
The 'dpaa2_io_store' returned is a DPIO service managed object.

Return pointer to dpaa2_io_store struct for successfuly created storage
memory, or NULL on error.

.. _`dpaa2_io_store_destroy`:

dpaa2_io_store_destroy
======================

.. c:function:: void dpaa2_io_store_destroy(struct dpaa2_io_store *s)

    Frees the dma memory storage for dequeue result.

    :param struct dpaa2_io_store \*s:
        the storage memory to be destroyed.

.. _`dpaa2_io_store_next`:

dpaa2_io_store_next
===================

.. c:function:: struct dpaa2_dq *dpaa2_io_store_next(struct dpaa2_io_store *s, int *is_last)

    Determine when the next dequeue result is available.

    :param struct dpaa2_io_store \*s:
        the dpaa2_io_store object.

    :param int \*is_last:
        indicate whether this is the last frame in the pull command.

.. _`dpaa2_io_store_next.description`:

Description
-----------

When an object driver performs dequeues to a dpaa2_io_store, this function
can be used to determine when the next frame result is available. Once
this function returns non-NULL, a subsequent call to it will try to find
the next dequeue result.

Note that if a pull-dequeue has a NULL result because the target FQ/channel
was empty, then this function will also return NULL (rather than expecting
the caller to always check for this. As such, "is_last" can be used to
differentiate between "end-of-empty-dequeue" and "still-waiting".

Return dequeue result for a valid dequeue result, or NULL for empty dequeue.

.. This file was automatic generated / don't edit.

