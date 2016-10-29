.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_flip_work.c

.. _`drm_flip_work_allocate_task`:

drm_flip_work_allocate_task
===========================

.. c:function:: struct drm_flip_task *drm_flip_work_allocate_task(void *data, gfp_t flags)

    allocate a flip-work task

    :param void \*data:
        data associated to the task

    :param gfp_t flags:
        allocator flags

.. _`drm_flip_work_allocate_task.description`:

Description
-----------

Allocate a drm_flip_task object and attach private data to it.

.. _`drm_flip_work_queue_task`:

drm_flip_work_queue_task
========================

.. c:function:: void drm_flip_work_queue_task(struct drm_flip_work *work, struct drm_flip_task *task)

    queue a specific task

    :param struct drm_flip_work \*work:
        the flip-work

    :param struct drm_flip_task \*task:
        the task to handle

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

    :param struct drm_flip_work \*work:
        the flip-work

    :param void \*val:
        the value to queue

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

    :param struct drm_flip_work \*work:
        the flip-work

    :param struct workqueue_struct \*wq:
        the work-queue to run the queued work on

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

    :param struct drm_flip_work \*work:
        the flip-work to initialize

    :param const char \*name:
        debug name

    :param drm_flip_func_t func:
        the callback work function

.. _`drm_flip_work_init.description`:

Description
-----------

Initializes/allocates resources for the flip-work

.. _`drm_flip_work_cleanup`:

drm_flip_work_cleanup
=====================

.. c:function:: void drm_flip_work_cleanup(struct drm_flip_work *work)

    cleans up flip-work

    :param struct drm_flip_work \*work:
        the flip-work to cleanup

.. _`drm_flip_work_cleanup.description`:

Description
-----------

Destroy resources allocated for the flip-work

.. This file was automatic generated / don't edit.
