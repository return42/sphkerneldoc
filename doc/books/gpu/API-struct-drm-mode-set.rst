.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-drm-mode-set:

===================
struct drm_mode_set
===================

*man struct drm_mode_set(9)*

*4.6.0-rc5*

new values for a CRTC config change


Synopsis
========

.. code-block:: c

    struct drm_mode_set {
      struct drm_framebuffer * fb;
      struct drm_crtc * crtc;
      struct drm_display_mode * mode;
      uint32_t x;
      uint32_t y;
      struct drm_connector ** connectors;
      size_t num_connectors;
    };


Members
=======

fb
    framebuffer to use for new config

crtc
    CRTC whose configuration we're about to change

mode
    mode timings to use

x
    position of this CRTC relative to ``fb``

y
    position of this CRTC relative to ``fb``

connectors
    array of connectors to drive with this CRTC if possible

num_connectors
    size of ``connectors`` array


Description
===========

Represents a single crtc the connectors that it drives with what mode
and from which framebuffer it scans out from.

This is used to set modes.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
