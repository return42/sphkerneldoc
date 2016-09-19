.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/v4l2-core/v4l2-mem2mem.c

.. _`v4l2_m2m_dev`:

struct v4l2_m2m_dev
===================

.. c:type:: struct v4l2_m2m_dev

    per-device context

.. _`v4l2_m2m_dev.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_m2m_dev {
        struct v4l2_m2m_ctx *curr_ctx;
        struct list_head job_queue;
        spinlock_t job_spinlock;
        const struct v4l2_m2m_ops *m2m_ops;
    }

.. _`v4l2_m2m_dev.members`:

Members
-------

curr_ctx
    currently running instance

job_queue
    instances queued to run

job_spinlock
    protects job_queue

m2m_ops
    driver callbacks

.. _`v4l2_m2m_get_vq`:

v4l2_m2m_get_vq
===============

.. c:function:: struct vb2_queue *v4l2_m2m_get_vq(struct v4l2_m2m_ctx *m2m_ctx, enum v4l2_buf_type type)

    return vb2_queue for the given type

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        *undescribed*

    :param enum v4l2_buf_type type:
        *undescribed*

.. _`v4l2_m2m_next_buf`:

v4l2_m2m_next_buf
=================

.. c:function:: void *v4l2_m2m_next_buf(struct v4l2_m2m_queue_ctx *q_ctx)

    return next buffer from the list of ready buffers

    :param struct v4l2_m2m_queue_ctx \*q_ctx:
        *undescribed*

.. _`v4l2_m2m_buf_remove`:

v4l2_m2m_buf_remove
===================

.. c:function:: void *v4l2_m2m_buf_remove(struct v4l2_m2m_queue_ctx *q_ctx)

    take off a buffer from the list of ready buffers and return it

    :param struct v4l2_m2m_queue_ctx \*q_ctx:
        *undescribed*

.. _`v4l2_m2m_get_curr_priv`:

v4l2_m2m_get_curr_priv
======================

.. c:function:: void *v4l2_m2m_get_curr_priv(struct v4l2_m2m_dev *m2m_dev)

    return driver private data for the currently running instance or NULL if no instance is running

    :param struct v4l2_m2m_dev \*m2m_dev:
        *undescribed*

.. _`v4l2_m2m_try_run`:

v4l2_m2m_try_run
================

.. c:function:: void v4l2_m2m_try_run(struct v4l2_m2m_dev *m2m_dev)

    select next job to perform and run it if possible

    :param struct v4l2_m2m_dev \*m2m_dev:
        *undescribed*

.. _`v4l2_m2m_try_run.description`:

Description
-----------

Get next transaction (if present) from the waiting jobs list and run it.

.. _`v4l2_m2m_try_schedule`:

v4l2_m2m_try_schedule
=====================

.. c:function:: void v4l2_m2m_try_schedule(struct v4l2_m2m_ctx *m2m_ctx)

    check whether an instance is ready to be added to the pending job queue and add it if so.

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance to be checked

.. _`v4l2_m2m_try_schedule.there-are-three-basic-requirements-an-instance-has-to-meet-to-be-able-to-run`:

There are three basic requirements an instance has to meet to be able to run
----------------------------------------------------------------------------

1) at least one source buffer has to be queued,
2) at least one destination buffer has to be queued,
3) streaming has to be on.

If a queue is buffered (for example a decoder hardware ringbuffer that has
to be drained before doing streamoff), allow scheduling without v4l2 buffers
on that queue.

There may also be additional, custom requirements. In such case the driver
should supply a custom callback (job_ready in v4l2_m2m_ops) that should
return 1 if the instance is ready.
An example of the above could be an instance that requires more than one
src/dst buffer per transaction.

.. _`v4l2_m2m_cancel_job`:

v4l2_m2m_cancel_job
===================

.. c:function:: void v4l2_m2m_cancel_job(struct v4l2_m2m_ctx *m2m_ctx)

    cancel pending jobs for the context

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        *undescribed*

.. _`v4l2_m2m_cancel_job.description`:

Description
-----------

In case of streamoff or release called on any context,
1] If the context is currently running, then abort job will be called
2] If the context is queued, then the context will be removed from
the job_queue

.. _`v4l2_m2m_job_finish`:

v4l2_m2m_job_finish
===================

.. c:function:: void v4l2_m2m_job_finish(struct v4l2_m2m_dev *m2m_dev, struct v4l2_m2m_ctx *m2m_ctx)

    inform the framework that a job has been finished and have it clean up

    :param struct v4l2_m2m_dev \*m2m_dev:
        *undescribed*

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        *undescribed*

.. _`v4l2_m2m_job_finish.description`:

Description
-----------

Called by a driver to yield back the device after it has finished with it.
Should be called as soon as possible after reaching a state which allows
other instances to take control of the device.

This function has to be called only after \ :c:func:`device_run`\  callback has been
called on the driver. To prevent recursion, it should not be called directly
from the \ :c:func:`device_run`\  callback though.

.. _`v4l2_m2m_reqbufs`:

v4l2_m2m_reqbufs
================

.. c:function:: int v4l2_m2m_reqbufs(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, struct v4l2_requestbuffers *reqbufs)

    multi-queue-aware REQBUFS multiplexer

    :param struct file \*file:
        *undescribed*

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        *undescribed*

    :param struct v4l2_requestbuffers \*reqbufs:
        *undescribed*

.. _`v4l2_m2m_querybuf`:

v4l2_m2m_querybuf
=================

.. c:function:: int v4l2_m2m_querybuf(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, struct v4l2_buffer *buf)

    multi-queue-aware QUERYBUF multiplexer

    :param struct file \*file:
        *undescribed*

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        *undescribed*

    :param struct v4l2_buffer \*buf:
        *undescribed*

.. _`v4l2_m2m_querybuf.description`:

Description
-----------

See \ :c:func:`v4l2_m2m_mmap`\  documentation for details.

.. _`v4l2_m2m_qbuf`:

v4l2_m2m_qbuf
=============

.. c:function:: int v4l2_m2m_qbuf(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, struct v4l2_buffer *buf)

    enqueue a source or destination buffer, depending on the type

    :param struct file \*file:
        *undescribed*

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        *undescribed*

    :param struct v4l2_buffer \*buf:
        *undescribed*

.. _`v4l2_m2m_dqbuf`:

v4l2_m2m_dqbuf
==============

.. c:function:: int v4l2_m2m_dqbuf(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, struct v4l2_buffer *buf)

    dequeue a source or destination buffer, depending on the type

    :param struct file \*file:
        *undescribed*

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        *undescribed*

    :param struct v4l2_buffer \*buf:
        *undescribed*

.. _`v4l2_m2m_prepare_buf`:

v4l2_m2m_prepare_buf
====================

.. c:function:: int v4l2_m2m_prepare_buf(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, struct v4l2_buffer *buf)

    prepare a source or destination buffer, depending on the type

    :param struct file \*file:
        *undescribed*

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        *undescribed*

    :param struct v4l2_buffer \*buf:
        *undescribed*

.. _`v4l2_m2m_create_bufs`:

v4l2_m2m_create_bufs
====================

.. c:function:: int v4l2_m2m_create_bufs(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, struct v4l2_create_buffers *create)

    create a source or destination buffer, depending on the type

    :param struct file \*file:
        *undescribed*

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        *undescribed*

    :param struct v4l2_create_buffers \*create:
        *undescribed*

.. _`v4l2_m2m_expbuf`:

v4l2_m2m_expbuf
===============

.. c:function:: int v4l2_m2m_expbuf(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, struct v4l2_exportbuffer *eb)

    export a source or destination buffer, depending on the type

    :param struct file \*file:
        *undescribed*

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        *undescribed*

    :param struct v4l2_exportbuffer \*eb:
        *undescribed*

.. _`v4l2_m2m_streamon`:

v4l2_m2m_streamon
=================

.. c:function:: int v4l2_m2m_streamon(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, enum v4l2_buf_type type)

    turn on streaming for a video queue

    :param struct file \*file:
        *undescribed*

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        *undescribed*

    :param enum v4l2_buf_type type:
        *undescribed*

.. _`v4l2_m2m_streamoff`:

v4l2_m2m_streamoff
==================

.. c:function:: int v4l2_m2m_streamoff(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, enum v4l2_buf_type type)

    turn off streaming for a video queue

    :param struct file \*file:
        *undescribed*

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        *undescribed*

    :param enum v4l2_buf_type type:
        *undescribed*

.. _`v4l2_m2m_poll`:

v4l2_m2m_poll
=============

.. c:function:: unsigned int v4l2_m2m_poll(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, struct poll_table_struct *wait)

    poll replacement, for destination buffers only

    :param struct file \*file:
        *undescribed*

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        *undescribed*

    :param struct poll_table_struct \*wait:
        *undescribed*

.. _`v4l2_m2m_poll.description`:

Description
-----------

Call from the driver's \ :c:func:`poll`\  function. Will poll both queues. If a buffer
is available to dequeue (with dqbuf) from the source queue, this will
indicate that a non-blocking write can be performed, while read will be
returned in case of the destination queue.

.. _`v4l2_m2m_mmap`:

v4l2_m2m_mmap
=============

.. c:function:: int v4l2_m2m_mmap(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, struct vm_area_struct *vma)

    source and destination queues-aware mmap multiplexer

    :param struct file \*file:
        *undescribed*

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        *undescribed*

    :param struct vm_area_struct \*vma:
        *undescribed*

.. _`v4l2_m2m_mmap.description`:

Description
-----------

Call from driver's \ :c:func:`mmap`\  function. Will handle \ :c:func:`mmap`\  for both queues
seamlessly for videobuffer, which will receive normal per-queue offsets and
proper videobuf queue pointers. The differentiation is made outside videobuf
by adding a predefined offset to buffers from one of the queues and
subtracting it before passing it back to videobuf. Only drivers (and
thus applications) receive modified offsets.

.. _`v4l2_m2m_init`:

v4l2_m2m_init
=============

.. c:function:: struct v4l2_m2m_dev *v4l2_m2m_init(const struct v4l2_m2m_ops *m2m_ops)

    initialize per-driver m2m data

    :param const struct v4l2_m2m_ops \*m2m_ops:
        *undescribed*

.. _`v4l2_m2m_init.description`:

Description
-----------

Usually called from driver's \ :c:func:`probe`\  function.

.. _`v4l2_m2m_release`:

v4l2_m2m_release
================

.. c:function:: void v4l2_m2m_release(struct v4l2_m2m_dev *m2m_dev)

    cleans up and frees a m2m_dev structure

    :param struct v4l2_m2m_dev \*m2m_dev:
        *undescribed*

.. _`v4l2_m2m_release.description`:

Description
-----------

Usually called from driver's \ :c:func:`remove`\  function.

.. _`v4l2_m2m_ctx_init`:

v4l2_m2m_ctx_init
=================

.. c:function:: struct v4l2_m2m_ctx *v4l2_m2m_ctx_init(struct v4l2_m2m_dev *m2m_dev, void *drv_priv, int (*queue_init)(void *priv, struct vb2_queue *src_vq, struct vb2_queue *dst_vq))

    allocate and initialize a m2m context \ ``priv``\  - driver's instance private data \ ``m2m_dev``\  - a previously initialized m2m_dev struct \ ``vq_init``\  - a callback for queue type-specific initialization function to be used for initializing videobuf_queues

    :param struct v4l2_m2m_dev \*m2m_dev:
        *undescribed*

    :param void \*drv_priv:
        *undescribed*

    :param int (\*queue_init)(void \*priv, struct vb2_queue \*src_vq, struct vb2_queue \*dst_vq):
        *undescribed*

.. _`v4l2_m2m_ctx_init.description`:

Description
-----------

Usually called from driver's \ :c:func:`open`\  function.

.. _`v4l2_m2m_ctx_release`:

v4l2_m2m_ctx_release
====================

.. c:function:: void v4l2_m2m_ctx_release(struct v4l2_m2m_ctx *m2m_ctx)

    release m2m context

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        *undescribed*

.. _`v4l2_m2m_ctx_release.description`:

Description
-----------

Usually called from driver's \ :c:func:`release`\  function.

.. _`v4l2_m2m_buf_queue`:

v4l2_m2m_buf_queue
==================

.. c:function:: void v4l2_m2m_buf_queue(struct v4l2_m2m_ctx *m2m_ctx, struct vb2_v4l2_buffer *vbuf)

    add a buffer to the proper ready buffers list.

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        *undescribed*

    :param struct vb2_v4l2_buffer \*vbuf:
        *undescribed*

.. _`v4l2_m2m_buf_queue.description`:

Description
-----------

Call from \ :c:func:`buf_queue`\ , videobuf_queue_ops callback.

.. This file was automatic generated / don't edit.

