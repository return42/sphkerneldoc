.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/shmem.c

.. _`shmem_recalc_inode`:

shmem_recalc_inode
==================

.. c:function:: void shmem_recalc_inode(struct inode *inode)

    recalculate the block usage of an inode

    :param inode:
        inode to recalc
    :type inode: struct inode \*

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

    :param name:
        name for dentry (to be seen in /proc/<pid>/maps
    :type name: const char \*

    :param size:
        size to be set for the file
    :type size: loff_t

    :param flags:
        VM_NORESERVE suppresses pre-accounting of the entire object size
    :type flags: unsigned long

.. _`shmem_file_setup`:

shmem_file_setup
================

.. c:function:: struct file *shmem_file_setup(const char *name, loff_t size, unsigned long flags)

    get an unlinked file living in tmpfs

    :param name:
        name for dentry (to be seen in /proc/<pid>/maps
    :type name: const char \*

    :param size:
        size to be set for the file
    :type size: loff_t

    :param flags:
        VM_NORESERVE suppresses pre-accounting of the entire object size
    :type flags: unsigned long

.. _`shmem_file_setup_with_mnt`:

shmem_file_setup_with_mnt
=========================

.. c:function:: struct file *shmem_file_setup_with_mnt(struct vfsmount *mnt, const char *name, loff_t size, unsigned long flags)

    get an unlinked file living in tmpfs

    :param mnt:
        the tmpfs mount where the file will be created
    :type mnt: struct vfsmount \*

    :param name:
        name for dentry (to be seen in /proc/<pid>/maps
    :type name: const char \*

    :param size:
        size to be set for the file
    :type size: loff_t

    :param flags:
        VM_NORESERVE suppresses pre-accounting of the entire object size
    :type flags: unsigned long

.. _`shmem_zero_setup`:

shmem_zero_setup
================

.. c:function:: int shmem_zero_setup(struct vm_area_struct *vma)

    setup a shared anonymous mapping

    :param vma:
        the vma to be mmapped is prepared by do_mmap_pgoff
    :type vma: struct vm_area_struct \*

.. _`shmem_read_mapping_page_gfp`:

shmem_read_mapping_page_gfp
===========================

.. c:function:: struct page *shmem_read_mapping_page_gfp(struct address_space *mapping, pgoff_t index, gfp_t gfp)

    read into page cache, using specified page allocation flags.

    :param mapping:
        the page's address_space
    :type mapping: struct address_space \*

    :param index:
        the page index
    :type index: pgoff_t

    :param gfp:
        the page allocator flags to use if allocating
    :type gfp: gfp_t

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

