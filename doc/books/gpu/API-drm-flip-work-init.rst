.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-flip-work-init:

==================
drm_flip_work_init
==================

*man drm_flip_work_init(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
