.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/videobuf2-core.h

.. _`vb2_memory`:

enum vb2_memory
===============

.. c:type:: enum vb2_memory

    type of memory model used to make the buffers visible on userspace.

.. _`vb2_memory.definition`:

Definition
----------

.. code-block:: c

    enum vb2_memory {
        VB2_MEMORY_UNKNOWN,
        VB2_MEMORY_MMAP,
        VB2_MEMORY_USERPTR,
        VB2_MEMORY_DMABUF
    };

.. _`vb2_memory.constants`:

Constants
---------

VB2_MEMORY_UNKNOWN
    Buffer status is unknown or it is not used yet on
    userspace.

VB2_MEMORY_MMAP
    The buffers are allocated by the Kernel and it is
    memory mapped via \ :c:func:`mmap`\  ioctl. This model is
    also used when the user is using the buffers via
    \ :c:func:`read`\  or \ :c:func:`write`\  system calls.

VB2_MEMORY_USERPTR
    The buffers was allocated in userspace and it is
    memory mapped via \ :c:func:`mmap`\  ioctl.

VB2_MEMORY_DMABUF
    The buffers are passed to userspace via DMA buffer.

.. _`vb2_mem_ops`:

struct vb2_mem_ops
==================

.. c:type:: struct vb2_mem_ops

    memory handling/memory allocator operations.

.. _`vb2_mem_ops.definition`:

Definition
----------

.. code-block:: c

    struct vb2_mem_ops {
        void *(*alloc)(struct device *dev, unsigned long attrs,unsigned long size,enum dma_data_direction dma_dir, gfp_t gfp_flags);
        void (*put)(void *buf_priv);
        struct dma_buf *(*get_dmabuf)(void *buf_priv, unsigned long flags);
        void *(*get_userptr)(struct device *dev, unsigned long vaddr,unsigned long size, enum dma_data_direction dma_dir);
        void (*put_userptr)(void *buf_priv);
        void (*prepare)(void *buf_priv);
        void (*finish)(void *buf_priv);
        void *(*attach_dmabuf)(struct device *dev,struct dma_buf *dbuf,unsigned long size, enum dma_data_direction dma_dir);
        void (*detach_dmabuf)(void *buf_priv);
        int (*map_dmabuf)(void *buf_priv);
        void (*unmap_dmabuf)(void *buf_priv);
        void *(*vaddr)(void *buf_priv);
        void *(*cookie)(void *buf_priv);
        unsigned int (*num_users)(void *buf_priv);
        int (*mmap)(void *buf_priv, struct vm_area_struct *vma);
    }

.. _`vb2_mem_ops.members`:

Members
-------

alloc
    allocate video memory and, optionally, allocator private data,
    return \ :c:func:`ERR_PTR`\  on failure or a pointer to allocator private,
    per-buffer data on success; the returned private structure
    will then be passed as \ ``buf_priv``\  argument to other ops in this
    structure. Additional gfp_flags to use when allocating the
    are also passed to this operation. These flags are from the
    gfp_flags field of vb2_queue.

put
    inform the allocator that the buffer will no longer be used;
    usually will result in the allocator freeing the buffer (if
    no other users of this buffer are present); the \ ``buf_priv``\ 
    argument is the allocator private per-buffer structure
    previously returned from the alloc callback.

get_dmabuf
    acquire userspace memory for a hardware operation; used for
    DMABUF memory types.

get_userptr
    acquire userspace memory for a hardware operation; used for
    USERPTR memory types; vaddr is the address passed to the
    videobuf layer when queuing a video buffer of USERPTR type;
    should return an allocator private per-buffer structure
    associated with the buffer on success, \ :c:func:`ERR_PTR`\  on failure;
    the returned private structure will then be passed as \ ``buf_priv``\ 
    argument to other ops in this structure.

put_userptr
    inform the allocator that a USERPTR buffer will no longer
    be used.

prepare
    called every time the buffer is passed from userspace to the
    driver, useful for cache synchronisation, optional.

finish
    called every time the buffer is passed back from the driver
    to the userspace, also optional.

attach_dmabuf
    attach a shared \ :c:type:`struct dma_buf <dma_buf>`\  for a hardware operation;
    used for DMABUF memory types; dev is the alloc device
    dbuf is the shared dma_buf; returns \ :c:func:`ERR_PTR`\  on failure;
    allocator private per-buffer structure on success;
    this needs to be used for further accesses to the buffer.

detach_dmabuf
    inform the exporter of the buffer that the current DMABUF
    buffer is no longer used; the \ ``buf_priv``\  argument is the
    allocator private per-buffer structure previously returned
    from the attach_dmabuf callback.

map_dmabuf
    request for access to the dmabuf from allocator; the allocator
    of dmabuf is informed that this driver is going to use the
    dmabuf.

unmap_dmabuf
    releases access control to the dmabuf - allocator is notified
    that this driver is done using the dmabuf for now.

vaddr
    return a kernel virtual address to a given memory buffer
    associated with the passed private structure or NULL if no
    such mapping exists.

cookie
    return allocator specific cookie for a given memory buffer
    associated with the passed private structure or NULL if not
    available.

num_users
    return the current number of users of a memory buffer;
    return 1 if the videobuf layer (or actually the driver using
    it) is the only user.

mmap
    setup a userspace mapping for a given memory buffer under
    the provided virtual memory region.

.. _`vb2_mem_ops.description`:

Description
-----------

Those operations are used by the videobuf2 core to implement the memory
handling/memory allocators for each type of supported streaming I/O method.

.. note::
   #) Required ops for USERPTR types: get_userptr, put_userptr.

   #) Required ops for MMAP types: alloc, put, num_users, mmap.

   #) Required ops for read/write access types: alloc, put, num_users, vaddr.

   #) Required ops for DMABUF types: attach_dmabuf, detach_dmabuf,
      map_dmabuf, unmap_dmabuf.

.. _`vb2_plane`:

struct vb2_plane
================

.. c:type:: struct vb2_plane

    plane information.

.. _`vb2_plane.definition`:

Definition
----------

.. code-block:: c

    struct vb2_plane {
        void *mem_priv;
        struct dma_buf *dbuf;
        unsigned int dbuf_mapped;
        unsigned int bytesused;
        unsigned int length;
        unsigned int min_length;
        union {
            unsigned int offset;
            unsigned long userptr;
            int fd;
        } m;
        unsigned int data_offset;
    }

.. _`vb2_plane.members`:

Members
-------

mem_priv
    private data with this plane.

dbuf
    dma_buf - shared buffer object.

dbuf_mapped
    flag to show whether dbuf is mapped or not

bytesused
    number of bytes occupied by data in the plane (payload).

length
    size of this plane (NOT the payload) in bytes.

min_length
    minimum required size of this plane (NOT the payload) in bytes.
    \ ``length``\  is always greater or equal to \ ``min_length``\ .

m
    Union with memtype-specific data.

m.offset
    when memory in the associated struct vb2_buffer is
    \ ``VB2_MEMORY_MMAP``\ , equals the offset from the start of
    the device memory for this plane (or is a "cookie" that
    should be passed to \ :c:func:`mmap`\  called on the video node).

m.userptr
    when memory is \ ``VB2_MEMORY_USERPTR``\ , a userspace pointer
    pointing to this plane.

m.fd
    when memory is \ ``VB2_MEMORY_DMABUF``\ , a userspace file
    descriptor associated with this plane.

data_offset
    offset in the plane to the start of data; usually 0,
    unless there is a header in front of the data.

.. _`vb2_plane.description`:

Description
-----------

Should contain enough information to be able to cover all the fields
of \ :c:type:`struct v4l2_plane <v4l2_plane>`\  at videodev2.h.

.. _`vb2_io_modes`:

enum vb2_io_modes
=================

.. c:type:: enum vb2_io_modes

    queue access methods.

.. _`vb2_io_modes.definition`:

Definition
----------

.. code-block:: c

    enum vb2_io_modes {
        VB2_MMAP,
        VB2_USERPTR,
        VB2_READ,
        VB2_WRITE,
        VB2_DMABUF
    };

.. _`vb2_io_modes.constants`:

Constants
---------

VB2_MMAP
    driver supports MMAP with streaming API.

VB2_USERPTR
    driver supports USERPTR with streaming API.

VB2_READ
    driver supports \ :c:func:`read`\  style access.

VB2_WRITE
    driver supports \ :c:func:`write`\  style access.

VB2_DMABUF
    driver supports DMABUF with streaming API.

.. _`vb2_buffer_state`:

enum vb2_buffer_state
=====================

.. c:type:: enum vb2_buffer_state

    current video buffer state.

.. _`vb2_buffer_state.definition`:

Definition
----------

.. code-block:: c

    enum vb2_buffer_state {
        VB2_BUF_STATE_DEQUEUED,
        VB2_BUF_STATE_PREPARING,
        VB2_BUF_STATE_PREPARED,
        VB2_BUF_STATE_QUEUED,
        VB2_BUF_STATE_REQUEUEING,
        VB2_BUF_STATE_ACTIVE,
        VB2_BUF_STATE_DONE,
        VB2_BUF_STATE_ERROR
    };

.. _`vb2_buffer_state.constants`:

Constants
---------

VB2_BUF_STATE_DEQUEUED
    buffer under userspace control.

VB2_BUF_STATE_PREPARING
    buffer is being prepared in videobuf.

VB2_BUF_STATE_PREPARED
    buffer prepared in videobuf and by the driver.

VB2_BUF_STATE_QUEUED
    buffer queued in videobuf, but not in driver.

VB2_BUF_STATE_REQUEUEING
    re-queue a buffer to the driver.

VB2_BUF_STATE_ACTIVE
    buffer queued in driver and possibly used
    in a hardware operation.

VB2_BUF_STATE_DONE
    buffer returned from driver to videobuf, but
    not yet dequeued to userspace.

VB2_BUF_STATE_ERROR
    same as above, but the operation on the buffer
    has ended with an error, which will be reported
    to the userspace when it is dequeued.

.. _`vb2_buffer`:

struct vb2_buffer
=================

.. c:type:: struct vb2_buffer

    represents a video buffer.

.. _`vb2_buffer.definition`:

Definition
----------

.. code-block:: c

    struct vb2_buffer {
        struct vb2_queue *vb2_queue;
        unsigned int index;
        unsigned int type;
        unsigned int memory;
        unsigned int num_planes;
        u64 timestamp;
    }

.. _`vb2_buffer.members`:

Members
-------

vb2_queue
    pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with the queue to
    which this driver belongs.

index
    id number of the buffer.

type
    buffer type.

memory
    the method, in which the actual data is passed.

num_planes
    number of planes in the buffer
    on an internal driver queue.

timestamp
    frame timestamp in ns.

.. _`vb2_ops`:

struct vb2_ops
==============

.. c:type:: struct vb2_ops

    driver-specific callbacks.

.. _`vb2_ops.definition`:

Definition
----------

.. code-block:: c

    struct vb2_ops {
        int (*queue_setup)(struct vb2_queue *q,unsigned int *num_buffers, unsigned int *num_planes, unsigned int sizes[], struct device *alloc_devs[]);
        void (*wait_prepare)(struct vb2_queue *q);
        void (*wait_finish)(struct vb2_queue *q);
        int (*buf_init)(struct vb2_buffer *vb);
        int (*buf_prepare)(struct vb2_buffer *vb);
        void (*buf_finish)(struct vb2_buffer *vb);
        void (*buf_cleanup)(struct vb2_buffer *vb);
        int (*start_streaming)(struct vb2_queue *q, unsigned int count);
        void (*stop_streaming)(struct vb2_queue *q);
        void (*buf_queue)(struct vb2_buffer *vb);
    }

.. _`vb2_ops.members`:

Members
-------

queue_setup
    called from \ :c:func:`VIDIOC_REQBUFS`\  and \ :c:func:`VIDIOC_CREATE_BUFS`\ 
    handlers before memory allocation. It can be called
    twice: if the original number of requested buffers
    could not be allocated, then it will be called a
    second time with the actually allocated number of
    buffers to verify if that is OK.
    The driver should return the required number of buffers
    in \*num_buffers, the required number of planes per
    buffer in \*num_planes, the size of each plane should be
    set in the sizes\[\] array and optional per-plane
    allocator specific device in the alloc_devs\[\] array.
    When called from \ :c:func:`VIDIOC_REQBUFS`\ , \*num_planes == 0,
    the driver has to use the currently configured format to
    determine the plane sizes and \*num_buffers is the total
    number of buffers that are being allocated. When called
    from \ :c:func:`VIDIOC_CREATE_BUFS`\ , \*num_planes != 0 and it
    describes the requested number of planes and sizes\[\]
    contains the requested plane sizes. In this case
    \*num_buffers are being allocated additionally to
    q->num_buffers. If either \*num_planes or the requested
    sizes are invalid callback must return \ ``-EINVAL``\ .

wait_prepare
    release any locks taken while calling vb2 functions;
    it is called before an ioctl needs to wait for a new
    buffer to arrive; required to avoid a deadlock in
    blocking access type.

wait_finish
    reacquire all locks released in the previous callback;
    required to continue operation after sleeping while
    waiting for a new buffer to arrive.

buf_init
    called once after allocating a buffer (in MMAP case)
    or after acquiring a new USERPTR buffer; drivers may
    perform additional buffer-related initialization;
    initialization failure (return != 0) will prevent
    queue setup from completing successfully; optional.

buf_prepare
    called every time the buffer is queued from userspace
    and from the \ :c:func:`VIDIOC_PREPARE_BUF`\  ioctl; drivers may
    perform any initialization required before each
    hardware operation in this callback; drivers can
    access/modify the buffer here as it is still synced for
    the CPU; drivers that support \ :c:func:`VIDIOC_CREATE_BUFS`\  must
    also validate the buffer size; if an error is returned,
    the buffer will not be queued in driver; optional.

buf_finish
    called before every dequeue of the buffer back to
    userspace; the buffer is synced for the CPU, so drivers
    can access/modify the buffer contents; drivers may
    perform any operations required before userspace
    accesses the buffer; optional. The buffer state can be
    one of the following: \ ``DONE``\  and \ ``ERROR``\  occur while
    streaming is in progress, and the \ ``PREPARED``\  state occurs
    when the queue has been canceled and all pending
    buffers are being returned to their default \ ``DEQUEUED``\ 
    state. Typically you only have to do something if the
    state is \ ``VB2_BUF_STATE_DONE``\ , since in all other cases
    the buffer contents will be ignored anyway.

buf_cleanup
    called once before the buffer is freed; drivers may
    perform any additional cleanup; optional.

start_streaming
    called once to enter 'streaming' state; the driver may
    receive buffers with \ ``buf_queue``\  callback
    before \ ``start_streaming``\  is called; the driver gets the
    number of already queued buffers in count parameter;
    driver can return an error if hardware fails, in that
    case all buffers that have been already given by
    the \ ``buf_queue``\  callback are to be returned by the driver
    by calling \ :c:func:`vb2_buffer_done`\  with \ ``VB2_BUF_STATE_QUEUED``\ 
    or \ ``VB2_BUF_STATE_REQUEUEING``\ . If you need a minimum
    number of buffers before you can start streaming, then
    set \ :c:type:`vb2_queue->min_buffers_needed <vb2_queue>`\ . If that is non-zero
    then \ ``start_streaming``\  won't be called until at least
    that many buffers have been queued up by userspace.

stop_streaming
    called when 'streaming' state must be disabled; driver
    should stop any DMA transactions or wait until they
    finish and give back all buffers it got from \ :c:type:`struct buf_queue <buf_queue>`\ 
    callback by calling \ :c:func:`vb2_buffer_done`\  with either
    \ ``VB2_BUF_STATE_DONE``\  or \ ``VB2_BUF_STATE_ERROR``\ ; may use
    \ :c:func:`vb2_wait_for_all_buffers`\  function

buf_queue
    passes buffer vb to the driver; driver may start
    hardware operation on this buffer; driver should give
    the buffer back by calling \ :c:func:`vb2_buffer_done`\  function;
    it is allways called after calling \ :c:func:`VIDIOC_STREAMON`\ 
    ioctl; might be called before \ ``start_streaming``\  callback
    if user pre-queued buffers before calling
    \ :c:func:`VIDIOC_STREAMON`\ .

.. _`vb2_ops.description`:

Description
-----------

These operations are not called from interrupt context except where
mentioned specifically.

.. _`vb2_buf_ops`:

struct vb2_buf_ops
==================

.. c:type:: struct vb2_buf_ops

    driver-specific callbacks.

.. _`vb2_buf_ops.definition`:

Definition
----------

.. code-block:: c

    struct vb2_buf_ops {
        int (*verify_planes_array)(struct vb2_buffer *vb, const void *pb);
        void (*fill_user_buffer)(struct vb2_buffer *vb, void *pb);
        int (*fill_vb2_buffer)(struct vb2_buffer *vb, const void *pb, struct vb2_plane *planes);
        void (*copy_timestamp)(struct vb2_buffer *vb, const void *pb);
    }

.. _`vb2_buf_ops.members`:

Members
-------

verify_planes_array
    Verify that a given user space structure contains
    enough planes for the buffer. This is called
    for each dequeued buffer.

fill_user_buffer
    given a \ :c:type:`struct vb2_buffer <vb2_buffer>`\  fill in the userspace structure.
    For V4L2 this is a \ :c:type:`struct v4l2_buffer <v4l2_buffer>`\ .

fill_vb2_buffer
    given a userspace structure, fill in the \ :c:type:`struct vb2_buffer <vb2_buffer>`\ .
    If the userspace structure is invalid, then this op
    will return an error.

copy_timestamp
    copy the timestamp from a userspace structure to
    the \ :c:type:`struct vb2_buffer <vb2_buffer>`\ .

.. _`vb2_plane_vaddr`:

vb2_plane_vaddr
===============

.. c:function:: void *vb2_plane_vaddr(struct vb2_buffer *vb, unsigned int plane_no)

    Return a kernel virtual address of a given plane.

    :param struct vb2_buffer \*vb:
        pointer to \ :c:type:`struct vb2_buffer <vb2_buffer>`\  to which the plane in
        question belongs to.

    :param unsigned int plane_no:
        plane number for which the address is to be returned.

.. _`vb2_plane_vaddr.description`:

Description
-----------

This function returns a kernel virtual address of a given plane if
such a mapping exist, NULL otherwise.

.. _`vb2_plane_cookie`:

vb2_plane_cookie
================

.. c:function:: void *vb2_plane_cookie(struct vb2_buffer *vb, unsigned int plane_no)

    Return allocator specific cookie for the given plane.

    :param struct vb2_buffer \*vb:
        pointer to \ :c:type:`struct vb2_buffer <vb2_buffer>`\  to which the plane in
        question belongs to.

    :param unsigned int plane_no:
        plane number for which the cookie is to be returned.

.. _`vb2_plane_cookie.description`:

Description
-----------

This function returns an allocator specific cookie for a given plane if
available, NULL otherwise. The allocator should provide some simple static
inline function, which would convert this cookie to the allocator specific
type that can be used directly by the driver to access the buffer. This can
be for example physical address, pointer to scatter list or IOMMU mapping.

.. _`vb2_buffer_done`:

vb2_buffer_done
===============

.. c:function:: void vb2_buffer_done(struct vb2_buffer *vb, enum vb2_buffer_state state)

    inform videobuf that an operation on a buffer is finished.

    :param struct vb2_buffer \*vb:
        pointer to \ :c:type:`struct vb2_buffer <vb2_buffer>`\  to be used.

    :param enum vb2_buffer_state state:
        state of the buffer, as defined by \ :c:type:`enum vb2_buffer_state <vb2_buffer_state>`\ .
        Either \ ``VB2_BUF_STATE_DONE``\  if the operation finished
        successfully, \ ``VB2_BUF_STATE_ERROR``\  if the operation finished
        with an error or any of \ ``VB2_BUF_STATE_QUEUED``\  or
        \ ``VB2_BUF_STATE_REQUEUEING``\  if the driver wants to
        requeue buffers (see below).

.. _`vb2_buffer_done.description`:

Description
-----------

This function should be called by the driver after a hardware operation on
a buffer is finished and the buffer may be returned to userspace. The driver
cannot use this buffer anymore until it is queued back to it by videobuf
by the means of \ :c:type:`vb2_ops->buf_queue <vb2_ops>`\  callback. Only buffers previously queued
to the driver by \ :c:type:`vb2_ops->buf_queue <vb2_ops>`\  can be passed to this function.

While streaming a buffer can only be returned in state DONE or ERROR.
The \ :c:type:`vb2_ops->start_streaming <vb2_ops>`\  op can also return them in case the DMA engine
cannot be started for some reason. In that case the buffers should be
returned with state QUEUED or REQUEUEING to put them back into the queue.

\ ``VB2_BUF_STATE_REQUEUEING``\  is like \ ``VB2_BUF_STATE_QUEUED``\ , but it also calls
\ :c:type:`vb2_ops->buf_queue <vb2_ops>`\  to queue buffers back to the driver. Note that calling
vb2_buffer_done(..., VB2_BUF_STATE_REQUEUEING) from interrupt context will
result in \ :c:type:`vb2_ops->buf_queue <vb2_ops>`\  being called in interrupt context as well.

.. _`vb2_discard_done`:

vb2_discard_done
================

.. c:function:: void vb2_discard_done(struct vb2_queue *q)

    discard all buffers marked as DONE.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

.. _`vb2_discard_done.description`:

Description
-----------

This function is intended to be used with suspend/resume operations. It
discards all 'done' buffers as they would be too old to be requested after
resume.

Drivers must stop the hardware and synchronize with interrupt handlers and/or
delayed works before calling this function to make sure no buffer will be
touched by the driver and/or hardware.

.. _`vb2_wait_for_all_buffers`:

vb2_wait_for_all_buffers
========================

.. c:function:: int vb2_wait_for_all_buffers(struct vb2_queue *q)

    wait until all buffers are given back to vb2.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

.. _`vb2_wait_for_all_buffers.description`:

Description
-----------

This function will wait until all buffers that have been given to the driver
by \ :c:type:`vb2_ops->buf_queue <vb2_ops>`\  are given back to vb2 with \ :c:func:`vb2_buffer_done`\ . It
doesn't call \ :c:type:`vb2_ops->wait_prepare <vb2_ops>`\ /&vb2_ops->wait_finish pair.
It is intended to be called with all locks taken, for example from
\ :c:type:`vb2_ops->stop_streaming <vb2_ops>`\  callback.

.. _`vb2_core_querybuf`:

vb2_core_querybuf
=================

.. c:function:: void vb2_core_querybuf(struct vb2_queue *q, unsigned int index, void *pb)

    query video buffer information.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param unsigned int index:
        id number of the buffer.

    :param void \*pb:
        buffer struct passed from userspace.

.. _`vb2_core_querybuf.description`:

Description
-----------

Videobuf2 core helper to implement \ :c:func:`VIDIOC_QUERYBUF`\  operation. It is called
internally by VB2 by an API-specific handler, like ``videobuf2-v4l2.h``.

The passed buffer should have been verified.

This function fills the relevant information for the userspace.

.. _`vb2_core_querybuf.return`:

Return
------

returns zero on success; an error code otherwise.

.. _`vb2_core_reqbufs`:

vb2_core_reqbufs
================

.. c:function:: int vb2_core_reqbufs(struct vb2_queue *q, enum vb2_memory memory, unsigned int *count)

    Initiate streaming.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param enum vb2_memory memory:
        memory type, as defined by \ :c:type:`enum vb2_memory <vb2_memory>`\ .

    :param unsigned int \*count:
        requested buffer count.

.. _`vb2_core_reqbufs.description`:

Description
-----------

Videobuf2 core helper to implement \ :c:func:`VIDIOC_REQBUF`\  operation. It is called
internally by VB2 by an API-specific handler, like ``videobuf2-v4l2.h``.

.. _`vb2_core_reqbufs.this-function`:

This function
-------------


#) verifies streaming parameters passed from the userspace;
#) sets up the queue;
#) negotiates number of buffers and planes per buffer with the driver
   to be used during streaming;
#) allocates internal buffer structures (&struct vb2_buffer), according to
   the agreed parameters;
#) for MMAP memory type, allocates actual video memory, using the
   memory handling/allocation routines provided during queue initialization.

If req->count is 0, all the memory will be freed instead.

If the queue has been allocated previously by a previous \ :c:func:`vb2_core_reqbufs`\ 
call and the queue is not busy, memory will be reallocated.

.. _`vb2_core_reqbufs.return`:

Return
------

returns zero on success; an error code otherwise.

.. _`vb2_core_create_bufs`:

vb2_core_create_bufs
====================

.. c:function:: int vb2_core_create_bufs(struct vb2_queue *q, enum vb2_memory memory, unsigned int *count, unsigned int requested_planes, const unsigned int requested_sizes)

    Allocate buffers and any required auxiliary structs

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param enum vb2_memory memory:
        memory type, as defined by \ :c:type:`enum vb2_memory <vb2_memory>`\ .

    :param unsigned int \*count:
        requested buffer count.

    :param unsigned int requested_planes:
        number of planes requested.

    :param const unsigned int requested_sizes:
        array with the size of the planes.

.. _`vb2_core_create_bufs.description`:

Description
-----------

Videobuf2 core helper to implement \ :c:func:`VIDIOC_CREATE_BUFS`\  operation. It is
called internally by VB2 by an API-specific handler, like
``videobuf2-v4l2.h``.

.. _`vb2_core_create_bufs.this-function`:

This function
-------------


#) verifies parameter sanity;
#) calls the \ :c:type:`vb2_ops->queue_setup <vb2_ops>`\  queue operation;
#) performs any necessary memory allocations.

.. _`vb2_core_create_bufs.return`:

Return
------

returns zero on success; an error code otherwise.

.. _`vb2_core_prepare_buf`:

vb2_core_prepare_buf
====================

.. c:function:: int vb2_core_prepare_buf(struct vb2_queue *q, unsigned int index, void *pb)

    Pass ownership of a buffer from userspace to the kernel.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param unsigned int index:
        id number of the buffer.

    :param void \*pb:
        buffer structure passed from userspace to
        \ :c:type:`v4l2_ioctl_ops->vidioc_prepare_buf <v4l2_ioctl_ops>`\  handler in driver.

.. _`vb2_core_prepare_buf.description`:

Description
-----------

Videobuf2 core helper to implement \ :c:func:`VIDIOC_PREPARE_BUF`\  operation. It is
called internally by VB2 by an API-specific handler, like
``videobuf2-v4l2.h``.

The passed buffer should have been verified.

This function calls vb2_ops->buf_prepare callback in the driver
(if provided), in which driver-specific buffer initialization can
be performed.

.. _`vb2_core_prepare_buf.return`:

Return
------

returns zero on success; an error code otherwise.

.. _`vb2_core_qbuf`:

vb2_core_qbuf
=============

.. c:function:: int vb2_core_qbuf(struct vb2_queue *q, unsigned int index, void *pb)

    Queue a buffer from userspace

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param unsigned int index:
        id number of the buffer

    :param void \*pb:
        buffer structure passed from userspace to
        v4l2_ioctl_ops->vidioc_qbuf handler in driver

.. _`vb2_core_qbuf.description`:

Description
-----------

Videobuf2 core helper to implement \ :c:func:`VIDIOC_QBUF`\  operation. It is called
internally by VB2 by an API-specific handler, like ``videobuf2-v4l2.h``.

.. _`vb2_core_qbuf.this-function`:

This function
-------------


#) if necessary, calls \ :c:type:`vb2_ops->buf_prepare <vb2_ops>`\  callback in the driver
   (if provided), in which driver-specific buffer initialization can
   be performed;
#) if streaming is on, queues the buffer in driver by the means of
   \ :c:type:`vb2_ops->buf_queue <vb2_ops>`\  callback for processing.

.. _`vb2_core_qbuf.return`:

Return
------

returns zero on success; an error code otherwise.

.. _`vb2_core_dqbuf`:

vb2_core_dqbuf
==============

.. c:function:: int vb2_core_dqbuf(struct vb2_queue *q, unsigned int *pindex, void *pb, bool nonblocking)

    Dequeue a buffer to the userspace

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue

    :param unsigned int \*pindex:
        pointer to the buffer index. May be NULL

    :param void \*pb:
        buffer structure passed from userspace to
        v4l2_ioctl_ops->vidioc_dqbuf handler in driver.

    :param bool nonblocking:
        if true, this call will not sleep waiting for a buffer if no
        buffers ready for dequeuing are present. Normally the driver
        would be passing (file->f_flags & O_NONBLOCK) here.

.. _`vb2_core_dqbuf.description`:

Description
-----------

Videobuf2 core helper to implement \ :c:func:`VIDIOC_DQBUF`\  operation. It is called
internally by VB2 by an API-specific handler, like ``videobuf2-v4l2.h``.

.. _`vb2_core_dqbuf.this-function`:

This function
-------------


#) calls buf_finish callback in the driver (if provided), in which
   driver can perform any additional operations that may be required before
   returning the buffer to userspace, such as cache sync,
#) the buffer struct members are filled with relevant information for
   the userspace.

.. _`vb2_core_dqbuf.return`:

Return
------

returns zero on success; an error code otherwise.

.. _`vb2_core_streamon`:

vb2_core_streamon
=================

.. c:function:: int vb2_core_streamon(struct vb2_queue *q, unsigned int type)

    Implements VB2 stream ON logic

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue

    :param unsigned int type:
        type of the queue to be started.
        For V4L2, this is defined by \ :c:type:`enum v4l2_buf_type <v4l2_buf_type>`\  type.

.. _`vb2_core_streamon.description`:

Description
-----------

Videobuf2 core helper to implement \ :c:func:`VIDIOC_STREAMON`\  operation. It is called
internally by VB2 by an API-specific handler, like ``videobuf2-v4l2.h``.

.. _`vb2_core_streamon.return`:

Return
------

returns zero on success; an error code otherwise.

.. _`vb2_core_streamoff`:

vb2_core_streamoff
==================

.. c:function:: int vb2_core_streamoff(struct vb2_queue *q, unsigned int type)

    Implements VB2 stream OFF logic

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue

    :param unsigned int type:
        type of the queue to be started.
        For V4L2, this is defined by \ :c:type:`enum v4l2_buf_type <v4l2_buf_type>`\  type.

.. _`vb2_core_streamoff.description`:

Description
-----------

Videobuf2 core helper to implement \ :c:func:`VIDIOC_STREAMOFF`\  operation. It is
called internally by VB2 by an API-specific handler, like
``videobuf2-v4l2.h``.

.. _`vb2_core_streamoff.return`:

Return
------

returns zero on success; an error code otherwise.

.. _`vb2_core_expbuf`:

vb2_core_expbuf
===============

.. c:function:: int vb2_core_expbuf(struct vb2_queue *q, int *fd, unsigned int type, unsigned int index, unsigned int plane, unsigned int flags)

    Export a buffer as a file descriptor.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param int \*fd:
        pointer to the file descriptor associated with DMABUF
        (set by driver).

    :param unsigned int type:
        buffer type.

    :param unsigned int index:
        id number of the buffer.

    :param unsigned int plane:
        index of the plane to be exported, 0 for single plane queues

    :param unsigned int flags:
        file flags for newly created file, as defined at
        include/uapi/asm-generic/fcntl.h.
        Currently, the only used flag is \ ``O_CLOEXEC``\ .
        is supported, refer to manual of open syscall for more details.

.. _`vb2_core_expbuf.description`:

Description
-----------


Videobuf2 core helper to implement \ :c:func:`VIDIOC_EXPBUF`\  operation. It is called
internally by VB2 by an API-specific handler, like ``videobuf2-v4l2.h``.

.. _`vb2_core_expbuf.return`:

Return
------

returns zero on success; an error code otherwise.

.. _`vb2_core_queue_init`:

vb2_core_queue_init
===================

.. c:function:: int vb2_core_queue_init(struct vb2_queue *q)

    initialize a videobuf2 queue

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.
        This structure should be allocated in driver

.. _`vb2_core_queue_init.description`:

Description
-----------

The \ :c:type:`struct vb2_queue <vb2_queue>`\  structure should be allocated by the driver. The driver is
responsible of clearing it's content and setting initial values for some
required entries before calling this function.

.. note::

   The following fields at @q should be set before calling this function:
   &vb2_queue->ops, &vb2_queue->mem_ops, &vb2_queue->type.

.. _`vb2_core_queue_release`:

vb2_core_queue_release
======================

.. c:function:: void vb2_core_queue_release(struct vb2_queue *q)

    stop streaming, release the queue and free memory

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

.. _`vb2_core_queue_release.description`:

Description
-----------

This function stops streaming and performs necessary clean ups, including
freeing video buffer memory. The driver is responsible for freeing
the \ :c:type:`struct vb2_queue <vb2_queue>`\  itself.

.. _`vb2_queue_error`:

vb2_queue_error
===============

.. c:function:: void vb2_queue_error(struct vb2_queue *q)

    signal a fatal error on the queue

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

.. _`vb2_queue_error.description`:

Description
-----------

Flag that a fatal unrecoverable error has occurred and wake up all processes
waiting on the queue. Polling will now set \ ``EPOLLERR``\  and queuing and dequeuing
buffers will return \ ``-EIO``\ .

The error flag will be cleared when canceling the queue, either from
\ :c:func:`vb2_streamoff`\  or \ :c:func:`vb2_queue_release`\ . Drivers should thus not call this
function before starting the stream, otherwise the error flag will remain set
until the queue is released when closing the device node.

.. _`vb2_mmap`:

vb2_mmap
========

.. c:function:: int vb2_mmap(struct vb2_queue *q, struct vm_area_struct *vma)

    map video buffers into application address space.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param struct vm_area_struct \*vma:
        pointer to \ :c:type:`struct vm_area_struct <vm_area_struct>`\  with the vma passed
        to the mmap file operation handler in the driver.

.. _`vb2_mmap.description`:

Description
-----------

Should be called from mmap file operation handler of a driver.
This function maps one plane of one of the available video buffers to
userspace. To map whole video memory allocated on reqbufs, this function
has to be called once per each plane per each buffer previously allocated.

When the userspace application calls mmap, it passes to it an offset returned
to it earlier by the means of \ :c:type:`v4l2_ioctl_ops->vidioc_querybuf <v4l2_ioctl_ops>`\  handler.
That offset acts as a "cookie", which is then used to identify the plane
to be mapped.

This function finds a plane with a matching offset and a mapping is performed
by the means of a provided memory operation.

The return values from this function are intended to be directly returned
from the mmap handler in driver.

.. _`vb2_get_unmapped_area`:

vb2_get_unmapped_area
=====================

.. c:function:: unsigned long vb2_get_unmapped_area(struct vb2_queue *q, unsigned long addr, unsigned long len, unsigned long pgoff, unsigned long flags)

    map video buffers into application address space.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param unsigned long addr:
        memory address.

    :param unsigned long len:
        buffer size.

    :param unsigned long pgoff:
        page offset.

    :param unsigned long flags:
        memory flags.

.. _`vb2_get_unmapped_area.description`:

Description
-----------

This function is used in noMMU platforms to propose address mapping
for a given buffer. It's intended to be used as a handler for the
\ :c:type:`file_operations->get_unmapped_area <file_operations>`\  operation.

This is called by the \ :c:func:`mmap`\  syscall routines will call this
to get a proposed address for the mapping, when ``!CONFIG_MMU``.

.. _`vb2_core_poll`:

vb2_core_poll
=============

.. c:function:: __poll_t vb2_core_poll(struct vb2_queue *q, struct file *file, poll_table *wait)

    implements poll \ :c:func:`syscall`\  logic.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param struct file \*file:
        \ :c:type:`struct file <file>`\  argument passed to the poll
        file operation handler.

    :param poll_table \*wait:
        \ :c:type:`struct poll_table <poll_table>`\  wait argument passed to the poll
        file operation handler.

.. _`vb2_core_poll.description`:

Description
-----------

This function implements poll file operation handler for a driver.
For CAPTURE queues, if a buffer is ready to be dequeued, the userspace will
be informed that the file descriptor of a video device is available for
reading.
For OUTPUT queues, if a buffer is ready to be dequeued, the file descriptor
will be reported as available for writing.

The return values from this function are intended to be directly returned
from poll handler in driver.

.. _`vb2_read`:

vb2_read
========

.. c:function:: size_t vb2_read(struct vb2_queue *q, char __user *data, size_t count, loff_t *ppos, int nonblock)

    implements \ :c:func:`read`\  syscall logic.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param char __user \*data:
        pointed to target userspace buffer

    :param size_t count:
        number of bytes to read

    :param loff_t \*ppos:
        file handle position tracking pointer

    :param int nonblock:
        mode selector (1 means blocking calls, 0 means nonblocking)

.. _`vb2_write`:

vb2_write
=========

.. c:function:: size_t vb2_write(struct vb2_queue *q, const char __user *data, size_t count, loff_t *ppos, int nonblock)

    implements \ :c:func:`write`\  syscall logic.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param const char __user \*data:
        pointed to target userspace buffer

    :param size_t count:
        number of bytes to write

    :param loff_t \*ppos:
        file handle position tracking pointer

    :param int nonblock:
        mode selector (1 means blocking calls, 0 means nonblocking)

.. _`vb2_thread_fnc`:

vb2_thread_fnc
==============

.. c:function:: int vb2_thread_fnc(struct vb2_buffer *vb, void *priv)

    callback function for use with vb2_thread.

    :param struct vb2_buffer \*vb:
        pointer to struct \ :c:type:`struct vb2_buffer <vb2_buffer>`\ .

    :param void \*priv:
        pointer to a private data.

.. _`vb2_thread_fnc.description`:

Description
-----------

This is called whenever a buffer is dequeued in the thread.

.. _`vb2_thread_start`:

vb2_thread_start
================

.. c:function:: int vb2_thread_start(struct vb2_queue *q, vb2_thread_fnc fnc, void *priv, const char *thread_name)

    start a thread for the given queue.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param vb2_thread_fnc fnc:
        \ :c:type:`struct vb2_thread_fnc <vb2_thread_fnc>`\  callback function.

    :param void \*priv:
        priv pointer passed to the callback function.

    :param const char \*thread_name:
        the name of the thread. This will be prefixed with "vb2-".

.. _`vb2_thread_start.description`:

Description
-----------

This starts a thread that will queue and dequeue until an error occurs
or \ :c:func:`vb2_thread_stop`\  is called.

.. attention::

  This function should not be used for anything else but the videobuf2-dvb
  support. If you think you have another good use-case for this, then please
  contact the linux-media mailing list first.

.. _`vb2_thread_stop`:

vb2_thread_stop
===============

.. c:function:: int vb2_thread_stop(struct vb2_queue *q)

    stop the thread for the given queue.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

.. _`vb2_is_streaming`:

vb2_is_streaming
================

.. c:function:: bool vb2_is_streaming(struct vb2_queue *q)

    return streaming status of the queue.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

.. _`vb2_fileio_is_active`:

vb2_fileio_is_active
====================

.. c:function:: bool vb2_fileio_is_active(struct vb2_queue *q)

    return true if fileio is active.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

.. _`vb2_fileio_is_active.description`:

Description
-----------

This returns true if \ :c:func:`read`\  or \ :c:func:`write`\  is used to stream the data
as opposed to stream I/O. This is almost never an important distinction,
except in rare cases. One such case is that using \ :c:func:`read`\  or \ :c:func:`write`\  to
stream a format using \ ``V4L2_FIELD_ALTERNATE``\  is not allowed since there
is no way you can pass the field information of each buffer to/from
userspace. A driver that supports this field format should check for
this in the \ :c:type:`vb2_ops->queue_setup <vb2_ops>`\  op and reject it if this function returns
true.

.. _`vb2_is_busy`:

vb2_is_busy
===========

.. c:function:: bool vb2_is_busy(struct vb2_queue *q)

    return busy status of the queue.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

.. _`vb2_is_busy.description`:

Description
-----------

This function checks if queue has any buffers allocated.

.. _`vb2_get_drv_priv`:

vb2_get_drv_priv
================

.. c:function:: void *vb2_get_drv_priv(struct vb2_queue *q)

    return driver private data associated with the queue.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

.. _`vb2_set_plane_payload`:

vb2_set_plane_payload
=====================

.. c:function:: void vb2_set_plane_payload(struct vb2_buffer *vb, unsigned int plane_no, unsigned long size)

    set bytesused for the plane \ ``plane_no``\ .

    :param struct vb2_buffer \*vb:
        pointer to \ :c:type:`struct vb2_buffer <vb2_buffer>`\  to which the plane in
        question belongs to.

    :param unsigned int plane_no:
        plane number for which payload should be set.

    :param unsigned long size:
        payload in bytes.

.. _`vb2_get_plane_payload`:

vb2_get_plane_payload
=====================

.. c:function:: unsigned long vb2_get_plane_payload(struct vb2_buffer *vb, unsigned int plane_no)

    get bytesused for the plane plane_no

    :param struct vb2_buffer \*vb:
        pointer to \ :c:type:`struct vb2_buffer <vb2_buffer>`\  to which the plane in
        question belongs to.

    :param unsigned int plane_no:
        plane number for which payload should be set.

.. _`vb2_plane_size`:

vb2_plane_size
==============

.. c:function:: unsigned long vb2_plane_size(struct vb2_buffer *vb, unsigned int plane_no)

    return plane size in bytes.

    :param struct vb2_buffer \*vb:
        pointer to \ :c:type:`struct vb2_buffer <vb2_buffer>`\  to which the plane in
        question belongs to.

    :param unsigned int plane_no:
        plane number for which size should be returned.

.. _`vb2_start_streaming_called`:

vb2_start_streaming_called
==========================

.. c:function:: bool vb2_start_streaming_called(struct vb2_queue *q)

    return streaming status of driver.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

.. _`vb2_clear_last_buffer_dequeued`:

vb2_clear_last_buffer_dequeued
==============================

.. c:function:: void vb2_clear_last_buffer_dequeued(struct vb2_queue *q)

    clear last buffer dequeued flag of queue.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

.. _`vb2_buffer_in_use`:

vb2_buffer_in_use
=================

.. c:function:: bool vb2_buffer_in_use(struct vb2_queue *q, struct vb2_buffer *vb)

    return true if the buffer is in use and the queue cannot be freed (by the means of VIDIOC_REQBUFS(0)) call.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param struct vb2_buffer \*vb:
        buffer for which plane size should be returned.

.. _`vb2_verify_memory_type`:

vb2_verify_memory_type
======================

.. c:function:: int vb2_verify_memory_type(struct vb2_queue *q, enum vb2_memory memory, unsigned int type)

    Check whether the memory type and buffer type passed to a buffer operation are compatible with the queue.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param enum vb2_memory memory:
        memory model, as defined by enum \ :c:type:`struct vb2_memory <vb2_memory>`\ .

    :param unsigned int type:
        private buffer type whose content is defined by the vb2-core
        caller. For example, for V4L2, it should match
        the types defined on enum \ :c:type:`struct v4l2_buf_type <v4l2_buf_type>`\ .

.. This file was automatic generated / don't edit.

