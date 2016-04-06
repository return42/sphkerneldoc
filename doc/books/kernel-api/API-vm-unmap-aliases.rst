
.. _API-vm-unmap-aliases:

================
vm_unmap_aliases
================

*man vm_unmap_aliases(9)*

*4.6.0-rc1*

unmap outstanding lazy aliases in the vmap layer


Synopsis
========

.. c:function:: void vm_unmap_aliases( void )

Arguments
=========

``void``
    no arguments


Description
===========

The vmap/vmalloc layer lazily flushes kernel virtual mappings primarily to amortize TLB flushing overheads. What this means is that any page you have now, may, in a former life,
have been mapped into kernel virtual address by the vmap layer and so there might be some CPUs with TLB entries still referencing that page (additional to the regular 1:1 kernel
mapping).

vm_unmap_aliases flushes all such lazy mappings. After it returns, we can be sure that none of the pages we have control over will have any aliases from the vmap layer.
