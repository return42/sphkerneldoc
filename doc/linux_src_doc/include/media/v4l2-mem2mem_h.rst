.. -*- coding: utf-8; mode: rst -*-

==============
v4l2-mem2mem.h
==============


.. _`v4l2_m2m_ops`:

struct v4l2_m2m_ops
===================

.. c:type:: v4l2_m2m_ops

    mem-to-mem device driver callbacks


.. _`v4l2_m2m_ops.definition`:

Definition
----------

.. code-block:: c

  struct v4l2_m2m_ops {
    void (* device_run) (void *priv);
    int (* job_ready) (void *priv);
    void (* job_abort) (void *priv);
    void (* lock) (void *priv);
    void (* unlock) (void *priv);
  };


.. _`v4l2_m2m_ops.members`:

Members
-------

:``device_run``:
    required. Begin the actual job (transaction) inside this
    callback.
    The job does NOT have to end before this callback returns
    (and it will be the usual case). When the job finishes,
    :c:func:`v4l2_m2m_job_finish` has to be called.

:``job_ready``:
    optional. Should return 0 if the driver does not have a job
    fully prepared to run yet (i.e. it will not be able to finish a
    transaction without sleeping). If not provided, it will be
    assumed that one source and one destination buffer are all
    that is required for the driver to perform one full transaction.
    This method may not sleep.

:``job_abort``:
    required. Informs the driver that it has to abort the currently
    running transaction as soon as possible (i.e. as soon as it can
    stop the device safely; e.g. in the next interrupt handler),
    even if the transaction would not have been finished by then.
    After the driver performs the necessary steps, it has to call
    :c:func:`v4l2_m2m_job_finish` (as if the transaction ended normally).
    This function does not have to (and will usually not) wait
    until the device enters a state when it can be stopped.

:``lock``:
    optional. Define a driver's own lock callback, instead of using
    m2m_ctx->q_lock.

:``unlock``:
    optional. Define a driver's own unlock callback, instead of
    using m2m_ctx->q_lock.




.. _`v4l2_m2m_num_src_bufs_ready`:

v4l2_m2m_num_src_bufs_ready
===========================

.. c:function:: unsigned int v4l2_m2m_num_src_bufs_ready (struct v4l2_m2m_ctx *m2m_ctx)

    return the number of source buffers ready for use

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        pointer to struct v4l2_m2m_ctx



.. _`v4l2_m2m_num_dst_bufs_ready`:

v4l2_m2m_num_dst_bufs_ready
===========================

.. c:function:: unsigned int v4l2_m2m_num_dst_bufs_ready (struct v4l2_m2m_ctx *m2m_ctx)

    return the number of destination buffers ready for use

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        pointer to struct v4l2_m2m_ctx



.. _`v4l2_m2m_next_src_buf`:

v4l2_m2m_next_src_buf
=====================

.. c:function:: void *v4l2_m2m_next_src_buf (struct v4l2_m2m_ctx *m2m_ctx)

    return next source buffer from the list of ready buffers

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        pointer to struct v4l2_m2m_ctx



.. _`v4l2_m2m_next_dst_buf`:

v4l2_m2m_next_dst_buf
=====================

.. c:function:: void *v4l2_m2m_next_dst_buf (struct v4l2_m2m_ctx *m2m_ctx)

    return next destination buffer from the list of ready buffers

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        pointer to struct v4l2_m2m_ctx



.. _`v4l2_m2m_get_src_vq`:

v4l2_m2m_get_src_vq
===================

.. c:function:: struct vb2_queue *v4l2_m2m_get_src_vq (struct v4l2_m2m_ctx *m2m_ctx)

    return vb2_queue for source buffers

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        pointer to struct v4l2_m2m_ctx



.. _`v4l2_m2m_get_dst_vq`:

v4l2_m2m_get_dst_vq
===================

.. c:function:: struct vb2_queue *v4l2_m2m_get_dst_vq (struct v4l2_m2m_ctx *m2m_ctx)

    return vb2_queue for destination buffers

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        pointer to struct v4l2_m2m_ctx



.. _`v4l2_m2m_src_buf_remove`:

v4l2_m2m_src_buf_remove
=======================

.. c:function:: void *v4l2_m2m_src_buf_remove (struct v4l2_m2m_ctx *m2m_ctx)

    take off a source buffer from the list of ready buffers and return it

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        pointer to struct v4l2_m2m_ctx



.. _`v4l2_m2m_dst_buf_remove`:

v4l2_m2m_dst_buf_remove
=======================

.. c:function:: void *v4l2_m2m_dst_buf_remove (struct v4l2_m2m_ctx *m2m_ctx)

    take off a destination buffer from the list of ready buffers and return it

    :param struct v4l2_m2m_ctx \*m2m_ctx:
        pointer to struct v4l2_m2m_ctx

