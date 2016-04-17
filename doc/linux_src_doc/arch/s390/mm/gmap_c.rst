.. -*- coding: utf-8; mode: rst -*-

======
gmap.c
======


.. _`gmap_alloc`:

gmap_alloc
==========

.. c:function:: struct gmap *gmap_alloc (struct mm_struct *mm, unsigned long limit)

    allocate a guest address space

    :param struct mm_struct \*mm:
        pointer to the parent mm_struct

    :param unsigned long limit:
        maximum address of the gmap address space



.. _`gmap_alloc.description`:

Description
-----------

Returns a guest address space structure.



.. _`gmap_free`:

gmap_free
=========

.. c:function:: void gmap_free (struct gmap *gmap)

    free a guest address space

    :param struct gmap \*gmap:
        pointer to the guest address space structure



.. _`gmap_enable`:

gmap_enable
===========

.. c:function:: void gmap_enable (struct gmap *gmap)

    switch primary space to the guest address space

    :param struct gmap \*gmap:
        pointer to the guest address space structure



.. _`gmap_disable`:

gmap_disable
============

.. c:function:: void gmap_disable (struct gmap *gmap)

    switch back to the standard primary address space

    :param struct gmap \*gmap:
        pointer to the guest address space structure



.. _`__gmap_segment_gaddr`:

__gmap_segment_gaddr
====================

.. c:function:: unsigned long __gmap_segment_gaddr (unsigned long *entry)

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

.. c:function:: int __gmap_unlink_by_vmaddr (struct gmap *gmap, unsigned long vmaddr)

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

.. c:function:: int __gmap_unmap_by_gaddr (struct gmap *gmap, unsigned long gaddr)

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

.. c:function:: int gmap_unmap_segment (struct gmap *gmap, unsigned long to, unsigned long len)

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

.. c:function:: int gmap_map_segment (struct gmap *gmap, unsigned long from, unsigned long to, unsigned long len)

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

.. c:function:: unsigned long __gmap_translate (struct gmap *gmap, unsigned long gaddr)

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



.. _`gmap_translate`:

gmap_translate
==============

.. c:function:: unsigned long gmap_translate (struct gmap *gmap, unsigned long gaddr)

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

.. c:function:: void gmap_unlink (struct mm_struct *mm, unsigned long *table, unsigned long vmaddr)

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

.. c:function:: int __gmap_link (struct gmap *gmap, unsigned long gaddr, unsigned long vmaddr)

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

.. c:function:: int gmap_fault (struct gmap *gmap, unsigned long gaddr, unsigned int fault_flags)

    resolve a fault on a guest address

    :param struct gmap \*gmap:
        pointer to guest mapping meta data structure

    :param unsigned long gaddr:
        guest address

    :param unsigned int fault_flags:
        flags to pass down to :c:func:`handle_mm_fault`



.. _`gmap_fault.description`:

Description
-----------

Returns 0 on success, -ENOMEM for out of memory conditions, and -EFAULT
if the vm address is already mapped to a different guest segment.



.. _`gmap_register_ipte_notifier`:

gmap_register_ipte_notifier
===========================

.. c:function:: void gmap_register_ipte_notifier (struct gmap_notifier *nb)

    register a pte invalidation callback

    :param struct gmap_notifier \*nb:
        pointer to the gmap notifier block



.. _`gmap_unregister_ipte_notifier`:

gmap_unregister_ipte_notifier
=============================

.. c:function:: void gmap_unregister_ipte_notifier (struct gmap_notifier *nb)

    remove a pte invalidation callback

    :param struct gmap_notifier \*nb:
        pointer to the gmap notifier block



.. _`gmap_ipte_notify`:

gmap_ipte_notify
================

.. c:function:: int gmap_ipte_notify (struct gmap *gmap, unsigned long gaddr, unsigned long len)

    mark a range of ptes for invalidation notification

    :param struct gmap \*gmap:
        pointer to guest mapping meta data structure

    :param unsigned long gaddr:
        virtual address in the guest address space

    :param unsigned long len:
        size of area



.. _`gmap_ipte_notify.description`:

Description
-----------

Returns 0 if for each page in the given range a gmap mapping exists and
the invalidation notification could be set. If the gmap mapping is missing
for one or more pages -EFAULT is returned. If no memory could be allocated
-ENOMEM is returned. This function establishes missing page table entries.



.. _`ptep_notify`:

ptep_notify
===========

.. c:function:: void ptep_notify (struct mm_struct *mm, unsigned long vmaddr, pte_t *pte)

    call all invalidation callbacks for a specific pte.

    :param struct mm_struct \*mm:
        pointer to the process mm_struct

    :param unsigned long vmaddr:

        *undescribed*

    :param pte_t \*pte:
        pointer to the page table entry



.. _`ptep_notify.description`:

Description
-----------

This function is assumed to be called with the page table lock held
for the pte to notify.

