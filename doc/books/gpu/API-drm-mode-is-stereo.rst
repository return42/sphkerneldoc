
.. _API-drm-mode-is-stereo:

==================
drm_mode_is_stereo
==================

*man drm_mode_is_stereo(9)*

*4.6.0-rc1*

check for stereo mode flags


Synopsis
========

.. c:function:: bool drm_mode_is_stereo( const struct drm_display_mode * mode )

Arguments
=========

``mode``
    drm_display_mode to check


Returns
=======

True if the mode is one of the stereo modes (like side-by-side), false if not.
