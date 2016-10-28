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
        int (*attach)(struct dma_buf *, struct device *,struct dma_buf_attachment *);
        void (*detach)(struct dma_buf *, struct dma_buf_attachment *);
        struct sg_table * (*map_dma_buf)(struct dma_buf_attachment *,enum dma_data_direction);
        void (*unmap_dma_buf)(struct dma_buf_attachment *,struct sg_table *,enum dma_data_direction);
        void (*release)(struct dma_buf *);
        int (*begin_cpu_access)(struct dma_buf *, enum dma_data_direction);
        int (*end_cpu_access)(struct dma_buf *, enum dma_data_direction);
        void *(*kmap_atomic)(struct dma_buf *, unsigned long);
        void (*kunmap_atomic)(struct dma_buf *, unsigned long, void *);
        void *(*kmap)(struct dma_buf *, unsigned long);
        void (*kunmap)(struct dma_buf *, unsigned long, void *);
        int (*mmap)(struct dma_buf *, struct vm_area_struct *vma);
        void *(*vmap)(struct dma_buf *);
        void (*vunmap)(struct dma_buf *, void *vaddr);
    }

.. _`dma_buf_ops.members`:

Members
-------

attach
    [optional] allows different devices to 'attach' themselves to the
    given buffer. It might return -EBUSY to signal that backing storage
    is already allocated and incompatible with the requirements
    of requesting device.

detach
    [optional] detach a given device from this buffer.

map_dma_buf
    returns list of scatter pages allocated, increases usecount
    of the buffer. Requires atleast one attach to be called
    before. Returned sg list should already be mapped into
    \_device\_ address space. This call may sleep. May also return
    -EINTR. Should return -EINVAL if attach hasn't been called yet.

unmap_dma_buf
    decreases usecount of buffer, might deallocate scatter
    pages.

release
    release this buffer; to be called after the last dma_buf_put.

begin_cpu_access
    [optional] called before cpu access to invalidate cpu
    caches and allocate backing storage (if not yet done)
    respectively pin the object into memory.

end_cpu_access
    [optional] called after cpu access to flush caches.

kmap_atomic
    maps a page from the buffer into kernel address
    space, users may not block until the subsequent unmap call.
    This callback must not sleep.

kunmap_atomic
    [optional] unmaps a atomically mapped page from the buffer.
    This Callback must not sleep.

kmap
    maps a page from the buffer into kernel address space.

kunmap
    [optional] unmaps a page from the buffer.

mmap
    used to expose the backing storage to userspace. Note that the
    mapping needs to be coherent - if the exporter doesn't directly
    support this, it needs to fake coherency by shooting down any ptes
    when transitioning away from the cpu domain.

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
        struct dma_buf_poll_cb_t cb_excl;
        struct dma_buf_poll_cb_t cb_shared;
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

    :param  name:
        export-info name

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

