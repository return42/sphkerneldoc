
.. _API-drm-mode-set-name:

=================
drm_mode_set_name
=================

*man drm_mode_set_name(9)*

*4.6.0-rc1*

set the name on a mode


Synopsis
========

.. c:function:: void drm_mode_set_name( struct drm_display_mode * mode )

Arguments
=========

``mode``
    name will be set in this mode


Description
===========

Set the name of ``mode`` to a standard format which is <hdisplay>x<vdisplay> with an optional 'i' suffix for interlaced modes.
