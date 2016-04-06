
.. _API-drm-flip-work-queue:

===================
drm_flip_work_queue
===================

*man drm_flip_work_queue(9)*

*4.6.0-rc1*

queue work


Synopsis
========

.. c:function:: void drm_flip_work_queue( struct drm_flip_work * work, void * val )

Arguments
=========

``work``
    the flip-work

``val``
    the value to queue


Description
===========

Queues work, that will later be run (passed back to drm_flip_func_t func) on a work queue after ``drm_flip_work_commit`` is called.
