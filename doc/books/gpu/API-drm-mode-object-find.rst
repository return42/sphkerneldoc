.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-object-find:

====================
drm_mode_object_find
====================

*man drm_mode_object_find(9)*

*4.6.0-rc5*

look up a drm object with static lifetime


Synopsis
========

.. c:function:: struct drm_mode_object * drm_mode_object_find( struct drm_device * dev, uint32_t id, uint32_t type )

Arguments
=========

``dev``
    drm device

``id``
    id of the mode object

``type``
    type of the mode object


Description
===========

Note that framebuffers cannot be looked up with this functions - since
those are reference counted, they need special treatment. Even with
DRM_MODE_OBJECT_ANY (although that will simply return NULL rather
than ``WARN_ON``).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
