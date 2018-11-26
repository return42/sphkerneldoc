.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_flip_work.c

.. _`drm_flip_work_allocate_task`:

drm_flip_work_allocate_task
===========================

.. c:function:: struct drm_flip_task *drm_flip_work_allocate_task(void *data, gfp_t flags)

    allocate a flip-work task

    :param data:
        data associated to the task
    :type data: void \*

    :param flags:
        allocator flags
    :type flags: gfp_t

.. _`drm_flip_work_allocate_task.description`:

Description
-----------

Allocate a drm_flip_task object and attach private data to it.

.. _`drm_flip_work_queue_task`:

drm_flip_work_queue_task
========================

.. c:function:: void drm_flip_work_queue_task(struct drm_flip_work *work, struct drm_flip_task *task)

    queue a specific task

    :param work:
        the flip-work
    :type work: struct drm_flip_work \*

    :param task:
        the task to handle
    :type task: struct drm_flip_task \*

.. _`drm_flip_work_queue_task.description`:

Description
-----------

Queues task, that will later be run (passed back to drm_flip_func_t
func) on a work queue after \ :c:func:`drm_flip_work_commit`\  is called.

.. _`drm_flip_work_queue`:

drm_flip_work_queue
===================

.. c:function:: void drm_flip_work_queue(struct drm_flip_work *work, void *val)

    queue work

    :param work:
        the flip-work
    :type work: struct drm_flip_work \*

    :param val:
        the value to queue
    :type val: void \*

.. _`drm_flip_work_queue.description`:

Description
-----------

Queues work, that will later be run (passed back to drm_flip_func_t
func) on a work queue after \ :c:func:`drm_flip_work_commit`\  is called.

.. _`drm_flip_work_commit`:

drm_flip_work_commit
====================

.. c:function:: void drm_flip_work_commit(struct drm_flip_work *work, struct workqueue_struct *wq)

    commit queued work

    :param work:
        the flip-work
    :type work: struct drm_flip_work \*

    :param wq:
        the work-queue to run the queued work on
    :type wq: struct workqueue_struct \*

.. _`drm_flip_work_commit.description`:

Description
-----------

Trigger work previously queued by \ :c:func:`drm_flip_work_queue`\  to run
on a workqueue.  The typical usage would be to queue work (via
\ :c:func:`drm_flip_work_queue`\ ) at any point (from vblank irq and/or
prior), and then from vblank irq commit the queued work.

.. _`drm_flip_work_init`:

drm_flip_work_init
==================

.. c:function:: void drm_flip_work_init(struct drm_flip_work *work, const char *name, drm_flip_func_t func)

    initialize flip-work

    :param work:
        the flip-work to initialize
    :type work: struct drm_flip_work \*

    :param name:
        debug name
    :type name: const char \*

    :param func:
        the callback work function
    :type func: drm_flip_func_t

.. _`drm_flip_work_init.description`:

Description
-----------

Initializes/allocates resources for the flip-work

.. _`drm_flip_work_cleanup`:

drm_flip_work_cleanup
=====================

.. c:function:: void drm_flip_work_cleanup(struct drm_flip_work *work)

    cleans up flip-work

    :param work:
        the flip-work to cleanup
    :type work: struct drm_flip_work \*

.. _`drm_flip_work_cleanup.description`:

Description
-----------

Destroy resources allocated for the flip-work

.. This file was automatic generated / don't edit.

