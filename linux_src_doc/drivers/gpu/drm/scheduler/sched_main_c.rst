.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/scheduler/sched_main.c

.. _`overview`:

Overview
========

The GPU scheduler provides entities which allow userspace to push jobs
into software queues which are then scheduled on a hardware run queue.
The software queues have a priority among them. The scheduler selects the entities
from the run queue using a FIFO. The scheduler provides dependency handling
features among jobs. The driver is supposed to provide callback functions for
backend operations to the scheduler like submitting a job to hardware run queue,
returning the dependencies of a job etc.

The organisation of the scheduler is the following:

1. Each hw run queue has one scheduler
2. Each scheduler has multiple run queues with different priorities
   (e.g., HIGH_HW,HIGH_SW, KERNEL, NORMAL)
3. Each scheduler run queue has a queue of entities to schedule
4. Entities themselves maintain a queue of jobs that will be scheduled on
   the hardware.

The jobs in a entity are always scheduled in the order that they were pushed.

.. _`drm_sched_rq_init`:

drm_sched_rq_init
=================

.. c:function:: void drm_sched_rq_init(struct drm_gpu_scheduler *sched, struct drm_sched_rq *rq)

    initialize a given run queue struct

    :param sched:
        *undescribed*
    :type sched: struct drm_gpu_scheduler \*

    :param rq:
        scheduler run queue
    :type rq: struct drm_sched_rq \*

.. _`drm_sched_rq_init.description`:

Description
-----------

Initializes a scheduler runqueue.

.. _`drm_sched_rq_add_entity`:

drm_sched_rq_add_entity
=======================

.. c:function:: void drm_sched_rq_add_entity(struct drm_sched_rq *rq, struct drm_sched_entity *entity)

    add an entity

    :param rq:
        scheduler run queue
    :type rq: struct drm_sched_rq \*

    :param entity:
        scheduler entity
    :type entity: struct drm_sched_entity \*

.. _`drm_sched_rq_add_entity.description`:

Description
-----------

Adds a scheduler entity to the run queue.

.. _`drm_sched_rq_remove_entity`:

drm_sched_rq_remove_entity
==========================

.. c:function:: void drm_sched_rq_remove_entity(struct drm_sched_rq *rq, struct drm_sched_entity *entity)

    remove an entity

    :param rq:
        scheduler run queue
    :type rq: struct drm_sched_rq \*

    :param entity:
        scheduler entity
    :type entity: struct drm_sched_entity \*

.. _`drm_sched_rq_remove_entity.description`:

Description
-----------

Removes a scheduler entity from the run queue.

.. _`drm_sched_rq_select_entity`:

drm_sched_rq_select_entity
==========================

.. c:function:: struct drm_sched_entity *drm_sched_rq_select_entity(struct drm_sched_rq *rq)

    Select an entity which could provide a job to run

    :param rq:
        scheduler run queue to check.
    :type rq: struct drm_sched_rq \*

.. _`drm_sched_rq_select_entity.description`:

Description
-----------

Try to find a ready entity, returns NULL if none found.

.. _`drm_sched_dependency_optimized`:

drm_sched_dependency_optimized
==============================

.. c:function:: bool drm_sched_dependency_optimized(struct dma_fence* fence, struct drm_sched_entity *entity)

    :param fence:
        the dependency fence
    :type fence: struct dma_fence\*

    :param entity:
        the entity which depends on the above fence
    :type entity: struct drm_sched_entity \*

.. _`drm_sched_dependency_optimized.description`:

Description
-----------

Returns true if the dependency can be optimized and false otherwise

.. _`drm_sched_start_timeout`:

drm_sched_start_timeout
=======================

.. c:function:: void drm_sched_start_timeout(struct drm_gpu_scheduler *sched)

    start timeout for reset worker

    :param sched:
        scheduler instance to start the worker for
    :type sched: struct drm_gpu_scheduler \*

.. _`drm_sched_start_timeout.description`:

Description
-----------

Start the timeout for the given scheduler.

.. _`drm_sched_hw_job_reset`:

drm_sched_hw_job_reset
======================

.. c:function:: void drm_sched_hw_job_reset(struct drm_gpu_scheduler *sched, struct drm_sched_job *bad)

    stop the scheduler if it contains the bad job

    :param sched:
        scheduler instance
    :type sched: struct drm_gpu_scheduler \*

    :param bad:
        bad scheduler job
    :type bad: struct drm_sched_job \*

.. _`drm_sched_job_recovery`:

drm_sched_job_recovery
======================

.. c:function:: void drm_sched_job_recovery(struct drm_gpu_scheduler *sched)

    recover jobs after a reset

    :param sched:
        scheduler instance
    :type sched: struct drm_gpu_scheduler \*

.. _`drm_sched_job_init`:

drm_sched_job_init
==================

.. c:function:: int drm_sched_job_init(struct drm_sched_job *job, struct drm_sched_entity *entity, void *owner)

    init a scheduler job

    :param job:
        scheduler job to init
    :type job: struct drm_sched_job \*

    :param entity:
        scheduler entity to use
    :type entity: struct drm_sched_entity \*

    :param owner:
        job owner for debugging
    :type owner: void \*

.. _`drm_sched_job_init.description`:

Description
-----------

Refer to \ :c:func:`drm_sched_entity_push_job`\  documentation
for locking considerations.

Returns 0 for success, negative error code otherwise.

.. _`drm_sched_ready`:

drm_sched_ready
===============

.. c:function:: bool drm_sched_ready(struct drm_gpu_scheduler *sched)

    is the scheduler ready

    :param sched:
        scheduler instance
    :type sched: struct drm_gpu_scheduler \*

.. _`drm_sched_ready.description`:

Description
-----------

Return true if we can push more jobs to the hw, otherwise false.

.. _`drm_sched_wakeup`:

drm_sched_wakeup
================

.. c:function:: void drm_sched_wakeup(struct drm_gpu_scheduler *sched)

    Wake up the scheduler when it is ready

    :param sched:
        scheduler instance
    :type sched: struct drm_gpu_scheduler \*

.. _`drm_sched_select_entity`:

drm_sched_select_entity
=======================

.. c:function:: struct drm_sched_entity *drm_sched_select_entity(struct drm_gpu_scheduler *sched)

    Select next entity to process

    :param sched:
        scheduler instance
    :type sched: struct drm_gpu_scheduler \*

.. _`drm_sched_select_entity.description`:

Description
-----------

Returns the entity to process or NULL if none are found.

.. _`drm_sched_process_job`:

drm_sched_process_job
=====================

.. c:function:: void drm_sched_process_job(struct dma_fence *f, struct dma_fence_cb *cb)

    process a job

    :param f:
        fence
    :type f: struct dma_fence \*

    :param cb:
        fence callbacks
    :type cb: struct dma_fence_cb \*

.. _`drm_sched_process_job.description`:

Description
-----------

Called after job has finished execution.

.. _`drm_sched_blocked`:

drm_sched_blocked
=================

.. c:function:: bool drm_sched_blocked(struct drm_gpu_scheduler *sched)

    check if the scheduler is blocked

    :param sched:
        scheduler instance
    :type sched: struct drm_gpu_scheduler \*

.. _`drm_sched_blocked.description`:

Description
-----------

Returns true if blocked, otherwise false.

.. _`drm_sched_main`:

drm_sched_main
==============

.. c:function:: int drm_sched_main(void *param)

    main scheduler thread

    :param param:
        scheduler instance
    :type param: void \*

.. _`drm_sched_main.description`:

Description
-----------

Returns 0.

.. _`drm_sched_init`:

drm_sched_init
==============

.. c:function:: int drm_sched_init(struct drm_gpu_scheduler *sched, const struct drm_sched_backend_ops *ops, unsigned hw_submission, unsigned hang_limit, long timeout, const char *name)

    Init a gpu scheduler instance

    :param sched:
        scheduler instance
    :type sched: struct drm_gpu_scheduler \*

    :param ops:
        backend operations for this scheduler
    :type ops: const struct drm_sched_backend_ops \*

    :param hw_submission:
        number of hw submissions that can be in flight
    :type hw_submission: unsigned

    :param hang_limit:
        number of times to allow a job to hang before dropping it
    :type hang_limit: unsigned

    :param timeout:
        timeout value in jiffies for the scheduler
    :type timeout: long

    :param name:
        name used for debugging
    :type name: const char \*

.. _`drm_sched_init.description`:

Description
-----------

Return 0 on success, otherwise error code.

.. _`drm_sched_fini`:

drm_sched_fini
==============

.. c:function:: void drm_sched_fini(struct drm_gpu_scheduler *sched)

    Destroy a gpu scheduler

    :param sched:
        scheduler instance
    :type sched: struct drm_gpu_scheduler \*

.. _`drm_sched_fini.description`:

Description
-----------

Tears down and cleans up the scheduler.

.. This file was automatic generated / don't edit.

