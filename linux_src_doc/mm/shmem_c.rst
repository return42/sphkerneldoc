.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/shmem.c

.. _`shmem_recalc_inode`:

shmem_recalc_inode
==================

.. c:function:: void shmem_recalc_inode(struct inode *inode)

    recalculate the block usage of an inode

    :param struct inode \*inode:
        inode to recalc

.. _`shmem_recalc_inode.description`:

Description
-----------

We have to calculate the free blocks since the mm can drop
undirtied hole pages behind our back.

But normally   info->alloced == inode->i_mapping->nrpages + info->swapped
So mm freed is info->alloced - (inode->i_mapping->nrpages + info->swapped)

It has to be called with the spinlock held.

.. _`shmem_kernel_file_setup`:

shmem_kernel_file_setup
=======================

.. c:function:: struct file *shmem_kernel_file_setup(const char *name, loff_t size, unsigned long flags)

    get an unlinked file living in tmpfs which must be kernel internal.  There will be NO LSM permission checks against the underlying inode.  So users of this interface must do LSM checks at a higher layer.  The users are the big_key and shm implementations.  LSM checks are provided at the key or shm level rather than the inode.

    :param const char \*name:
        name for dentry (to be seen in /proc/<pid>/maps

    :param loff_t size:
        size to be set for the file

    :param unsigned long flags:
        VM_NORESERVE suppresses pre-accounting of the entire object size

.. _`shmem_file_setup`:

shmem_file_setup
================

.. c:function:: struct file *shmem_file_setup(const char *name, loff_t size, unsigned long flags)

    get an unlinked file living in tmpfs

    :param const char \*name:
        name for dentry (to be seen in /proc/<pid>/maps

    :param loff_t size:
        size to be set for the file

    :param unsigned long flags:
        VM_NORESERVE suppresses pre-accounting of the entire object size

.. _`shmem_file_setup_with_mnt`:

shmem_file_setup_with_mnt
=========================

.. c:function:: struct file *shmem_file_setup_with_mnt(struct vfsmount *mnt, const char *name, loff_t size, unsigned long flags)

    get an unlinked file living in tmpfs

    :param struct vfsmount \*mnt:
        the tmpfs mount where the file will be created

    :param const char \*name:
        name for dentry (to be seen in /proc/<pid>/maps

    :param loff_t size:
        size to be set for the file

    :param unsigned long flags:
        VM_NORESERVE suppresses pre-accounting of the entire object size

.. _`shmem_zero_setup`:

shmem_zero_setup
================

.. c:function:: int shmem_zero_setup(struct vm_area_struct *vma)

    setup a shared anonymous mapping

    :param struct vm_area_struct \*vma:
        the vma to be mmapped is prepared by do_mmap_pgoff

.. _`shmem_read_mapping_page_gfp`:

shmem_read_mapping_page_gfp
===========================

.. c:function:: struct page *shmem_read_mapping_page_gfp(struct address_space *mapping, pgoff_t index, gfp_t gfp)

    read into page cache, using specified page allocation flags.

    :param struct address_space \*mapping:
        the page's address_space

    :param pgoff_t index:
        the page index

    :param gfp_t gfp:
        the page allocator flags to use if allocating

.. _`shmem_read_mapping_page_gfp.description`:

Description
-----------

This behaves as a tmpfs "read_cache_page_gfp(mapping, index, gfp)",
with any new page allocations done using the specified allocation flags.
But \ :c:func:`read_cache_page_gfp`\  uses the ->readpage() method: which does not
suit tmpfs, since it may have pages in swapcache, and needs to find those
for itself; although drivers/gpu/drm i915 and ttm rely upon this support.

\ :c:func:`i915_gem_object_get_pages_gtt`\  mixes \__GFP_NORETRY \| \__GFP_NOWARN in
with the \ :c:func:`mapping_gfp_mask`\ , to avoid OOMing the machine unnecessarily.

.. This file was automatic generated / don't edit.

