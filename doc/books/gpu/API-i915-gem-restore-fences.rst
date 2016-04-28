.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-gem-restore-fences:

=======================
i915_gem_restore_fences
=======================

*man i915_gem_restore_fences(9)*

*4.6.0-rc5*

restore fence state


Synopsis
========

.. c:function:: void i915_gem_restore_fences( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

Restore the hw fence state to match the software tracking again, to be
called after a gpu reset and on resume.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
