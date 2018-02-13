.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/scheduler/gpu_scheduler.c

.. _`drm_sched_rq_select_entity`:

drm_sched_rq_select_entity
==========================

.. c:function:: struct drm_sched_entity *drm_sched_rq_select_entity(struct drm_sched_rq *rq)

    :param struct drm_sched_rq \*rq:
        *undescribed*

.. _`drm_sched_rq_select_entity.description`:

Description
-----------

\ ``rq``\           The run queue to check.

Try to find a ready entity, returns NULL if none found.

.. _`drm_sched_entity_init`:

drm_sched_entity_init
=====================

.. c:function:: int drm_sched_entity_init(struct drm_gpu_scheduler *sched, struct drm_sched_entity *entity, struct drm_sched_rq *rq, uint32_t jobs, atomic_t *guilty)

    :param struct drm_gpu_scheduler \*sched:
        *undescribed*

    :param struct drm_sched_entity \*entity:
        *undescribed*

    :param struct drm_sched_rq \*rq:
        *undescribed*

    :param uint32_t jobs:
        *undescribed*

    :param atomic_t \*guilty:
        *undescribed*

.. _`drm_sched_entity_init.description`:

Description
-----------

\ ``sched``\        The pointer to the scheduler
\ ``entity``\       The pointer to a valid drm_sched_entity
\ ``rq``\           The run queue this entity belongs
\ ``kernel``\       If this is an entity for the kernel
\ ``jobs``\         The max number of jobs in the job queue

return 0 if succeed. negative error code on failure

.. _`drm_sched_entity_is_initialized`:

drm_sched_entity_is_initialized
===============================

.. c:function:: bool drm_sched_entity_is_initialized(struct drm_gpu_scheduler *sched, struct drm_sched_entity *entity)

    :param struct drm_gpu_scheduler \*sched:
        *undescribed*

    :param struct drm_sched_entity \*entity:
        *undescribed*

.. _`drm_sched_entity_is_initialized.description`:

Description
-----------

\ ``sched``\        Pointer to scheduler instance
\ ``entity``\       The pointer to a valid scheduler entity

return true if entity is initialized, false otherwise

.. _`drm_sched_entity_is_idle`:

drm_sched_entity_is_idle
========================

.. c:function:: bool drm_sched_entity_is_idle(struct drm_sched_entity *entity)

    :param struct drm_sched_entity \*entity:
        *undescribed*

.. _`drm_sched_entity_is_idle.description`:

Description
-----------

\ ``entity``\       The pointer to a valid scheduler entity

Return true if entity don't has any unscheduled jobs.

.. _`drm_sched_entity_is_ready`:

drm_sched_entity_is_ready
=========================

.. c:function:: bool drm_sched_entity_is_ready(struct drm_sched_entity *entity)

    :param struct drm_sched_entity \*entity:
        *undescribed*

.. _`drm_sched_entity_is_ready.description`:

Description
-----------

\ ``entity``\       The pointer to a valid scheduler entity

Return true if entity could provide a job.

.. _`drm_sched_entity_fini`:

drm_sched_entity_fini
=====================

.. c:function:: void drm_sched_entity_fini(struct drm_gpu_scheduler *sched, struct drm_sched_entity *entity)

    :param struct drm_gpu_scheduler \*sched:
        *undescribed*

    :param struct drm_sched_entity \*entity:
        *undescribed*

.. _`drm_sched_entity_fini.description`:

Description
-----------

\ ``sched``\        Pointer to scheduler instance
\ ``entity``\       The pointer to a valid scheduler entity

Cleanup and free the allocated resources.

.. _`drm_sched_entity_push_job`:

drm_sched_entity_push_job
=========================

.. c:function:: void drm_sched_entity_push_job(struct drm_sched_job *sched_job, struct drm_sched_entity *entity)

    :param struct drm_sched_job \*sched_job:
        *undescribed*

    :param struct drm_sched_entity \*entity:
        *undescribed*

.. _`drm_sched_entity_push_job.description`:

Description
-----------

\ ``sched_job``\            The pointer to job required to submit

Returns 0 for success, negative error code otherwise.

.. _`drm_sched_ready`:

drm_sched_ready
===============

.. c:function:: bool drm_sched_ready(struct drm_gpu_scheduler *sched)

    :param struct drm_gpu_scheduler \*sched:
        *undescribed*

.. _`drm_sched_wakeup`:

drm_sched_wakeup
================

.. c:function:: void drm_sched_wakeup(struct drm_gpu_scheduler *sched)

    :param struct drm_gpu_scheduler \*sched:
        *undescribed*

.. _`drm_sched_select_entity`:

drm_sched_select_entity
=======================

.. c:function:: struct drm_sched_entity *drm_sched_select_entity(struct drm_gpu_scheduler *sched)

    :param struct drm_gpu_scheduler \*sched:
        *undescribed*

.. _`drm_sched_init`:

drm_sched_init
==============

.. c:function:: int drm_sched_init(struct drm_gpu_scheduler *sched, const struct drm_sched_backend_ops *ops, unsigned hw_submission, unsigned hang_limit, long timeout, const char *name)

    :param struct drm_gpu_scheduler \*sched:
        *undescribed*

    :param const struct drm_sched_backend_ops \*ops:
        *undescribed*

    :param unsigned hw_submission:
        *undescribed*

    :param unsigned hang_limit:
        *undescribed*

    :param long timeout:
        *undescribed*

    :param const char \*name:
        *undescribed*

.. _`drm_sched_init.description`:

Description
-----------

\ ``sched``\                The pointer to the scheduler
\ ``ops``\                  The backend operations for this scheduler.
\ ``hw_submissions``\       Number of hw submissions to do.
\ ``name``\                 Name used for debugging

Return 0 on success, otherwise error code.

.. _`drm_sched_fini`:

drm_sched_fini
==============

.. c:function:: void drm_sched_fini(struct drm_gpu_scheduler *sched)

    :param struct drm_gpu_scheduler \*sched:
        *undescribed*

.. _`drm_sched_fini.description`:

Description
-----------

\ ``sched``\        The pointer to the scheduler

.. This file was automatic generated / don't edit.

