
.. _API-drm-display-mode-to-videomode:

=============================
drm_display_mode_to_videomode
=============================

*man drm_display_mode_to_videomode(9)*

*4.6.0-rc1*

fill in ``vm`` using ``dmode``,


Synopsis
========

.. c:function:: void drm_display_mode_to_videomode( const struct drm_display_mode * dmode, struct videomode * vm )

Arguments
=========

``dmode``
    drm_display_mode structure to use as source

``vm``
    videomode structure to use as destination


Description
===========

Fills out ``vm`` using the display mode specified in ``dmode``.
