.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-add-affected-connectors:

==================================
drm_atomic_add_affected_connectors
==================================

*man drm_atomic_add_affected_connectors(9)*

*4.6.0-rc5*

add connectors for crtc


Synopsis
========

.. c:function:: int drm_atomic_add_affected_connectors( struct drm_atomic_state * state, struct drm_crtc * crtc )

Arguments
=========

``state``
    atomic state

``crtc``
    DRM crtc


Description
===========

This function walks the current configuration and adds all connectors
currently using ``crtc`` to the atomic configuration ``state``. Note
that this function must acquire the connection mutex. This can
potentially cause unneeded seralization if the update is just for the
planes on one crtc. Hence drivers and helpers should only call this when
really needed (e.g. when a full modeset needs to happen due to some
change).


Returns
=======

0 on success or can fail with -EDEADLK or -ENOMEM. When the error is
EDEADLK then the w/w mutex code has detected a deadlock and the entire
atomic sequence must be restarted. All other errors are fatal.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
