
.. _API-drm-plane-init:

==============
drm_plane_init
==============

*man drm_plane_init(9)*

*4.6.0-rc1*

Initialize a legacy plane


Synopsis
========

.. c:function:: int drm_plane_init( struct drm_device * dev, struct drm_plane * plane, unsigned long possible_crtcs, const struct drm_plane_funcs * funcs, const uint32_t * formats, unsigned int format_count, bool is_primary )

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
    array of supported formats (``DRM_FORMAT_``\ ⋆)

``format_count``
    number of elements in ``formats``

``is_primary``
    plane type (primary vs overlay)


Description
===========

Legacy API to initialize a DRM plane.

New drivers should call ``drm_universal_plane_init`` instead.


Returns
=======

Zero on success, error code on failure.
