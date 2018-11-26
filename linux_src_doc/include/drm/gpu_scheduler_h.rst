.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/gpu_scheduler.h

.. _`drm_sched_entity`:

struct drm_sched_entity
=======================

.. c:type:: struct drm_sched_entity

    A wrapper around a job queue (typically attached to the DRM file_priv).

.. _`drm_sched_entity.definition`:

Definition
----------

.. code-block:: c

    struct drm_sched_entity {
        struct list_head list;
        struct drm_sched_rq *rq;
        struct drm_sched_rq **rq_list;
        unsigned int num_rq_list;
        spinlock_t rq_lock;
        struct spsc_queue job_queue;
        atomic_t fence_seq;
        uint64_t fence_context;
        struct dma_fence *dependency;
        struct dma_fence_cb cb;
        atomic_t *guilty;
        struct dma_fence *last_scheduled;
        struct task_struct *last_user;
        bool stopped;
    }

.. _`drm_sched_entity.members`:

Members
-------

list
    used to append this struct to the list of entities in the
    runqueue.

rq
    runqueue on which this entity is currently scheduled.

rq_list
    a list of run queues on which jobs from this entity can
    be scheduled

num_rq_list
    number of run queues in the rq_list

rq_lock
    lock to modify the runqueue to which this entity belongs.

job_queue
    the list of jobs of this entity.

fence_seq
    a linearly increasing seqno incremented with each
    new \ :c:type:`struct drm_sched_fence <drm_sched_fence>`\  which is part of the entity.

fence_context
    a unique context for all the fences which belong
    to this entity.
    The \ :c:type:`drm_sched_fence.scheduled <drm_sched_fence>`\  uses the
    fence_context but \ :c:type:`drm_sched_fence.finished <drm_sched_fence>`\  uses
    fence_context + 1.

dependency
    the dependency fence of the job which is on the top
    of the job queue.

cb
    callback for the dependency fence above.

guilty
    points to ctx's guilty.

last_scheduled
    points to the finished fence of the last scheduled job.

last_user
    last group leader pushing a job into the entity.

stopped
    Marks the enity as removed from rq and destined for termination.

.. _`drm_sched_entity.description`:

Description
-----------

Entities will emit jobs in order to their corresponding hardware
ring, and the scheduler will alternate between entities based on
scheduling policy.

.. _`drm_sched_rq`:

struct drm_sched_rq
===================

.. c:type:: struct drm_sched_rq

    queue of entities to be scheduled.

.. _`drm_sched_rq.definition`:

Definition
----------

.. code-block:: c

    struct drm_sched_rq {
        spinlock_t lock;
        struct drm_gpu_scheduler *sched;
        struct list_head entities;
        struct drm_sched_entity *current_entity;
    }

.. _`drm_sched_rq.members`:

Members
-------

lock
    to modify the entities list.

sched
    the scheduler to which this rq belongs to.

entities
    list of the entities to be scheduled.

current_entity
    the entity which is to be scheduled.

.. _`drm_sched_rq.description`:

Description
-----------

Run queue is a set of entities scheduling command submissions for
one specific ring. It implements the scheduling policy that selects
the next entity to emit commands from.

.. _`drm_sched_fence`:

struct drm_sched_fence
======================

.. c:type:: struct drm_sched_fence

    fences corresponding to the scheduling of a job.

.. _`drm_sched_fence.definition`:

Definition
----------

.. code-block:: c

    struct drm_sched_fence {
        struct dma_fence scheduled;
        struct dma_fence finished;
        struct dma_fence_cb cb;
        struct dma_fence *parent;
        struct drm_gpu_scheduler *sched;
        spinlock_t lock;
        void *owner;
    }

.. _`drm_sched_fence.members`:

Members
-------

scheduled
    this fence is what will be signaled by the schedulerwhen the job is scheduled.

finished
    this fence is what will be signaled by the schedulerwhen the job is completed.

    When setting up an out fence for the job, you should use
    this, since it's available immediately upon
    \ :c:func:`drm_sched_job_init`\ , and the fence returned by the driver
    from \ :c:func:`run_job`\  won't be created until the dependencies have
    resolved.

cb
    the callback for the parent fence below.

parent
    the fence returned by \ :c:type:`drm_sched_backend_ops.run_jobwhen <drm_sched_backend_ops>`\  scheduling the job on hardware. We signal the
    \ :c:type:`drm_sched_fence.finished <drm_sched_fence>`\  fence once parent is signalled.

sched
    the scheduler instance to which the job having this structbelongs to.

lock
    the lock used by the scheduled and the finished fences.

owner
    job owner for debugging

.. _`drm_sched_job`:

struct drm_sched_job
====================

.. c:type:: struct drm_sched_job

    A job to be run by an entity.

.. _`drm_sched_job.definition`:

Definition
----------

.. code-block:: c

    struct drm_sched_job {
        struct spsc_node queue_node;
        struct drm_gpu_scheduler *sched;
        struct drm_sched_fence *s_fence;
        struct dma_fence_cb finish_cb;
        struct work_struct finish_work;
        struct list_head node;
        uint64_t id;
        atomic_t karma;
        enum drm_sched_priority s_priority;
        struct drm_sched_entity *entity;
    }

.. _`drm_sched_job.members`:

Members
-------

queue_node
    used to append this struct to the queue of jobs in an entity.

sched
    the scheduler instance on which this job is scheduled.

s_fence
    contains the fences for the scheduling of job.

finish_cb
    the callback for the finished fence.

finish_work
    schedules the function \ ``drm_sched_job_finish``\  once the job has
    finished to remove the job from the
    \ ``drm_gpu_scheduler.ring_mirror_list``\ .

node
    used to append this struct to the \ ``drm_gpu_scheduler.ring_mirror_list``\ .

id
    a unique id assigned to each job scheduled on the scheduler.

karma
    increment on every hang caused by this job. If this exceeds the hang
    limit of the scheduler then the job is marked guilty and will not
    be scheduled further.

s_priority
    the priority of the job.

entity
    the entity to which this job belongs.

.. _`drm_sched_job.description`:

Description
-----------

A job is created by the driver using \ :c:func:`drm_sched_job_init`\ , and
should call \ :c:func:`drm_sched_entity_push_job`\  once it wants the scheduler
to schedule the job.

.. _`drm_sched_backend_ops`:

struct drm_sched_backend_ops
============================

.. c:type:: struct drm_sched_backend_ops


.. _`drm_sched_backend_ops.definition`:

Definition
----------

.. code-block:: c

    struct drm_sched_backend_ops {
        struct dma_fence *(*dependency)(struct drm_sched_job *sched_job, struct drm_sched_entity *s_entity);
        struct dma_fence *(*run_job)(struct drm_sched_job *sched_job);
        void (*timedout_job)(struct drm_sched_job *sched_job);
        void (*free_job)(struct drm_sched_job *sched_job);
    }

.. _`drm_sched_backend_ops.members`:

Members
-------

dependency
    Called when the scheduler is considering schedulingthis job next, to get another struct dma_fence for this job to
    block on.  Once it returns NULL, \ :c:func:`run_job`\  may be called.

run_job
    Called to execute the job once all of the dependencieshave been resolved.  This may be called multiple times, if
    \ :c:func:`timedout_job`\  has happened and \ :c:func:`drm_sched_job_recovery`\ 
    decides to try it again.

timedout_job
    Called when a job has taken too long to execute,to trigger GPU recovery.

free_job
    Called once the job's finished fence has been signaledand it's time to clean it up.

.. _`drm_sched_backend_ops.description`:

Description
-----------

Define the backend operations called by the scheduler,
these functions should be implemented in driver side.

.. _`drm_gpu_scheduler`:

struct drm_gpu_scheduler
========================

.. c:type:: struct drm_gpu_scheduler


.. _`drm_gpu_scheduler.definition`:

Definition
----------

.. code-block:: c

    struct drm_gpu_scheduler {
        const struct drm_sched_backend_ops *ops;
        uint32_t hw_submission_limit;
        long timeout;
        const char *name;
        struct drm_sched_rq sched_rq[DRM_SCHED_PRIORITY_MAX];
        wait_queue_head_t wake_up_worker;
        wait_queue_head_t job_scheduled;
        atomic_t hw_rq_count;
        atomic64_t job_id_count;
        struct delayed_work work_tdr;
        struct task_struct *thread;
        struct list_head ring_mirror_list;
        spinlock_t job_list_lock;
        int hang_limit;
        atomic_t num_jobs;
    }

.. _`drm_gpu_scheduler.members`:

Members
-------

ops
    backend operations provided by the driver.

hw_submission_limit
    the max size of the hardware queue.

timeout
    the time after which a job is removed from the scheduler.

name
    name of the ring for which this scheduler is being used.

sched_rq
    priority wise array of run queues.

wake_up_worker
    the wait queue on which the scheduler sleeps until a job
    is ready to be scheduled.

job_scheduled
    once \ ``drm_sched_entity_do_release``\  is called the scheduler
    waits on this wait queue until all the scheduled jobs are
    finished.

hw_rq_count
    the number of jobs currently in the hardware queue.

job_id_count
    used to assign unique id to the each job.

work_tdr
    schedules a delayed call to \ ``drm_sched_job_timedout``\  after the
    timeout interval is over.

thread
    the kthread on which the scheduler which run.

ring_mirror_list
    the list of jobs which are currently in the job queue.

job_list_lock
    lock to protect the ring_mirror_list.

hang_limit
    once the hangs by a job crosses this limit then it is marked
    guilty and it will be considered for scheduling further.

num_jobs
    the number of jobs in queue in the scheduler

.. _`drm_gpu_scheduler.description`:

Description
-----------

One scheduler is implemented for each hardware ring.

.. This file was automatic generated / don't edit.

