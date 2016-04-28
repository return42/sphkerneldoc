.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-vb2-mem-ops:

==================
struct vb2_mem_ops
==================

*man struct vb2_mem_ops(9)*

*4.6.0-rc5*

memory handling/memory allocator operations


Synopsis
========

.. code-block:: c

    struct vb2_mem_ops {
      void *(* alloc) (void *alloc_ctx, unsigned long size,enum dma_data_direction dma_dir,gfp_t gfp_flags);
      void (* put) (void *buf_priv);
      struct dma_buf *(* get_dmabuf) (void *buf_priv, unsigned long flags);
      void *(* get_userptr) (void *alloc_ctx, unsigned long vaddr,unsigned long size,enum dma_data_direction dma_dir);
      void (* put_userptr) (void *buf_priv);
      void (* prepare) (void *buf_priv);
      void (* finish) (void *buf_priv);
      void *(* attach_dmabuf) (void *alloc_ctx, struct dma_buf *dbuf,unsigned long size,enum dma_data_direction dma_dir);
      void (* detach_dmabuf) (void *buf_priv);
      int (* map_dmabuf) (void *buf_priv);
      void (* unmap_dmabuf) (void *buf_priv);
      void *(* vaddr) (void *buf_priv);
      void *(* cookie) (void *buf_priv);
      unsigned int  (* num_users) (void *buf_priv);
      int (* mmap) (void *buf_priv, struct vm_area_struct *vma);
    };


Members
=======

alloc
    allocate video memory and, optionally, allocator private data,
    return NULL on failure or a pointer to allocator private, per-buffer
    data on success; the returned private structure will then be passed
    as buf_priv argument to other ops in this structure. Additional
    gfp_flags to use when allocating the are also passed to this
    operation. These flags are from the gfp_flags field of vb2_queue.

put
    inform the allocator that the buffer will no longer be used; usually
    will result in the allocator freeing the buffer (if no other users
    of this buffer are present); the buf_priv argument is the allocator
    private per-buffer structure previously returned from the alloc
    callback.

get_dmabuf
    acquire userspace memory for a hardware operation; used for DMABUF
    memory types.

get_userptr
    acquire userspace memory for a hardware operation; used for USERPTR
    memory types; vaddr is the address passed to the videobuf layer when
    queuing a video buffer of USERPTR type; should return an allocator
    private per-buffer structure associated with the buffer on success,
    NULL on failure; the returned private structure will then be passed
    as buf_priv argument to other ops in this structure.

put_userptr
    inform the allocator that a USERPTR buffer will no longer be used.

prepare
    called every time the buffer is passed from userspace to the driver,
    useful for cache synchronisation, optional.

finish
    called every time the buffer is passed back from the driver to the
    userspace, also optional.

attach_dmabuf
    attach a shared struct dma_buf for a hardware operation; used for
    DMABUF memory types; alloc_ctx is the alloc context dbuf is the
    shared dma_buf; returns NULL on failure; allocator private
    per-buffer structure on success; this needs to be used for further
    accesses to the buffer.

detach_dmabuf
    inform the exporter of the buffer that the current DMABUF buffer is
    no longer used; the buf_priv argument is the allocator private
    per-buffer structure previously returned from the attach_dmabuf
    callback.

map_dmabuf
    request for access to the dmabuf from allocator; the allocator of
    dmabuf is informed that this driver is going to use the dmabuf.

unmap_dmabuf
    releases access control to the dmabuf - allocator is notified that
    this driver is done using the dmabuf for now.

vaddr
    return a kernel virtual address to a given memory buffer associated
    with the passed private structure or NULL if no such mapping exists.

cookie
    return allocator specific cookie for a given memory buffer
    associated with the passed private structure or NULL if not
    available.

num_users
    return the current number of users of a memory buffer; return 1 if
    the videobuf layer (or actually the driver using it) is the only
    user.

mmap
    setup a userspace mapping for a given memory buffer under the
    provided virtual memory region.


Required ops for USERPTR types
==============================

get_userptr, put_userptr.


Required ops for MMAP types
===========================

alloc, put, num_users, mmap. Required ops for read/write access types:
alloc, put, num_users, vaddr.


Required ops for DMABUF types
=============================

attach_dmabuf, detach_dmabuf, map_dmabuf, unmap_dmabuf.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
