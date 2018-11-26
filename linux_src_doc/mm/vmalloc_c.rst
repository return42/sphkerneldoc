.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/vmalloc.c

.. _`new_vmap_block`:

new_vmap_block
==============

.. c:function:: void *new_vmap_block(unsigned int order, gfp_t gfp_mask)

    allocates new vmap_block and occupies 2^order pages in this block. Of course pages number can't exceed VMAP_BBMAP_BITS

    :param order:
        how many 2^order pages should be occupied in newly allocated block
    :type order: unsigned int

    :param gfp_mask:
        flags for the page level allocator
    :type gfp_mask: gfp_t

.. _`new_vmap_block.return`:

Return
------

virtual address in a newly allocated block or ERR_PTR(-errno)

.. _`vm_unmap_aliases`:

vm_unmap_aliases
================

.. c:function:: void vm_unmap_aliases( void)

    unmap outstanding lazy aliases in the vmap layer

    :param void:
        no arguments
    :type void: 

.. _`vm_unmap_aliases.description`:

Description
-----------

The vmap/vmalloc layer lazily flushes kernel virtual mappings primarily
to amortize TLB flushing overheads. What this means is that any page you
have now, may, in a former life, have been mapped into kernel virtual
address by the vmap layer and so there might be some CPUs with TLB entries
still referencing that page (additional to the regular 1:1 kernel mapping).

vm_unmap_aliases flushes all such lazy mappings. After it returns, we can
be sure that none of the pages we have control over will have any aliases
from the vmap layer.

.. _`vm_unmap_ram`:

vm_unmap_ram
============

.. c:function:: void vm_unmap_ram(const void *mem, unsigned int count)

    unmap linear kernel address space set up by vm_map_ram

    :param mem:
        the pointer returned by vm_map_ram
    :type mem: const void \*

    :param count:
        the count passed to that vm_map_ram call (cannot unmap partial)
    :type count: unsigned int

.. _`vm_map_ram`:

vm_map_ram
==========

.. c:function:: void *vm_map_ram(struct page **pages, unsigned int count, int node, pgprot_t prot)

    map pages linearly into kernel virtual address (vmalloc space)

    :param pages:
        an array of pointers to the pages to be mapped
    :type pages: struct page \*\*

    :param count:
        number of pages
    :type count: unsigned int

    :param node:
        prefer to allocate data structures on this node
    :type node: int

    :param prot:
        memory protection to use. PAGE_KERNEL for regular RAM
    :type prot: pgprot_t

.. _`vm_map_ram.description`:

Description
-----------

If you use this function for less than VMAP_MAX_ALLOC pages, it could be
faster than vmap so it's good.  But if you mix long-life and short-life
objects with \ :c:func:`vm_map_ram`\ , it could consume lots of address space through
fragmentation (especially on a 32bit machine).  You could see failures in
the end.  Please use this function for short-lived objects.

.. _`vm_map_ram.return`:

Return
------

a pointer to the address that has been mapped, or \ ``NULL``\  on failure

.. _`vm_area_add_early`:

vm_area_add_early
=================

.. c:function:: void vm_area_add_early(struct vm_struct *vm)

    add vmap area early during boot

    :param vm:
        vm_struct to add
    :type vm: struct vm_struct \*

.. _`vm_area_add_early.description`:

Description
-----------

This function is used to add fixed kernel vm area to vmlist before
\ :c:func:`vmalloc_init`\  is called.  \ ``vm->addr``\ , \ ``vm->size``\ , and \ ``vm->flags``\ 
should contain proper values and the other fields should be zero.

DO NOT USE THIS FUNCTION UNLESS YOU KNOW WHAT YOU'RE DOING.

.. _`vm_area_register_early`:

vm_area_register_early
======================

.. c:function:: void vm_area_register_early(struct vm_struct *vm, size_t align)

    register vmap area early during boot

    :param vm:
        vm_struct to register
    :type vm: struct vm_struct \*

    :param align:
        requested alignment
    :type align: size_t

.. _`vm_area_register_early.description`:

Description
-----------

This function is used to register kernel vm area before
\ :c:func:`vmalloc_init`\  is called.  \ ``vm->size``\  and \ ``vm->flags``\  should contain
proper values on entry and other fields should be zero.  On return,
vm->addr contains the allocated address.

DO NOT USE THIS FUNCTION UNLESS YOU KNOW WHAT YOU'RE DOING.

.. _`map_kernel_range_noflush`:

map_kernel_range_noflush
========================

.. c:function:: int map_kernel_range_noflush(unsigned long addr, unsigned long size, pgprot_t prot, struct page **pages)

    map kernel VM area with the specified pages

    :param addr:
        start of the VM area to map
    :type addr: unsigned long

    :param size:
        size of the VM area to map
    :type size: unsigned long

    :param prot:
        page protection flags to use
    :type prot: pgprot_t

    :param pages:
        pages to map
    :type pages: struct page \*\*

.. _`map_kernel_range_noflush.description`:

Description
-----------

Map PFN_UP(@size) pages at \ ``addr``\ .  The VM area \ ``addr``\  and \ ``size``\ 
specify should have been allocated using \ :c:func:`get_vm_area`\  and its
friends.

.. _`map_kernel_range_noflush.note`:

NOTE
----

This function does NOT do any cache flushing.  The caller is
responsible for calling \ :c:func:`flush_cache_vmap`\  on to-be-mapped areas
before calling this function.

.. _`map_kernel_range_noflush.return`:

Return
------

The number of pages mapped on success, -errno on failure.

.. _`unmap_kernel_range_noflush`:

unmap_kernel_range_noflush
==========================

.. c:function:: void unmap_kernel_range_noflush(unsigned long addr, unsigned long size)

    unmap kernel VM area

    :param addr:
        start of the VM area to unmap
    :type addr: unsigned long

    :param size:
        size of the VM area to unmap
    :type size: unsigned long

.. _`unmap_kernel_range_noflush.description`:

Description
-----------

Unmap PFN_UP(@size) pages at \ ``addr``\ .  The VM area \ ``addr``\  and \ ``size``\ 
specify should have been allocated using \ :c:func:`get_vm_area`\  and its
friends.

.. _`unmap_kernel_range_noflush.note`:

NOTE
----

This function does NOT do any cache flushing.  The caller is
responsible for calling \ :c:func:`flush_cache_vunmap`\  on to-be-mapped areas
before calling this function and \ :c:func:`flush_tlb_kernel_range`\  after.

.. _`unmap_kernel_range`:

unmap_kernel_range
==================

.. c:function:: void unmap_kernel_range(unsigned long addr, unsigned long size)

    unmap kernel VM area and flush cache and TLB

    :param addr:
        start of the VM area to unmap
    :type addr: unsigned long

    :param size:
        size of the VM area to unmap
    :type size: unsigned long

.. _`unmap_kernel_range.description`:

Description
-----------

Similar to \ :c:func:`unmap_kernel_range_noflush`\  but flushes vcache before
the unmapping and tlb after.

.. _`get_vm_area`:

get_vm_area
===========

.. c:function:: struct vm_struct *get_vm_area(unsigned long size, unsigned long flags)

    reserve a contiguous kernel virtual area

    :param size:
        size of the area
    :type size: unsigned long

    :param flags:
        \ ``VM_IOREMAP``\  for I/O mappings or VM_ALLOC
    :type flags: unsigned long

.. _`get_vm_area.description`:

Description
-----------

     Search an area of \ ``size``\  in the kernel virtual mapping area,
     and reserved it for out purposes.  Returns the area descriptor
     on success or \ ``NULL``\  on failure.

.. _`find_vm_area`:

find_vm_area
============

.. c:function:: struct vm_struct *find_vm_area(const void *addr)

    find a continuous kernel virtual area

    :param addr:
        base address
    :type addr: const void \*

.. _`find_vm_area.description`:

Description
-----------

     Search for the kernel VM area starting at \ ``addr``\ , and return it.
     It is up to the caller to do all required locking to keep the returned
     pointer valid.

.. _`remove_vm_area`:

remove_vm_area
==============

.. c:function:: struct vm_struct *remove_vm_area(const void *addr)

    find and remove a continuous kernel virtual area

    :param addr:
        base address
    :type addr: const void \*

.. _`remove_vm_area.description`:

Description
-----------

     Search for the kernel VM area starting at \ ``addr``\ , and remove it.
     This function returns the found VM area, but using it is NOT safe
     on SMP machines, except for its size or flags.

.. _`vfree_atomic`:

vfree_atomic
============

.. c:function:: void vfree_atomic(const void *addr)

    release memory allocated by \ :c:func:`vmalloc`\ 

    :param addr:
        memory base address
    :type addr: const void \*

.. _`vfree_atomic.description`:

Description
-----------

     This one is just like \ :c:func:`vfree`\  but can be called in any atomic context
     except NMIs.

.. _`vfree`:

vfree
=====

.. c:function:: void vfree(const void *addr)

    release memory allocated by \ :c:func:`vmalloc`\ 

    :param addr:
        memory base address
    :type addr: const void \*

.. _`vfree.description`:

Description
-----------

     Free the virtually continuous memory area starting at \ ``addr``\ , as
     obtained from \ :c:func:`vmalloc`\ , \ :c:func:`vmalloc_32`\  or \ :c:func:`__vmalloc`\ . If \ ``addr``\  is
     NULL, no operation is performed.

     Must not be called in NMI context (strictly speaking, only if we don't
     have CONFIG_ARCH_HAVE_NMI_SAFE_CMPXCHG, but making the calling
     conventions for \ :c:func:`vfree`\  arch-depenedent would be a really bad idea)

     May sleep if called *not* from interrupt context.

.. _`vfree.note`:

NOTE
----

assumes that the object at \ ``addr``\  has a size >= sizeof(llist_node)

.. _`vunmap`:

vunmap
======

.. c:function:: void vunmap(const void *addr)

    release virtual mapping obtained by \ :c:func:`vmap`\ 

    :param addr:
        memory base address
    :type addr: const void \*

.. _`vunmap.description`:

Description
-----------

     Free the virtually contiguous memory area starting at \ ``addr``\ ,
     which was created from the page array passed to \ :c:func:`vmap`\ .

     Must not be called in interrupt context.

.. _`vmap`:

vmap
====

.. c:function:: void *vmap(struct page **pages, unsigned int count, unsigned long flags, pgprot_t prot)

    map an array of pages into virtually contiguous space

    :param pages:
        array of page pointers
    :type pages: struct page \*\*

    :param count:
        number of pages to map
    :type count: unsigned int

    :param flags:
        vm_area->flags
    :type flags: unsigned long

    :param prot:
        page protection for the mapping
    :type prot: pgprot_t

.. _`vmap.description`:

Description
-----------

     Maps \ ``count``\  pages from \ ``pages``\  into contiguous kernel virtual
     space.

.. _`__vmalloc_node_range`:

__vmalloc_node_range
====================

.. c:function:: void *__vmalloc_node_range(unsigned long size, unsigned long align, unsigned long start, unsigned long end, gfp_t gfp_mask, pgprot_t prot, unsigned long vm_flags, int node, const void *caller)

    allocate virtually contiguous memory

    :param size:
        allocation size
    :type size: unsigned long

    :param align:
        desired alignment
    :type align: unsigned long

    :param start:
        vm area range start
    :type start: unsigned long

    :param end:
        vm area range end
    :type end: unsigned long

    :param gfp_mask:
        flags for the page level allocator
    :type gfp_mask: gfp_t

    :param prot:
        protection mask for the allocated pages
    :type prot: pgprot_t

    :param vm_flags:
        additional vm area flags (e.g. \ ``VM_NO_GUARD``\ )
    :type vm_flags: unsigned long

    :param node:
        node to use for allocation or NUMA_NO_NODE
    :type node: int

    :param caller:
        caller's return address
    :type caller: const void \*

.. _`__vmalloc_node_range.description`:

Description
-----------

     Allocate enough pages to cover \ ``size``\  from the page level
     allocator with \ ``gfp_mask``\  flags.  Map them into contiguous
     kernel virtual space, using a pagetable protection of \ ``prot``\ .

.. _`__vmalloc_node`:

__vmalloc_node
==============

.. c:function:: void *__vmalloc_node(unsigned long size, unsigned long align, gfp_t gfp_mask, pgprot_t prot, int node, const void *caller)

    allocate virtually contiguous memory

    :param size:
        allocation size
    :type size: unsigned long

    :param align:
        desired alignment
    :type align: unsigned long

    :param gfp_mask:
        flags for the page level allocator
    :type gfp_mask: gfp_t

    :param prot:
        protection mask for the allocated pages
    :type prot: pgprot_t

    :param node:
        node to use for allocation or NUMA_NO_NODE
    :type node: int

    :param caller:
        caller's return address
    :type caller: const void \*

.. _`__vmalloc_node.description`:

Description
-----------

     Allocate enough pages to cover \ ``size``\  from the page level
     allocator with \ ``gfp_mask``\  flags.  Map them into contiguous
     kernel virtual space, using a pagetable protection of \ ``prot``\ .

     Reclaim modifiers in \ ``gfp_mask``\  - __GFP_NORETRY, __GFP_RETRY_MAYFAIL
     and __GFP_NOFAIL are not supported

     Any use of gfp flags outside of GFP_KERNEL should be consulted
     with mm people.

.. _`vmalloc`:

vmalloc
=======

.. c:function:: void *vmalloc(unsigned long size)

    allocate virtually contiguous memory

    :param size:
        allocation size
        Allocate enough pages to cover \ ``size``\  from the page level
        allocator and map them into contiguous kernel virtual space.
    :type size: unsigned long

.. _`vmalloc.description`:

Description
-----------

     For tight control over page level allocator and protection flags
     use \ :c:func:`__vmalloc`\  instead.

.. _`vzalloc`:

vzalloc
=======

.. c:function:: void *vzalloc(unsigned long size)

    allocate virtually contiguous memory with zero fill

    :param size:
        allocation size
        Allocate enough pages to cover \ ``size``\  from the page level
        allocator and map them into contiguous kernel virtual space.
        The memory allocated is set to zero.
    :type size: unsigned long

.. _`vzalloc.description`:

Description
-----------

     For tight control over page level allocator and protection flags
     use \ :c:func:`__vmalloc`\  instead.

.. _`vmalloc_user`:

vmalloc_user
============

.. c:function:: void *vmalloc_user(unsigned long size)

    allocate zeroed virtually contiguous memory for userspace

    :param size:
        allocation size
    :type size: unsigned long

.. _`vmalloc_user.description`:

Description
-----------

The resulting memory area is zeroed so it can be mapped to userspace
without leaking data.

.. _`vmalloc_node`:

vmalloc_node
============

.. c:function:: void *vmalloc_node(unsigned long size, int node)

    allocate memory on a specific node

    :param size:
        allocation size
    :type size: unsigned long

    :param node:
        numa node
    :type node: int

.. _`vmalloc_node.description`:

Description
-----------

     Allocate enough pages to cover \ ``size``\  from the page level
     allocator and map them into contiguous kernel virtual space.

     For tight control over page level allocator and protection flags
     use \ :c:func:`__vmalloc`\  instead.

.. _`vzalloc_node`:

vzalloc_node
============

.. c:function:: void *vzalloc_node(unsigned long size, int node)

    allocate memory on a specific node with zero fill

    :param size:
        allocation size
    :type size: unsigned long

    :param node:
        numa node
    :type node: int

.. _`vzalloc_node.description`:

Description
-----------

Allocate enough pages to cover \ ``size``\  from the page level
allocator and map them into contiguous kernel virtual space.
The memory allocated is set to zero.

For tight control over page level allocator and protection flags
use \ :c:func:`__vmalloc_node`\  instead.

.. _`vmalloc_exec`:

vmalloc_exec
============

.. c:function:: void *vmalloc_exec(unsigned long size)

    allocate virtually contiguous, executable memory

    :param size:
        allocation size
    :type size: unsigned long

.. _`vmalloc_exec.description`:

Description
-----------

     Kernel-internal function to allocate enough pages to cover \ ``size``\ 
     the page level allocator and map them into contiguous and
     executable kernel virtual space.

     For tight control over page level allocator and protection flags
     use \ :c:func:`__vmalloc`\  instead.

.. _`vmalloc_32`:

vmalloc_32
==========

.. c:function:: void *vmalloc_32(unsigned long size)

    allocate virtually contiguous memory (32bit addressable)

    :param size:
        allocation size
    :type size: unsigned long

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

    :param size:
        allocation size
    :type size: unsigned long

.. _`vmalloc_32_user.description`:

Description
-----------

The resulting memory area is 32bit addressable and zeroed so it can be
mapped to userspace without leaking data.

.. _`vread`:

vread
=====

.. c:function:: long vread(char *buf, char *addr, unsigned long count)

    read vmalloc area in a safe way.

    :param buf:
        buffer for reading data
    :type buf: char \*

    :param addr:
        vm address.
    :type addr: char \*

    :param count:
        number of bytes to be read.
    :type count: unsigned long

.. _`vread.description`:

Description
-----------

     Returns # of bytes which addr and buf should be increased.
     (same number to \ ``count``\ ). Returns 0 if [addr...addr+count) doesn't
     includes any intersect with alive vmalloc area.

     This function checks that addr is a valid vmalloc'ed area, and
     copy data from that area to a given buffer. If the given memory range
     of [addr...addr+count) includes some valid address, data is copied to
     proper area of \ ``buf``\ . If there are memory holes, they'll be zero-filled.
     IOREMAP area is treated as memory hole and no copy is done.

     If [addr...addr+count) doesn't includes any intersects with alive
     vm_struct area, returns 0. \ ``buf``\  should be kernel's buffer.

.. _`vread.note`:

Note
----

In usual ops, \ :c:func:`vread`\  is never necessary because the caller
     should know \ :c:func:`vmalloc`\  area is valid and can use \ :c:func:`memcpy`\ .
     This is for routines which have to access vmalloc area without
     any informaion, as /dev/kmem.

.. _`vwrite`:

vwrite
======

.. c:function:: long vwrite(char *buf, char *addr, unsigned long count)

    write vmalloc area in a safe way.

    :param buf:
        buffer for source data
    :type buf: char \*

    :param addr:
        vm address.
    :type addr: char \*

    :param count:
        number of bytes to be read.
    :type count: unsigned long

.. _`vwrite.description`:

Description
-----------

     Returns # of bytes which addr and buf should be incresed.
     (same number to \ ``count``\ ).
     If [addr...addr+count) doesn't includes any intersect with valid
     vmalloc area, returns 0.

     This function checks that addr is a valid vmalloc'ed area, and
     copy data from a buffer to the given addr. If specified range of
     [addr...addr+count) includes some valid address, data is copied from
     proper area of \ ``buf``\ . If there are memory holes, no copy to hole.
     IOREMAP area is treated as memory hole and no copy is done.

     If [addr...addr+count) doesn't includes any intersects with alive
     vm_struct area, returns 0. \ ``buf``\  should be kernel's buffer.

.. _`vwrite.note`:

Note
----

In usual ops, \ :c:func:`vwrite`\  is never necessary because the caller
     should know \ :c:func:`vmalloc`\  area is valid and can use \ :c:func:`memcpy`\ .
     This is for routines which have to access vmalloc area without
     any informaion, as /dev/kmem.

.. _`remap_vmalloc_range_partial`:

remap_vmalloc_range_partial
===========================

.. c:function:: int remap_vmalloc_range_partial(struct vm_area_struct *vma, unsigned long uaddr, void *kaddr, unsigned long size)

    map vmalloc pages to userspace

    :param vma:
        vma to cover
    :type vma: struct vm_area_struct \*

    :param uaddr:
        target user address to start at
    :type uaddr: unsigned long

    :param kaddr:
        virtual address of vmalloc kernel memory
    :type kaddr: void \*

    :param size:
        size of map area
    :type size: unsigned long

.. _`remap_vmalloc_range_partial.return`:

Return
------

0 for success, -Exxx on failure

     This function checks that \ ``kaddr``\  is a valid vmalloc'ed area,
     and that it is big enough to cover the range starting at
     \ ``uaddr``\  in \ ``vma``\ . Will return failure if that criteria isn't
     met.

     Similar to \ :c:func:`remap_pfn_range`\  (see mm/memory.c)

.. _`remap_vmalloc_range`:

remap_vmalloc_range
===================

.. c:function:: int remap_vmalloc_range(struct vm_area_struct *vma, void *addr, unsigned long pgoff)

    map vmalloc pages to userspace

    :param vma:
        vma to cover (map full range of vma)
    :type vma: struct vm_area_struct \*

    :param addr:
        vmalloc memory
    :type addr: void \*

    :param pgoff:
        number of pages into addr before first page to map
    :type pgoff: unsigned long

.. _`remap_vmalloc_range.return`:

Return
------

0 for success, -Exxx on failure

     This function checks that addr is a valid vmalloc'ed area, and
     that it is big enough to cover the vma. Will return failure if
     that criteria isn't met.

     Similar to \ :c:func:`remap_pfn_range`\  (see mm/memory.c)

.. _`alloc_vm_area`:

alloc_vm_area
=============

.. c:function:: struct vm_struct *alloc_vm_area(size_t size, pte_t **ptes)

    allocate a range of kernel address space

    :param size:
        size of the area
    :type size: size_t

    :param ptes:
        returns the PTEs for the address space
    :type ptes: pte_t \*\*

.. _`alloc_vm_area.return`:

Return
------

NULL on failure, vm_struct on success

     This function reserves a range of kernel address space, and
     allocates pagetables to map that range.  No actual mappings
     are created.

     If \ ``ptes``\  is non-NULL, pointers to the PTEs (in init_mm)
     allocated for the VM area are returned.

.. _`pvm_find_next_prev`:

pvm_find_next_prev
==================

.. c:function:: bool pvm_find_next_prev(unsigned long end, struct vmap_area **pnext, struct vmap_area **pprev)

    find the next and prev vmap_area surrounding \ ``end``\ 

    :param end:
        target address
    :type end: unsigned long

    :param pnext:
        out arg for the next vmap_area
    :type pnext: struct vmap_area \*\*

    :param pprev:
        out arg for the previous vmap_area
    :type pprev: struct vmap_area \*\*

.. _`pvm_find_next_prev.return`:

Return
------

\ ``true``\  if either or both of next and prev are found,
         \ ``false``\  if no vmap_area exists

Find vmap_areas end addresses of which enclose \ ``end``\ .  ie. if not
NULL, *pnext->va_end > \ ``end``\  and *pprev->va_end <= \ ``end``\ .

.. _`pvm_determine_end`:

pvm_determine_end
=================

.. c:function:: unsigned long pvm_determine_end(struct vmap_area **pnext, struct vmap_area **pprev, unsigned long align)

    find the highest aligned address between two vmap_areas

    :param pnext:
        in/out arg for the next vmap_area
    :type pnext: struct vmap_area \*\*

    :param pprev:
        in/out arg for the previous vmap_area
    :type pprev: struct vmap_area \*\*

    :param align:
        alignment
    :type align: unsigned long

.. _`pvm_determine_end.return`:

Return
------

determined end address

Find the highest aligned address between *@pnext and *@pprev below
VMALLOC_END.  *@pnext and *@pprev are adjusted so that the aligned
down address is between the end addresses of the two vmap_areas.

Please note that the address returned by this function may fall
inside *@pnext vmap_area.  The caller is responsible for checking
that.

.. _`pcpu_get_vm_areas`:

pcpu_get_vm_areas
=================

.. c:function:: struct vm_struct **pcpu_get_vm_areas(const unsigned long *offsets, const size_t *sizes, int nr_vms, size_t align)

    allocate vmalloc areas for percpu allocator

    :param offsets:
        array containing offset of each area
    :type offsets: const unsigned long \*

    :param sizes:
        array containing size of each area
    :type sizes: const size_t \*

    :param nr_vms:
        the number of areas to allocate
    :type nr_vms: int

    :param align:
        alignment, all entries in \ ``offsets``\  and \ ``sizes``\  must be aligned to this
    :type align: size_t

.. _`pcpu_get_vm_areas.return`:

Return
------

kmalloc'd vm_struct pointer array pointing to allocated
         vm_structs on success, \ ``NULL``\  on failure

Percpu allocator wants to use congruent vm areas so that it can
maintain the offsets among percpu areas.  This function allocates
congruent vmalloc areas for it with GFP_KERNEL.  These areas tend to
be scattered pretty far, distance between two areas easily going up
to gigabytes.  To avoid interacting with regular vmallocs, these
areas are allocated from top.

Despite its complicated look, this allocator is rather simple.  It
does everything top-down and scans areas from the end looking for
matching slot.  While scanning, if any of the areas overlaps with
existing vmap_area, the base address is pulled down to fit the
area.  Scanning is repeated till all the areas fit and then all
necessary data structures are inserted and the result is returned.

.. _`pcpu_free_vm_areas`:

pcpu_free_vm_areas
==================

.. c:function:: void pcpu_free_vm_areas(struct vm_struct **vms, int nr_vms)

    free vmalloc areas for percpu allocator

    :param vms:
        vm_struct pointer array returned by \ :c:func:`pcpu_get_vm_areas`\ 
    :type vms: struct vm_struct \*\*

    :param nr_vms:
        the number of allocated areas
    :type nr_vms: int

.. _`pcpu_free_vm_areas.description`:

Description
-----------

Free vm_structs and the array allocated by \ :c:func:`pcpu_get_vm_areas`\ .

.. This file was automatic generated / don't edit.

