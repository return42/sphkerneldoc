
.. _API-drm-mode-hsync:

==============
drm_mode_hsync
==============

*man drm_mode_hsync(9)*

*4.6.0-rc1*

get the hsync of a mode


Synopsis
========

.. c:function:: int drm_mode_hsync( const struct drm_display_mode * mode )

Arguments
=========

``mode``
    mode


Returns
=======

``modes``'s hsync rate in kHz, rounded to the nearest integer. Calculates the value first if it is not yet set.
