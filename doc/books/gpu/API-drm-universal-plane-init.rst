.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-universal-plane-init:

========================
drm_universal_plane_init
========================

*man drm_universal_plane_init(9)*

*4.6.0-rc5*

Initialize a new universal plane object


Synopsis
========

.. c:function:: int drm_universal_plane_init( struct drm_device * dev, struct drm_plane * plane, unsigned long possible_crtcs, const struct drm_plane_funcs * funcs, const uint32_t * formats, unsigned int format_count, enum drm_plane_type type, const char * name, ... )

Arguments
=========

``dev``
    DRM device

``plane``
    plane object to init

``possible_crtcs``
    bitmask of possible CRTCs

``funcs``
    callbacks for the new plane

``formats``
    array of supported formats (``DRM_FORMAT_``\ *)

``format_count``
    number of elements in ``formats``

``type``
    type of plane (overlay, primary, cursor)

``name``
    printf style format string for the plane name, or NULL for default
    name

``...``
    variable arguments


Description
===========

Initializes a plane object of type ``type``.


Returns
=======

Zero on success, error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
