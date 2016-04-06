
.. _API-drm-flip-work-cleanup:

=====================
drm_flip_work_cleanup
=====================

*man drm_flip_work_cleanup(9)*

*4.6.0-rc1*

cleans up flip-work


Synopsis
========

.. c:function:: void drm_flip_work_cleanup( struct drm_flip_work * work )

Arguments
=========

``work``
    the flip-work to cleanup


Description
===========

Destroy resources allocated for the flip-work
