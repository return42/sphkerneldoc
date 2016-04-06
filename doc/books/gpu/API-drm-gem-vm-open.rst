
.. _API-drm-gem-vm-open:

===============
drm_gem_vm_open
===============

*man drm_gem_vm_open(9)*

*4.6.0-rc1*

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

This function implements the #vm_operations_struct ``open`` callback for GEM drivers. This must be used together with ``drm_gem_vm_close``.
