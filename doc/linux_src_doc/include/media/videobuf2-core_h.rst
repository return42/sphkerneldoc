.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/videobuf2-core.h

.. _`vb2_mem_ops`:

struct vb2_mem_ops
==================

.. c:type:: struct vb2_mem_ops

    memory handling/memory allocator operations

.. _`vb2_mem_ops.definition`:

Definition
----------

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
        unsigned int (* num_users) (void *buf_priv);
        int (* mmap) (void *buf_priv, struct vm_area_struct *vma);
    }

.. _`vb2_mem_ops.members`:

Members
-------

alloc
    allocate video memory and, optionally, allocator private data,
    return NULL on failure or a pointer to allocator private,
    per-buffer data on success; the returned private structure
    will then be passed as buf_priv argument to other ops in this
    structure. Additional gfp_flags to use when allocating the
    are also passed to this operation. These flags are from the
    gfp_flags field of vb2_queue.

put
    inform the allocator that the buffer will no longer be used;
    usually will result in the allocator freeing the buffer (if
    no other users of this buffer are present); the buf_priv
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
    associated with the buffer on success, NULL on failure;
    the returned private structure will then be passed as buf_priv
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
    attach a shared struct dma_buf for a hardware operation;
    used for DMABUF memory types; alloc_ctx is the alloc context
    dbuf is the shared dma_buf; returns NULL on failure;
    allocator private per-buffer structure on success;
    this needs to be used for further accesses to the buffer.

detach_dmabuf
    inform the exporter of the buffer that the current DMABUF
    buffer is no longer used; the buf_priv argument is the
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

.. _`vb2_mem_ops.required-ops-for-userptr-types`:

Required ops for USERPTR types
------------------------------

get_userptr, put_userptr.

.. _`vb2_mem_ops.required-ops-for-mmap-types`:

Required ops for MMAP types
---------------------------

alloc, put, num_users, mmap.
Required ops for read/write access types: alloc, put, num_users, vaddr.

.. _`vb2_mem_ops.required-ops-for-dmabuf-types`:

Required ops for DMABUF types
-----------------------------

attach_dmabuf, detach_dmabuf, map_dmabuf,
unmap_dmabuf.

.. _`vb2_plane`:

struct vb2_plane
================

.. c:type:: struct vb2_plane

    plane information

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
        union m;
        unsigned int data_offset;
    }

.. _`vb2_plane.members`:

Members
-------

mem_priv
    private data with this plane

dbuf
    dma_buf - shared buffer object

dbuf_mapped
    flag to show whether dbuf is mapped or not

bytesused
    number of bytes occupied by data in the plane (payload)

length
    size of this plane (NOT the payload) in bytes

min_length
    minimum required size of this plane (NOT the payload) in bytes.
    \ ``length``\  is always greater or equal to \ ``min_length``\ .

m
    Union with memtype-specific data (\ ``offset``\ , \ ``userptr``\  or
    \ ``fd``\ ).

data_offset
    offset in the plane to the start of data; usually 0,
    unless there is a header in front of the data
    Should contain enough information to be able to cover all the fields
    of struct v4l2_plane at videodev2.h

.. _`vb2_io_modes`:

enum vb2_io_modes
=================

.. c:type:: enum vb2_io_modes

    queue access methods

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
    driver supports MMAP with streaming API

VB2_USERPTR
    driver supports USERPTR with streaming API

VB2_READ
    driver supports \ :c:func:`read`\  style access

VB2_WRITE
    driver supports \ :c:func:`write`\  style access

VB2_DMABUF
    driver supports DMABUF with streaming API

.. _`vb2_buffer_state`:

enum vb2_buffer_state
=====================

.. c:type:: enum vb2_buffer_state

    current video buffer state

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
    buffer under userspace control

VB2_BUF_STATE_PREPARING
    buffer is being prepared in videobuf

VB2_BUF_STATE_PREPARED
    buffer prepared in videobuf and by the driver

VB2_BUF_STATE_QUEUED
    buffer queued in videobuf, but not in driver

VB2_BUF_STATE_REQUEUEING
    re-queue a buffer to the driver

VB2_BUF_STATE_ACTIVE
    buffer queued in driver and possibly used
    in a hardware operation

VB2_BUF_STATE_DONE
    buffer returned from driver to videobuf, but
    not yet dequeued to userspace

VB2_BUF_STATE_ERROR
    same as above, but the operation on the buffer
    has ended with an error, which will be reported
    to the userspace when it is dequeued

.. _`vb2_buffer`:

struct vb2_buffer
=================

.. c:type:: struct vb2_buffer

    represents a video buffer

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
        struct vb2_plane planes[VB2_MAX_PLANES];
        u64 timestamp;
    }

.. _`vb2_buffer.members`:

Members
-------

vb2_queue
    the queue to which this driver belongs

index
    id number of the buffer

type
    buffer type

memory
    the method, in which the actual data is passed

num_planes
    number of planes in the buffer
    on an internal driver queue

planes
    private per-plane information; do not change

timestamp
    frame timestamp in ns

.. _`vb2_ops`:

struct vb2_ops
==============

.. c:type:: struct vb2_ops

    driver-specific callbacks

.. _`vb2_ops.definition`:

Definition
----------

.. code-block:: c

    struct vb2_ops {
        int (* queue_setup) (struct vb2_queue *q,unsigned int *num_buffers, unsigned int *num_planes,unsigned int sizes[], void *alloc_ctxs[]);
        void (* wait_prepare) (struct vb2_queue *q);
        void (* wait_finish) (struct vb2_queue *q);
        int (* buf_init) (struct vb2_buffer *vb);
        int (* buf_prepare) (struct vb2_buffer *vb);
        void (* buf_finish) (struct vb2_buffer *vb);
        void (* buf_cleanup) (struct vb2_buffer *vb);
        int (* start_streaming) (struct vb2_queue *q, unsigned int count);
        void (* stop_streaming) (struct vb2_queue *q);
        void (* buf_queue) (struct vb2_buffer *vb);
    }

.. _`vb2_ops.members`:

Members
-------

queue_setup
    called from VIDIOC_REQBUFS and VIDIOC_CREATE_BUFS
    handlers before memory allocation. It can be called
    twice: if the original number of requested buffers
    could not be allocated, then it will be called a
    second time with the actually allocated number of
    buffers to verify if that is OK.
    The driver should return the required number of buffers
    in \*num_buffers, the required number of planes per
    buffer in \*num_planes, the size of each plane should be
    set in the sizes[] array and optional per-plane
    allocator specific context in the alloc_ctxs[] array.
    When called from VIDIOC_REQBUFS, \*num_planes == 0, the
    driver has to use the currently configured format to
    determine the plane sizes and \*num_buffers is the total
    number of buffers that are being allocated. When called
    from VIDIOC_CREATE_BUFS, \*num_planes != 0 and it
    describes the requested number of planes and sizes[]
    contains the requested plane sizes. If either
    \*num_planes or the requested sizes are invalid callback
    must return -EINVAL. In this case \*num_buffers are
    being allocated additionally to q->num_buffers.

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
    and from the VIDIOC_PREPARE_BUF ioctl; drivers may
    perform any initialization required before each
    hardware operation in this callback; drivers can
    access/modify the buffer here as it is still synced for
    the CPU; drivers that support VIDIOC_CREATE_BUFS must
    also validate the buffer size; if an error is returned,
    the buffer will not be queued in driver; optional.

buf_finish
    called before every dequeue of the buffer back to
    userspace; the buffer is synced for the CPU, so drivers
    can access/modify the buffer contents; drivers may
    perform any operations required before userspace
    accesses the buffer; optional. The buffer state can be
    one of the following: DONE and ERROR occur while
    streaming is in progress, and the PREPARED state occurs
    when the queue has been canceled and all pending
    buffers are being returned to their default DEQUEUED
    state. Typically you only have to do something if the
    state is VB2_BUF_STATE_DONE, since in all other cases
    the buffer contents will be ignored anyway.

buf_cleanup
    called once before the buffer is freed; drivers may
    perform any additional cleanup; optional.

start_streaming
    called once to enter 'streaming' state; the driver may
    receive buffers with \ ``buf_queue``\  callback before
    \ ``start_streaming``\  is called; the driver gets the number
    of already queued buffers in count parameter; driver
    can return an error if hardware fails, in that case all
    buffers that have been already given by the \ ``buf_queue``\ 
    callback are to be returned by the driver by calling
    \ ``vb2_buffer_done``\ (VB2_BUF_STATE_QUEUED).
    If you need a minimum number of buffers before you can
    start streaming, then set \ ``min_buffers_needed``\  in the
    vb2_queue structure. If that is non-zero then
    start_streaming won't be called until at least that
    many buffers have been queued up by userspace.

stop_streaming
    called when 'streaming' state must be disabled; driver
    should stop any DMA transactions or wait until they
    finish and give back all buffers it got from \ :c:func:`buf_queue`\ 
    callback by calling @\ :c:func:`vb2_buffer_done`\  with either
    VB2_BUF_STATE_DONE or VB2_BUF_STATE_ERROR; may use
    \ :c:func:`vb2_wait_for_all_buffers`\  function

buf_queue
    passes buffer vb to the driver; driver may start
    hardware operation on this buffer; driver should give
    the buffer back by calling \ :c:func:`vb2_buffer_done`\  function;
    it is allways called after calling STREAMON ioctl;
    might be called before start_streaming callback if user
    pre-queued buffers before calling STREAMON.

.. _`vb2_buf_ops`:

struct vb2_buf_ops
==================

.. c:type:: struct vb2_buf_ops

    driver-specific callbacks

.. _`vb2_buf_ops.definition`:

Definition
----------

.. code-block:: c

    struct vb2_buf_ops {
        int (* verify_planes_array) (struct vb2_buffer *vb, const void *pb);
        void (* fill_user_buffer) (struct vb2_buffer *vb, void *pb);
        int (* fill_vb2_buffer) (struct vb2_buffer *vb, const void *pb,struct vb2_plane *planes);
        void (* copy_timestamp) (struct vb2_buffer *vb, const void *pb);
    }

.. _`vb2_buf_ops.members`:

Members
-------

verify_planes_array
    Verify that a given user space structure contains
    enough planes for the buffer. This is called
    for each dequeued buffer.

fill_user_buffer
    given a vb2_buffer fill in the userspace structure.
    For V4L2 this is a struct v4l2_buffer.

fill_vb2_buffer
    given a userspace structure, fill in the vb2_buffer.
    If the userspace structure is invalid, then this op
    will return an error.

copy_timestamp
    copy the timestamp from a userspace structure to
    the vb2_buffer struct.

.. _`vb2_thread_start`:

vb2_thread_start
================

.. c:function:: int vb2_thread_start(struct vb2_queue *q, vb2_thread_fnc fnc, void *priv, const char *thread_name)

    start a thread for the given queue.

    :param struct vb2_queue \*q:
        videobuf queue

    :param vb2_thread_fnc fnc:
        callback function

    :param void \*priv:
        priv pointer passed to the callback function

    :param const char \*thread_name:
        the name of the thread. This will be prefixed with "vb2-".

.. _`vb2_thread_start.description`:

Description
-----------

This starts a thread that will queue and dequeue until an error occurs
or \ ``vb2_thread_stop``\  is called.

This function should not be used for anything else but the videobuf2-dvb
support. If you think you have another good use-case for this, then please
contact the linux-media mailinglist first.

.. _`vb2_thread_stop`:

vb2_thread_stop
===============

.. c:function:: int vb2_thread_stop(struct vb2_queue *q)

    stop the thread for the given queue.

    :param struct vb2_queue \*q:
        videobuf queue

.. _`vb2_is_streaming`:

vb2_is_streaming
================

.. c:function:: bool vb2_is_streaming(struct vb2_queue *q)

    return streaming status of the queue

    :param struct vb2_queue \*q:
        videobuf queue

.. _`vb2_fileio_is_active`:

vb2_fileio_is_active
====================

.. c:function:: bool vb2_fileio_is_active(struct vb2_queue *q)

    return true if fileio is active.

    :param struct vb2_queue \*q:
        videobuf queue

.. _`vb2_fileio_is_active.description`:

Description
-----------

This returns true if \ :c:func:`read`\  or \ :c:func:`write`\  is used to stream the data
as opposed to stream I/O. This is almost never an important distinction,
except in rare cases. One such case is that using \ :c:func:`read`\  or \ :c:func:`write`\  to
stream a format using V4L2_FIELD_ALTERNATE is not allowed since there
is no way you can pass the field information of each buffer to/from
userspace. A driver that supports this field format should check for
this in the queue_setup op and reject it if this function returns true.

.. _`vb2_is_busy`:

vb2_is_busy
===========

.. c:function:: bool vb2_is_busy(struct vb2_queue *q)

    return busy status of the queue

    :param struct vb2_queue \*q:
        videobuf queue

.. _`vb2_is_busy.description`:

Description
-----------

This function checks if queue has any buffers allocated.

.. _`vb2_get_drv_priv`:

vb2_get_drv_priv
================

.. c:function:: void *vb2_get_drv_priv(struct vb2_queue *q)

    return driver private data associated with the queue

    :param struct vb2_queue \*q:
        videobuf queue

.. _`vb2_set_plane_payload`:

vb2_set_plane_payload
=====================

.. c:function:: void vb2_set_plane_payload(struct vb2_buffer *vb, unsigned int plane_no, unsigned long size)

    set bytesused for the plane plane_no

    :param struct vb2_buffer \*vb:
        buffer for which plane payload should be set

    :param unsigned int plane_no:
        plane number for which payload should be set

    :param unsigned long size:
        payload in bytes

.. _`vb2_get_plane_payload`:

vb2_get_plane_payload
=====================

.. c:function:: unsigned long vb2_get_plane_payload(struct vb2_buffer *vb, unsigned int plane_no)

    get bytesused for the plane plane_no

    :param struct vb2_buffer \*vb:
        buffer for which plane payload should be set

    :param unsigned int plane_no:
        plane number for which payload should be set

.. _`vb2_plane_size`:

vb2_plane_size
==============

.. c:function:: unsigned long vb2_plane_size(struct vb2_buffer *vb, unsigned int plane_no)

    return plane size in bytes

    :param struct vb2_buffer \*vb:
        buffer for which plane size should be returned

    :param unsigned int plane_no:
        plane number for which size should be returned

.. _`vb2_start_streaming_called`:

vb2_start_streaming_called
==========================

.. c:function:: bool vb2_start_streaming_called(struct vb2_queue *q)

    return streaming status of driver

    :param struct vb2_queue \*q:
        videobuf queue

.. _`vb2_clear_last_buffer_dequeued`:

vb2_clear_last_buffer_dequeued
==============================

.. c:function:: void vb2_clear_last_buffer_dequeued(struct vb2_queue *q)

    clear last buffer dequeued flag of queue

    :param struct vb2_queue \*q:
        videobuf queue

.. This file was automatic generated / don't edit.

