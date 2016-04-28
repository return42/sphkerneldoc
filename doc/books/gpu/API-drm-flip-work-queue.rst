.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-flip-work-queue:

===================
drm_flip_work_queue
===================

*man drm_flip_work_queue(9)*

*4.6.0-rc5*

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

Queues work, that will later be run (passed back to drm_flip_func_t
func) on a work queue after ``drm_flip_work_commit`` is called.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
