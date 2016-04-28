.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-mmap-obj:

================
drm_gem_mmap_obj
================

*man drm_gem_mmap_obj(9)*

*4.6.0-rc5*

memory map a GEM object


Synopsis
========

.. c:function:: int drm_gem_mmap_obj( struct drm_gem_object * obj, unsigned long obj_size, struct vm_area_struct * vma )

Arguments
=========

``obj``
    the GEM object to map

``obj_size``
    the object size to be mapped, in bytes

``vma``
    VMA for the area to be mapped


Description
===========

Set up the VMA to prepare mapping of the GEM object using the
gem_vm_ops provided by the driver. Depending on their requirements,
drivers can either provide a fault handler in their gem_vm_ops (in
which case any accesses to the object will be trapped, to perform
migration, GTT binding, surface register allocation, or performance
monitoring), or mmap the buffer memory synchronously after calling
drm_gem_mmap_obj.

This function is mainly intended to implement the DMABUF mmap operation,
when the GEM object is not looked up based on its fake offset. To
implement the DRM mmap operation, drivers should use the
``drm_gem_mmap`` function.

``drm_gem_mmap_obj`` assumes the user is granted access to the buffer
while ``drm_gem_mmap`` prevents unprivileged users from mapping random
objects. So callers must verify access restrictions before calling this
helper.

Return 0 or success or -EINVAL if the object size is smaller than the
VMA size, or if no gem_vm_ops are provided.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
