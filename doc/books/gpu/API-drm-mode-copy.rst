
.. _API-drm-mode-copy:

=============
drm_mode_copy
=============

*man drm_mode_copy(9)*

*4.6.0-rc1*

copy the mode


Synopsis
========

.. c:function:: void drm_mode_copy( struct drm_display_mode * dst, const struct drm_display_mode * src )

Arguments
=========

``dst``
    mode to overwrite

``src``
    mode to copy


Description
===========

Copy an existing mode into another mode, preserving the object id and list head of the destination mode.
