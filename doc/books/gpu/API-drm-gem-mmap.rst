.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-mmap:

============
drm_gem_mmap
============

*man drm_gem_mmap(9)*

*4.6.0-rc5*

memory map routine for GEM objects


Synopsis
========

.. c:function:: int drm_gem_mmap( struct file * filp, struct vm_area_struct * vma )

Arguments
=========

``filp``
    DRM file pointer

``vma``
    VMA for the area to be mapped


Description
===========

If a driver supports GEM object mapping, mmap calls on the DRM file
descriptor will end up here.

Look up the GEM object based on the offset passed in (vma->vm_pgoff
will contain the fake offset we created when the GTT map ioctl was
called on the object) and map it with a call to ``drm_gem_mmap_obj``.

If the caller is not granted access to the buffer object, the mmap will
fail with EACCES. Please see the vma manager for more information.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
