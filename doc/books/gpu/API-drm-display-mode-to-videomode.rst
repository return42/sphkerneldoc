.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-display-mode-to-videomode:

=============================
drm_display_mode_to_videomode
=============================

*man drm_display_mode_to_videomode(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
