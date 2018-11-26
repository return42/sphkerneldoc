.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/common/videobuf2/videobuf2-memops.c

.. _`vb2_create_framevec`:

vb2_create_framevec
===================

.. c:function:: struct frame_vector *vb2_create_framevec(unsigned long start, unsigned long length, bool write)

    map virtual addresses to pfns

    :param start:
        Virtual user address where we start mapping
    :type start: unsigned long

    :param length:
        Length of a range to map
    :type length: unsigned long

    :param write:
        Should we map for writing into the area
    :type write: bool

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

    :param vec:
        vector of pfns / pages to release
    :type vec: struct frame_vector \*

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

    :param vma:
        virtual memory region for the mapping
    :type vma: struct vm_area_struct \*

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

    :param vma:
        virtual memory region for the mapping
    :type vma: struct vm_area_struct \*

.. _`vb2_common_vm_close.description`:

Description
-----------

This function releases the user from the provided vma. It expects
struct vb2_vmarea_handler pointer in vma->vm_private_data.

.. This file was automatic generated / don't edit.

