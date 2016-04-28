.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-modeset-unlock-crtc:

=======================
drm_modeset_unlock_crtc
=======================

*man drm_modeset_unlock_crtc(9)*

*4.6.0-rc5*

drop crtc lock


Synopsis
========

.. c:function:: void drm_modeset_unlock_crtc( struct drm_crtc * crtc )

Arguments
=========

``crtc``
    drm crtc


Description
===========

This drops the crtc lock acquire with ``drm_modeset_lock_crtc`` and all
other locks acquired through the hidden context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
