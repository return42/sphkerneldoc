.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/v4l2-core/videobuf2-memops.c

.. _`vb2_create_framevec`:

vb2_create_framevec
===================

.. c:function:: struct frame_vector *vb2_create_framevec(unsigned long start, unsigned long length, bool write)

    map virtual addresses to pfns

    :param unsigned long start:
        Virtual user address where we start mapping

    :param unsigned long length:
        Length of a range to map

    :param bool write:
        Should we map for writing into the area

.. _`vb2_create_framevec.description`:

Description
-----------

This function allocates and fills in a vector with pfns corresponding to
virtual address range passed in arguments. If pfns have corresponding pages,
page references are also grabbed to pin pages in memory. The function
returns pointer to the vector on success and error pointer in case of
failure. Returned vector needs to be freed via \ :c:func:`vb2_destroy_pfnvec`\ .

.. _`vb2_destroy_framevec`:

vb2_destroy_framevec
====================

.. c:function:: void vb2_destroy_framevec(struct frame_vector *vec)

    release vector of mapped pfns

    :param struct frame_vector \*vec:
        vector of pfns / pages to release

.. _`vb2_destroy_framevec.description`:

Description
-----------

This releases references to all pages in the vector \ ``vec``\  (if corresponding
pfns are backed by pages) and frees the passed vector.

.. _`vb2_common_vm_open`:

vb2_common_vm_open
==================

.. c:function:: void vb2_common_vm_open(struct vm_area_struct *vma)

    increase refcount of the vma

    :param struct vm_area_struct \*vma:
        virtual memory region for the mapping

.. _`vb2_common_vm_open.description`:

Description
-----------

This function adds another user to the provided vma. It expects
struct vb2_vmarea_handler pointer in vma->vm_private_data.

.. _`vb2_common_vm_close`:

vb2_common_vm_close
===================

.. c:function:: void vb2_common_vm_close(struct vm_area_struct *vma)

    decrease refcount of the vma

    :param struct vm_area_struct \*vma:
        virtual memory region for the mapping

.. _`vb2_common_vm_close.description`:

Description
-----------

This function releases the user from the provided vma. It expects
struct vb2_vmarea_handler pointer in vma->vm_private_data.

.. This file was automatic generated / don't edit.

