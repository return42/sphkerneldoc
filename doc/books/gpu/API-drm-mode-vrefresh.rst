
.. _API-drm-mode-vrefresh:

=================
drm_mode_vrefresh
=================

*man drm_mode_vrefresh(9)*

*4.6.0-rc1*

get the vrefresh of a mode


Synopsis
========

.. c:function:: int drm_mode_vrefresh( const struct drm_display_mode * mode )

Arguments
=========

``mode``
    mode


Returns
=======

``modes``'s vrefresh rate in Hz, rounded to the nearest integer. Calculates the value first if it is not yet set.
