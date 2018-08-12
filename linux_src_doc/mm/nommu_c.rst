.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/nommu.c

.. _`follow_pfn`:

follow_pfn
==========

.. c:function:: int follow_pfn(struct vm_area_struct *vma, unsigned long address, unsigned long *pfn)

    look up PFN at a user virtual address

    :param struct vm_area_struct \*vma:
        memory mapping

    :param unsigned long address:
        user virtual address

    :param unsigned long \*pfn:
        location to store found PFN

.. _`follow_pfn.description`:

Description
-----------

Only IO mappings and raw PFN mappings are allowed.

Returns zero and the pfn at \ ``pfn``\  on success, -ve otherwise.

.. _`vmalloc_node`:

vmalloc_node
============

.. c:function:: void *vmalloc_node(unsigned long size, int node)

    allocate memory on a specific node

    :param unsigned long size:
        allocation size

    :param int node:
        numa node

.. _`vmalloc_node.description`:

Description
-----------

Allocate enough pages to cover \ ``size``\  from the page level
allocator and map them into contiguous kernel virtual space.

For tight control over page level allocator and protection flags
use \__vmalloc() instead.

.. _`vzalloc_node`:

vzalloc_node
============

.. c:function:: void *vzalloc_node(unsigned long size, int node)

    allocate memory on a specific node with zero fill

    :param unsigned long size:
        allocation size

    :param int node:
        numa node

.. _`vzalloc_node.description`:

Description
-----------

Allocate enough pages to cover \ ``size``\  from the page level
allocator and map them into contiguous kernel virtual space.
The memory allocated is set to zero.

For tight control over page level allocator and protection flags
use \__vmalloc() instead.

.. _`vmalloc_exec`:

vmalloc_exec
============

.. c:function:: void *vmalloc_exec(unsigned long size)

    allocate virtually contiguous, executable memory

    :param unsigned long size:
        allocation size

.. _`vmalloc_exec.description`:

Description
-----------

Kernel-internal function to allocate enough pages to cover \ ``size``\ 
the page level allocator and map them into contiguous and
executable kernel virtual space.

For tight control over page level allocator and protection flags
use \__vmalloc() instead.

.. _`vmalloc_32`:

vmalloc_32
==========

.. c:function:: void *vmalloc_32(unsigned long size)

    allocate virtually contiguous memory (32bit addressable)

    :param unsigned long size:
        allocation size

.. _`vmalloc_32.description`:

Description
-----------

Allocate enough 32bit PA addressable pages to cover \ ``size``\  from the
page level allocator and map them into contiguous kernel virtual space.

.. _`vmalloc_32_user`:

vmalloc_32_user
===============

.. c:function:: void *vmalloc_32_user(unsigned long size)

    allocate zeroed virtually contiguous 32bit memory

    :param unsigned long size:
        allocation size

.. _`vmalloc_32_user.description`:

Description
-----------

The resulting memory area is 32bit addressable and zeroed so it can be
mapped to userspace without leaking data.

VM_USERMAP is set on the corresponding VMA so that subsequent calls to
\ :c:func:`remap_vmalloc_range`\  are permissible.

.. _`access_remote_vm`:

access_remote_vm
================

.. c:function:: int access_remote_vm(struct mm_struct *mm, unsigned long addr, void *buf, int len, unsigned int gup_flags)

    access another process' address space

    :param struct mm_struct \*mm:
        the mm_struct of the target address space

    :param unsigned long addr:
        start address to access

    :param void \*buf:
        source or destination buffer

    :param int len:
        number of bytes to transfer

    :param unsigned int gup_flags:
        flags modifying lookup behaviour

.. _`access_remote_vm.description`:

Description
-----------

The caller must hold a reference on \ ``mm``\ .

.. _`nommu_shrink_inode_mappings`:

nommu_shrink_inode_mappings
===========================

.. c:function:: int nommu_shrink_inode_mappings(struct inode *inode, size_t size, size_t newsize)

    Shrink the shared mappings on an inode

    :param struct inode \*inode:
        The inode to check

    :param size_t size:
        The current filesize of the inode

    :param size_t newsize:
        The proposed filesize of the inode

.. _`nommu_shrink_inode_mappings.description`:

Description
-----------

Check the shared mappings on an inode on behalf of a shrinking truncate to
make sure that that any outstanding VMAs aren't broken and then shrink the
vm_regions that extend that beyond so that \ :c:func:`do_mmap_pgoff`\  doesn't
automatically grant mappings that are too large.

.. This file was automatic generated / don't edit.

