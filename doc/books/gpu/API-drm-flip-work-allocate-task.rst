.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-flip-work-allocate-task:

===========================
drm_flip_work_allocate_task
===========================

*man drm_flip_work_allocate_task(9)*

*4.6.0-rc5*

allocate a flip-work task


Synopsis
========

.. c:function:: struct drm_flip_task * drm_flip_work_allocate_task( void * data, gfp_t flags )

Arguments
=========

``data``
    data associated to the task

``flags``
    allocator flags


Description
===========

Allocate a drm_flip_task object and attach private data to it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
