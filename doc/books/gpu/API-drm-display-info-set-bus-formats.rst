.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-display-info-set-bus-formats:

================================
drm_display_info_set_bus_formats
================================

*man drm_display_info_set_bus_formats(9)*

*4.6.0-rc5*

set the supported bus formats


Synopsis
========

.. c:function:: int drm_display_info_set_bus_formats( struct drm_display_info * info, const u32 * formats, unsigned int num_formats )

Arguments
=========

``info``
    display info to store bus formats in

``formats``
    array containing the supported bus formats

``num_formats``
    the number of entries in the fmts array


Description
===========

Store the supported bus formats in display info structure. See
MEDIA_BUS_FMT_* definitions in include/uapi/linux/media-bus-format.h
for a full list of available formats.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
