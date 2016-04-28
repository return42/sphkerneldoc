.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-create-dirty-info-property:

===================================
drm_mode_create_dirty_info_property
===================================

*man drm_mode_create_dirty_info_property(9)*

*4.6.0-rc5*

create dirty property


Synopsis
========

.. c:function:: int drm_mode_create_dirty_info_property( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

Called by a driver the first time it's needed, must be attached to
desired connectors.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
