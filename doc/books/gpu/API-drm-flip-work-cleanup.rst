.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-flip-work-cleanup:

=====================
drm_flip_work_cleanup
=====================

*man drm_flip_work_cleanup(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
