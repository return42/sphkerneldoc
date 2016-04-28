.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-vm-open:

===============
drm_gem_vm_open
===============

*man drm_gem_vm_open(9)*

*4.6.0-rc5*

vma->ops->open implementation for GEM


Synopsis
========

.. c:function:: void drm_gem_vm_open( struct vm_area_struct * vma )

Arguments
=========

``vma``
    VM area structure


Description
===========

This function implements the #vm_operations_struct ``open`` callback
for GEM drivers. This must be used together with ``drm_gem_vm_close``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
