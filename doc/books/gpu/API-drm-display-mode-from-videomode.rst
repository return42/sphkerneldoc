.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-display-mode-from-videomode:

===============================
drm_display_mode_from_videomode
===============================

*man drm_display_mode_from_videomode(9)*

*4.6.0-rc5*

fill in ``dmode`` using ``vm``,


Synopsis
========

.. c:function:: void drm_display_mode_from_videomode( const struct videomode * vm, struct drm_display_mode * dmode )

Arguments
=========

``vm``
    videomode structure to use as source

``dmode``
    drm_display_mode structure to use as destination


Description
===========

Fills out ``dmode`` using the display mode specified in ``vm``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
