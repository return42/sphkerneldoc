.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/scheduler/sched_entity.c

.. _`drm_sched_entity_init`:

drm_sched_entity_init
=====================

.. c:function:: int drm_sched_entity_init(struct drm_sched_entity *entity, struct drm_sched_rq **rq_list, unsigned int num_rq_list, atomic_t *guilty)

    Init a context entity used by scheduler when submit to HW ring.

    :param entity:
        scheduler entity to init
    :type entity: struct drm_sched_entity \*

    :param rq_list:
        the list of run queue on which jobs from this
        entity can be submitted
    :type rq_list: struct drm_sched_rq \*\*

    :param num_rq_list:
        number of run queue in rq_list
    :type num_rq_list: unsigned int

    :param guilty:
        atomic_t set to 1 when a job on this queue
        is found to be guilty causing a timeout
    :type guilty: atomic_t \*

.. _`drm_sched_entity_init.note`:

Note
----

the rq_list should have atleast one element to schedule
the entity

Returns 0 on success or a negative error code on failure.

.. _`drm_sched_entity_is_idle`:

drm_sched_entity_is_idle
========================

.. c:function:: bool drm_sched_entity_is_idle(struct drm_sched_entity *entity)

    Check if entity is idle

    :param entity:
        scheduler entity
    :type entity: struct drm_sched_entity \*

.. _`drm_sched_entity_is_idle.description`:

Description
-----------

Returns true if the entity does not have any unscheduled jobs.

.. _`drm_sched_entity_is_ready`:

drm_sched_entity_is_ready
=========================

.. c:function:: bool drm_sched_entity_is_ready(struct drm_sched_entity *entity)

    Check if entity is ready

    :param entity:
        scheduler entity
    :type entity: struct drm_sched_entity \*

.. _`drm_sched_entity_is_ready.description`:

Description
-----------

Return true if entity could provide a job.

.. _`drm_sched_entity_get_free_sched`:

drm_sched_entity_get_free_sched
===============================

.. c:function:: struct drm_sched_rq *drm_sched_entity_get_free_sched(struct drm_sched_entity *entity)

    Get the rq from rq_list with least load

    :param entity:
        scheduler entity
    :type entity: struct drm_sched_entity \*

.. _`drm_sched_entity_get_free_sched.description`:

Description
-----------

Return the pointer to the rq with least load.

.. _`drm_sched_entity_flush`:

drm_sched_entity_flush
======================

.. c:function:: long drm_sched_entity_flush(struct drm_sched_entity *entity, long timeout)

    Flush a context entity

    :param entity:
        scheduler entity
    :type entity: struct drm_sched_entity \*

    :param timeout:
        time to wait in for Q to become empty in jiffies.
    :type timeout: long

.. _`drm_sched_entity_flush.description`:

Description
-----------

Splitting \ :c:func:`drm_sched_entity_fini`\  into two functions, The first one does the
waiting, removes the entity from the runqueue and returns an error when the
process was killed.

Returns the remaining time in jiffies left from the input timeout

.. _`drm_sched_entity_kill_jobs_cb`:

drm_sched_entity_kill_jobs_cb
=============================

.. c:function:: void drm_sched_entity_kill_jobs_cb(struct dma_fence *f, struct dma_fence_cb *cb)

    helper for drm_sched_entity_kill_jobs

    :param f:
        signaled fence
    :type f: struct dma_fence \*

    :param cb:
        our callback structure
    :type cb: struct dma_fence_cb \*

.. _`drm_sched_entity_kill_jobs_cb.description`:

Description
-----------

Signal the scheduler finished fence when the entity in question is killed.

.. _`drm_sched_entity_kill_jobs`:

drm_sched_entity_kill_jobs
==========================

.. c:function:: void drm_sched_entity_kill_jobs(struct drm_sched_entity *entity)

    Make sure all remaining jobs are killed

    :param entity:
        entity which is cleaned up
    :type entity: struct drm_sched_entity \*

.. _`drm_sched_entity_kill_jobs.description`:

Description
-----------

Makes sure that all remaining jobs in an entity are killed before it is
destroyed.

.. _`drm_sched_entity_fini`:

drm_sched_entity_fini
=====================

.. c:function:: void drm_sched_entity_fini(struct drm_sched_entity *entity)

    Destroy a context entity

    :param entity:
        scheduler entity
    :type entity: struct drm_sched_entity \*

.. _`drm_sched_entity_fini.description`:

Description
-----------

This should be called after \ ``drm_sched_entity_do_release``\ . It goes over the
entity and signals all jobs with an error code if the process was killed.

.. _`drm_sched_entity_destroy`:

drm_sched_entity_destroy
========================

.. c:function:: void drm_sched_entity_destroy(struct drm_sched_entity *entity)

    Destroy a context entity

    :param entity:
        scheduler entity
    :type entity: struct drm_sched_entity \*

.. _`drm_sched_entity_destroy.description`:

Description
-----------

Calls \ :c:func:`drm_sched_entity_do_release`\  and \ :c:func:`drm_sched_entity_cleanup`\ 

.. _`drm_sched_entity_clear_dep`:

drm_sched_entity_clear_dep
==========================

.. c:function:: void drm_sched_entity_clear_dep(struct dma_fence *f, struct dma_fence_cb *cb)

    callback to clear the entities dependency

    :param f:
        *undescribed*
    :type f: struct dma_fence \*

    :param cb:
        *undescribed*
    :type cb: struct dma_fence_cb \*

.. _`drm_sched_entity_wakeup`:

drm_sched_entity_wakeup
=======================

.. c:function:: void drm_sched_entity_wakeup(struct dma_fence *f, struct dma_fence_cb *cb)

    callback to clear the entities dependency and wake up scheduler

    :param f:
        *undescribed*
    :type f: struct dma_fence \*

    :param cb:
        *undescribed*
    :type cb: struct dma_fence_cb \*

.. _`drm_sched_entity_set_rq_priority`:

drm_sched_entity_set_rq_priority
================================

.. c:function:: void drm_sched_entity_set_rq_priority(struct drm_sched_rq **rq, enum drm_sched_priority priority)

    helper for drm_sched_entity_set_priority

    :param rq:
        *undescribed*
    :type rq: struct drm_sched_rq \*\*

    :param priority:
        *undescribed*
    :type priority: enum drm_sched_priority

.. _`drm_sched_entity_set_priority`:

drm_sched_entity_set_priority
=============================

.. c:function:: void drm_sched_entity_set_priority(struct drm_sched_entity *entity, enum drm_sched_priority priority)

    Sets priority of the entity

    :param entity:
        scheduler entity
    :type entity: struct drm_sched_entity \*

    :param priority:
        scheduler priority
    :type priority: enum drm_sched_priority

.. _`drm_sched_entity_set_priority.description`:

Description
-----------

Update the priority of runqueus used for the entity.

.. _`drm_sched_entity_add_dependency_cb`:

drm_sched_entity_add_dependency_cb
==================================

.. c:function:: bool drm_sched_entity_add_dependency_cb(struct drm_sched_entity *entity)

    add callback for the entities dependency

    :param entity:
        entity with dependency
    :type entity: struct drm_sched_entity \*

.. _`drm_sched_entity_add_dependency_cb.description`:

Description
-----------

Add a callback to the current dependency of the entity to wake up the
scheduler when the entity becomes available.

.. _`drm_sched_entity_pop_job`:

drm_sched_entity_pop_job
========================

.. c:function:: struct drm_sched_job *drm_sched_entity_pop_job(struct drm_sched_entity *entity)

    get a ready to be scheduled job from the entity

    :param entity:
        entity to get the job from
    :type entity: struct drm_sched_entity \*

.. _`drm_sched_entity_pop_job.description`:

Description
-----------

Process all dependencies and try to get one job from the entities queue.

.. _`drm_sched_entity_select_rq`:

drm_sched_entity_select_rq
==========================

.. c:function:: void drm_sched_entity_select_rq(struct drm_sched_entity *entity)

    select a new rq for the entity

    :param entity:
        scheduler entity
    :type entity: struct drm_sched_entity \*

.. _`drm_sched_entity_select_rq.description`:

Description
-----------

Check all prerequisites and select a new rq for the entity for load
balancing.

.. _`drm_sched_entity_push_job`:

drm_sched_entity_push_job
=========================

.. c:function:: void drm_sched_entity_push_job(struct drm_sched_job *sched_job, struct drm_sched_entity *entity)

    Submit a job to the entity's job queue

    :param sched_job:
        job to submit
    :type sched_job: struct drm_sched_job \*

    :param entity:
        scheduler entity
    :type entity: struct drm_sched_entity \*

.. _`drm_sched_entity_push_job.note`:

Note
----

To guarantee that the order of insertion to queue matches
the job's fence sequence number this function should be
called with drm_sched_job_init under common lock.

Returns 0 for success, negative error code otherwise.

.. This file was automatic generated / don't edit.

