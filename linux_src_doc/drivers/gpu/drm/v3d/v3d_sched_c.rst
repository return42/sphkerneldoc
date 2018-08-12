.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/v3d/v3d_sched.c

.. _`broadcom-v3d-scheduling`:

Broadcom V3D scheduling
=======================

The shared DRM GPU scheduler is used to coordinate submitting jobs
to the hardware.  Each DRM fd (roughly a client process) gets its
own scheduler entity, which will process jobs in order.  The GPU
scheduler will round-robin between clients to submit the next job.

For simplicity, and in order to keep latency low for interactive
jobs when bulk background jobs are queued up, we submit a new job
to the HW only when it has completed the last one, instead of
filling up the CT[01]Q FIFOs with jobs.  Similarly, we use
\ :c:func:`v3d_job_dependency`\  to manage the dependency between bin and
render, instead of having the clients submit jobs with using the
HW's semaphores to interlock between them.

.. _`v3d_job_dependency`:

v3d_job_dependency
==================

.. c:function:: struct dma_fence *v3d_job_dependency(struct drm_sched_job *sched_job, struct drm_sched_entity *s_entity)

    \ :c:func:`v3d_job_run`\  won't be called until all of them have been signaled.

    :param struct drm_sched_job \*sched_job:
        *undescribed*

    :param struct drm_sched_entity \*s_entity:
        *undescribed*

.. This file was automatic generated / don't edit.

