.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-mem2mem.h

.. _`v4l2_m2m_ops`:

struct v4l2_m2m_ops
===================

.. c:type:: struct v4l2_m2m_ops

    mem-to-mem device driver callbacks

.. _`v4l2_m2m_ops.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_m2m_ops {
        void (*device_run)(void *priv);
        int (*job_ready)(void *priv);
        void (*job_abort)(void *priv);
        void (*lock)(void *priv);
        void (*unlock)(void *priv);
    }

.. _`v4l2_m2m_ops.members`:

Members
-------

device_run
    required. Begin the actual job (transaction) inside this
    callback.
    The job does NOT have to end before this callback returns
    (and it will be the usual case). When the job finishes,
    \ :c:func:`v4l2_m2m_job_finish`\  has to be called.

job_ready
    optional. Should return 0 if the driver does not have a job
    fully prepared to run yet (i.e. it will not be able to finish a
    transaction without sleeping). If not provided, it will be
    assumed that one source and one destination buffer are all
    that is required for the driver to perform one full transaction.
    This method may not sleep.

job_abort
    required. Informs the driver that it has to abort the currently
    running transaction as soon as possible (i.e. as soon as it can
    stop the device safely; e.g. in the next interrupt handler),
    even if the transaction would not have been finished by then.
    After the driver performs the necessary steps, it has to call
    \ :c:func:`v4l2_m2m_job_finish`\  (as if the transaction ended normally).
    This function does not have to (and will usually not) wait
    until the device enters a state when it can be stopped.

lock
    optional. Define a driver's own lock callback, instead of using
    \ :c:type:`v4l2_m2m_ctx->q_lock <v4l2_m2m_ctx>`\ .

unlock
    optional. Define a driver's own unlock callback, instead of
    using \ :c:type:`v4l2_m2m_ctx->q_lock <v4l2_m2m_ctx>`\ .

.. _`v4l2_m2m_queue_ctx`:

struct v4l2_m2m_queue_ctx
=========================

.. c:type:: struct v4l2_m2m_queue_ctx

    represents a queue for buffers ready to be processed

.. _`v4l2_m2m_queue_ctx.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_m2m_queue_ctx {
        struct vb2_queue q;
        struct list_head rdy_queue;
        spinlock_t rdy_spinlock;
        u8 num_rdy;
        bool buffered;
    }

.. _`v4l2_m2m_queue_ctx.members`:

Members
-------

q
    pointer to struct \ :c:type:`struct vb2_queue <vb2_queue>`\ 

rdy_queue
    List of V4L2 mem-to-mem queues

rdy_spinlock
    spin lock to protect the struct usage

num_rdy
    number of buffers ready to be processed

buffered
    is the queue buffered?

.. _`v4l2_m2m_queue_ctx.description`:

Description
-----------

Queue for buffers ready to be processed as soon as this
instance receives access to the device.

.. _`v4l2_m2m_ctx`:

struct v4l2_m2m_ctx
===================

.. c:type:: struct v4l2_m2m_ctx

    Memory to memory context structure

.. _`v4l2_m2m_ctx.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_m2m_ctx {
        struct mutex *q_lock;
        struct v4l2_m2m_dev *m2m_dev;
        struct v4l2_m2m_queue_ctx cap_q_ctx;
        struct v4l2_m2m_queue_ctx out_q_ctx;
        struct list_head queue;
        unsigned long job_flags;
        wait_queue_head_t finished;
        void *priv;
    }

.. _`v4l2_m2m_ctx.members`:

Members
-------

q_lock
    struct \ :c:type:`struct mutex <mutex>`\  lock

m2m_dev
    opaque pointer to the internal data to handle M2M context

cap_q_ctx
    Capture (output to memory) queue context

out_q_ctx
    Output (input from memory) queue context

queue
    List of memory to memory contexts

job_flags
    Job queue flags, used internally by v4l2-mem2mem.c:
    \ ``TRANS_QUEUED``\ , \ ``TRANS_RUNNING``\  and \ ``TRANS_ABORT``\ .

finished
    Wait queue used to signalize when a job queue finished.

priv
    Instance private data

.. _`v4l2_m2m_ctx.description`:

Description
-----------

The memory to memory context is specific to a file handle, NOT to e.g.
a device.

.. _`v4l2_m2m_buffer`:

struct v4l2_m2m_buffer
======================

.. c:type:: struct v4l2_m2m_buffer

    Memory to memory buffer

.. _`v4l2_m2m_buffer.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_m2m_buffer {
        struct vb2_v4l2_buffer vb;
        struct list_head list;
    }

.. _`v4l2_m2m_buffer.members`:

Members
-------

vb
    pointer to struct \ :c:type:`struct vb2_v4l2_buffer <vb2_v4l2_buffer>`\ 

list
    list of m2m buffers

.. _`v4l2_m2m_get_curr_priv`:

v4l2_m2m_get_curr_priv
======================

.. c:function:: void *v4l2_m2m_get_curr_priv(struct v4l2_m2m_dev *m2m_dev)

    return driver private data for the currently running instance or NULL if no instance is running

    :param struct v4l2_m2m_dev \*m2m_dev:
        opaque pointer to the internal data to handle M2M context

.. _`v4l2_m2m_get_vq`:

v4l2_m2m_get_vq
===============

.. c:function:: struct vb2_queue *v4l2_m2m_get_vq(struct v4l2_m2m_ctx *m2m_ctx, enum v4l2_buf_type type)

    return vb2_queue for the given type

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

    :param enum v4l2_buf_type type:
        type of the V4L2 buffer, as defined by enum \ :c:type:`struct v4l2_buf_type <v4l2_buf_type>`\ 

.. _`v4l2_m2m_try_schedule`:

v4l2_m2m_try_schedule
=====================

.. c:function:: void v4l2_m2m_try_schedule(struct v4l2_m2m_ctx *m2m_ctx)

    check whether an instance is ready to be added to the pending job queue and add it if so.

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

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

.. _`v4l2_m2m_job_finish`:

v4l2_m2m_job_finish
===================

.. c:function:: void v4l2_m2m_job_finish(struct v4l2_m2m_dev *m2m_dev, struct v4l2_m2m_ctx *m2m_ctx)

    inform the framework that a job has been finished and have it clean up

    :param struct v4l2_m2m_dev \*m2m_dev:
        opaque pointer to the internal data to handle M2M context

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

.. _`v4l2_m2m_job_finish.description`:

Description
-----------

Called by a driver to yield back the device after it has finished with it.
Should be called as soon as possible after reaching a state which allows
other instances to take control of the device.

This function has to be called only after \ :c:type:`v4l2_m2m_ops->device_run <v4l2_m2m_ops>`\ 
callback has been called on the driver. To prevent recursion, it should
not be called directly from the \ :c:type:`v4l2_m2m_ops->device_run <v4l2_m2m_ops>`\  callback though.

.. _`v4l2_m2m_reqbufs`:

v4l2_m2m_reqbufs
================

.. c:function:: int v4l2_m2m_reqbufs(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, struct v4l2_requestbuffers *reqbufs)

    multi-queue-aware REQBUFS multiplexer

    :param struct file \*file:
        pointer to struct \ :c:type:`struct file <file>`\ 

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

    :param struct v4l2_requestbuffers \*reqbufs:
        pointer to struct \ :c:type:`struct v4l2_requestbuffers <v4l2_requestbuffers>`\ 

.. _`v4l2_m2m_querybuf`:

v4l2_m2m_querybuf
=================

.. c:function:: int v4l2_m2m_querybuf(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, struct v4l2_buffer *buf)

    multi-queue-aware QUERYBUF multiplexer

    :param struct file \*file:
        pointer to struct \ :c:type:`struct file <file>`\ 

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

    :param struct v4l2_buffer \*buf:
        pointer to struct \ :c:type:`struct v4l2_buffer <v4l2_buffer>`\ 

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
        pointer to struct \ :c:type:`struct file <file>`\ 

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

    :param struct v4l2_buffer \*buf:
        pointer to struct \ :c:type:`struct v4l2_buffer <v4l2_buffer>`\ 

.. _`v4l2_m2m_dqbuf`:

v4l2_m2m_dqbuf
==============

.. c:function:: int v4l2_m2m_dqbuf(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, struct v4l2_buffer *buf)

    dequeue a source or destination buffer, depending on the type

    :param struct file \*file:
        pointer to struct \ :c:type:`struct file <file>`\ 

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

    :param struct v4l2_buffer \*buf:
        pointer to struct \ :c:type:`struct v4l2_buffer <v4l2_buffer>`\ 

.. _`v4l2_m2m_prepare_buf`:

v4l2_m2m_prepare_buf
====================

.. c:function:: int v4l2_m2m_prepare_buf(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, struct v4l2_buffer *buf)

    prepare a source or destination buffer, depending on the type

    :param struct file \*file:
        pointer to struct \ :c:type:`struct file <file>`\ 

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

    :param struct v4l2_buffer \*buf:
        pointer to struct \ :c:type:`struct v4l2_buffer <v4l2_buffer>`\ 

.. _`v4l2_m2m_create_bufs`:

v4l2_m2m_create_bufs
====================

.. c:function:: int v4l2_m2m_create_bufs(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, struct v4l2_create_buffers *create)

    create a source or destination buffer, depending on the type

    :param struct file \*file:
        pointer to struct \ :c:type:`struct file <file>`\ 

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

    :param struct v4l2_create_buffers \*create:
        pointer to struct \ :c:type:`struct v4l2_create_buffers <v4l2_create_buffers>`\ 

.. _`v4l2_m2m_expbuf`:

v4l2_m2m_expbuf
===============

.. c:function:: int v4l2_m2m_expbuf(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, struct v4l2_exportbuffer *eb)

    export a source or destination buffer, depending on the type

    :param struct file \*file:
        pointer to struct \ :c:type:`struct file <file>`\ 

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

    :param struct v4l2_exportbuffer \*eb:
        pointer to struct \ :c:type:`struct v4l2_exportbuffer <v4l2_exportbuffer>`\ 

.. _`v4l2_m2m_streamon`:

v4l2_m2m_streamon
=================

.. c:function:: int v4l2_m2m_streamon(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, enum v4l2_buf_type type)

    turn on streaming for a video queue

    :param struct file \*file:
        pointer to struct \ :c:type:`struct file <file>`\ 

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

    :param enum v4l2_buf_type type:
        type of the V4L2 buffer, as defined by enum \ :c:type:`struct v4l2_buf_type <v4l2_buf_type>`\ 

.. _`v4l2_m2m_streamoff`:

v4l2_m2m_streamoff
==================

.. c:function:: int v4l2_m2m_streamoff(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, enum v4l2_buf_type type)

    turn off streaming for a video queue

    :param struct file \*file:
        pointer to struct \ :c:type:`struct file <file>`\ 

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

    :param enum v4l2_buf_type type:
        type of the V4L2 buffer, as defined by enum \ :c:type:`struct v4l2_buf_type <v4l2_buf_type>`\ 

.. _`v4l2_m2m_poll`:

v4l2_m2m_poll
=============

.. c:function:: unsigned int v4l2_m2m_poll(struct file *file, struct v4l2_m2m_ctx *m2m_ctx, struct poll_table_struct *wait)

    poll replacement, for destination buffers only

    :param struct file \*file:
        pointer to struct \ :c:type:`struct file <file>`\ 

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

    :param struct poll_table_struct \*wait:
        pointer to struct \ :c:type:`struct poll_table_struct <poll_table_struct>`\ 

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
        pointer to struct \ :c:type:`struct file <file>`\ 

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

    :param struct vm_area_struct \*vma:
        pointer to struct \ :c:type:`struct vm_area_struct <vm_area_struct>`\ 

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
        pointer to struct v4l2_m2m_ops

.. _`v4l2_m2m_init.description`:

Description
-----------

Usually called from driver's ``probe()`` function.

.. _`v4l2_m2m_init.return`:

Return
------

returns an opaque pointer to the internal data to handle M2M context

.. _`v4l2_m2m_release`:

v4l2_m2m_release
================

.. c:function:: void v4l2_m2m_release(struct v4l2_m2m_dev *m2m_dev)

    cleans up and frees a m2m_dev structure

    :param struct v4l2_m2m_dev \*m2m_dev:
        opaque pointer to the internal data to handle M2M context

.. _`v4l2_m2m_release.description`:

Description
-----------

Usually called from driver's ``remove()`` function.

.. _`v4l2_m2m_ctx_init`:

v4l2_m2m_ctx_init
=================

.. c:function:: struct v4l2_m2m_ctx *v4l2_m2m_ctx_init(struct v4l2_m2m_dev *m2m_dev, void *drv_priv, int (*queue_init)(void *priv, struct vb2_queue *src_vq, struct vb2_queue *dst_vq))

    allocate and initialize a m2m context

    :param struct v4l2_m2m_dev \*m2m_dev:
        opaque pointer to the internal data to handle M2M context

    :param void \*drv_priv:
        driver's instance private data

    :param int (\*queue_init)(void \*priv, struct vb2_queue \*src_vq, struct vb2_queue \*dst_vq):
        a callback for queue type-specific initialization function
        to be used for initializing videobuf_queues

.. _`v4l2_m2m_ctx_init.description`:

Description
-----------

Usually called from driver's ``open()`` function.

.. _`v4l2_m2m_ctx_release`:

v4l2_m2m_ctx_release
====================

.. c:function:: void v4l2_m2m_ctx_release(struct v4l2_m2m_ctx *m2m_ctx)

    release m2m context

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

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
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

    :param struct vb2_v4l2_buffer \*vbuf:
        pointer to struct \ :c:type:`struct vb2_v4l2_buffer <vb2_v4l2_buffer>`\ 

.. _`v4l2_m2m_buf_queue.description`:

Description
-----------

Call from videobuf_queue_ops->ops->buf_queue, videobuf_queue_ops callback.

.. _`v4l2_m2m_num_src_bufs_ready`:

v4l2_m2m_num_src_bufs_ready
===========================

.. c:function:: unsigned int v4l2_m2m_num_src_bufs_ready(struct v4l2_m2m_ctx *m2m_ctx)

    return the number of source buffers ready for use

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

.. _`v4l2_m2m_num_dst_bufs_ready`:

v4l2_m2m_num_dst_bufs_ready
===========================

.. c:function:: unsigned int v4l2_m2m_num_dst_bufs_ready(struct v4l2_m2m_ctx *m2m_ctx)

    return the number of destination buffers ready for use

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

.. _`v4l2_m2m_next_buf`:

v4l2_m2m_next_buf
=================

.. c:function:: void *v4l2_m2m_next_buf(struct v4l2_m2m_queue_ctx *q_ctx)

    return next buffer from the list of ready buffers

    :param struct v4l2_m2m_queue_ctx \*q_ctx:
        pointer to struct \ ``v4l2_m2m_queue_ctx``\ 

.. _`v4l2_m2m_next_src_buf`:

v4l2_m2m_next_src_buf
=====================

.. c:function:: void *v4l2_m2m_next_src_buf(struct v4l2_m2m_ctx *m2m_ctx)

    return next source buffer from the list of ready buffers

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

.. _`v4l2_m2m_next_dst_buf`:

v4l2_m2m_next_dst_buf
=====================

.. c:function:: void *v4l2_m2m_next_dst_buf(struct v4l2_m2m_ctx *m2m_ctx)

    return next destination buffer from the list of ready buffers

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

.. _`v4l2_m2m_get_src_vq`:

v4l2_m2m_get_src_vq
===================

.. c:function:: struct vb2_queue *v4l2_m2m_get_src_vq(struct v4l2_m2m_ctx *m2m_ctx)

    return vb2_queue for source buffers

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

.. _`v4l2_m2m_get_dst_vq`:

v4l2_m2m_get_dst_vq
===================

.. c:function:: struct vb2_queue *v4l2_m2m_get_dst_vq(struct v4l2_m2m_ctx *m2m_ctx)

    return vb2_queue for destination buffers

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

.. _`v4l2_m2m_buf_remove`:

v4l2_m2m_buf_remove
===================

.. c:function:: void *v4l2_m2m_buf_remove(struct v4l2_m2m_queue_ctx *q_ctx)

    take off a buffer from the list of ready buffers and return it

    :param struct v4l2_m2m_queue_ctx \*q_ctx:
        pointer to struct \ ``v4l2_m2m_queue_ctx``\ 

.. _`v4l2_m2m_src_buf_remove`:

v4l2_m2m_src_buf_remove
=======================

.. c:function:: void *v4l2_m2m_src_buf_remove(struct v4l2_m2m_ctx *m2m_ctx)

    take off a source buffer from the list of ready buffers and return it

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

.. _`v4l2_m2m_dst_buf_remove`:

v4l2_m2m_dst_buf_remove
=======================

.. c:function:: void *v4l2_m2m_dst_buf_remove(struct v4l2_m2m_ctx *m2m_ctx)

    take off a destination buffer from the list of ready buffers and return it

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        m2m context assigned to the instance given by struct \ :c:type:`struct v4l2_m2m_ctx <v4l2_m2m_ctx>`\ 

.. This file was automatic generated / don't edit.

