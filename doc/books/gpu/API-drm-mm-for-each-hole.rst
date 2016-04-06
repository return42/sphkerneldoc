
.. _API-drm-mm-for-each-hole:

====================
drm_mm_for_each_hole
====================

*man drm_mm_for_each_hole(9)*

*4.6.0-rc1*

iterator to walk over all holes


Synopsis
========

.. c:function:: drm_mm_for_each_hole( entry, mm, hole_start, hole_end )

Arguments
=========

``entry``
    drm_mm_node used internally to track progress

``mm``
    drm_mm allocator to walk

``hole_start``
    ulong variable to assign the hole start to on each iteration

``hole_end``
    ulong variable to assign the hole end to on each iteration


Description
===========

This iterator walks over all holes in the range allocator. It is implemented with list_for_each, so not save against removal of elements. ``entry`` is used internally and will
not reflect a real drm_mm_node for the very first hole. Hence users of this iterator may not access it.


Implementation Note
===================

We need to inline list_for_each_entry in order to be able to set hole_start and hole_end on each iteration while keeping the macro sane.

The __drm_mm_for_each_hole version is similar, but with added support for going backwards.
