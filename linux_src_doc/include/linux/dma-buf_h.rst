.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/dma-buf.h

.. _`dma_buf_ops`:

struct dma_buf_ops
==================

.. c:type:: struct dma_buf_ops

    operations possible on struct dma_buf

.. _`dma_buf_ops.definition`:

Definition
----------

.. code-block:: c

    struct dma_buf_ops {
        int (*attach)(struct dma_buf *, struct device *, struct dma_buf_attachment *);
        void (*detach)(struct dma_buf *, struct dma_buf_attachment *);
        struct sg_table * (*map_dma_buf)(struct dma_buf_attachment *, enum dma_data_direction);
        void (*unmap_dma_buf)(struct dma_buf_attachment *,struct sg_table *, enum dma_data_direction);
        void (*release)(struct dma_buf *);
        int (*begin_cpu_access)(struct dma_buf *, enum dma_data_direction);
        int (*end_cpu_access)(struct dma_buf *, enum dma_data_direction);
        void *(*map_atomic)(struct dma_buf *, unsigned long);
        void (*unmap_atomic)(struct dma_buf *, unsigned long, void *);
        void *(*map)(struct dma_buf *, unsigned long);
        void (*unmap)(struct dma_buf *, unsigned long, void *);
        int (*mmap)(struct dma_buf *, struct vm_area_struct *vma);
        void *(*vmap)(struct dma_buf *);
        void (*vunmap)(struct dma_buf *, void *vaddr);
    }

.. _`dma_buf_ops.members`:

Members
-------

attach

    This is called from \ :c:func:`dma_buf_attach`\  to make sure that a given
    \ :c:type:`struct device <device>`\  can access the provided \ :c:type:`struct dma_buf <dma_buf>`\ . Exporters which support
    buffer objects in special locations like VRAM or device-specific
    carveout areas should check whether the buffer could be move to
    system memory (or directly accessed by the provided device), and
    otherwise need to fail the attach operation.

    The exporter should also in general check whether the current
    allocation fullfills the DMA constraints of the new device. If this
    is not the case, and the allocation cannot be moved, it should also
    fail the attach operation.

    Any exporter-private housekeeping data can be stored in the
    \ :c:type:`dma_buf_attachment.priv <dma_buf_attachment>`\  pointer.

    This callback is optional.

    Returns:

    0 on success, negative error code on failure. It might return -EBUSY
    to signal that backing storage is already allocated and incompatible
    with the requirements of requesting device.

detach

    This is called by \ :c:func:`dma_buf_detach`\  to release a \ :c:type:`struct dma_buf_attachment <dma_buf_attachment>`\ .
    Provided so that exporters can clean up any housekeeping for an
    \ :c:type:`struct dma_buf_attachment <dma_buf_attachment>`\ .

    This callback is optional.

map_dma_buf

    This is called by \ :c:func:`dma_buf_map_attachment`\  and is used to map a
    shared \ :c:type:`struct dma_buf <dma_buf>`\  into device address space, and it is mandatory. It
    can only be called if \ ``attach``\  has been called successfully. This
    essentially pins the DMA buffer into place, and it cannot be moved
    any more

    This call may sleep, e.g. when the backing storage first needs to be
    allocated, or moved to a location suitable for all currently attached
    devices.

    Note that any specific buffer attributes required for this function
    should get added to device_dma_parameters accessible via
    \ :c:type:`device.dma_params <device>`\  from the \ :c:type:`struct dma_buf_attachment <dma_buf_attachment>`\ . The \ ``attach``\  callback
    should also check these constraints.

    If this is being called for the first time, the exporter can now
    choose to scan through the list of attachments for this buffer,
    collate the requirements of the attached devices, and choose an
    appropriate backing storage for the buffer.

    Based on enum dma_data_direction, it might be possible to have
    multiple users accessing at the same time (for reading, maybe), or
    any other kind of sharing that the exporter might wish to make
    available to buffer-users.

    Returns:

    A \ :c:type:`struct sg_table <sg_table>`\  scatter list of or the backing storage of the DMA buffer,
    already mapped into the device address space of the \ :c:type:`struct device <device>`\  attached
    with the provided \ :c:type:`struct dma_buf_attachment <dma_buf_attachment>`\ .

    On failure, returns a negative error value wrapped into a pointer.
    May also return -EINTR when a signal was received while being
    blocked.

unmap_dma_buf

    This is called by \ :c:func:`dma_buf_unmap_attachment`\  and should unmap and
    release the \ :c:type:`struct sg_table <sg_table>`\  allocated in \ ``map_dma_buf``\ , and it is mandatory.
    It should also unpin the backing storage if this is the last mapping
    of the DMA buffer, it the exporter supports backing storage
    migration.

release

    Called after the last dma_buf_put to release the \ :c:type:`struct dma_buf <dma_buf>`\ , and
    mandatory.

begin_cpu_access

    This is called from \ :c:func:`dma_buf_begin_cpu_access`\  and allows the
    exporter to ensure that the memory is actually available for cpu
    access - the exporter might need to allocate or swap-in and pin the
    backing storage. The exporter also needs to ensure that cpu access is
    coherent for the access direction. The direction can be used by the
    exporter to optimize the cache flushing, i.e. access with a different
    direction (read instead of write) might return stale or even bogus
    data (e.g. when the exporter needs to copy the data to temporary
    storage).

    This callback is optional.

    FIXME: This is both called through the DMA_BUF_IOCTL_SYNC command
    from userspace (where storage shouldn't be pinned to avoid handing
    de-factor mlock rights to userspace) and for the kernel-internal
    users of the various kmap interfaces, where the backing storage must
    be pinned to guarantee that the atomic kmap calls can succeed. Since
    there's no in-kernel users of the kmap interfaces yet this isn't a
    real problem.

    Returns:

    0 on success or a negative error code on failure. This can for
    example fail when the backing storage can't be allocated. Can also
    return -ERESTARTSYS or -EINTR when the call has been interrupted and
    needs to be restarted.

end_cpu_access

    This is called from \ :c:func:`dma_buf_end_cpu_access`\  when the importer is
    done accessing the CPU. The exporter can use this to flush caches and
    unpin any resources pinned in \ ``begin_cpu_access``\ .
    The result of any dma_buf kmap calls after end_cpu_access is
    undefined.

    This callback is optional.

    Returns:

    0 on success or a negative error code on failure. Can return
    -ERESTARTSYS or -EINTR when the call has been interrupted and needs
    to be restarted.

map_atomic
    maps a page from the buffer into kernel address
    space, users may not block until the subsequent unmap call.
    This callback must not sleep.

unmap_atomic
    [optional] unmaps a atomically mapped page from the buffer.
    This Callback must not sleep.

map
    maps a page from the buffer into kernel address space.

unmap
    [optional] unmaps a page from the buffer.

mmap

    This callback is used by the \ :c:func:`dma_buf_mmap`\  function

    Note that the mapping needs to be incoherent, userspace is expected
    to braket CPU access using the DMA_BUF_IOCTL_SYNC interface.

    Because dma-buf buffers have invariant size over their lifetime, the
    dma-buf core checks whether a vma is too large and rejects such
    mappings. The exporter hence does not need to duplicate this check.
    Drivers do not need to check this themselves.

    If an exporter needs to manually flush caches and hence needs to fake
    coherency for mmap support, it needs to be able to zap all the ptes
    pointing at the backing storage. Now linux mm needs a struct
    address_space associated with the struct file stored in vma->vm_file
    to do that with the function unmap_mapping_range. But the dma_buf
    framework only backs every dma_buf fd with the anon_file struct file,
    i.e. all dma_bufs share the same file.

    Hence exporters need to setup their own file (and address_space)
    association by setting vma->vm_file and adjusting vma->vm_pgoff in
    the dma_buf mmap callback. In the specific case of a gem driver the
    exporter could use the shmem file already provided by gem (and set
    vm_pgoff = 0). Exporters can then zap ptes by unmapping the
    corresponding range of the struct address_space associated with their
    own file.

    This callback is optional.

    Returns:

    0 on success or a negative error code on failure.

vmap
    [optional] creates a virtual mapping for the buffer into kernel
    address space. Same restrictions as for vmap and friends apply.

vunmap
    [optional] unmaps a vmap from the buffer

.. _`dma_buf`:

struct dma_buf
==============

.. c:type:: struct dma_buf

    shared buffer object

.. _`dma_buf.definition`:

Definition
----------

.. code-block:: c

    struct dma_buf {
        size_t size;
        struct file *file;
        struct list_head attachments;
        const struct dma_buf_ops *ops;
        struct mutex lock;
        unsigned vmapping_counter;
        void *vmap_ptr;
        const char *exp_name;
        struct module *owner;
        struct list_head list_node;
        void *priv;
        struct reservation_object *resv;
        wait_queue_head_t poll;
        struct dma_buf_poll_cb_t {
            struct dma_fence_cb cb;
            wait_queue_head_t *poll;
            __poll_t active;
        } cb_excl, cb_shared;
    }

.. _`dma_buf.members`:

Members
-------

size
    size of the buffer

file
    file pointer used for sharing buffers across, and for refcounting.

attachments
    list of dma_buf_attachment that denotes all devices attached.

ops
    dma_buf_ops associated with this buffer object.

lock
    used internally to serialize list manipulation, attach/detach and vmap/unmap

vmapping_counter
    used internally to refcnt the vmaps

vmap_ptr
    the current vmap ptr if vmapping_counter > 0

exp_name
    name of the exporter; useful for debugging.

owner
    pointer to exporter module; used for refcounting when exporter is a
    kernel module.

list_node
    node for dma_buf accounting and debugging.

priv
    exporter specific private data for this buffer object.

resv
    reservation object linked to this dma-buf

poll
    for userspace poll support

cb_excl
    for userspace poll support

cb_shared
    for userspace poll support

.. _`dma_buf.description`:

Description
-----------

This represents a shared buffer, created by calling \ :c:func:`dma_buf_export`\ . The
userspace representation is a normal file descriptor, which can be created by
calling \ :c:func:`dma_buf_fd`\ .

Shared dma buffers are reference counted using \ :c:func:`dma_buf_put`\  and
\ :c:func:`get_dma_buf`\ .

Device DMA access is handled by the separate \ :c:type:`struct dma_buf_attachment <dma_buf_attachment>`\ .

.. _`dma_buf_attachment`:

struct dma_buf_attachment
=========================

.. c:type:: struct dma_buf_attachment

    holds device-buffer attachment data

.. _`dma_buf_attachment.definition`:

Definition
----------

.. code-block:: c

    struct dma_buf_attachment {
        struct dma_buf *dmabuf;
        struct device *dev;
        struct list_head node;
        void *priv;
    }

.. _`dma_buf_attachment.members`:

Members
-------

dmabuf
    buffer for this attachment.

dev
    device attached to the buffer.

node
    list of dma_buf_attachment.

priv
    exporter specific attachment data.

.. _`dma_buf_attachment.description`:

Description
-----------

This structure holds the attachment information between the dma_buf buffer
and its user device(s). The list contains one attachment struct per device
attached to the buffer.

An attachment is created by calling \ :c:func:`dma_buf_attach`\ , and released again by
calling \ :c:func:`dma_buf_detach`\ . The DMA mapping itself needed to initiate a
transfer is created by \ :c:func:`dma_buf_map_attachment`\  and freed again by calling
\ :c:func:`dma_buf_unmap_attachment`\ .

.. _`dma_buf_export_info`:

struct dma_buf_export_info
==========================

.. c:type:: struct dma_buf_export_info

    holds information needed to export a dma_buf

.. _`dma_buf_export_info.definition`:

Definition
----------

.. code-block:: c

    struct dma_buf_export_info {
        const char *exp_name;
        struct module *owner;
        const struct dma_buf_ops *ops;
        size_t size;
        int flags;
        struct reservation_object *resv;
        void *priv;
    }

.. _`dma_buf_export_info.members`:

Members
-------

exp_name
    name of the exporter - useful for debugging.

owner
    pointer to exporter module - used for refcounting kernel module

ops
    Attach allocator-defined dma buf ops to the new buffer

size
    Size of the buffer

flags
    mode flags for the file

resv
    reservation-object, NULL to allocate default one

priv
    Attach private data of allocator to this buffer

.. _`dma_buf_export_info.description`:

Description
-----------

This structure holds the information required to export the buffer. Used
with \ :c:func:`dma_buf_export`\  only.

.. _`define_dma_buf_export_info`:

DEFINE_DMA_BUF_EXPORT_INFO
==========================

.. c:function::  DEFINE_DMA_BUF_EXPORT_INFO( name)

    helper macro for exporters

    :param  name:
        export-info name

.. _`define_dma_buf_export_info.description`:

Description
-----------

DEFINE_DMA_BUF_EXPORT_INFO macro defines the \ :c:type:`struct dma_buf_export_info <dma_buf_export_info>`\ ,
zeroes it out and pre-populates exp_name in it.

.. _`get_dma_buf`:

get_dma_buf
===========

.. c:function:: void get_dma_buf(struct dma_buf *dmabuf)

    convenience wrapper for get_file.

    :param struct dma_buf \*dmabuf:
        [in]    pointer to dma_buf

.. _`get_dma_buf.description`:

Description
-----------

Increments the reference count on the dma-buf, needed in case of drivers
that either need to create additional references to the dmabuf on the
kernel side.  For example, an exporter that needs to keep a dmabuf ptr
so that subsequent exports don't create a new dmabuf.

.. This file was automatic generated / don't edit.

