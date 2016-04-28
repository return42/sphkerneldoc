.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-object-unreference:

==========================
drm_gem_object_unreference
==========================

*man drm_gem_object_unreference(9)*

*4.6.0-rc5*

release a GEM BO reference


Synopsis
========

.. c:function:: void drm_gem_object_unreference( struct drm_gem_object * obj )

Arguments
=========

``obj``
    GEM buffer object


Description
===========

This releases a reference to ``obj``. Callers must hold the
dev->struct_mutex lock when calling this function, even when the driver
doesn't use dev->struct_mutex for anything.

For drivers not encumbered with legacy locking use
``drm_gem_object_unreference_unlocked`` instead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
