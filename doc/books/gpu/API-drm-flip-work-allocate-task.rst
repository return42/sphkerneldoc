
.. _API-drm-flip-work-allocate-task:

===========================
drm_flip_work_allocate_task
===========================

*man drm_flip_work_allocate_task(9)*

*4.6.0-rc1*

allocate a flip-work task


Synopsis
========

.. c:function:: struct drm_flip_task ⋆ drm_flip_work_allocate_task( void * data, gfp_t flags )

Arguments
=========

``data``
    data associated to the task

``flags``
    allocator flags


Description
===========

Allocate a drm_flip_task object and attach private data to it.
