
.. _API-drm-flip-work-queue-task:

========================
drm_flip_work_queue_task
========================

*man drm_flip_work_queue_task(9)*

*4.6.0-rc1*

queue a specific task


Synopsis
========

.. c:function:: void drm_flip_work_queue_task( struct drm_flip_work * work, struct drm_flip_task * task )

Arguments
=========

``work``
    the flip-work

``task``
    the task to handle


Description
===========

Queues task, that will later be run (passed back to drm_flip_func_t func) on a work queue after ``drm_flip_work_commit`` is called.
