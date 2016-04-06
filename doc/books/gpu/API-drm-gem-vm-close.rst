
.. _API-drm-gem-vm-close:

================
drm_gem_vm_close
================

*man drm_gem_vm_close(9)*

*4.6.0-rc1*

vma->ops->close implementation for GEM


Synopsis
========

.. c:function:: void drm_gem_vm_close( struct vm_area_struct * vma )

Arguments
=========

``vma``
    VM area structure


Description
===========

This function implements the #vm_operations_struct ``close`` callback for GEM drivers. This must be used together with ``drm_gem_vm_open``.
