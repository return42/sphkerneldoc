.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/mm/gmap.c

.. _`gmap_alloc`:

gmap_alloc
==========

.. c:function:: struct gmap *gmap_alloc(unsigned long limit)

    allocate and initialize a guest address space

    :param limit:
        maximum address of the gmap address space
    :type limit: unsigned long

.. _`gmap_alloc.description`:

Description
-----------

Returns a guest address space structure.

.. _`gmap_create`:

gmap_create
===========

.. c:function:: struct gmap *gmap_create(struct mm_struct *mm, unsigned long limit)

    create a guest address space

    :param mm:
        pointer to the parent mm_struct
    :type mm: struct mm_struct \*

    :param limit:
        maximum size of the gmap address space
    :type limit: unsigned long

.. _`gmap_create.description`:

Description
-----------

Returns a guest address space structure.

.. _`gmap_free`:

gmap_free
=========

.. c:function:: void gmap_free(struct gmap *gmap)

    free a guest address space

    :param gmap:
        pointer to the guest address space structure
    :type gmap: struct gmap \*

.. _`gmap_free.description`:

Description
-----------

No locks required. There are no references to this gmap anymore.

.. _`gmap_get`:

gmap_get
========

.. c:function:: struct gmap *gmap_get(struct gmap *gmap)

    increase reference counter for guest address space

    :param gmap:
        pointer to the guest address space structure
    :type gmap: struct gmap \*

.. _`gmap_get.description`:

Description
-----------

Returns the gmap pointer

.. _`gmap_put`:

gmap_put
========

.. c:function:: void gmap_put(struct gmap *gmap)

    decrease reference counter for guest address space

    :param gmap:
        pointer to the guest address space structure
    :type gmap: struct gmap \*

.. _`gmap_put.description`:

Description
-----------

If the reference counter reaches zero the guest address space is freed.

.. _`gmap_remove`:

gmap_remove
===========

.. c:function:: void gmap_remove(struct gmap *gmap)

    remove a guest address space but do not free it yet

    :param gmap:
        pointer to the guest address space structure
    :type gmap: struct gmap \*

.. _`gmap_enable`:

gmap_enable
===========

.. c:function:: void gmap_enable(struct gmap *gmap)

    switch primary space to the guest address space

    :param gmap:
        pointer to the guest address space structure
    :type gmap: struct gmap \*

.. _`gmap_disable`:

gmap_disable
============

.. c:function:: void gmap_disable(struct gmap *gmap)

    switch back to the standard primary address space

    :param gmap:
        pointer to the guest address space structure
    :type gmap: struct gmap \*

.. _`gmap_get_enabled`:

gmap_get_enabled
================

.. c:function:: struct gmap *gmap_get_enabled( void)

    get a pointer to the currently enabled gmap

    :param void:
        no arguments
    :type void: 

.. _`gmap_get_enabled.description`:

Description
-----------

Returns a pointer to the currently enabled gmap. 0 if none is enabled.

.. _`__gmap_segment_gaddr`:

\__gmap_segment_gaddr
=====================

.. c:function:: unsigned long __gmap_segment_gaddr(unsigned long *entry)

    find virtual address from segment pointer

    :param entry:
        pointer to a segment table entry in the guest address space
    :type entry: unsigned long \*

.. _`__gmap_segment_gaddr.description`:

Description
-----------

Returns the virtual address in the guest address space for the segment

.. _`__gmap_unlink_by_vmaddr`:

\__gmap_unlink_by_vmaddr
========================

.. c:function:: int __gmap_unlink_by_vmaddr(struct gmap *gmap, unsigned long vmaddr)

    unlink a single segment via a host address

    :param gmap:
        pointer to the guest address space structure
    :type gmap: struct gmap \*

    :param vmaddr:
        address in the host process address space
    :type vmaddr: unsigned long

.. _`__gmap_unlink_by_vmaddr.description`:

Description
-----------

Returns 1 if a TLB flush is required

.. _`__gmap_unmap_by_gaddr`:

\__gmap_unmap_by_gaddr
======================

.. c:function:: int __gmap_unmap_by_gaddr(struct gmap *gmap, unsigned long gaddr)

    unmap a single segment via a guest address

    :param gmap:
        pointer to the guest address space structure
    :type gmap: struct gmap \*

    :param gaddr:
        address in the guest address space
    :type gaddr: unsigned long

.. _`__gmap_unmap_by_gaddr.description`:

Description
-----------

Returns 1 if a TLB flush is required

.. _`gmap_unmap_segment`:

gmap_unmap_segment
==================

.. c:function:: int gmap_unmap_segment(struct gmap *gmap, unsigned long to, unsigned long len)

    unmap segment from the guest address space

    :param gmap:
        pointer to the guest address space structure
    :type gmap: struct gmap \*

    :param to:
        address in the guest address space
    :type to: unsigned long

    :param len:
        length of the memory area to unmap
    :type len: unsigned long

.. _`gmap_unmap_segment.description`:

Description
-----------

Returns 0 if the unmap succeeded, -EINVAL if not.

.. _`gmap_map_segment`:

gmap_map_segment
================

.. c:function:: int gmap_map_segment(struct gmap *gmap, unsigned long from, unsigned long to, unsigned long len)

    map a segment to the guest address space

    :param gmap:
        pointer to the guest address space structure
    :type gmap: struct gmap \*

    :param from:
        source address in the parent address space
    :type from: unsigned long

    :param to:
        target address in the guest address space
    :type to: unsigned long

    :param len:
        length of the memory area to map
    :type len: unsigned long

.. _`gmap_map_segment.description`:

Description
-----------

Returns 0 if the mmap succeeded, -EINVAL or -ENOMEM if not.

.. _`__gmap_translate`:

\__gmap_translate
=================

.. c:function:: unsigned long __gmap_translate(struct gmap *gmap, unsigned long gaddr)

    translate a guest address to a user space address

    :param gmap:
        pointer to guest mapping meta data structure
    :type gmap: struct gmap \*

    :param gaddr:
        guest address
    :type gaddr: unsigned long

.. _`__gmap_translate.description`:

Description
-----------

Returns user space address which corresponds to the guest address or
-EFAULT if no such mapping exists.
This function does not establish potentially missing page table entries.
The mmap_sem of the mm that belongs to the address space must be held
when this function gets called.

.. _`__gmap_translate.note`:

Note
----

Can also be called for shadow gmaps.

.. _`gmap_translate`:

gmap_translate
==============

.. c:function:: unsigned long gmap_translate(struct gmap *gmap, unsigned long gaddr)

    translate a guest address to a user space address

    :param gmap:
        pointer to guest mapping meta data structure
    :type gmap: struct gmap \*

    :param gaddr:
        guest address
    :type gaddr: unsigned long

.. _`gmap_translate.description`:

Description
-----------

Returns user space address which corresponds to the guest address or
-EFAULT if no such mapping exists.
This function does not establish potentially missing page table entries.

.. _`gmap_unlink`:

gmap_unlink
===========

.. c:function:: void gmap_unlink(struct mm_struct *mm, unsigned long *table, unsigned long vmaddr)

    disconnect a page table from the gmap shadow tables

    :param mm:
        *undescribed*
    :type mm: struct mm_struct \*

    :param table:
        pointer to the host page table
    :type table: unsigned long \*

    :param vmaddr:
        vm address associated with the host page table
    :type vmaddr: unsigned long

.. _`__gmap_link`:

\__gmap_link
============

.. c:function:: int __gmap_link(struct gmap *gmap, unsigned long gaddr, unsigned long vmaddr)

    set up shadow page tables to connect a host to a guest address

    :param gmap:
        pointer to guest mapping meta data structure
    :type gmap: struct gmap \*

    :param gaddr:
        guest address
    :type gaddr: unsigned long

    :param vmaddr:
        vm address
    :type vmaddr: unsigned long

.. _`__gmap_link.description`:

Description
-----------

Returns 0 on success, -ENOMEM for out of memory conditions, and -EFAULT
if the vm address is already mapped to a different guest segment.
The mmap_sem of the mm that belongs to the address space must be held
when this function gets called.

.. _`gmap_fault`:

gmap_fault
==========

.. c:function:: int gmap_fault(struct gmap *gmap, unsigned long gaddr, unsigned int fault_flags)

    resolve a fault on a guest address

    :param gmap:
        pointer to guest mapping meta data structure
    :type gmap: struct gmap \*

    :param gaddr:
        guest address
    :type gaddr: unsigned long

    :param fault_flags:
        flags to pass down to \ :c:func:`handle_mm_fault`\ 
    :type fault_flags: unsigned int

.. _`gmap_fault.description`:

Description
-----------

Returns 0 on success, -ENOMEM for out of memory conditions, and -EFAULT
if the vm address is already mapped to a different guest segment.

.. _`gmap_register_pte_notifier`:

gmap_register_pte_notifier
==========================

.. c:function:: void gmap_register_pte_notifier(struct gmap_notifier *nb)

    register a pte invalidation callback

    :param nb:
        pointer to the gmap notifier block
    :type nb: struct gmap_notifier \*

.. _`gmap_unregister_pte_notifier`:

gmap_unregister_pte_notifier
============================

.. c:function:: void gmap_unregister_pte_notifier(struct gmap_notifier *nb)

    remove a pte invalidation callback

    :param nb:
        pointer to the gmap notifier block
    :type nb: struct gmap_notifier \*

.. _`gmap_call_notifier`:

gmap_call_notifier
==================

.. c:function:: void gmap_call_notifier(struct gmap *gmap, unsigned long start, unsigned long end)

    call all registered invalidation callbacks

    :param gmap:
        pointer to guest mapping meta data structure
    :type gmap: struct gmap \*

    :param start:
        start virtual address in the guest address space
    :type start: unsigned long

    :param end:
        end virtual address in the guest address space
    :type end: unsigned long

.. _`gmap_table_walk`:

gmap_table_walk
===============

.. c:function:: unsigned long *gmap_table_walk(struct gmap *gmap, unsigned long gaddr, int level)

    walk the gmap page tables

    :param gmap:
        pointer to guest mapping meta data structure
    :type gmap: struct gmap \*

    :param gaddr:
        virtual address in the guest address space
    :type gaddr: unsigned long

    :param level:
        returns a pointer to a region-1 table entry (or NULL)
    :type level: int

.. _`gmap_table_walk.description`:

Description
-----------

Returns a table entry pointer for the given guest address and \ ``level``\ 

Returns NULL if the gmap page tables could not be walked to the
requested level.

.. _`gmap_table_walk.note`:

Note
----

Can also be called for shadow gmaps.

.. _`gmap_pte_op_walk`:

gmap_pte_op_walk
================

.. c:function:: pte_t *gmap_pte_op_walk(struct gmap *gmap, unsigned long gaddr, spinlock_t **ptl)

    walk the gmap page table, get the page table lock and return the pte pointer

    :param gmap:
        pointer to guest mapping meta data structure
    :type gmap: struct gmap \*

    :param gaddr:
        virtual address in the guest address space
    :type gaddr: unsigned long

    :param ptl:
        pointer to the spinlock pointer
    :type ptl: spinlock_t \*\*

.. _`gmap_pte_op_walk.description`:

Description
-----------

Returns a pointer to the locked pte for a guest address, or NULL

.. _`gmap_pte_op_fixup`:

gmap_pte_op_fixup
=================

.. c:function:: int gmap_pte_op_fixup(struct gmap *gmap, unsigned long gaddr, unsigned long vmaddr, int prot)

    force a page in and connect the gmap page table

    :param gmap:
        pointer to guest mapping meta data structure
    :type gmap: struct gmap \*

    :param gaddr:
        virtual address in the guest address space
    :type gaddr: unsigned long

    :param vmaddr:
        address in the host process address space
    :type vmaddr: unsigned long

    :param prot:
        indicates access rights: PROT_NONE, PROT_READ or PROT_WRITE
    :type prot: int

.. _`gmap_pte_op_fixup.description`:

Description
-----------

Returns 0 if the caller can retry \__gmap_translate (might fail again),
-ENOMEM if out of memory and -EFAULT if anything goes wrong while fixing
up or connecting the gmap page table.

.. _`gmap_pte_op_end`:

gmap_pte_op_end
===============

.. c:function:: void gmap_pte_op_end(spinlock_t *ptl)

    release the page table lock

    :param ptl:
        pointer to the spinlock pointer
    :type ptl: spinlock_t \*

.. _`gmap_pmd_op_walk`:

gmap_pmd_op_walk
================

.. c:function:: pmd_t *gmap_pmd_op_walk(struct gmap *gmap, unsigned long gaddr)

    walk the gmap tables, get the guest table lock and return the pmd pointer

    :param gmap:
        pointer to guest mapping meta data structure
    :type gmap: struct gmap \*

    :param gaddr:
        virtual address in the guest address space
    :type gaddr: unsigned long

.. _`gmap_pmd_op_walk.description`:

Description
-----------

Returns a pointer to the pmd for a guest address, or NULL

.. _`gmap_pmd_op_end`:

gmap_pmd_op_end
===============

.. c:function:: void gmap_pmd_op_end(struct gmap *gmap, pmd_t *pmdp)

    release the guest_table_lock if needed

    :param gmap:
        pointer to the guest mapping meta data structure
    :type gmap: struct gmap \*

    :param pmdp:
        pointer to the pmd
    :type pmdp: pmd_t \*

.. _`gmap_mprotect_notify`:

gmap_mprotect_notify
====================

.. c:function:: int gmap_mprotect_notify(struct gmap *gmap, unsigned long gaddr, unsigned long len, int prot)

    change access rights for a range of ptes and call the notifier if any pte changes again

    :param gmap:
        pointer to guest mapping meta data structure
    :type gmap: struct gmap \*

    :param gaddr:
        virtual address in the guest address space
    :type gaddr: unsigned long

    :param len:
        size of area
    :type len: unsigned long

    :param prot:
        indicates access rights: PROT_NONE, PROT_READ or PROT_WRITE
    :type prot: int

.. _`gmap_mprotect_notify.description`:

Description
-----------

Returns 0 if for each page in the given range a gmap mapping exists,
the new access rights could be set and the notifier could be armed.
If the gmap mapping is missing for one or more pages -EFAULT is
returned. If no memory could be allocated -ENOMEM is returned.
This function establishes missing page table entries.

.. _`gmap_read_table`:

gmap_read_table
===============

.. c:function:: int gmap_read_table(struct gmap *gmap, unsigned long gaddr, unsigned long *val)

    get an unsigned long value from a guest page table using absolute addressing, without marking the page referenced.

    :param gmap:
        pointer to guest mapping meta data structure
    :type gmap: struct gmap \*

    :param gaddr:
        virtual address in the guest address space
    :type gaddr: unsigned long

    :param val:
        pointer to the unsigned long value to return
    :type val: unsigned long \*

.. _`gmap_read_table.description`:

Description
-----------

Returns 0 if the value was read, -ENOMEM if out of memory and -EFAULT
if reading using the virtual address failed. -EINVAL if called on a gmap
shadow.

Called with gmap->mm->mmap_sem in read.

.. _`gmap_insert_rmap`:

gmap_insert_rmap
================

.. c:function:: void gmap_insert_rmap(struct gmap *sg, unsigned long vmaddr, struct gmap_rmap *rmap)

    add a rmap to the host_to_rmap radix tree

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param vmaddr:
        vm address associated with the rmap
    :type vmaddr: unsigned long

    :param rmap:
        pointer to the rmap structure
    :type rmap: struct gmap_rmap \*

.. _`gmap_insert_rmap.description`:

Description
-----------

Called with the sg->guest_table_lock

.. _`gmap_protect_rmap`:

gmap_protect_rmap
=================

.. c:function:: int gmap_protect_rmap(struct gmap *sg, unsigned long raddr, unsigned long paddr, unsigned long len)

    restrict access rights to memory (RO) and create an rmap

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param raddr:
        rmap address in the shadow gmap
    :type raddr: unsigned long

    :param paddr:
        address in the parent guest address space
    :type paddr: unsigned long

    :param len:
        length of the memory area to protect
    :type len: unsigned long

.. _`gmap_protect_rmap.description`:

Description
-----------

Returns 0 if successfully protected and the rmap was created, -ENOMEM
if out of memory and -EFAULT if paddr is invalid.

.. _`gmap_idte_one`:

gmap_idte_one
=============

.. c:function:: void gmap_idte_one(unsigned long asce, unsigned long vaddr)

    invalidate a single region or segment table entry

    :param asce:
        region or segment table \*origin\* + table-type bits
    :type asce: unsigned long

    :param vaddr:
        virtual address to identify the table entry to flush
    :type vaddr: unsigned long

.. _`gmap_idte_one.description`:

Description
-----------

The invalid bit of a single region or segment table entry is set
and the associated TLB entries depending on the entry are flushed.
The table-type of the \ ``asce``\  identifies the portion of the \ ``vaddr``\ 
that is used as the invalidation index.

.. _`gmap_unshadow_page`:

gmap_unshadow_page
==================

.. c:function:: void gmap_unshadow_page(struct gmap *sg, unsigned long raddr)

    remove a page from a shadow page table

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param raddr:
        rmap address in the shadow guest address space
    :type raddr: unsigned long

.. _`gmap_unshadow_page.description`:

Description
-----------

Called with the sg->guest_table_lock

.. _`__gmap_unshadow_pgt`:

\__gmap_unshadow_pgt
====================

.. c:function:: void __gmap_unshadow_pgt(struct gmap *sg, unsigned long raddr, unsigned long *pgt)

    remove all entries from a shadow page table

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param raddr:
        rmap address in the shadow guest address space
    :type raddr: unsigned long

    :param pgt:
        pointer to the start of a shadow page table
    :type pgt: unsigned long \*

.. _`__gmap_unshadow_pgt.description`:

Description
-----------

Called with the sg->guest_table_lock

.. _`gmap_unshadow_pgt`:

gmap_unshadow_pgt
=================

.. c:function:: void gmap_unshadow_pgt(struct gmap *sg, unsigned long raddr)

    remove a shadow page table from a segment entry

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param raddr:
        address in the shadow guest address space
    :type raddr: unsigned long

.. _`gmap_unshadow_pgt.description`:

Description
-----------

Called with the sg->guest_table_lock

.. _`__gmap_unshadow_sgt`:

\__gmap_unshadow_sgt
====================

.. c:function:: void __gmap_unshadow_sgt(struct gmap *sg, unsigned long raddr, unsigned long *sgt)

    remove all entries from a shadow segment table

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param raddr:
        rmap address in the shadow guest address space
    :type raddr: unsigned long

    :param sgt:
        pointer to the start of a shadow segment table
    :type sgt: unsigned long \*

.. _`__gmap_unshadow_sgt.description`:

Description
-----------

Called with the sg->guest_table_lock

.. _`gmap_unshadow_sgt`:

gmap_unshadow_sgt
=================

.. c:function:: void gmap_unshadow_sgt(struct gmap *sg, unsigned long raddr)

    remove a shadow segment table from a region-3 entry

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param raddr:
        rmap address in the shadow guest address space
    :type raddr: unsigned long

.. _`gmap_unshadow_sgt.description`:

Description
-----------

Called with the shadow->guest_table_lock

.. _`__gmap_unshadow_r3t`:

\__gmap_unshadow_r3t
====================

.. c:function:: void __gmap_unshadow_r3t(struct gmap *sg, unsigned long raddr, unsigned long *r3t)

    remove all entries from a shadow region-3 table

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param raddr:
        address in the shadow guest address space
    :type raddr: unsigned long

    :param r3t:
        pointer to the start of a shadow region-3 table
    :type r3t: unsigned long \*

.. _`__gmap_unshadow_r3t.description`:

Description
-----------

Called with the sg->guest_table_lock

.. _`gmap_unshadow_r3t`:

gmap_unshadow_r3t
=================

.. c:function:: void gmap_unshadow_r3t(struct gmap *sg, unsigned long raddr)

    remove a shadow region-3 table from a region-2 entry

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param raddr:
        rmap address in the shadow guest address space
    :type raddr: unsigned long

.. _`gmap_unshadow_r3t.description`:

Description
-----------

Called with the sg->guest_table_lock

.. _`__gmap_unshadow_r2t`:

\__gmap_unshadow_r2t
====================

.. c:function:: void __gmap_unshadow_r2t(struct gmap *sg, unsigned long raddr, unsigned long *r2t)

    remove all entries from a shadow region-2 table

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param raddr:
        rmap address in the shadow guest address space
    :type raddr: unsigned long

    :param r2t:
        pointer to the start of a shadow region-2 table
    :type r2t: unsigned long \*

.. _`__gmap_unshadow_r2t.description`:

Description
-----------

Called with the sg->guest_table_lock

.. _`gmap_unshadow_r2t`:

gmap_unshadow_r2t
=================

.. c:function:: void gmap_unshadow_r2t(struct gmap *sg, unsigned long raddr)

    remove a shadow region-2 table from a region-1 entry

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param raddr:
        rmap address in the shadow guest address space
    :type raddr: unsigned long

.. _`gmap_unshadow_r2t.description`:

Description
-----------

Called with the sg->guest_table_lock

.. _`__gmap_unshadow_r1t`:

\__gmap_unshadow_r1t
====================

.. c:function:: void __gmap_unshadow_r1t(struct gmap *sg, unsigned long raddr, unsigned long *r1t)

    remove all entries from a shadow region-1 table

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param raddr:
        rmap address in the shadow guest address space
    :type raddr: unsigned long

    :param r1t:
        pointer to the start of a shadow region-1 table
    :type r1t: unsigned long \*

.. _`__gmap_unshadow_r1t.description`:

Description
-----------

Called with the shadow->guest_table_lock

.. _`gmap_unshadow`:

gmap_unshadow
=============

.. c:function:: void gmap_unshadow(struct gmap *sg)

    remove a shadow page table completely

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

.. _`gmap_unshadow.description`:

Description
-----------

Called with sg->guest_table_lock

.. _`gmap_find_shadow`:

gmap_find_shadow
================

.. c:function:: struct gmap *gmap_find_shadow(struct gmap *parent, unsigned long asce, int edat_level)

    find a specific asce in the list of shadow tables

    :param parent:
        pointer to the parent gmap
    :type parent: struct gmap \*

    :param asce:
        ASCE for which the shadow table is created
    :type asce: unsigned long

    :param edat_level:
        edat level to be used for the shadow translation
    :type edat_level: int

.. _`gmap_find_shadow.description`:

Description
-----------

Returns the pointer to a gmap if a shadow table with the given asce is
already available, ERR_PTR(-EAGAIN) if another one is just being created,
otherwise NULL

.. _`gmap_shadow_valid`:

gmap_shadow_valid
=================

.. c:function:: int gmap_shadow_valid(struct gmap *sg, unsigned long asce, int edat_level)

    check if a shadow guest address space matches the given properties and is still valid

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param asce:
        ASCE for which the shadow table is requested
    :type asce: unsigned long

    :param edat_level:
        edat level to be used for the shadow translation
    :type edat_level: int

.. _`gmap_shadow_valid.description`:

Description
-----------

Returns 1 if the gmap shadow is still valid and matches the given
properties, the caller can continue using it. Returns 0 otherwise, the
caller has to request a new shadow gmap in this case.

.. _`gmap_shadow`:

gmap_shadow
===========

.. c:function:: struct gmap *gmap_shadow(struct gmap *parent, unsigned long asce, int edat_level)

    create/find a shadow guest address space

    :param parent:
        pointer to the parent gmap
    :type parent: struct gmap \*

    :param asce:
        ASCE for which the shadow table is created
    :type asce: unsigned long

    :param edat_level:
        edat level to be used for the shadow translation
    :type edat_level: int

.. _`gmap_shadow.description`:

Description
-----------

The pages of the top level page table referred by the asce parameter
will be set to read-only and marked in the PGSTEs of the kvm process.
The shadow table will be removed automatically on any change to the
PTE mapping for the source table.

Returns a guest address space structure, ERR_PTR(-ENOMEM) if out of memory,
ERR_PTR(-EAGAIN) if the caller has to retry and ERR_PTR(-EFAULT) if the
parent gmap table could not be protected.

.. _`gmap_shadow_r2t`:

gmap_shadow_r2t
===============

.. c:function:: int gmap_shadow_r2t(struct gmap *sg, unsigned long saddr, unsigned long r2t, int fake)

    create an empty shadow region 2 table

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param saddr:
        faulting address in the shadow gmap
    :type saddr: unsigned long

    :param r2t:
        parent gmap address of the region 2 table to get shadowed
    :type r2t: unsigned long

    :param fake:
        r2t references contiguous guest memory block, not a r2t
    :type fake: int

.. _`gmap_shadow_r2t.description`:

Description
-----------

The r2t parameter specifies the address of the source table. The
four pages of the source table are made read-only in the parent gmap
address space. A write to the source table area \ ``r2t``\  will automatically
remove the shadow r2 table and all of its decendents.

Returns 0 if successfully shadowed or already shadowed, -EAGAIN if the
shadow table structure is incomplete, -ENOMEM if out of memory and
-EFAULT if an address in the parent gmap could not be resolved.

Called with sg->mm->mmap_sem in read.

.. _`gmap_shadow_r3t`:

gmap_shadow_r3t
===============

.. c:function:: int gmap_shadow_r3t(struct gmap *sg, unsigned long saddr, unsigned long r3t, int fake)

    create a shadow region 3 table

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param saddr:
        faulting address in the shadow gmap
    :type saddr: unsigned long

    :param r3t:
        parent gmap address of the region 3 table to get shadowed
    :type r3t: unsigned long

    :param fake:
        r3t references contiguous guest memory block, not a r3t
    :type fake: int

.. _`gmap_shadow_r3t.description`:

Description
-----------

Returns 0 if successfully shadowed or already shadowed, -EAGAIN if the
shadow table structure is incomplete, -ENOMEM if out of memory and
-EFAULT if an address in the parent gmap could not be resolved.

Called with sg->mm->mmap_sem in read.

.. _`gmap_shadow_sgt`:

gmap_shadow_sgt
===============

.. c:function:: int gmap_shadow_sgt(struct gmap *sg, unsigned long saddr, unsigned long sgt, int fake)

    create a shadow segment table

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param saddr:
        faulting address in the shadow gmap
    :type saddr: unsigned long

    :param sgt:
        parent gmap address of the segment table to get shadowed
    :type sgt: unsigned long

    :param fake:
        sgt references contiguous guest memory block, not a sgt
    :type fake: int

.. _`gmap_shadow_sgt.return`:

Return
------

0 if successfully shadowed or already shadowed, -EAGAIN if the
shadow table structure is incomplete, -ENOMEM if out of memory and
-EFAULT if an address in the parent gmap could not be resolved.

Called with sg->mm->mmap_sem in read.

.. _`gmap_shadow_pgt_lookup`:

gmap_shadow_pgt_lookup
======================

.. c:function:: int gmap_shadow_pgt_lookup(struct gmap *sg, unsigned long saddr, unsigned long *pgt, int *dat_protection, int *fake)

    find a shadow page table

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param saddr:
        the address in the shadow aguest address space
    :type saddr: unsigned long

    :param pgt:
        parent gmap address of the page table to get shadowed
    :type pgt: unsigned long \*

    :param dat_protection:
        if the pgtable is marked as protected by dat
    :type dat_protection: int \*

    :param fake:
        pgt references contiguous guest memory block, not a pgtable
    :type fake: int \*

.. _`gmap_shadow_pgt_lookup.description`:

Description
-----------

Returns 0 if the shadow page table was found and -EAGAIN if the page
table was not found.

Called with sg->mm->mmap_sem in read.

.. _`gmap_shadow_pgt`:

gmap_shadow_pgt
===============

.. c:function:: int gmap_shadow_pgt(struct gmap *sg, unsigned long saddr, unsigned long pgt, int fake)

    instantiate a shadow page table

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param saddr:
        faulting address in the shadow gmap
    :type saddr: unsigned long

    :param pgt:
        parent gmap address of the page table to get shadowed
    :type pgt: unsigned long

    :param fake:
        pgt references contiguous guest memory block, not a pgtable
    :type fake: int

.. _`gmap_shadow_pgt.description`:

Description
-----------

Returns 0 if successfully shadowed or already shadowed, -EAGAIN if the
shadow table structure is incomplete, -ENOMEM if out of memory,
-EFAULT if an address in the parent gmap could not be resolved and

Called with gmap->mm->mmap_sem in read

.. _`gmap_shadow_page`:

gmap_shadow_page
================

.. c:function:: int gmap_shadow_page(struct gmap *sg, unsigned long saddr, pte_t pte)

    create a shadow page mapping

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param saddr:
        faulting address in the shadow gmap
    :type saddr: unsigned long

    :param pte:
        pte in parent gmap address space to get shadowed
    :type pte: pte_t

.. _`gmap_shadow_page.description`:

Description
-----------

Returns 0 if successfully shadowed or already shadowed, -EAGAIN if the
shadow table structure is incomplete, -ENOMEM if out of memory and
-EFAULT if an address in the parent gmap could not be resolved.

Called with sg->mm->mmap_sem in read.

.. _`gmap_shadow_notify`:

gmap_shadow_notify
==================

.. c:function:: void gmap_shadow_notify(struct gmap *sg, unsigned long vmaddr, unsigned long gaddr)

    handle notifications for shadow gmap

    :param sg:
        *undescribed*
    :type sg: struct gmap \*

    :param vmaddr:
        *undescribed*
    :type vmaddr: unsigned long

    :param gaddr:
        *undescribed*
    :type gaddr: unsigned long

.. _`gmap_shadow_notify.description`:

Description
-----------

Called with sg->parent->shadow_lock.

.. _`ptep_notify`:

ptep_notify
===========

.. c:function:: void ptep_notify(struct mm_struct *mm, unsigned long vmaddr, pte_t *pte, unsigned long bits)

    call all invalidation callbacks for a specific pte.

    :param mm:
        pointer to the process mm_struct
    :type mm: struct mm_struct \*

    :param vmaddr:
        *undescribed*
    :type vmaddr: unsigned long

    :param pte:
        pointer to the page table entry
    :type pte: pte_t \*

    :param bits:
        bits from the pgste that caused the notify call
    :type bits: unsigned long

.. _`ptep_notify.description`:

Description
-----------

This function is assumed to be called with the page table lock held
for the pte to notify.

.. _`gmap_pmdp_xchg`:

gmap_pmdp_xchg
==============

.. c:function:: void gmap_pmdp_xchg(struct gmap *gmap, pmd_t *pmdp, pmd_t new, unsigned long gaddr)

    exchange a gmap pmd with another

    :param gmap:
        pointer to the guest address space structure
    :type gmap: struct gmap \*

    :param pmdp:
        pointer to the pmd entry
    :type pmdp: pmd_t \*

    :param new:
        replacement entry
    :type new: pmd_t

    :param gaddr:
        the affected guest address
    :type gaddr: unsigned long

.. _`gmap_pmdp_xchg.description`:

Description
-----------

This function is assumed to be called with the guest_table_lock
held.

.. _`gmap_pmdp_invalidate`:

gmap_pmdp_invalidate
====================

.. c:function:: void gmap_pmdp_invalidate(struct mm_struct *mm, unsigned long vmaddr)

    invalidate all affected guest pmd entries without flushing

    :param mm:
        pointer to the process mm_struct
    :type mm: struct mm_struct \*

    :param vmaddr:
        virtual address in the process address space
    :type vmaddr: unsigned long

.. _`gmap_pmdp_csp`:

gmap_pmdp_csp
=============

.. c:function:: void gmap_pmdp_csp(struct mm_struct *mm, unsigned long vmaddr)

    csp all affected guest pmd entries

    :param mm:
        pointer to the process mm_struct
    :type mm: struct mm_struct \*

    :param vmaddr:
        virtual address in the process address space
    :type vmaddr: unsigned long

.. _`gmap_pmdp_idte_local`:

gmap_pmdp_idte_local
====================

.. c:function:: void gmap_pmdp_idte_local(struct mm_struct *mm, unsigned long vmaddr)

    invalidate and clear a guest pmd entry

    :param mm:
        pointer to the process mm_struct
    :type mm: struct mm_struct \*

    :param vmaddr:
        virtual address in the process address space
    :type vmaddr: unsigned long

.. _`gmap_pmdp_idte_global`:

gmap_pmdp_idte_global
=====================

.. c:function:: void gmap_pmdp_idte_global(struct mm_struct *mm, unsigned long vmaddr)

    invalidate and clear a guest pmd entry

    :param mm:
        pointer to the process mm_struct
    :type mm: struct mm_struct \*

    :param vmaddr:
        virtual address in the process address space
    :type vmaddr: unsigned long

.. _`gmap_test_and_clear_dirty_pmd`:

gmap_test_and_clear_dirty_pmd
=============================

.. c:function:: bool gmap_test_and_clear_dirty_pmd(struct gmap *gmap, pmd_t *pmdp, unsigned long gaddr)

    test and reset segment dirty status

    :param gmap:
        pointer to guest address space
    :type gmap: struct gmap \*

    :param pmdp:
        pointer to the pmd to be tested
    :type pmdp: pmd_t \*

    :param gaddr:
        virtual address in the guest address space
    :type gaddr: unsigned long

.. _`gmap_test_and_clear_dirty_pmd.description`:

Description
-----------

This function is assumed to be called with the guest_table_lock
held.

.. _`gmap_sync_dirty_log_pmd`:

gmap_sync_dirty_log_pmd
=======================

.. c:function:: void gmap_sync_dirty_log_pmd(struct gmap *gmap, unsigned long bitmap, unsigned long gaddr, unsigned long vmaddr)

    set bitmap based on dirty status of segment

    :param gmap:
        pointer to guest address space
    :type gmap: struct gmap \*

    :param bitmap:
        dirty bitmap for this pmd
    :type bitmap: unsigned long

    :param gaddr:
        virtual address in the guest address space
    :type gaddr: unsigned long

    :param vmaddr:
        virtual address in the host address space
    :type vmaddr: unsigned long

.. _`gmap_sync_dirty_log_pmd.description`:

Description
-----------

This function is assumed to be called with the guest_table_lock
held.

.. This file was automatic generated / don't edit.

