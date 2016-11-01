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

.. This file was automatic generated / don't edit.

