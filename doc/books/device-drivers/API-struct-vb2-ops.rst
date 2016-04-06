
.. _API-struct-vb2-ops:

==============
struct vb2_ops
==============

*man struct vb2_ops(9)*

*4.6.0-rc1*

driver-specific callbacks


Synopsis
========

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
    };


Members
=======

queue_setup
    called from VIDIOC_REQBUFS and VIDIOC_CREATE_BUFS handlers before memory allocation. It can be called

wait_prepare
    release any locks taken while calling vb2 functions; it is called before an ioctl needs to wait for a new buffer to arrive; required to avoid a deadlock in blocking access
    type.

wait_finish
    reacquire all locks released in the previous callback; required to continue operation after sleeping while waiting for a new buffer to arrive.

buf_init
    called once after allocating a buffer (in MMAP case) or after acquiring a new USERPTR buffer; drivers may perform additional buffer-related initialization; initialization
    failure (return != 0) will prevent queue setup from completing successfully; optional.

buf_prepare
    called every time the buffer is queued from userspace and from the VIDIOC_PREPARE_BUF ioctl; drivers may perform any initialization required before each hardware operation in
    this callback; drivers can access/modify the buffer here as it is still synced for the CPU; drivers that support VIDIOC_CREATE_BUFS must also validate the buffer size; if an
    error is returned, the buffer will not be queued in driver; optional.

buf_finish
    called before every dequeue of the buffer back to userspace; the buffer is synced for the CPU, so drivers can access/modify the buffer contents; drivers may perform any
    operations required before userspace accesses the buffer; optional. The buffer state can be

buf_cleanup
    called once before the buffer is freed; drivers may perform any additional cleanup; optional.

start_streaming
    called once to enter 'streaming' state; the driver may receive buffers with ``buf_queue`` callback before ``start_streaming`` is called; the driver gets the number of already
    queued buffers in count parameter; driver can return an error if hardware fails, in that case all buffers that have been already given by the ``buf_queue`` callback are to be
    returned by the driver by calling ``vb2_buffer_done`` (VB2_BUF_STATE_QUEUED). If you need a minimum number of buffers before you can start streaming, then set
    ``min_buffers_needed`` in the vb2_queue structure. If that is non-zero then start_streaming won't be called until at least that many buffers have been queued up by userspace.

stop_streaming
    called when 'streaming' state must be disabled; driver should stop any DMA transactions or wait until they finish and give back all buffers it got from ``buf_queue`` callback
    by calling ``vb2_buffer_done`` () with either VB2_BUF_STATE_DONE or VB2_BUF_STATE_ERROR; may use ``vb2_wait_for_all_buffers`` function

buf_queue
    passes buffer vb to the driver; driver may start hardware operation on this buffer; driver should give the buffer back by calling ``vb2_buffer_done`` function; it is allways
    called after calling STREAMON ioctl; might be called before start_streaming callback if user pre-queued buffers before calling STREAMON.


twice
=====

if the original number of requested buffers could not be allocated, then it will be called a second time with the actually allocated number of buffers to verify if that is OK. The
driver should return the required number of buffers in ⋆num_buffers, the required number of planes per buffer in ⋆num_planes, the size of each plane should be set in the sizes[]
array and optional per-plane allocator specific context in the alloc_ctxs[] array. When called from VIDIOC_REQBUFS, ⋆num_planes == 0, the driver has to use the currently
configured format to determine the plane sizes and ⋆num_buffers is the total number of buffers that are being allocated. When called from VIDIOC_CREATE_BUFS, ⋆num_planes != 0
and it describes the requested number of planes and sizes[] contains the requested plane sizes. If either ⋆num_planes or the requested sizes are invalid callback must return
-EINVAL. In this case ⋆num_buffers are being allocated additionally to q->num_buffers.


one of the following
====================

DONE and ERROR occur while streaming is in progress, and the PREPARED state occurs when the queue has been canceled and all pending buffers are being returned to their default
DEQUEUED state. Typically you only have to do something if the state is VB2_BUF_STATE_DONE, since in all other cases the buffer contents will be ignored anyway.
