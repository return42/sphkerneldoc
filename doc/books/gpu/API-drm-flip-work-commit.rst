
.. _API-drm-flip-work-commit:

====================
drm_flip_work_commit
====================

*man drm_flip_work_commit(9)*

*4.6.0-rc1*

commit queued work


Synopsis
========

.. c:function:: void drm_flip_work_commit( struct drm_flip_work * work, struct workqueue_struct * wq )

Arguments
=========

``work``
    the flip-work

``wq``
    the work-queue to run the queued work on


Description
===========

Trigger work previously queued by ``drm_flip_work_queue`` to run on a workqueue. The typical usage would be to queue work (via ``drm_flip_work_queue``) at any point (from vblank
irq and/or prior), and then from vblank irq commit the queued work.
