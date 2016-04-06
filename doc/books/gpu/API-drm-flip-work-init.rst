
.. _API-drm-flip-work-init:

==================
drm_flip_work_init
==================

*man drm_flip_work_init(9)*

*4.6.0-rc1*

initialize flip-work


Synopsis
========

.. c:function:: void drm_flip_work_init( struct drm_flip_work * work, const char * name, drm_flip_func_t func )

Arguments
=========

``work``
    the flip-work to initialize

``name``
    debug name

``func``
    the callback work function


Description
===========

Initializes/allocates resources for the flip-work
