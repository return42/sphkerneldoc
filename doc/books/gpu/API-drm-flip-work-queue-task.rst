.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-flip-work-queue-task:

========================
drm_flip_work_queue_task
========================

*man drm_flip_work_queue_task(9)*

*4.6.0-rc5*

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

Queues task, that will later be run (passed back to drm_flip_func_t
func) on a work queue after ``drm_flip_work_commit`` is called.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
