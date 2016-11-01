.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/scheduler/gpu_scheduler.c

.. _`amd_sched_rq_select_entity`:

amd_sched_rq_select_entity
==========================

.. c:function:: struct amd_sched_entity *amd_sched_rq_select_entity(struct amd_sched_rq *rq)

    :param struct amd_sched_rq \*rq:
        *undescribed*

.. _`amd_sched_rq_select_entity.description`:

Description
-----------

@rq          The run queue to check.

Try to find a ready entity, returns NULL if none found.

.. _`amd_sched_entity_init`:

amd_sched_entity_init
=====================

.. c:function:: int amd_sched_entity_init(struct amd_gpu_scheduler *sched, struct amd_sched_entity *entity, struct amd_sched_rq *rq, uint32_t jobs)

    :param struct amd_gpu_scheduler \*sched:
        *undescribed*

    :param struct amd_sched_entity \*entity:
        *undescribed*

    :param struct amd_sched_rq \*rq:
        *undescribed*

    :param uint32_t jobs:
        *undescribed*

.. _`amd_sched_entity_init.description`:

Description
-----------

@sched       The pointer to the scheduler
\ ``entity``\       The pointer to a valid amd_sched_entity
\ ``rq``\           The run queue this entity belongs
\ ``kernel``\       If this is an entity for the kernel
\ ``jobs``\         The max number of jobs in the job queue

return 0 if succeed. negative error code on failure

.. _`amd_sched_entity_is_initialized`:

amd_sched_entity_is_initialized
===============================

.. c:function:: bool amd_sched_entity_is_initialized(struct amd_gpu_scheduler *sched, struct amd_sched_entity *entity)

    :param struct amd_gpu_scheduler \*sched:
        *undescribed*

    :param struct amd_sched_entity \*entity:
        *undescribed*

.. _`amd_sched_entity_is_initialized.description`:

Description
-----------

@sched       Pointer to scheduler instance
\ ``entity``\       The pointer to a valid scheduler entity

return true if entity is initialized, false otherwise

.. _`amd_sched_entity_is_idle`:

amd_sched_entity_is_idle
========================

.. c:function:: bool amd_sched_entity_is_idle(struct amd_sched_entity *entity)

    :param struct amd_sched_entity \*entity:
        *undescribed*

.. _`amd_sched_entity_is_idle.description`:

Description
-----------

@entity      The pointer to a valid scheduler entity

Return true if entity don't has any unscheduled jobs.

.. _`amd_sched_entity_is_ready`:

amd_sched_entity_is_ready
=========================

.. c:function:: bool amd_sched_entity_is_ready(struct amd_sched_entity *entity)

    :param struct amd_sched_entity \*entity:
        *undescribed*

.. _`amd_sched_entity_is_ready.description`:

Description
-----------

@entity      The pointer to a valid scheduler entity

Return true if entity could provide a job.

.. _`amd_sched_entity_fini`:

amd_sched_entity_fini
=====================

.. c:function:: void amd_sched_entity_fini(struct amd_gpu_scheduler *sched, struct amd_sched_entity *entity)

    :param struct amd_gpu_scheduler \*sched:
        *undescribed*

    :param struct amd_sched_entity \*entity:
        *undescribed*

.. _`amd_sched_entity_fini.description`:

Description
-----------

@sched       Pointer to scheduler instance
\ ``entity``\       The pointer to a valid scheduler entity

Cleanup and free the allocated resources.

.. _`amd_sched_entity_in`:

amd_sched_entity_in
===================

.. c:function:: bool amd_sched_entity_in(struct amd_sched_job *sched_job)

    :param struct amd_sched_job \*sched_job:
        *undescribed*

.. _`amd_sched_entity_in.description`:

Description
-----------

@sched_job           The pointer to job required to submit

Returns true if we could submit the job.

.. _`amd_sched_entity_push_job`:

amd_sched_entity_push_job
=========================

.. c:function:: void amd_sched_entity_push_job(struct amd_sched_job *sched_job)

    :param struct amd_sched_job \*sched_job:
        *undescribed*

.. _`amd_sched_entity_push_job.description`:

Description
-----------

@sched_job           The pointer to job required to submit

Returns 0 for success, negative error code otherwise.

.. _`amd_sched_ready`:

amd_sched_ready
===============

.. c:function:: bool amd_sched_ready(struct amd_gpu_scheduler *sched)

    :param struct amd_gpu_scheduler \*sched:
        *undescribed*

.. _`amd_sched_wakeup`:

amd_sched_wakeup
================

.. c:function:: void amd_sched_wakeup(struct amd_gpu_scheduler *sched)

    :param struct amd_gpu_scheduler \*sched:
        *undescribed*

.. _`amd_sched_select_entity`:

amd_sched_select_entity
=======================

.. c:function:: struct amd_sched_entity *amd_sched_select_entity(struct amd_gpu_scheduler *sched)

    :param struct amd_gpu_scheduler \*sched:
        *undescribed*

.. _`amd_sched_init`:

amd_sched_init
==============

.. c:function:: int amd_sched_init(struct amd_gpu_scheduler *sched, const struct amd_sched_backend_ops *ops, unsigned hw_submission, long timeout, const char *name)

    :param struct amd_gpu_scheduler \*sched:
        *undescribed*

    :param const struct amd_sched_backend_ops \*ops:
        *undescribed*

    :param unsigned hw_submission:
        *undescribed*

    :param long timeout:
        *undescribed*

    :param const char \*name:
        *undescribed*

.. _`amd_sched_init.description`:

Description
-----------

@sched               The pointer to the scheduler
\ ``ops``\                  The backend operations for this scheduler.
\ ``hw_submissions``\       Number of hw submissions to do.
\ ``name``\                 Name used for debugging

Return 0 on success, otherwise error code.

.. _`amd_sched_fini`:

amd_sched_fini
==============

.. c:function:: void amd_sched_fini(struct amd_gpu_scheduler *sched)

    :param struct amd_gpu_scheduler \*sched:
        *undescribed*

.. _`amd_sched_fini.description`:

Description
-----------

@sched       The pointer to the scheduler

.. This file was automatic generated / don't edit.

