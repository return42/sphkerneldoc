.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-ggtt-view-size:

===================
i915_ggtt_view_size
===================

*man i915_ggtt_view_size(9)*

*4.6.0-rc5*

Get the size of a GGTT view.


Synopsis
========

.. c:function:: size_t i915_ggtt_view_size( struct drm_i915_gem_object * obj, const struct i915_ggtt_view * view )

Arguments
=========

``obj``
    Object the view is of.

``view``
    The view in question.


Description
===========

``return`` The size of the GGTT view in bytes.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
