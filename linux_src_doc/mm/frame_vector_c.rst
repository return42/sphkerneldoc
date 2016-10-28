.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/frame_vector.c

.. _`get_vaddr_frames`:

get_vaddr_frames
================

.. c:function:: int get_vaddr_frames(unsigned long start, unsigned int nr_frames, bool write, bool force, struct frame_vector *vec)

    map virtual addresses to pfns

    :param unsigned long start:
        starting user address

    :param unsigned int nr_frames:
        number of pages / pfns from start to map

    :param bool write:
        whether pages will be written to by the caller

    :param bool force:
        whether to force write access even if user mapping is
        readonly. See description of the same argument of

    :param struct frame_vector \*vec:
        structure which receives pages / pfns of the addresses mapped.
        It should have space for at least nr_frames entries.

.. _`get_vaddr_frames.description`:

Description
-----------

This function maps virtual addresses from \ ``start``\  and fills \ ``vec``\  structure
with page frame numbers or page pointers to corresponding pages (choice
depends on the type of the vma underlying the virtual address). If \ ``start``\ 
belongs to a normal vma, the function grabs reference to each of the pages
to pin them in memory. If \ ``start``\  belongs to VM_IO \| VM_PFNMAP vma, we don't
touch page structures and the caller must make sure pfns aren't reused for
anything else while he is using them.

The function returns number of pages mapped which may be less than
\ ``nr_frames``\ . In particular we stop mapping if there are more vmas of
different type underlying the specified range of virtual addresses.
When the function isn't able to map a single page, it returns error.

This function takes care of grabbing mmap_sem as necessary.

.. _`put_vaddr_frames`:

put_vaddr_frames
================

.. c:function:: void put_vaddr_frames(struct frame_vector *vec)

    drop references to pages if \ :c:func:`get_vaddr_frames`\  acquired them

    :param struct frame_vector \*vec:
        frame vector to put

.. _`put_vaddr_frames.description`:

Description
-----------

Drop references to pages if \ :c:func:`get_vaddr_frames`\  acquired them. We also
invalidate the frame vector so that it is prepared for the next call into
\ :c:func:`get_vaddr_frames`\ .

.. _`frame_vector_to_pages`:

frame_vector_to_pages
=====================

.. c:function:: int frame_vector_to_pages(struct frame_vector *vec)

    convert frame vector to contain page pointers

    :param struct frame_vector \*vec:
        frame vector to convert

.. _`frame_vector_to_pages.description`:

Description
-----------

Convert \ ``vec``\  to contain array of page pointers.  If the conversion is
successful, return 0. Otherwise return an error. Note that we do not grab
page references for the page structures.

.. _`frame_vector_to_pfns`:

frame_vector_to_pfns
====================

.. c:function:: void frame_vector_to_pfns(struct frame_vector *vec)

    convert frame vector to contain pfns

    :param struct frame_vector \*vec:
        frame vector to convert

.. _`frame_vector_to_pfns.description`:

Description
-----------

Convert \ ``vec``\  to contain array of pfns.

.. _`frame_vector_create`:

frame_vector_create
===================

.. c:function:: struct frame_vector *frame_vector_create(unsigned int nr_frames)

    allocate & initialize structure for pinned pfns

    :param unsigned int nr_frames:
        number of pfns slots we should reserve

.. _`frame_vector_create.description`:

Description
-----------

Allocate and initialize struct pinned_pfns to be able to hold \ ``nr_pfns``\ 
pfns.

.. _`frame_vector_destroy`:

frame_vector_destroy
====================

.. c:function:: void frame_vector_destroy(struct frame_vector *vec)

    free memory allocated to carry frame vector

    :param struct frame_vector \*vec:
        Frame vector to free

.. _`frame_vector_destroy.description`:

Description
-----------

Free structure allocated by \ :c:func:`frame_vector_create`\  to carry frames.

.. This file was automatic generated / don't edit.

