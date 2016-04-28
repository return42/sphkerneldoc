.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-gem-object-put-fence:

=========================
i915_gem_object_put_fence
=========================

*man i915_gem_object_put_fence(9)*

*4.6.0-rc5*

force-remove fence for an object


Synopsis
========

.. c:function:: int i915_gem_object_put_fence( struct drm_i915_gem_object * obj )

Arguments
=========

``obj``
    object to map through a fence reg


Description
===========

This function force-removes any fence from the given object, which is
useful if the kernel wants to do untiled GTT access.


Returns
=======

0 on success, negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
