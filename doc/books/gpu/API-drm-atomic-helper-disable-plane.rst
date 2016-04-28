.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-disable-plane:

===============================
drm_atomic_helper_disable_plane
===============================

*man drm_atomic_helper_disable_plane(9)*

*4.6.0-rc5*

Helper for primary plane disable using * atomic


Synopsis
========

.. c:function:: int drm_atomic_helper_disable_plane( struct drm_plane * plane )

Arguments
=========

``plane``
    plane to disable


Description
===========

Provides a default plane disable handler using the atomic driver
interface.


RETURNS
=======

Zero on success, error code on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
