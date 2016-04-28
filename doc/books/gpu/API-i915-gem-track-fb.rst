.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-gem-track-fb:

=================
i915_gem_track_fb
=================

*man i915_gem_track_fb(9)*

*4.6.0-rc5*

update frontbuffer tracking


Synopsis
========

.. c:function:: void i915_gem_track_fb( struct drm_i915_gem_object * old, struct drm_i915_gem_object * new, unsigned frontbuffer_bits )

Arguments
=========

``old``
    current GEM buffer for the frontbuffer slots

``new``
    new GEM buffer for the frontbuffer slots

``frontbuffer_bits``
    bitmask of frontbuffer slots


Description
===========

This updates the frontbuffer tracking bits ``frontbuffer_bits`` by
clearing them from ``old`` and setting them in ``new``. Both ``old`` and
``new`` can be NULL.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
