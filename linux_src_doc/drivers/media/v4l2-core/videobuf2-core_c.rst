.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/v4l2-core/videobuf2-core.c

.. _`__vb2_buf_mem_alloc`:

__vb2_buf_mem_alloc
===================

.. c:function:: int __vb2_buf_mem_alloc(struct vb2_buffer *vb)

    allocate video memory for the given buffer

    :param struct vb2_buffer \*vb:
        *undescribed*

.. _`__vb2_buf_mem_free`:

__vb2_buf_mem_free
==================

.. c:function:: void __vb2_buf_mem_free(struct vb2_buffer *vb)

    free memory of the given buffer

    :param struct vb2_buffer \*vb:
        *undescribed*

.. _`__vb2_buf_userptr_put`:

__vb2_buf_userptr_put
=====================

.. c:function:: void __vb2_buf_userptr_put(struct vb2_buffer *vb)

    release userspace memory associated with a USERPTR buffer

    :param struct vb2_buffer \*vb:
        *undescribed*

.. _`__vb2_plane_dmabuf_put`:

__vb2_plane_dmabuf_put
======================

.. c:function:: void __vb2_plane_dmabuf_put(struct vb2_buffer *vb, struct vb2_plane *p)

    release memory associated with a DMABUF shared plane

    :param struct vb2_buffer \*vb:
        *undescribed*

    :param struct vb2_plane \*p:
        *undescribed*

.. _`__vb2_buf_dmabuf_put`:

__vb2_buf_dmabuf_put
====================

.. c:function:: void __vb2_buf_dmabuf_put(struct vb2_buffer *vb)

    release memory associated with a DMABUF shared buffer

    :param struct vb2_buffer \*vb:
        *undescribed*

.. _`__setup_offsets`:

__setup_offsets
===============

.. c:function:: void __setup_offsets(struct vb2_buffer *vb)

    setup unique offsets ("cookies") for every plane in the buffer.

    :param struct vb2_buffer \*vb:
        *undescribed*

.. _`__vb2_queue_alloc`:

__vb2_queue_alloc
=================

.. c:function:: int __vb2_queue_alloc(struct vb2_queue *q, enum vb2_memory memory, unsigned int num_buffers, unsigned int num_planes, const unsigned plane_sizes)

    allocate videobuf buffer structures and (for MMAP type) video buffer memory for all buffers/planes on the queue and initializes the queue

    :param struct vb2_queue \*q:
        *undescribed*

    :param enum vb2_memory memory:
        *undescribed*

    :param unsigned int num_buffers:
        *undescribed*

    :param unsigned int num_planes:
        *undescribed*

    :param const unsigned plane_sizes:
        *undescribed*

.. _`__vb2_queue_alloc.description`:

Description
-----------

Returns the number of buffers successfully allocated.

.. _`__vb2_free_mem`:

__vb2_free_mem
==============

.. c:function:: void __vb2_free_mem(struct vb2_queue *q, unsigned int buffers)

    release all video buffer memory for a given queue

    :param struct vb2_queue \*q:
        *undescribed*

    :param unsigned int buffers:
        *undescribed*

.. _`__vb2_queue_free`:

__vb2_queue_free
================

.. c:function:: int __vb2_queue_free(struct vb2_queue *q, unsigned int buffers)

    free buffers at the end of the queue - video memory and related information, if no buffers are left return the queue to an uninitialized state. Might be called even if the queue has already been freed.

    :param struct vb2_queue \*q:
        *undescribed*

    :param unsigned int buffers:
        *undescribed*

.. _`__buffers_in_use`:

__buffers_in_use
================

.. c:function:: bool __buffers_in_use(struct vb2_queue *q)

    return true if any buffers on the queue are in use and the queue cannot be freed (by the means of REQBUFS(0)) call

    :param struct vb2_queue \*q:
        *undescribed*

.. _`__verify_userptr_ops`:

__verify_userptr_ops
====================

.. c:function:: int __verify_userptr_ops(struct vb2_queue *q)

    verify that all memory operations required for USERPTR queue type have been provided

    :param struct vb2_queue \*q:
        *undescribed*

.. _`__verify_mmap_ops`:

__verify_mmap_ops
=================

.. c:function:: int __verify_mmap_ops(struct vb2_queue *q)

    verify that all memory operations required for MMAP queue type have been provided

    :param struct vb2_queue \*q:
        *undescribed*

.. _`__verify_dmabuf_ops`:

__verify_dmabuf_ops
===================

.. c:function:: int __verify_dmabuf_ops(struct vb2_queue *q)

    verify that all memory operations required for DMABUF queue type have been provided

    :param struct vb2_queue \*q:
        *undescribed*

.. _`__prepare_mmap`:

__prepare_mmap
==============

.. c:function:: int __prepare_mmap(struct vb2_buffer *vb, const void *pb)

    prepare an MMAP buffer

    :param struct vb2_buffer \*vb:
        *undescribed*

    :param const void \*pb:
        *undescribed*

.. _`__prepare_userptr`:

__prepare_userptr
=================

.. c:function:: int __prepare_userptr(struct vb2_buffer *vb, const void *pb)

    prepare a USERPTR buffer

    :param struct vb2_buffer \*vb:
        *undescribed*

    :param const void \*pb:
        *undescribed*

.. _`__prepare_dmabuf`:

__prepare_dmabuf
================

.. c:function:: int __prepare_dmabuf(struct vb2_buffer *vb, const void *pb)

    prepare a DMABUF buffer

    :param struct vb2_buffer \*vb:
        *undescribed*

    :param const void \*pb:
        *undescribed*

.. _`__enqueue_in_driver`:

__enqueue_in_driver
===================

.. c:function:: void __enqueue_in_driver(struct vb2_buffer *vb)

    enqueue a vb2_buffer in driver for processing

    :param struct vb2_buffer \*vb:
        *undescribed*

.. _`vb2_start_streaming`:

vb2_start_streaming
===================

.. c:function:: int vb2_start_streaming(struct vb2_queue *q)

    Attempt to start streaming.

    :param struct vb2_queue \*q:
        videobuf2 queue

.. _`vb2_start_streaming.description`:

Description
-----------

Attempt to start streaming. When this function is called there must be
at least q->min_buffers_needed buffers queued up (i.e. the minimum
number of buffers required for the DMA engine to function). If the
\ ``start_streaming``\  op fails it is supposed to return all the driver-owned
buffers back to vb2 in state QUEUED. Check if that happened and if
not warn and reclaim them forcefully.

.. _`__vb2_wait_for_done_vb`:

__vb2_wait_for_done_vb
======================

.. c:function:: int __vb2_wait_for_done_vb(struct vb2_queue *q, int nonblocking)

    wait for a buffer to become available for dequeuing

    :param struct vb2_queue \*q:
        *undescribed*

    :param int nonblocking:
        *undescribed*

.. _`__vb2_wait_for_done_vb.description`:

Description
-----------

Will sleep if required for nonblocking == false.

.. _`__vb2_get_done_vb`:

__vb2_get_done_vb
=================

.. c:function:: int __vb2_get_done_vb(struct vb2_queue *q, struct vb2_buffer **vb, void *pb, int nonblocking)

    get a buffer ready for dequeuing

    :param struct vb2_queue \*q:
        *undescribed*

    :param struct vb2_buffer \*\*vb:
        *undescribed*

    :param void \*pb:
        *undescribed*

    :param int nonblocking:
        *undescribed*

.. _`__vb2_get_done_vb.description`:

Description
-----------

Will sleep if required for nonblocking == false.

.. _`__vb2_dqbuf`:

__vb2_dqbuf
===========

.. c:function:: void __vb2_dqbuf(struct vb2_buffer *vb)

    bring back the buffer to the DEQUEUED state

    :param struct vb2_buffer \*vb:
        *undescribed*

.. _`__vb2_queue_cancel`:

__vb2_queue_cancel
==================

.. c:function:: void __vb2_queue_cancel(struct vb2_queue *q)

    cancel and stop (pause) streaming

    :param struct vb2_queue \*q:
        *undescribed*

.. _`__vb2_queue_cancel.description`:

Description
-----------

Removes all queued buffers from driver's queue and all buffers queued by
userspace from videobuf's queue. Returns to state after reqbufs.

.. _`__find_plane_by_offset`:

__find_plane_by_offset
======================

.. c:function:: int __find_plane_by_offset(struct vb2_queue *q, unsigned long off, unsigned int *_buffer, unsigned int *_plane)

    find plane associated with the given offset off

    :param struct vb2_queue \*q:
        *undescribed*

    :param unsigned long off:
        *undescribed*

    :param unsigned int \*_buffer:
        *undescribed*

    :param unsigned int \*_plane:
        *undescribed*

.. _`vb2_fileio_buf`:

struct vb2_fileio_buf
=====================

.. c:type:: struct vb2_fileio_buf

    buffer context used by file io emulator

.. _`vb2_fileio_buf.definition`:

Definition
----------

.. code-block:: c

    struct vb2_fileio_buf {
        void *vaddr;
        unsigned int size;
        unsigned int pos;
        unsigned int queued:1;
    }

.. _`vb2_fileio_buf.members`:

Members
-------

vaddr
    *undescribed*

size
    *undescribed*

pos
    *undescribed*

queued
    *undescribed*

.. _`vb2_fileio_buf.description`:

Description
-----------

vb2 provides a compatibility layer and emulator of file io (read and
write) calls on top of streaming API. This structure is used for
tracking context related to the buffers.

.. _`vb2_fileio_data`:

struct vb2_fileio_data
======================

.. c:type:: struct vb2_fileio_data

    queue context used by file io emulator

.. _`vb2_fileio_data.definition`:

Definition
----------

.. code-block:: c

    struct vb2_fileio_data {
        unsigned int count;
        unsigned int type;
        unsigned int memory;
        struct vb2_fileio_buf bufs;
        unsigned int cur_index;
        unsigned int initial_index;
        unsigned int q_count;
        unsigned int dq_count;
        unsigned read_once:1;
        unsigned write_immediately:1;
    }

.. _`vb2_fileio_data.members`:

Members
-------

count
    *undescribed*

type
    *undescribed*

memory
    *undescribed*

bufs
    *undescribed*

cur_index
    the index of the buffer currently being read from or
    written to. If equal to q->num_buffers then a new buffer
    must be dequeued.

initial_index
    in the \ :c:func:`read`\  case all buffers are queued up immediately
    in \__vb2_init_fileio() and \__vb2_perform_fileio() just cycles
    buffers. However, in the \ :c:func:`write`\  case no buffers are initially
    queued, instead whenever a buffer is full it is queued up by
    \__vb2_perform_fileio(). Only once all available buffers have
    been queued up will \__vb2_perform_fileio() start to dequeue
    buffers. This means that initially \__vb2_perform_fileio()
    needs to know what buffer index to use when it is queuing up
    the buffers for the first time. That initial index is stored
    in this field. Once it is equal to q->num_buffers all
    available buffers have been queued and \__vb2_perform_fileio()
    should start the normal dequeue/queue cycle.

q_count
    *undescribed*

dq_count
    *undescribed*

read_once
    *undescribed*

write_immediately
    *undescribed*

.. _`vb2_fileio_data.description`:

Description
-----------

vb2 provides a compatibility layer and emulator of file io (read and
write) calls on top of streaming API. For proper operation it required
this structure to save the driver state between each call of the read
or write function.

.. _`__vb2_init_fileio`:

__vb2_init_fileio
=================

.. c:function:: int __vb2_init_fileio(struct vb2_queue *q, int read)

    initialize file io emulator

    :param struct vb2_queue \*q:
        videobuf2 queue

    :param int read:
        mode selector (1 means read, 0 means write)

.. _`__vb2_cleanup_fileio`:

__vb2_cleanup_fileio
====================

.. c:function:: int __vb2_cleanup_fileio(struct vb2_queue *q)

    free resourced used by file io emulator

    :param struct vb2_queue \*q:
        videobuf2 queue

.. _`__vb2_perform_fileio`:

__vb2_perform_fileio
====================

.. c:function:: size_t __vb2_perform_fileio(struct vb2_queue *q, char __user *data, size_t count, loff_t *ppos, int nonblock, int read)

    perform a single file io (read or write) operation

    :param struct vb2_queue \*q:
        videobuf2 queue

    :param char __user \*data:
        pointed to target userspace buffer

    :param size_t count:
        number of bytes to read or write

    :param loff_t \*ppos:
        file handle position tracking pointer

    :param int nonblock:
        mode selector (1 means blocking calls, 0 means nonblocking)

    :param int read:
        access mode selector (1 means read, 0 means write)

.. This file was automatic generated / don't edit.

