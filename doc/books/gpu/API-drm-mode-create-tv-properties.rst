
.. _API-drm-mode-create-tv-properties:

=============================
drm_mode_create_tv_properties
=============================

*man drm_mode_create_tv_properties(9)*

*4.6.0-rc1*

create TV specific connector properties


Synopsis
========

.. c:function:: int drm_mode_create_tv_properties( struct drm_device * dev, unsigned int num_modes, const char *const modes[] )

Arguments
=========

``dev``
    DRM device

``num_modes``
    number of different TV formats (modes) supported

``modes[]``
    array of pointers to strings containing name of each format


Description
===========

Called by a driver's TV initialization routine, this function creates the TV specific connector properties for a given device. Caller is responsible for allocating a list of format
names and passing them to this routine.
