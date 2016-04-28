.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-cma-mmap:

================
drm_gem_cma_mmap
================

*man drm_gem_cma_mmap(9)*

*4.6.0-rc5*

memory-map a CMA GEM object


Synopsis
========

.. c:function:: int drm_gem_cma_mmap( struct file * filp, struct vm_area_struct * vma )

Arguments
=========

``filp``
    file object

``vma``
    VMA for the area to be mapped


Description
===========

This function implements an augmented version of the GEM DRM file mmap


operation for CMA objects
=========================

In addition to the usual GEM VMA setup it immediately faults in the
entire object instead of using on-demaind faulting. Drivers which employ
the CMA helpers should use this function as their ->``mmap`` handler in
the DRM device file's file_operations structure.


Returns
=======

0 on success or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
