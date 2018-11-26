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
    #ifdef CONFIG_MEDIA_CONTROLLER
        struct media_entity *source;
        struct media_pad source_pad;
        struct media_entity sink;
        struct media_pad sink_pad;
        struct media_entity proc;
        struct media_pad proc_pads[2];
        struct media_intf_devnode *intf_devnode;
    #endif
        struct list_head job_queue;
        spinlock_t job_spinlock;
        const struct v4l2_m2m_ops *m2m_ops;
    }

.. _`v4l2_m2m_dev.members`:

Members
-------

curr_ctx
    currently running instance

source
    \ :c:type:`struct media_entity <media_entity>`\  pointer with the source entity
    Used only when the M2M device is registered via
    \ :c:func:`v4l2_m2m_unregister_media_controller`\ .

source_pad
    \ :c:type:`struct media_pad <media_pad>`\  with the source pad.
    Used only when the M2M device is registered via
    \ :c:func:`v4l2_m2m_unregister_media_controller`\ .

sink
    \ :c:type:`struct media_entity <media_entity>`\  pointer with the sink entity
    Used only when the M2M device is registered via
    \ :c:func:`v4l2_m2m_unregister_media_controller`\ .

sink_pad
    \ :c:type:`struct media_pad <media_pad>`\  with the sink pad.
    Used only when the M2M device is registered via
    \ :c:func:`v4l2_m2m_unregister_media_controller`\ .

proc
    \ :c:type:`struct media_entity <media_entity>`\  pointer with the M2M device itself.

proc_pads
    \ :c:type:`struct media_pad <media_pad>`\  with the \ ``proc``\  pads.
    Used only when the M2M device is registered via
    \ :c:func:`v4l2_m2m_unregister_media_controller`\ .

intf_devnode
    \ :c:type:`struct media_intf <media_intf>`\  devnode pointer with the interface
    with controls the M2M device.

job_queue
    instances queued to run

job_spinlock
    protects job_queue

m2m_ops
    driver callbacks

.. _`v4l2_m2m_try_run`:

v4l2_m2m_try_run
================

.. c:function:: void v4l2_m2m_try_run(struct v4l2_m2m_dev *m2m_dev)

    select next job to perform and run it if possible

    :param m2m_dev:
        per-device context
    :type m2m_dev: struct v4l2_m2m_dev \*

.. _`v4l2_m2m_try_run.description`:

Description
-----------

Get next transaction (if present) from the waiting jobs list and run it.

.. _`v4l2_m2m_try_schedule`:

v4l2_m2m_try_schedule
=====================

.. c:function:: void v4l2_m2m_try_schedule(struct v4l2_m2m_ctx *m2m_ctx)

    schedule and possibly run a job for any context

    :param m2m_ctx:
        m2m context
    :type m2m_ctx: struct v4l2_m2m_ctx \*

.. _`v4l2_m2m_try_schedule.description`:

Description
-----------

Check if this context is ready to queue a job. If suitable,
run the next queued job on the mem2mem device.

This function shouldn't run in interrupt context.

Note that \ :c:func:`v4l2_m2m_try_schedule`\  can schedule one job for this context,
and then run another job for another context.

.. _`v4l2_m2m_cancel_job`:

v4l2_m2m_cancel_job
===================

.. c:function:: void v4l2_m2m_cancel_job(struct v4l2_m2m_ctx *m2m_ctx)

    cancel pending jobs for the context

    :param m2m_ctx:
        m2m context with jobs to be canceled
    :type m2m_ctx: struct v4l2_m2m_ctx \*

.. _`v4l2_m2m_cancel_job.description`:

Description
-----------

In case of streamoff or release called on any context,
1] If the context is currently running, then abort job will be called
2] If the context is queued, then the context will be removed from
the job_queue

.. This file was automatic generated / don't edit.

