.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma-buf/dma-buf.c

.. _`fence-polling`:

fence polling
=============

To support cross-device and cross-driver synchronization of buffer access
implicit fences (represented internally in the kernel with \ :c:type:`struct fence <fence>`\ ) can
be attached to a \ :c:type:`struct dma_buf <dma_buf>`\ . The glue for that and a few related things are
provided in the \ :c:type:`struct reservation_object <reservation_object>`\  structure.

Userspace can query the state of these implicitly tracked fences using \ :c:func:`poll`\ 
and related system calls:

- Checking for POLLIN, i.e. read access, can be use to query the state of the
  most recent write or exclusive fence.

- Checking for POLLOUT, i.e. write access, can be used to query the state of
  all attached fences, shared and exclusive ones.

Note that this only signals the completion of the respective fences, i.e. the
DMA transfers are complete. Cache flushing and any other necessary
preparations before CPU access can begin still need to happen.

.. _`dma-buf-device-access`:

dma buf device access
=====================

For device DMA access to a shared DMA buffer the usual sequence of operations
is fairly simple:

1. The exporter defines his exporter instance using
   \ :c:func:`DEFINE_DMA_BUF_EXPORT_INFO`\  and calls \ :c:func:`dma_buf_export`\  to wrap a private
   buffer object into a \ :c:type:`struct dma_buf <dma_buf>`\ . It then exports that \ :c:type:`struct dma_buf <dma_buf>`\  to userspace
   as a file descriptor by calling \ :c:func:`dma_buf_fd`\ .

2. Userspace passes this file-descriptors to all drivers it wants this buffer
   to share with: First the filedescriptor is converted to a \ :c:type:`struct dma_buf <dma_buf>`\  using
   \ :c:func:`dma_buf_get`\ . The the buffer is attached to the device using
   \ :c:func:`dma_buf_attach`\ .

   Up to this stage the exporter is still free to migrate or reallocate the
   backing storage.

3. Once the buffer is attached to all devices userspace can inniate DMA
   access to the shared buffer. In the kernel this is done by calling
   \ :c:func:`dma_buf_map_attachment`\  and \ :c:func:`dma_buf_unmap_attachment`\ .

4. Once a driver is done with a shared buffer it needs to call
   \ :c:func:`dma_buf_detach`\  (after cleaning up any mappings) and then release the
   reference acquired with dma_buf_get by calling \ :c:func:`dma_buf_put`\ .

For the detailed semantics exporters are expected to implement see
\ :c:type:`struct dma_buf_ops <dma_buf_ops>`\ .

.. _`dma_buf_export`:

dma_buf_export
==============

.. c:function:: struct dma_buf *dma_buf_export(const struct dma_buf_export_info *exp_info)

    Creates a new dma_buf, and associates an anon file with this buffer, so it can be exported. Also connect the allocator specific data and ops to the buffer. Additionally, provide a name string for exporter; useful in debugging.

    :param const struct dma_buf_export_info \*exp_info:
        [in]    holds all the export related information provided
        by the exporter. see \ :c:type:`struct dma_buf_export_info <dma_buf_export_info>`\ 
        for further details.

.. _`dma_buf_export.description`:

Description
-----------

Returns, on success, a newly created dma_buf object, which wraps the
supplied private data and operations for dma_buf_ops. On either missing
ops, or error in allocating struct dma_buf, will return negative error.

For most cases the easiest way to create \ ``exp_info``\  is through the
\ ``DEFINE_DMA_BUF_EXPORT_INFO``\  macro.

.. _`dma_buf_fd`:

dma_buf_fd
==========

.. c:function:: int dma_buf_fd(struct dma_buf *dmabuf, int flags)

    returns a file descriptor for the given dma_buf

    :param struct dma_buf \*dmabuf:
        [in]    pointer to dma_buf for which fd is required.

    :param int flags:
        [in]    flags to give to fd

.. _`dma_buf_fd.description`:

Description
-----------

On success, returns an associated 'fd'. Else, returns error.

.. _`dma_buf_get`:

dma_buf_get
===========

.. c:function:: struct dma_buf *dma_buf_get(int fd)

    returns the dma_buf structure related to an fd

    :param int fd:
        [in]    fd associated with the dma_buf to be returned

.. _`dma_buf_get.description`:

Description
-----------

On success, returns the dma_buf structure associated with an fd; uses
file's refcounting done by fget to increase refcount. returns ERR_PTR
otherwise.

.. _`dma_buf_put`:

dma_buf_put
===========

.. c:function:: void dma_buf_put(struct dma_buf *dmabuf)

    decreases refcount of the buffer

    :param struct dma_buf \*dmabuf:
        [in]    buffer to reduce refcount of

.. _`dma_buf_put.description`:

Description
-----------

Uses file's refcounting done implicitly by \ :c:func:`fput`\ .

If, as a result of this call, the refcount becomes 0, the 'release' file
operation related to this fd is called. It calls \ :c:type:`dma_buf_ops.release <dma_buf_ops>`\  vfunc
in turn, and frees the memory allocated for dmabuf when exported.

.. _`dma_buf_attach`:

dma_buf_attach
==============

.. c:function:: struct dma_buf_attachment *dma_buf_attach(struct dma_buf *dmabuf, struct device *dev)

    Add the device to dma_buf's attachments list; optionally, calls \ :c:func:`attach`\  of dma_buf_ops to allow device-specific attach functionality

    :param struct dma_buf \*dmabuf:
        [in]    buffer to attach device to.

    :param struct device \*dev:
        [in]    device to be attached.

.. _`dma_buf_attach.description`:

Description
-----------

Returns struct dma_buf_attachment pointer for this attachment. Attachments
must be cleaned up by calling \ :c:func:`dma_buf_detach`\ .

.. _`dma_buf_attach.return`:

Return
------


A pointer to newly created \ :c:type:`struct dma_buf_attachment <dma_buf_attachment>`\  on success, or a negative
error code wrapped into a pointer on failure.

Note that this can fail if the backing storage of \ ``dmabuf``\  is in a place not
accessible to \ ``dev``\ , and cannot be moved to a more suitable place. This is
indicated with the error code -EBUSY.

.. _`dma_buf_detach`:

dma_buf_detach
==============

.. c:function:: void dma_buf_detach(struct dma_buf *dmabuf, struct dma_buf_attachment *attach)

    Remove the given attachment from dmabuf's attachments list; optionally calls \ :c:func:`detach`\  of dma_buf_ops for device-specific detach

    :param struct dma_buf \*dmabuf:
        [in]    buffer to detach from.

    :param struct dma_buf_attachment \*attach:
        [in]    attachment to be detached; is free'd after this call.

.. _`dma_buf_detach.description`:

Description
-----------

Clean up a device attachment obtained by calling \ :c:func:`dma_buf_attach`\ .

.. _`dma_buf_map_attachment`:

dma_buf_map_attachment
======================

.. c:function:: struct sg_table *dma_buf_map_attachment(struct dma_buf_attachment *attach, enum dma_data_direction direction)

    Returns the scatterlist table of the attachment; mapped into _device_ address space. Is a wrapper for \ :c:func:`map_dma_buf`\  of the dma_buf_ops.

    :param struct dma_buf_attachment \*attach:
        [in]    attachment whose scatterlist is to be returned

    :param enum dma_data_direction direction:
        [in]    direction of DMA transfer

.. _`dma_buf_map_attachment.description`:

Description
-----------

Returns sg_table containing the scatterlist to be returned; returns ERR_PTR
on error. May return -EINTR if it is interrupted by a signal.

A mapping must be unmapped again using \ :c:func:`dma_buf_map_attachment`\ . Note that
the underlying backing storage is pinned for as long as a mapping exists,
therefore users/importers should not hold onto a mapping for undue amounts of
time.

.. _`dma_buf_unmap_attachment`:

dma_buf_unmap_attachment
========================

.. c:function:: void dma_buf_unmap_attachment(struct dma_buf_attachment *attach, struct sg_table *sg_table, enum dma_data_direction direction)

    unmaps and decreases usecount of the buffer;might deallocate the scatterlist associated. Is a wrapper for \ :c:func:`unmap_dma_buf`\  of dma_buf_ops.

    :param struct dma_buf_attachment \*attach:
        [in]    attachment to unmap buffer from

    :param struct sg_table \*sg_table:
        [in]    scatterlist info of the buffer to unmap

    :param enum dma_data_direction direction:
        [in]    direction of DMA transfer

.. _`dma_buf_unmap_attachment.description`:

Description
-----------

This unmaps a DMA mapping for \ ``attached``\  obtained by \ :c:func:`dma_buf_map_attachment`\ .

.. _`cpu-access`:

cpu access
==========

There are mutliple reasons for supporting CPU access to a dma buffer object:

- Fallback operations in the kernel, for example when a device is connected
  over USB and the kernel needs to shuffle the data around first before
  sending it away. Cache coherency is handled by braketing any transactions
  with calls to \ :c:func:`dma_buf_begin_cpu_access`\  and \ :c:func:`dma_buf_end_cpu_access`\ 
  access.

  To support dma_buf objects residing in highmem cpu access is page-based
  using an api similar to kmap. Accessing a dma_buf is done in aligned chunks
  of PAGE_SIZE size. Before accessing a chunk it needs to be mapped, which
  returns a pointer in kernel virtual address space. Afterwards the chunk
  needs to be unmapped again. There is no limit on how often a given chunk
  can be mapped and unmapped, i.e. the importer does not need to call
  begin_cpu_access again before mapping the same chunk again.

  Interfaces::
     void \*dma_buf_kmap(struct dma_buf \*, unsigned long);
     void dma_buf_kunmap(struct dma_buf \*, unsigned long, void \*);

  There are also atomic variants of these interfaces. Like for kmap they
  facilitate non-blocking fast-paths. Neither the importer nor the exporter
  (in the callback) is allowed to block when using these.

  Interfaces::
     void \*dma_buf_kmap_atomic(struct dma_buf \*, unsigned long);
     void dma_buf_kunmap_atomic(struct dma_buf \*, unsigned long, void \*);

  For importers all the restrictions of using kmap apply, like the limited
  supply of kmap_atomic slots. Hence an importer shall only hold onto at
  max 2 atomic dma_buf kmaps at the same time (in any given process context).

  dma_buf kmap calls outside of the range specified in begin_cpu_access are
  undefined. If the range is not PAGE_SIZE aligned, kmap needs to succeed on
  the partial chunks at the beginning and end but may return stale or bogus
  data outside of the range (in these partial chunks).

  Note that these calls need to always succeed. The exporter needs to
  complete any preparations that might fail in begin_cpu_access.

  For some cases the overhead of kmap can be too high, a vmap interface
  is introduced. This interface should be used very carefully, as vmalloc
  space is a limited resources on many architectures.

  Interfaces::
     void \*dma_buf_vmap(struct dma_buf \*dmabuf)
     void dma_buf_vunmap(struct dma_buf \*dmabuf, void \*vaddr)

  The vmap call can fail if there is no vmap support in the exporter, or if
  it runs out of vmalloc space. Fallback to kmap should be implemented. Note
  that the dma-buf layer keeps a reference count for all vmap access and
  calls down into the exporter's vmap function only when no vmapping exists,
  and only unmaps it once. Protection against concurrent vmap/vunmap calls is
  provided by taking the dma_buf->lock mutex.

- For full compatibility on the importer side with existing userspace
  interfaces, which might already support mmap'ing buffers. This is needed in
  many processing pipelines (e.g. feeding a software rendered image into a
  hardware pipeline, thumbnail creation, snapshots, ...). Also, Android's ION
  framework already supported this and for DMA buffer file descriptors to
  replace ION buffers mmap support was needed.

  There is no special interfaces, userspace simply calls mmap on the dma-buf
  fd. But like for CPU access there's a need to braket the actual access,
  which is handled by the ioctl (DMA_BUF_IOCTL_SYNC). Note that
  DMA_BUF_IOCTL_SYNC can fail with -EAGAIN or -EINTR, in which case it must
  be restarted.

  Some systems might need some sort of cache coherency management e.g. when
  CPU and GPU domains are being accessed through dma-buf at the same time.
  To circumvent this problem there are begin/end coherency markers, that
  forward directly to existing dma-buf device drivers vfunc hooks. Userspace
  can make use of those markers through the DMA_BUF_IOCTL_SYNC ioctl. The
  sequence would be used like following:

    - mmap dma-buf fd
    - for each drawing/upload cycle in CPU 1. SYNC_START ioctl, 2. read/write
      to mmap area 3. SYNC_END ioctl. This can be repeated as often as you
      want (with the new data being consumed by say the GPU or the scanout
      device)
    - munmap once you don't need the buffer any more

   For correctness and optimal performance, it is always required to use
   SYNC_START and SYNC_END before and after, respectively, when accessing the
   mapped address. Userspace cannot rely on coherent access, even when there
   are systems where it just works without calling these ioctls.

- And as a CPU fallback in userspace processing pipelines.

  Similar to the motivation for kernel cpu access it is again important that
  the userspace code of a given importing subsystem can use the same
  interfaces with a imported dma-buf buffer object as with a native buffer
  object. This is especially important for drm where the userspace part of
  contemporary OpenGL, X, and other drivers is huge, and reworking them to
  use a different way to mmap a buffer rather invasive.

  The assumption in the current dma-buf interfaces is that redirecting the
  initial mmap is all that's needed. A survey of some of the existing
  subsystems shows that no driver seems to do any nefarious thing like
  syncing up with outstanding asynchronous processing on the device or
  allocating special resources at fault time. So hopefully this is good
  enough, since adding interfaces to intercept pagefaults and allow pte
  shootdowns would increase the complexity quite a bit.

  Interface::
     int dma_buf_mmap(struct dma_buf \*, struct vm_area_struct \*,
                    unsigned long);

  If the importing subsystem simply provides a special-purpose mmap call to
  set up a mapping in userspace, calling do_mmap with dma_buf->file will
  equally achieve that for a dma-buf object.

.. _`dma_buf_begin_cpu_access`:

dma_buf_begin_cpu_access
========================

.. c:function:: int dma_buf_begin_cpu_access(struct dma_buf *dmabuf, enum dma_data_direction direction)

    Must be called before accessing a dma_buf from the cpu in the kernel context. Calls begin_cpu_access to allow exporter-specific preparations. Coherency is only guaranteed in the specified range for the specified access direction.

    :param struct dma_buf \*dmabuf:
        [in]    buffer to prepare cpu access for.

    :param enum dma_data_direction direction:
        [in]    length of range for cpu access.

.. _`dma_buf_begin_cpu_access.description`:

Description
-----------

After the cpu access is complete the caller should call
\ :c:func:`dma_buf_end_cpu_access`\ . Only when cpu access is braketed by both calls is
it guaranteed to be coherent with other DMA access.

Can return negative error values, returns 0 on success.

.. _`dma_buf_end_cpu_access`:

dma_buf_end_cpu_access
======================

.. c:function:: int dma_buf_end_cpu_access(struct dma_buf *dmabuf, enum dma_data_direction direction)

    Must be called after accessing a dma_buf from the cpu in the kernel context. Calls end_cpu_access to allow exporter-specific actions. Coherency is only guaranteed in the specified range for the specified access direction.

    :param struct dma_buf \*dmabuf:
        [in]    buffer to complete cpu access for.

    :param enum dma_data_direction direction:
        [in]    length of range for cpu access.

.. _`dma_buf_end_cpu_access.description`:

Description
-----------

This terminates CPU access started with \ :c:func:`dma_buf_begin_cpu_access`\ .

Can return negative error values, returns 0 on success.

.. _`dma_buf_kmap_atomic`:

dma_buf_kmap_atomic
===================

.. c:function:: void *dma_buf_kmap_atomic(struct dma_buf *dmabuf, unsigned long page_num)

    Map a page of the buffer object into kernel address space. The same restrictions as for kmap_atomic and friends apply.

    :param struct dma_buf \*dmabuf:
        [in]    buffer to map page from.

    :param unsigned long page_num:
        [in]    page in PAGE_SIZE units to map.

.. _`dma_buf_kmap_atomic.description`:

Description
-----------

This call must always succeed, any necessary preparations that might fail
need to be done in begin_cpu_access.

.. _`dma_buf_kunmap_atomic`:

dma_buf_kunmap_atomic
=====================

.. c:function:: void dma_buf_kunmap_atomic(struct dma_buf *dmabuf, unsigned long page_num, void *vaddr)

    Unmap a page obtained by dma_buf_kmap_atomic.

    :param struct dma_buf \*dmabuf:
        [in]    buffer to unmap page from.

    :param unsigned long page_num:
        [in]    page in PAGE_SIZE units to unmap.

    :param void \*vaddr:
        [in]    kernel space pointer obtained from dma_buf_kmap_atomic.

.. _`dma_buf_kunmap_atomic.description`:

Description
-----------

This call must always succeed.

.. _`dma_buf_kmap`:

dma_buf_kmap
============

.. c:function:: void *dma_buf_kmap(struct dma_buf *dmabuf, unsigned long page_num)

    Map a page of the buffer object into kernel address space. The same restrictions as for kmap and friends apply.

    :param struct dma_buf \*dmabuf:
        [in]    buffer to map page from.

    :param unsigned long page_num:
        [in]    page in PAGE_SIZE units to map.

.. _`dma_buf_kmap.description`:

Description
-----------

This call must always succeed, any necessary preparations that might fail
need to be done in begin_cpu_access.

.. _`dma_buf_kunmap`:

dma_buf_kunmap
==============

.. c:function:: void dma_buf_kunmap(struct dma_buf *dmabuf, unsigned long page_num, void *vaddr)

    Unmap a page obtained by dma_buf_kmap.

    :param struct dma_buf \*dmabuf:
        [in]    buffer to unmap page from.

    :param unsigned long page_num:
        [in]    page in PAGE_SIZE units to unmap.

    :param void \*vaddr:
        [in]    kernel space pointer obtained from dma_buf_kmap.

.. _`dma_buf_kunmap.description`:

Description
-----------

This call must always succeed.

.. _`dma_buf_mmap`:

dma_buf_mmap
============

.. c:function:: int dma_buf_mmap(struct dma_buf *dmabuf, struct vm_area_struct *vma, unsigned long pgoff)

    Setup up a userspace mmap with the given vma

    :param struct dma_buf \*dmabuf:
        [in]    buffer that should back the vma

    :param struct vm_area_struct \*vma:
        [in]    vma for the mmap

    :param unsigned long pgoff:
        [in]    offset in pages where this mmap should start within the
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

.. c:function:: void *dma_buf_vmap(struct dma_buf *dmabuf)

    Create virtual mapping for the buffer object into kernel address space. Same restrictions as for vmap and friends apply.

    :param struct dma_buf \*dmabuf:
        [in]    buffer to vmap

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

.. c:function:: void dma_buf_vunmap(struct dma_buf *dmabuf, void *vaddr)

    Unmap a vmap obtained by dma_buf_vmap.

    :param struct dma_buf \*dmabuf:
        [in]    buffer to vunmap

    :param void \*vaddr:
        [in]    vmap to vunmap

.. This file was automatic generated / don't edit.

