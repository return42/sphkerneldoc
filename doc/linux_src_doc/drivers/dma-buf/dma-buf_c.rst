.. -*- coding: utf-8; mode: rst -*-

=========
dma-buf.c
=========

.. _`dma_buf_export`:

dma_buf_export
==============

.. c:function:: struct dma_buf *dma_buf_export (const struct dma_buf_export_info *exp_info)

    Creates a new dma_buf, and associates an anon file with this buffer, so it can be exported. Also connect the allocator specific data and ops to the buffer. Additionally, provide a name string for exporter; useful in debugging.

    :param const struct dma_buf_export_info \*exp_info:
        [in]        holds all the export related information provided
        by the exporter. see struct dma_buf_export_info
        for further details.


.. _`dma_buf_export.description`:

Description
-----------

Returns, on success, a newly created dma_buf object, which wraps the
supplied private data and operations for dma_buf_ops. On either missing
ops, or error in allocating struct dma_buf, will return negative error.


.. _`dma_buf_fd`:

dma_buf_fd
==========

.. c:function:: int dma_buf_fd (struct dma_buf *dmabuf, int flags)

    returns a file descriptor for the given dma_buf

    :param struct dma_buf \*dmabuf:
        [in]        pointer to dma_buf for which fd is required.

    :param int flags:
        [in]    flags to give to fd


.. _`dma_buf_fd.description`:

Description
-----------

On success, returns an associated 'fd'. Else, returns error.


.. _`dma_buf_get`:

dma_buf_get
===========

.. c:function:: struct dma_buf *dma_buf_get (int fd)

    returns the dma_buf structure related to an fd

    :param int fd:
        [in]        fd associated with the dma_buf to be returned


.. _`dma_buf_get.description`:

Description
-----------

On success, returns the dma_buf structure associated with an fd; uses
file's refcounting done by fget to increase refcount. returns ERR_PTR
otherwise.


.. _`dma_buf_put`:

dma_buf_put
===========

.. c:function:: void dma_buf_put (struct dma_buf *dmabuf)

    decreases refcount of the buffer

    :param struct dma_buf \*dmabuf:
        [in]        buffer to reduce refcount of


.. _`dma_buf_put.description`:

Description
-----------

Uses file's refcounting done implicitly by :c:func:`fput`


.. _`dma_buf_attach`:

dma_buf_attach
==============

.. c:function:: struct dma_buf_attachment *dma_buf_attach (struct dma_buf *dmabuf, struct device *dev)

    Add the device to dma_buf's attachments list; optionally, calls attach() of dma_buf_ops to allow device-specific attach functionality

    :param struct dma_buf \*dmabuf:
        [in]        buffer to attach device to.

    :param struct device \*dev:
        [in]        device to be attached.


.. _`dma_buf_attach.description`:

Description
-----------

Returns struct dma_buf_attachment * for this attachment; returns ERR_PTR on
error.


.. _`dma_buf_detach`:

dma_buf_detach
==============

.. c:function:: void dma_buf_detach (struct dma_buf *dmabuf, struct dma_buf_attachment *attach)

    Remove the given attachment from dmabuf's attachments list; optionally calls detach() of dma_buf_ops for device-specific detach

    :param struct dma_buf \*dmabuf:
        [in]        buffer to detach from.

    :param struct dma_buf_attachment \*attach:
        [in]        attachment to be detached; is free'd after this call.


.. _`dma_buf_map_attachment`:

dma_buf_map_attachment
======================

.. c:function:: struct sg_table *dma_buf_map_attachment (struct dma_buf_attachment *attach, enum dma_data_direction direction)

    Returns the scatterlist table of the attachment; mapped into _device_ address space. Is a wrapper for map_dma_buf() of the dma_buf_ops.

    :param struct dma_buf_attachment \*attach:
        [in]        attachment whose scatterlist is to be returned

    :param enum dma_data_direction direction:
        [in]        direction of DMA transfer


.. _`dma_buf_map_attachment.description`:

Description
-----------

Returns sg_table containing the scatterlist to be returned; returns ERR_PTR
on error.


.. _`dma_buf_unmap_attachment`:

dma_buf_unmap_attachment
========================

.. c:function:: void dma_buf_unmap_attachment (struct dma_buf_attachment *attach, struct sg_table *sg_table, enum dma_data_direction direction)

    unmaps and decreases usecount of the buffer;might deallocate the scatterlist associated. Is a wrapper for unmap_dma_buf() of dma_buf_ops.

    :param struct dma_buf_attachment \*attach:
        [in]        attachment to unmap buffer from

    :param struct sg_table \*sg_table:
        [in]        scatterlist info of the buffer to unmap

    :param enum dma_data_direction direction:
        [in]    direction of DMA transfer


.. _`dma_buf_begin_cpu_access`:

dma_buf_begin_cpu_access
========================

.. c:function:: int dma_buf_begin_cpu_access (struct dma_buf *dmabuf, enum dma_data_direction direction)

    Must be called before accessing a dma_buf from the cpu in the kernel context. Calls begin_cpu_access to allow exporter-specific preparations. Coherency is only guaranteed in the specified range for the specified access direction.

    :param struct dma_buf \*dmabuf:
        [in]        buffer to prepare cpu access for.

    :param enum dma_data_direction direction:
        [in]        length of range for cpu access.


.. _`dma_buf_begin_cpu_access.description`:

Description
-----------

Can return negative error values, returns 0 on success.


.. _`dma_buf_end_cpu_access`:

dma_buf_end_cpu_access
======================

.. c:function:: int dma_buf_end_cpu_access (struct dma_buf *dmabuf, enum dma_data_direction direction)

    Must be called after accessing a dma_buf from the cpu in the kernel context. Calls end_cpu_access to allow exporter-specific actions. Coherency is only guaranteed in the specified range for the specified access direction.

    :param struct dma_buf \*dmabuf:
        [in]        buffer to complete cpu access for.

    :param enum dma_data_direction direction:
        [in]        length of range for cpu access.


.. _`dma_buf_end_cpu_access.description`:

Description
-----------

Can return negative error values, returns 0 on success.


.. _`dma_buf_kmap_atomic`:

dma_buf_kmap_atomic
===================

.. c:function:: void *dma_buf_kmap_atomic (struct dma_buf *dmabuf, unsigned long page_num)

    Map a page of the buffer object into kernel address space. The same restrictions as for kmap_atomic and friends apply.

    :param struct dma_buf \*dmabuf:
        [in]        buffer to map page from.

    :param unsigned long page_num:
        [in]        page in PAGE_SIZE units to map.


.. _`dma_buf_kmap_atomic.description`:

Description
-----------

This call must always succeed, any necessary preparations that might fail
need to be done in begin_cpu_access.


.. _`dma_buf_kunmap_atomic`:

dma_buf_kunmap_atomic
=====================

.. c:function:: void dma_buf_kunmap_atomic (struct dma_buf *dmabuf, unsigned long page_num, void *vaddr)

    Unmap a page obtained by dma_buf_kmap_atomic.

    :param struct dma_buf \*dmabuf:
        [in]        buffer to unmap page from.

    :param unsigned long page_num:
        [in]        page in PAGE_SIZE units to unmap.

    :param void \*vaddr:
        [in]        kernel space pointer obtained from dma_buf_kmap_atomic.


.. _`dma_buf_kunmap_atomic.description`:

Description
-----------

This call must always succeed.


.. _`dma_buf_kmap`:

dma_buf_kmap
============

.. c:function:: void *dma_buf_kmap (struct dma_buf *dmabuf, unsigned long page_num)

    Map a page of the buffer object into kernel address space. The same restrictions as for kmap and friends apply.

    :param struct dma_buf \*dmabuf:
        [in]        buffer to map page from.

    :param unsigned long page_num:
        [in]        page in PAGE_SIZE units to map.


.. _`dma_buf_kmap.description`:

Description
-----------

This call must always succeed, any necessary preparations that might fail
need to be done in begin_cpu_access.


.. _`dma_buf_kunmap`:

dma_buf_kunmap
==============

.. c:function:: void dma_buf_kunmap (struct dma_buf *dmabuf, unsigned long page_num, void *vaddr)

    Unmap a page obtained by dma_buf_kmap.

    :param struct dma_buf \*dmabuf:
        [in]        buffer to unmap page from.

    :param unsigned long page_num:
        [in]        page in PAGE_SIZE units to unmap.

    :param void \*vaddr:
        [in]        kernel space pointer obtained from dma_buf_kmap.


.. _`dma_buf_kunmap.description`:

Description
-----------

This call must always succeed.


.. _`dma_buf_mmap`:

dma_buf_mmap
============

.. c:function:: int dma_buf_mmap (struct dma_buf *dmabuf, struct vm_area_struct *vma, unsigned long pgoff)

    Setup up a userspace mmap with the given vma

    :param struct dma_buf \*dmabuf:
        [in]        buffer that should back the vma

    :param struct vm_area_struct \*vma:
        [in]        vma for the mmap

    :param unsigned long pgoff:
        [in]        offset in pages where this mmap should start within the
        dma-buf buffer.


.. _`dma_buf_mmap.description`:

Description
-----------

This function adjusts the passed in vma so that it points at the file of the
dma_buf operation. It also adjusts the starting pgoff and does bounds
checking on the size of the vma. Then it calls the exporters mmap function to
set up the mapping.

Can return negative error values, returns 0 on success.


.. _`dma_buf_vmap`:

dma_buf_vmap
============

.. c:function:: void *dma_buf_vmap (struct dma_buf *dmabuf)

    Create virtual mapping for the buffer object into kernel address space. Same restrictions as for vmap and friends apply.

    :param struct dma_buf \*dmabuf:
        [in]        buffer to vmap


.. _`dma_buf_vmap.description`:

Description
-----------

This call may fail due to lack of virtual mapping address space.
These calls are optional in drivers. The intended use for them
is for mapping objects linear in kernel space for high use objects.
Please attempt to use kmap/kunmap before thinking about these interfaces.

Returns NULL on error.


.. _`dma_buf_vunmap`:

dma_buf_vunmap
==============

.. c:function:: void dma_buf_vunmap (struct dma_buf *dmabuf, void *vaddr)

    Unmap a vmap obtained by dma_buf_vmap.

    :param struct dma_buf \*dmabuf:
        [in]        buffer to vunmap

    :param void \*vaddr:
        [in]        vmap to vunmap

