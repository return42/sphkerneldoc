.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-create-tv-properties:

=============================
drm_mode_create_tv_properties
=============================

*man drm_mode_create_tv_properties(9)*

*4.6.0-rc5*

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

Called by a driver's TV initialization routine, this function creates
the TV specific connector properties for a given device. Caller is
responsible for allocating a list of format names and passing them to
this routine.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
