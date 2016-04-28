.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-rotation-simplify:

=====================
drm_rotation_simplify
=====================

*man drm_rotation_simplify(9)*

*4.6.0-rc5*

Try to simplify the rotation


Synopsis
========

.. c:function:: unsigned int drm_rotation_simplify( unsigned int rotation, unsigned int supported_rotations )

Arguments
=========

``rotation``
    Rotation to be simplified

``supported_rotations``
    Supported rotations


Description
===========

Attempt to simplify the rotation to a form that is supported. Eg. if the
hardware supports everything except DRM_REFLECT_X


one could call this function like this
======================================

drm_rotation_simplify(rotation, BIT(DRM_ROTATE_0) |
BIT(DRM_ROTATE_90) | BIT(DRM_ROTATE_180) | BIT(DRM_ROTATE_270)
| BIT(DRM_REFLECT_Y));

to eliminate the DRM_ROTATE_X flag. Depending on what kind of
transforms the hardware supports, this function may not be able to
produce a supported transform, so the caller should check the result
afterwards.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
