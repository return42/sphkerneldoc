.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/mm/gmap.c

.. _`gmap_alloc`:

gmap_alloc
==========

.. c:function:: struct gmap *gmap_alloc(unsigned long limit)

    allocate and initialize a guest address space

    :param unsigned long limit:
        maximum address of the gmap address space

.. _`gmap_alloc.description`:

Description
-----------

Returns a guest address space structure.

.. _`gmap_create`:

gmap_create
===========

.. c:function:: struct gmap *gmap_create(struct mm_struct *mm, unsigned long limit)

    create a guest address space

    :param struct mm_struct \*mm:
        pointer to the parent mm_struct

    :param unsigned long limit:
        maximum size of the gmap address space

.. _`gmap_create.description`:

Description
-----------

Returns a guest address space structure.

.. _`gmap_free`:

gmap_free
=========

.. c:function:: void gmap_free(struct gmap *gmap)

    free a guest address space

    :param struct gmap \*gmap:
        pointer to the guest address space structure

.. _`gmap_free.description`:

Description
-----------

No locks required. There are no references to this gmap anymore.

.. _`gmap_get`:

gmap_get
========

.. c:function:: struct gmap *gmap_get(struct gmap *gmap)

    increase reference counter for guest address space

    :param struct gmap \*gmap:
        pointer to the guest address space structure

.. _`gmap_get.description`:

Description
-----------

Returns the gmap pointer

.. _`gmap_put`:

gmap_put
========

.. c:function:: void gmap_put(struct gmap *gmap)

    decrease reference counter for guest address space

    :param struct gmap \*gmap:
        pointer to the guest address space structure

.. _`gmap_put.description`:

Description
-----------

If the reference counter reaches zero the guest address space is freed.

.. _`gmap_remove`:

gmap_remove
===========

.. c:function:: void gmap_remove(struct gmap *gmap)

    remove a guest address space but do not free it yet

    :param struct gmap \*gmap:
        pointer to the guest address space structure

.. _`gmap_enable`:

gmap_enable
===========

.. c:function:: void gmap_enable(struct gmap *gmap)

    switch primary space to the guest address space

    :param struct gmap \*gmap:
        pointer to the guest address space structure

.. _`gmap_disable`:

gmap_disable
============

.. c:function:: void gmap_disable(struct gmap *gmap)

    switch back to the standard primary address space

    :param struct gmap \*gmap:
        pointer to the guest address space structure

.. _`gmap_get_enabled`:

gmap_get_enabled
================

.. c:function:: struct gmap *gmap_get_enabled( void)

    get a pointer to the currently enabled gmap

    :param  void:
        no arguments

.. _`gmap_get_enabled.description`:

Description
-----------

Returns a pointer to the currently enabled gmap. 0 if none is enabled.

.. _`__gmap_segment_gaddr`:

__gmap_segment_gaddr
====================

.. c:function:: unsigned long __gmap_segment_gaddr(unsigned long *entry)

    find virtual address from segment pointer

    :param unsigned long \*entry:
        pointer to a segment table entry in the guest address space

.. _`__gmap_segment_gaddr.description`:

Description
-----------

Returns the virtual address in the guest address space for the segment

.. _`__gmap_unlink_by_vmaddr`:

__gmap_unlink_by_vmaddr
=======================

.. c:function:: int __gmap_unlink_by_vmaddr(struct gmap *gmap, unsigned long vmaddr)

    unlink a single segment via a host address

    :param struct gmap \*gmap:
        pointer to the guest address space structure

    :param unsigned long vmaddr:
        address in the host process address space

.. _`__gmap_unlink_by_vmaddr.description`:

Description
-----------

Returns 1 if a TLB flush is required

.. _`__gmap_unmap_by_gaddr`:

__gmap_unmap_by_gaddr
=====================

.. c:function:: int __gmap_unmap_by_gaddr(struct gmap *gmap, unsigned long gaddr)

    unmap a single segment via a guest address

    :param struct gmap \*gmap:
        pointer to the guest address space structure

    :param unsigned long gaddr:
        address in the guest address space

.. _`__gmap_unmap_by_gaddr.description`:

Description
-----------

Returns 1 if a TLB flush is required

.. _`gmap_unmap_segment`:

gmap_unmap_segment
==================

.. c:function:: int gmap_unmap_segment(struct gmap *gmap, unsigned long to, unsigned long len)

    unmap segment from the guest address space

    :param struct gmap \*gmap:
        pointer to the guest address space structure

    :param unsigned long to:
        address in the guest address space

    :param unsigned long len:
        length of the memory area to unmap

.. _`gmap_unmap_segment.description`:

Description
-----------

Returns 0 if the unmap succeeded, -EINVAL if not.

.. _`gmap_map_segment`:

gmap_map_segment
================

.. c:function:: int gmap_map_segment(struct gmap *gmap, unsigned long from, unsigned long to, unsigned long len)

    map a segment to the guest address space

    :param struct gmap \*gmap:
        pointer to the guest address space structure

    :param unsigned long from:
        source address in the parent address space

    :param unsigned long to:
        target address in the guest address space

    :param unsigned long len:
        length of the memory area to map

.. _`gmap_map_segment.description`:

Description
-----------

Returns 0 if the mmap succeeded, -EINVAL or -ENOMEM if not.

.. _`__gmap_translate`:

__gmap_translate
================

.. c:function:: unsigned long __gmap_translate(struct gmap *gmap, unsigned long gaddr)

    translate a guest address to a user space address

    :param struct gmap \*gmap:
        pointer to guest mapping meta data structure

    :param unsigned long gaddr:
        guest address

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

    :param struct gmap \*gmap:
        pointer to guest mapping meta data structure

    :param unsigned long gaddr:
        guest address

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

    :param struct mm_struct \*mm:
        *undescribed*

    :param unsigned long \*table:
        pointer to the host page table

    :param unsigned long vmaddr:
        vm address associated with the host page table

.. _`__gmap_link`:

__gmap_link
===========

.. c:function:: int __gmap_link(struct gmap *gmap, unsigned long gaddr, unsigned long vmaddr)

    set up shadow page tables to connect a host to a guest address

    :param struct gmap \*gmap:
        pointer to guest mapping meta data structure

    :param unsigned long gaddr:
        guest address

    :param unsigned long vmaddr:
        vm address

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

    :param struct gmap \*gmap:
        pointer to guest mapping meta data structure

    :param unsigned long gaddr:
        guest address

    :param unsigned int fault_flags:
        flags to pass down to \ :c:func:`handle_mm_fault`\ 

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

    :param struct gmap_notifier \*nb:
        pointer to the gmap notifier block

.. _`gmap_unregister_pte_notifier`:

gmap_unregister_pte_notifier
============================

.. c:function:: void gmap_unregister_pte_notifier(struct gmap_notifier *nb)

    remove a pte invalidation callback

    :param struct gmap_notifier \*nb:
        pointer to the gmap notifier block

.. _`gmap_call_notifier`:

gmap_call_notifier
==================

.. c:function:: void gmap_call_notifier(struct gmap *gmap, unsigned long start, unsigned long end)

    call all registered invalidation callbacks

    :param struct gmap \*gmap:
        pointer to guest mapping meta data structure

    :param unsigned long start:
        start virtual address in the guest address space

    :param unsigned long end:
        end virtual address in the guest address space

.. _`gmap_table_walk`:

gmap_table_walk
===============

.. c:function:: unsigned long *gmap_table_walk(struct gmap *gmap, unsigned long gaddr, int level)

    walk the gmap page tables

    :param struct gmap \*gmap:
        pointer to guest mapping meta data structure

    :param unsigned long gaddr:
        virtual address in the guest address space

    :param int level:
        returns a pointer to a region-1 table entry (or NULL)

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

    :param struct gmap \*gmap:
        pointer to guest mapping meta data structure

    :param unsigned long gaddr:
        virtual address in the guest address space

    :param spinlock_t \*\*ptl:
        pointer to the spinlock pointer

.. _`gmap_pte_op_walk.description`:

Description
-----------

Returns a pointer to the locked pte for a guest address, or NULL

.. _`gmap_pte_op_walk.note`:

Note
----

Can also be called for shadow gmaps.

.. _`gmap_pte_op_fixup`:

gmap_pte_op_fixup
=================

.. c:function:: int gmap_pte_op_fixup(struct gmap *gmap, unsigned long gaddr, unsigned long vmaddr, int prot)

    force a page in and connect the gmap page table

    :param struct gmap \*gmap:
        pointer to guest mapping meta data structure

    :param unsigned long gaddr:
        virtual address in the guest address space

    :param unsigned long vmaddr:
        address in the host process address space

    :param int prot:
        indicates access rights: PROT_NONE, PROT_READ or PROT_WRITE

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

    :param spinlock_t \*ptl:
        pointer to the spinlock pointer

.. _`gmap_mprotect_notify`:

gmap_mprotect_notify
====================

.. c:function:: int gmap_mprotect_notify(struct gmap *gmap, unsigned long gaddr, unsigned long len, int prot)

    change access rights for a range of ptes and call the notifier if any pte changes again

    :param struct gmap \*gmap:
        pointer to guest mapping meta data structure

    :param unsigned long gaddr:
        virtual address in the guest address space

    :param unsigned long len:
        size of area

    :param int prot:
        indicates access rights: PROT_NONE, PROT_READ or PROT_WRITE

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

    :param struct gmap \*gmap:
        pointer to guest mapping meta data structure

    :param unsigned long gaddr:
        virtual address in the guest address space

    :param unsigned long \*val:
        pointer to the unsigned long value to return

.. _`gmap_read_table.description`:

Description
-----------

Returns 0 if the value was read, -ENOMEM if out of memory and -EFAULT
if reading using the virtual address failed.

Called with gmap->mm->mmap_sem in read.

.. _`gmap_insert_rmap`:

gmap_insert_rmap
================

.. c:function:: void gmap_insert_rmap(struct gmap *sg, unsigned long vmaddr, struct gmap_rmap *rmap)

    add a rmap to the host_to_rmap radix tree

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long vmaddr:
        vm address associated with the rmap

    :param struct gmap_rmap \*rmap:
        pointer to the rmap structure

.. _`gmap_insert_rmap.description`:

Description
-----------

Called with the sg->guest_table_lock

.. _`gmap_protect_rmap`:

gmap_protect_rmap
=================

.. c:function:: int gmap_protect_rmap(struct gmap *sg, unsigned long raddr, unsigned long paddr, unsigned long len, int prot)

    modify access rights to memory and create an rmap

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long raddr:
        rmap address in the shadow gmap

    :param unsigned long paddr:
        address in the parent guest address space

    :param unsigned long len:
        length of the memory area to protect

    :param int prot:
        indicates access rights: none, read-only or read-write

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

    :param unsigned long asce:
        region or segment table \*origin\* + table-type bits

    :param unsigned long vaddr:
        virtual address to identify the table entry to flush

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

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long raddr:
        rmap address in the shadow guest address space

.. _`gmap_unshadow_page.description`:

Description
-----------

Called with the sg->guest_table_lock

.. _`__gmap_unshadow_pgt`:

__gmap_unshadow_pgt
===================

.. c:function:: void __gmap_unshadow_pgt(struct gmap *sg, unsigned long raddr, unsigned long *pgt)

    remove all entries from a shadow page table

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long raddr:
        rmap address in the shadow guest address space

    :param unsigned long \*pgt:
        pointer to the start of a shadow page table

.. _`__gmap_unshadow_pgt.description`:

Description
-----------

Called with the sg->guest_table_lock

.. _`gmap_unshadow_pgt`:

gmap_unshadow_pgt
=================

.. c:function:: void gmap_unshadow_pgt(struct gmap *sg, unsigned long raddr)

    remove a shadow page table from a segment entry

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long raddr:
        address in the shadow guest address space

.. _`gmap_unshadow_pgt.description`:

Description
-----------

Called with the sg->guest_table_lock

.. _`__gmap_unshadow_sgt`:

__gmap_unshadow_sgt
===================

.. c:function:: void __gmap_unshadow_sgt(struct gmap *sg, unsigned long raddr, unsigned long *sgt)

    remove all entries from a shadow segment table

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long raddr:
        rmap address in the shadow guest address space

    :param unsigned long \*sgt:
        pointer to the start of a shadow segment table

.. _`__gmap_unshadow_sgt.description`:

Description
-----------

Called with the sg->guest_table_lock

.. _`gmap_unshadow_sgt`:

gmap_unshadow_sgt
=================

.. c:function:: void gmap_unshadow_sgt(struct gmap *sg, unsigned long raddr)

    remove a shadow segment table from a region-3 entry

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long raddr:
        rmap address in the shadow guest address space

.. _`gmap_unshadow_sgt.description`:

Description
-----------

Called with the shadow->guest_table_lock

.. _`__gmap_unshadow_r3t`:

__gmap_unshadow_r3t
===================

.. c:function:: void __gmap_unshadow_r3t(struct gmap *sg, unsigned long raddr, unsigned long *r3t)

    remove all entries from a shadow region-3 table

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long raddr:
        address in the shadow guest address space

    :param unsigned long \*r3t:
        pointer to the start of a shadow region-3 table

.. _`__gmap_unshadow_r3t.description`:

Description
-----------

Called with the sg->guest_table_lock

.. _`gmap_unshadow_r3t`:

gmap_unshadow_r3t
=================

.. c:function:: void gmap_unshadow_r3t(struct gmap *sg, unsigned long raddr)

    remove a shadow region-3 table from a region-2 entry

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long raddr:
        rmap address in the shadow guest address space

.. _`gmap_unshadow_r3t.description`:

Description
-----------

Called with the sg->guest_table_lock

.. _`__gmap_unshadow_r2t`:

__gmap_unshadow_r2t
===================

.. c:function:: void __gmap_unshadow_r2t(struct gmap *sg, unsigned long raddr, unsigned long *r2t)

    remove all entries from a shadow region-2 table

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long raddr:
        rmap address in the shadow guest address space

    :param unsigned long \*r2t:
        pointer to the start of a shadow region-2 table

.. _`__gmap_unshadow_r2t.description`:

Description
-----------

Called with the sg->guest_table_lock

.. _`gmap_unshadow_r2t`:

gmap_unshadow_r2t
=================

.. c:function:: void gmap_unshadow_r2t(struct gmap *sg, unsigned long raddr)

    remove a shadow region-2 table from a region-1 entry

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long raddr:
        rmap address in the shadow guest address space

.. _`gmap_unshadow_r2t.description`:

Description
-----------

Called with the sg->guest_table_lock

.. _`__gmap_unshadow_r1t`:

__gmap_unshadow_r1t
===================

.. c:function:: void __gmap_unshadow_r1t(struct gmap *sg, unsigned long raddr, unsigned long *r1t)

    remove all entries from a shadow region-1 table

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long raddr:
        rmap address in the shadow guest address space

    :param unsigned long \*r1t:
        pointer to the start of a shadow region-1 table

.. _`__gmap_unshadow_r1t.description`:

Description
-----------

Called with the shadow->guest_table_lock

.. _`gmap_unshadow`:

gmap_unshadow
=============

.. c:function:: void gmap_unshadow(struct gmap *sg)

    remove a shadow page table completely

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

.. _`gmap_unshadow.description`:

Description
-----------

Called with sg->guest_table_lock

.. _`gmap_find_shadow`:

gmap_find_shadow
================

.. c:function:: struct gmap *gmap_find_shadow(struct gmap *parent, unsigned long asce, int edat_level)

    find a specific asce in the list of shadow tables

    :param struct gmap \*parent:
        pointer to the parent gmap

    :param unsigned long asce:
        ASCE for which the shadow table is created

    :param int edat_level:
        edat level to be used for the shadow translation

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

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long asce:
        ASCE for which the shadow table is requested

    :param int edat_level:
        edat level to be used for the shadow translation

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

    :param struct gmap \*parent:
        pointer to the parent gmap

    :param unsigned long asce:
        ASCE for which the shadow table is created

    :param int edat_level:
        edat level to be used for the shadow translation

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

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long saddr:
        faulting address in the shadow gmap

    :param unsigned long r2t:
        parent gmap address of the region 2 table to get shadowed

    :param int fake:
        r2t references contiguous guest memory block, not a r2t

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

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long saddr:
        faulting address in the shadow gmap

    :param unsigned long r3t:
        parent gmap address of the region 3 table to get shadowed

    :param int fake:
        r3t references contiguous guest memory block, not a r3t

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

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long saddr:
        faulting address in the shadow gmap

    :param unsigned long sgt:
        parent gmap address of the segment table to get shadowed

    :param int fake:
        sgt references contiguous guest memory block, not a sgt

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

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long saddr:
        the address in the shadow aguest address space

    :param unsigned long \*pgt:
        parent gmap address of the page table to get shadowed

    :param int \*dat_protection:
        if the pgtable is marked as protected by dat

    :param int \*fake:
        pgt references contiguous guest memory block, not a pgtable

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

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long saddr:
        faulting address in the shadow gmap

    :param unsigned long pgt:
        parent gmap address of the page table to get shadowed

    :param int fake:
        pgt references contiguous guest memory block, not a pgtable

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

    :param struct gmap \*sg:
        pointer to the shadow guest address space structure

    :param unsigned long saddr:
        faulting address in the shadow gmap

    :param pte_t pte:
        pte in parent gmap address space to get shadowed

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

.. c:function:: void gmap_shadow_notify(struct gmap *sg, unsigned long vmaddr, unsigned long gaddr, pte_t *pte)

    handle notifications for shadow gmap

    :param struct gmap \*sg:
        *undescribed*

    :param unsigned long vmaddr:
        *undescribed*

    :param unsigned long gaddr:
        *undescribed*

    :param pte_t \*pte:
        *undescribed*

.. _`gmap_shadow_notify.description`:

Description
-----------

Called with sg->parent->shadow_lock.

.. _`ptep_notify`:

ptep_notify
===========

.. c:function:: void ptep_notify(struct mm_struct *mm, unsigned long vmaddr, pte_t *pte, unsigned long bits)

    call all invalidation callbacks for a specific pte.

    :param struct mm_struct \*mm:
        pointer to the process mm_struct

    :param unsigned long vmaddr:
        *undescribed*

    :param pte_t \*pte:
        pointer to the page table entry

    :param unsigned long bits:
        bits from the pgste that caused the notify call

.. _`ptep_notify.description`:

Description
-----------

This function is assumed to be called with the page table lock held
for the pte to notify.

.. This file was automatic generated / don't edit.

