.. -*- coding: utf-8; mode: rst -*-

================
videobuf2-core.c
================



.. _xref___vb2_buf_mem_alloc:

__vb2_buf_mem_alloc
===================

.. c:function:: int __vb2_buf_mem_alloc (struct vb2_buffer * vb)

    allocate video memory for the given buffer

    :param struct vb2_buffer * vb:

        _undescribed_




.. _xref___vb2_buf_mem_free:

__vb2_buf_mem_free
==================

.. c:function:: void __vb2_buf_mem_free (struct vb2_buffer * vb)

    free memory of the given buffer

    :param struct vb2_buffer * vb:

        _undescribed_




.. _xref___vb2_buf_userptr_put:

__vb2_buf_userptr_put
=====================

.. c:function:: void __vb2_buf_userptr_put (struct vb2_buffer * vb)

    release userspace memory associated with a USERPTR buffer

    :param struct vb2_buffer * vb:

        _undescribed_




.. _xref___vb2_plane_dmabuf_put:

__vb2_plane_dmabuf_put
======================

.. c:function:: void __vb2_plane_dmabuf_put (struct vb2_buffer * vb, struct vb2_plane * p)

    release memory associated with a DMABUF shared plane

    :param struct vb2_buffer * vb:

        _undescribed_

    :param struct vb2_plane * p:

        _undescribed_




.. _xref___vb2_buf_dmabuf_put:

__vb2_buf_dmabuf_put
====================

.. c:function:: void __vb2_buf_dmabuf_put (struct vb2_buffer * vb)

    release memory associated with a DMABUF shared buffer

    :param struct vb2_buffer * vb:

        _undescribed_




.. _xref___setup_offsets:

__setup_offsets
===============

.. c:function:: void __setup_offsets (struct vb2_buffer * vb)

    setup unique offsets ("cookies") for every plane in the buffer.

    :param struct vb2_buffer * vb:

        _undescribed_




.. _xref___vb2_queue_alloc:

__vb2_queue_alloc
=================

.. c:function:: int __vb2_queue_alloc (struct vb2_queue * q, enum vb2_memory memory, unsigned int num_buffers, unsigned int num_planes, const unsigned plane_sizes[VB2_MAX_PLANES])

    allocate videobuf buffer structures and (for MMAP type) video buffer memory for all buffers/planes on the queue and initializes the queue

    :param struct vb2_queue * q:

        _undescribed_

    :param enum vb2_memory memory:

        _undescribed_

    :param unsigned int num_buffers:

        _undescribed_

    :param unsigned int num_planes:

        _undescribed_

    :param const unsigned plane_sizes[VB2_MAX_PLANES]:



Description
-----------



Returns the number of buffers successfully allocated.




.. _xref___vb2_free_mem:

__vb2_free_mem
==============

.. c:function:: void __vb2_free_mem (struct vb2_queue * q, unsigned int buffers)

    release all video buffer memory for a given queue

    :param struct vb2_queue * q:

        _undescribed_

    :param unsigned int buffers:

        _undescribed_




.. _xref___vb2_queue_free:

__vb2_queue_free
================

.. c:function:: int __vb2_queue_free (struct vb2_queue * q, unsigned int buffers)

    free buffers at the end of the queue - video memory and related information, if no buffers are left return the queue to an uninitialized state. Might be called even if the queue has already been freed.

    :param struct vb2_queue * q:

        _undescribed_

    :param unsigned int buffers:

        _undescribed_




.. _xref_vb2_buffer_in_use:

vb2_buffer_in_use
=================

.. c:function:: bool vb2_buffer_in_use (struct vb2_queue * q, struct vb2_buffer * vb)

    return true if the buffer is in use and the queue cannot be freed (by the means of REQBUFS(0)) call

    :param struct vb2_queue * q:

        _undescribed_

    :param struct vb2_buffer * vb:

        _undescribed_




.. _xref___buffers_in_use:

__buffers_in_use
================

.. c:function:: bool __buffers_in_use (struct vb2_queue * q)

    return true if any buffers on the queue are in use and the queue cannot be freed (by the means of REQBUFS(0)) call

    :param struct vb2_queue * q:

        _undescribed_




.. _xref_vb2_core_querybuf:

vb2_core_querybuf
=================

.. c:function:: void vb2_core_querybuf (struct vb2_queue * q, unsigned int index, void * pb)

    query video buffer information

    :param struct vb2_queue * q:
        videobuf queue

    :param unsigned int index:
        id number of the buffer

    :param void * pb:
        buffer struct passed from userspace



Description
-----------

Should be called from vidioc_querybuf ioctl handler in driver.
The passed buffer should have been verified.
This function fills the relevant information for the userspace.




.. _xref___verify_userptr_ops:

__verify_userptr_ops
====================

.. c:function:: int __verify_userptr_ops (struct vb2_queue * q)

    verify that all memory operations required for USERPTR queue type have been provided

    :param struct vb2_queue * q:

        _undescribed_




.. _xref___verify_mmap_ops:

__verify_mmap_ops
=================

.. c:function:: int __verify_mmap_ops (struct vb2_queue * q)

    verify that all memory operations required for MMAP queue type have been provided

    :param struct vb2_queue * q:

        _undescribed_




.. _xref___verify_dmabuf_ops:

__verify_dmabuf_ops
===================

.. c:function:: int __verify_dmabuf_ops (struct vb2_queue * q)

    verify that all memory operations required for DMABUF queue type have been provided

    :param struct vb2_queue * q:

        _undescribed_




.. _xref_vb2_verify_memory_type:

vb2_verify_memory_type
======================

.. c:function:: int vb2_verify_memory_type (struct vb2_queue * q, enum vb2_memory memory, unsigned int type)

    Check whether the memory type and buffer type passed to a buffer operation are compatible with the queue.

    :param struct vb2_queue * q:

        _undescribed_

    :param enum vb2_memory memory:

        _undescribed_

    :param unsigned int type:

        _undescribed_




.. _xref_vb2_core_reqbufs:

vb2_core_reqbufs
================

.. c:function:: int vb2_core_reqbufs (struct vb2_queue * q, enum vb2_memory memory, unsigned int * count)

    Initiate streaming

    :param struct vb2_queue * q:
        videobuf2 queue

    :param enum vb2_memory memory:
        memory type

    :param unsigned int * count:
        requested buffer count



Description
-----------

Should be called from vidioc_reqbufs ioctl handler of a driver.



This function
-------------

1) verifies streaming parameters passed from the userspace,
2) sets up the queue,
3) negotiates number of buffers and planes per buffer with the driver
   to be used during streaming,
4) allocates internal buffer structures (struct vb2_buffer), according to
   the agreed parameters,
5) for MMAP memory type, allocates actual video memory, using the
   memory handling/allocation routines provided during queue initialization


If req->count is 0, all the memory will be freed instead.
If the queue has been allocated previously (by a previous vb2_reqbufs) call
and the queue is not busy, memory will be reallocated.


The return values from this function are intended to be directly returned
from vidioc_reqbufs handler in driver.




.. _xref_vb2_core_create_bufs:

vb2_core_create_bufs
====================

.. c:function:: int vb2_core_create_bufs (struct vb2_queue * q, enum vb2_memory memory, unsigned int * count, unsigned requested_planes, const unsigned requested_sizes[])

    Allocate buffers and any required auxiliary structs

    :param struct vb2_queue * q:
        videobuf2 queue

    :param enum vb2_memory memory:
        memory type

    :param unsigned int * count:
        requested buffer count

    :param unsigned requested_planes:

        _undescribed_

    :param const unsigned requested_sizes[]:



Description
-----------

Should be called from vidioc_create_bufs ioctl handler of a driver.



This function
-------------

1) verifies parameter sanity
2) calls the .:c:func:`queue_setup` queue operation
3) performs any necessary memory allocations


The return values from this function are intended to be directly returned
from vidioc_create_bufs handler in driver.




.. _xref_vb2_plane_vaddr:

vb2_plane_vaddr
===============

.. c:function:: void * vb2_plane_vaddr (struct vb2_buffer * vb, unsigned int plane_no)

    Return a kernel virtual address of a given plane

    :param struct vb2_buffer * vb:
        vb2_buffer to which the plane in question belongs to

    :param unsigned int plane_no:
        plane number for which the address is to be returned



Description
-----------

This function returns a kernel virtual address of a given plane if
such a mapping exist, NULL otherwise.




.. _xref_vb2_plane_cookie:

vb2_plane_cookie
================

.. c:function:: void * vb2_plane_cookie (struct vb2_buffer * vb, unsigned int plane_no)

    Return allocator specific cookie for the given plane

    :param struct vb2_buffer * vb:
        vb2_buffer to which the plane in question belongs to

    :param unsigned int plane_no:
        plane number for which the cookie is to be returned



Description
-----------

This function returns an allocator specific cookie for a given plane if
available, NULL otherwise. The allocator should provide some simple static
inline function, which would convert this cookie to the allocator specific
type that can be used directly by the driver to access the buffer. This can
be for example physical address, pointer to scatter list or IOMMU mapping.




.. _xref_vb2_buffer_done:

vb2_buffer_done
===============

.. c:function:: void vb2_buffer_done (struct vb2_buffer * vb, enum vb2_buffer_state state)

    inform videobuf that an operation on a buffer is finished

    :param struct vb2_buffer * vb:
        vb2_buffer returned from the driver

    :param enum vb2_buffer_state state:
        either VB2_BUF_STATE_DONE if the operation finished successfully,
        		VB2_BUF_STATE_ERROR if the operation finished with an error or
        		VB2_BUF_STATE_QUEUED if the driver wants to requeue buffers.
        		If start_streaming fails then it should return buffers with state
        		VB2_BUF_STATE_QUEUED to put them back into the queue.



Description
-----------

This function should be called by the driver after a hardware operation on
a buffer is finished and the buffer may be returned to userspace. The driver
cannot use this buffer anymore until it is queued back to it by videobuf
by the means of buf_queue callback. Only buffers previously queued to the
driver by buf_queue can be passed to this function.


While streaming a buffer can only be returned in state DONE or ERROR.
The start_streaming op can also return them in case the DMA engine cannot
be started for some reason. In that case the buffers should be returned with
state QUEUED.




.. _xref_vb2_discard_done:

vb2_discard_done
================

.. c:function:: void vb2_discard_done (struct vb2_queue * q)

    discard all buffers marked as DONE

    :param struct vb2_queue * q:
        videobuf2 queue



Description
-----------

This function is intended to be used with suspend/resume operations. It
discards all 'done' buffers as they would be too old to be requested after
resume.


Drivers must stop the hardware and synchronize with interrupt handlers and/or
delayed works before calling this function to make sure no buffer will be
touched by the driver and/or hardware.




.. _xref___qbuf_mmap:

__qbuf_mmap
===========

.. c:function:: int __qbuf_mmap (struct vb2_buffer * vb, const void * pb)

    handle qbuf of an MMAP buffer

    :param struct vb2_buffer * vb:

        _undescribed_

    :param const void * pb:

        _undescribed_




.. _xref___qbuf_userptr:

__qbuf_userptr
==============

.. c:function:: int __qbuf_userptr (struct vb2_buffer * vb, const void * pb)

    handle qbuf of a USERPTR buffer

    :param struct vb2_buffer * vb:

        _undescribed_

    :param const void * pb:

        _undescribed_




.. _xref___qbuf_dmabuf:

__qbuf_dmabuf
=============

.. c:function:: int __qbuf_dmabuf (struct vb2_buffer * vb, const void * pb)

    handle qbuf of a DMABUF buffer

    :param struct vb2_buffer * vb:

        _undescribed_

    :param const void * pb:

        _undescribed_




.. _xref___enqueue_in_driver:

__enqueue_in_driver
===================

.. c:function:: void __enqueue_in_driver (struct vb2_buffer * vb)

    enqueue a vb2_buffer in driver for processing

    :param struct vb2_buffer * vb:

        _undescribed_




.. _xref_vb2_core_prepare_buf:

vb2_core_prepare_buf
====================

.. c:function:: int vb2_core_prepare_buf (struct vb2_queue * q, unsigned int index, void * pb)

    Pass ownership of a buffer from userspace to the kernel

    :param struct vb2_queue * q:
        videobuf2 queue

    :param unsigned int index:
        id number of the buffer

    :param void * pb:
        buffer structure passed from userspace to vidioc_prepare_buf
        		handler in driver



Description
-----------

Should be called from vidioc_prepare_buf ioctl handler of a driver.
The passed buffer should have been verified.
This function calls buf_prepare callback in the driver (if provided),
in which driver-specific buffer initialization can be performed,


The return values from this function are intended to be directly returned
from vidioc_prepare_buf handler in driver.




.. _xref_vb2_start_streaming:

vb2_start_streaming
===================

.. c:function:: int vb2_start_streaming (struct vb2_queue * q)

    Attempt to start streaming.

    :param struct vb2_queue * q:
        videobuf2 queue



Description
-----------

Attempt to start streaming. When this function is called there must be
at least q->min_buffers_needed buffers queued up (i.e. the minimum
number of buffers required for the DMA engine to function). If the
**start_streaming** op fails it is supposed to return all the driver-owned
buffers back to vb2 in state QUEUED. Check if that happened and if
not warn and reclaim them forcefully.




.. _xref_vb2_core_qbuf:

vb2_core_qbuf
=============

.. c:function:: int vb2_core_qbuf (struct vb2_queue * q, unsigned int index, void * pb)

    Queue a buffer from userspace

    :param struct vb2_queue * q:
        videobuf2 queue

    :param unsigned int index:
        id number of the buffer

    :param void * pb:
        buffer structure passed from userspace to vidioc_qbuf handler
        		in driver



Description
-----------

Should be called from vidioc_qbuf ioctl handler of a driver.
The passed buffer should have been verified.



This function
-------------

1) if necessary, calls buf_prepare callback in the driver (if provided), in
   which driver-specific buffer initialization can be performed,
2) if streaming is on, queues the buffer in driver by the means of buf_queue
   callback for processing.


The return values from this function are intended to be directly returned
from vidioc_qbuf handler in driver.




.. _xref___vb2_wait_for_done_vb:

__vb2_wait_for_done_vb
======================

.. c:function:: int __vb2_wait_for_done_vb (struct vb2_queue * q, int nonblocking)

    wait for a buffer to become available for dequeuing

    :param struct vb2_queue * q:

        _undescribed_

    :param int nonblocking:

        _undescribed_



Description
-----------



Will sleep if required for nonblocking == false.




.. _xref___vb2_get_done_vb:

__vb2_get_done_vb
=================

.. c:function:: int __vb2_get_done_vb (struct vb2_queue * q, struct vb2_buffer ** vb, int nonblocking)

    get a buffer ready for dequeuing

    :param struct vb2_queue * q:

        _undescribed_

    :param struct vb2_buffer ** vb:

        _undescribed_

    :param int nonblocking:

        _undescribed_



Description
-----------



Will sleep if required for nonblocking == false.




.. _xref_vb2_wait_for_all_buffers:

vb2_wait_for_all_buffers
========================

.. c:function:: int vb2_wait_for_all_buffers (struct vb2_queue * q)

    wait until all buffers are given back to vb2

    :param struct vb2_queue * q:
        videobuf2 queue



Description
-----------

This function will wait until all buffers that have been given to the driver
by :c:func:`buf_queue` are given back to vb2 with :c:func:`vb2_buffer_done`. It doesn't call
wait_prepare, wait_finish pair. It is intended to be called with all locks
taken, for example from :c:func:`stop_streaming` callback.




.. _xref___vb2_dqbuf:

__vb2_dqbuf
===========

.. c:function:: void __vb2_dqbuf (struct vb2_buffer * vb)

    bring back the buffer to the DEQUEUED state

    :param struct vb2_buffer * vb:

        _undescribed_




.. _xref_vb2_core_dqbuf:

vb2_core_dqbuf
==============

.. c:function:: int vb2_core_dqbuf (struct vb2_queue * q, unsigned int * pindex, void * pb, bool nonblocking)

    Dequeue a buffer to the userspace

    :param struct vb2_queue * q:
        videobuf2 queue

    :param unsigned int * pindex:

        _undescribed_

    :param void * pb:
        buffer structure passed from userspace to vidioc_dqbuf handler
        		in driver

    :param bool nonblocking:
        if true, this call will not sleep waiting for a buffer if no
        		 buffers ready for dequeuing are present. Normally the driver
        		 would be passing (file->f_flags & O_NONBLOCK) here



Description
-----------

Should be called from vidioc_dqbuf ioctl handler of a driver.
The passed buffer should have been verified.



This function
-------------

1) calls buf_finish callback in the driver (if provided), in which
   driver can perform any additional operations that may be required before
   returning the buffer to userspace, such as cache sync,
2) the buffer struct members are filled with relevant information for
   the userspace.


The return values from this function are intended to be directly returned
from vidioc_dqbuf handler in driver.




.. _xref___vb2_queue_cancel:

__vb2_queue_cancel
==================

.. c:function:: void __vb2_queue_cancel (struct vb2_queue * q)

    cancel and stop (pause) streaming

    :param struct vb2_queue * q:

        _undescribed_



Description
-----------



Removes all queued buffers from driver's queue and all buffers queued by
userspace from videobuf's queue. Returns to state after reqbufs.




.. _xref_vb2_queue_error:

vb2_queue_error
===============

.. c:function:: void vb2_queue_error (struct vb2_queue * q)

    signal a fatal error on the queue

    :param struct vb2_queue * q:
        videobuf2 queue



Description
-----------

Flag that a fatal unrecoverable error has occurred and wake up all processes
waiting on the queue. Polling will now set POLLERR and queuing and dequeuing
buffers will return -EIO.


The error flag will be cleared when cancelling the queue, either from
vb2_streamoff or vb2_queue_release. Drivers should thus not call this
function before starting the stream, otherwise the error flag will remain set
until the queue is released when closing the device node.




.. _xref___find_plane_by_offset:

__find_plane_by_offset
======================

.. c:function:: int __find_plane_by_offset (struct vb2_queue * q, unsigned long off, unsigned int * _buffer, unsigned int * _plane)

    find plane associated with the given offset off

    :param struct vb2_queue * q:

        _undescribed_

    :param unsigned long off:

        _undescribed_

    :param unsigned int * _buffer:

        _undescribed_

    :param unsigned int * _plane:

        _undescribed_




.. _xref_vb2_core_expbuf:

vb2_core_expbuf
===============

.. c:function:: int vb2_core_expbuf (struct vb2_queue * q, int * fd, unsigned int type, unsigned int index, unsigned int plane, unsigned int flags)

    Export a buffer as a file descriptor

    :param struct vb2_queue * q:
        videobuf2 queue

    :param int * fd:
        file descriptor associated with DMABUF (set by driver) *

    :param unsigned int type:
        buffer type

    :param unsigned int index:
        id number of the buffer

    :param unsigned int plane:
        index of the plane to be exported, 0 for single plane queues

    :param unsigned int flags:
        flags for newly created file, currently only O_CLOEXEC is
        		supported, refer to manual of open syscall for more details



Description
-----------

The return values from this function are intended to be directly returned
from vidioc_expbuf handler in driver.




.. _xref_vb2_mmap:

vb2_mmap
========

.. c:function:: int vb2_mmap (struct vb2_queue * q, struct vm_area_struct * vma)

    map video buffers into application address space

    :param struct vb2_queue * q:
        videobuf2 queue

    :param struct vm_area_struct * vma:
        vma passed to the mmap file operation handler in the driver



Description
-----------

Should be called from mmap file operation handler of a driver.
This function maps one plane of one of the available video buffers to
userspace. To map whole video memory allocated on reqbufs, this function
has to be called once per each plane per each buffer previously allocated.


When the userspace application calls mmap, it passes to it an offset returned
to it earlier by the means of vidioc_querybuf handler. That offset acts as
a "cookie", which is then used to identify the plane to be mapped.
This function finds a plane with a matching offset and a mapping is performed
by the means of a provided memory operation.


The return values from this function are intended to be directly returned
from the mmap handler in driver.




.. _xref_vb2_core_queue_init:

vb2_core_queue_init
===================

.. c:function:: int vb2_core_queue_init (struct vb2_queue * q)

    initialize a videobuf2 queue

    :param struct vb2_queue * q:
        videobuf2 queue; this structure should be allocated in driver



Description
-----------

The vb2_queue structure should be allocated by the driver. The driver is
responsible of clearing it's content and setting initial values for some
required entries before calling this function.
q->ops, q->mem_ops, q->type and q->io_modes are mandatory. Please refer
to the struct vb2_queue description in include/media/videobuf2-core.h
for more information.




.. _xref_vb2_core_queue_release:

vb2_core_queue_release
======================

.. c:function:: void vb2_core_queue_release (struct vb2_queue * q)

    stop streaming, release the queue and free memory

    :param struct vb2_queue * q:
        videobuf2 queue



Description
-----------

This function stops streaming and performs necessary clean ups, including
freeing video buffer memory. The driver is responsible for freeing
the vb2_queue structure itself.




.. _xref_vb2_core_poll:

vb2_core_poll
=============

.. c:function:: unsigned int vb2_core_poll (struct vb2_queue * q, struct file * file, poll_table * wait)

    implements poll userspace operation

    :param struct vb2_queue * q:
        videobuf2 queue

    :param struct file * file:
        file argument passed to the poll file operation handler

    :param poll_table * wait:
        wait argument passed to the poll file operation handler



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




.. _xref_struct_vb2_fileio_buf:

struct vb2_fileio_buf
=====================

.. c:type:: struct vb2_fileio_buf

    buffer context used by file io emulator



Definition
----------

.. code-block:: c

  struct vb2_fileio_buf {
  };



Members
-------




Description
-----------



vb2 provides a compatibility layer and emulator of file io (read and
write) calls on top of streaming API. This structure is used for
tracking context related to the buffers.




.. _xref_struct_vb2_fileio_data:

struct vb2_fileio_data
======================

.. c:type:: struct vb2_fileio_data

    queue context used by file io emulator



Definition
----------

.. code-block:: c

  struct vb2_fileio_data {
    unsigned int cur_index;
    unsigned int initial_index;
  };



Members
-------

:``unsigned int cur_index``:
    the index of the buffer currently being read from or
    		written to. If equal to q->num_buffers then a new buffer
    		must be dequeued.

:``unsigned int initial_index``:
    in the :c:func:`read` case all buffers are queued up immediately
    		in :c:func:`__vb2_init_fileio` and :c:func:`__vb2_perform_fileio` just cycles
    		buffers. However, in the :c:func:`write` case no buffers are initially
    		queued, instead whenever a buffer is full it is queued up by
    		:c:func:`__vb2_perform_fileio`. Only once all available buffers have
    		been queued up will :c:func:`__vb2_perform_fileio` start to dequeue
    		buffers. This means that initially :c:func:`__vb2_perform_fileio`
    		needs to know what buffer index to use when it is queuing up
    		the buffers for the first time. That initial index is stored
    		in this field. Once it is equal to q->num_buffers all
    		available buffers have been queued and :c:func:`__vb2_perform_fileio`
    		should start the normal dequeue/queue cycle.




Description
-----------

vb2 provides a compatibility layer and emulator of file io (read and
write) calls on top of streaming API. For proper operation it required
this structure to save the driver state between each call of the read
or write function.




.. _xref___vb2_init_fileio:

__vb2_init_fileio
=================

.. c:function:: int __vb2_init_fileio (struct vb2_queue * q, int read)

    initialize file io emulator

    :param struct vb2_queue * q:
        videobuf2 queue

    :param int read:
        mode selector (1 means read, 0 means write)




.. _xref___vb2_cleanup_fileio:

__vb2_cleanup_fileio
====================

.. c:function:: int __vb2_cleanup_fileio (struct vb2_queue * q)

    free resourced used by file io emulator

    :param struct vb2_queue * q:
        videobuf2 queue




.. _xref___vb2_perform_fileio:

__vb2_perform_fileio
====================

.. c:function:: size_t __vb2_perform_fileio (struct vb2_queue * q, char __user * data, size_t count, loff_t * ppos, int nonblock, int read)

    perform a single file io (read or write) operation

    :param struct vb2_queue * q:
        videobuf2 queue

    :param char __user * data:
        pointed to target userspace buffer

    :param size_t count:
        number of bytes to read or write

    :param loff_t * ppos:
        file handle position tracking pointer

    :param int nonblock:
        mode selector (1 means blocking calls, 0 means nonblocking)

    :param int read:
        access mode selector (1 means read, 0 means write)


