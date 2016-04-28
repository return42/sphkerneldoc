.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-set-config:

============================
drm_atomic_helper_set_config
============================

*man drm_atomic_helper_set_config(9)*

*4.6.0-rc5*

set a new config from userspace


Synopsis
========

.. c:function:: int drm_atomic_helper_set_config( struct drm_mode_set * set )

Arguments
=========

``set``
    mode set configuration


Description
===========

Provides a default crtc set_config handler using the atomic driver
interface.


Returns
=======

Returns 0 on success, negative errno numbers on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
