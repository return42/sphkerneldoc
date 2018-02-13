.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/videobuf2-v4l2.h

.. _`vb2_v4l2_buffer`:

struct vb2_v4l2_buffer
======================

.. c:type:: struct vb2_v4l2_buffer

    video buffer information for v4l2.

.. _`vb2_v4l2_buffer.definition`:

Definition
----------

.. code-block:: c

    struct vb2_v4l2_buffer {
        struct vb2_buffer vb2_buf;
        __u32 flags;
        __u32 field;
        struct v4l2_timecode timecode;
        __u32 sequence;
    }

.. _`vb2_v4l2_buffer.members`:

Members
-------

vb2_buf
    embedded struct \ :c:type:`struct vb2_buffer <vb2_buffer>`\ .

flags
    buffer informational flags.

field
    field order of the image in the buffer, as defined by
    \ :c:type:`enum v4l2_field <v4l2_field>`\ .

timecode
    frame timecode.

sequence
    sequence count of this frame.

.. _`vb2_v4l2_buffer.description`:

Description
-----------

Should contain enough information to be able to cover all the fields
of \ :c:type:`struct v4l2_buffer <v4l2_buffer>`\  at ``videodev2.h``.

.. _`vb2_reqbufs`:

vb2_reqbufs
===========

.. c:function:: int vb2_reqbufs(struct vb2_queue *q, struct v4l2_requestbuffers *req)

    Wrapper for \ :c:func:`vb2_core_reqbufs`\  that also verifies the memory and type values.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param struct v4l2_requestbuffers \*req:
        \ :c:type:`struct v4l2_requestbuffers <v4l2_requestbuffers>`\  passed from userspace to
        \ :c:type:`v4l2_ioctl_ops->vidioc_reqbufs <v4l2_ioctl_ops>`\  handler in driver.

.. _`vb2_create_bufs`:

vb2_create_bufs
===============

.. c:function:: int vb2_create_bufs(struct vb2_queue *q, struct v4l2_create_buffers *create)

    Wrapper for \ :c:func:`vb2_core_create_bufs`\  that also verifies the memory and type values.

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param struct v4l2_create_buffers \*create:
        creation parameters, passed from userspace to
        \ :c:type:`v4l2_ioctl_ops->vidioc_create_bufs <v4l2_ioctl_ops>`\  handler in driver

.. _`vb2_prepare_buf`:

vb2_prepare_buf
===============

.. c:function:: int vb2_prepare_buf(struct vb2_queue *q, struct v4l2_buffer *b)

    Pass ownership of a buffer from userspace to the kernel

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param struct v4l2_buffer \*b:
        buffer structure passed from userspace to
        \ :c:type:`v4l2_ioctl_ops->vidioc_prepare_buf <v4l2_ioctl_ops>`\  handler in driver

.. _`vb2_prepare_buf.description`:

Description
-----------

Should be called from \ :c:type:`v4l2_ioctl_ops->vidioc_prepare_buf <v4l2_ioctl_ops>`\  ioctl handler
of a driver.

.. _`vb2_prepare_buf.this-function`:

This function
-------------


#) verifies the passed buffer,
#) calls \ :c:type:`vb2_ops->buf_prepare <vb2_ops>`\  callback in the driver (if provided),
   in which driver-specific buffer initialization can be performed.

The return values from this function are intended to be directly returned
from \ :c:type:`v4l2_ioctl_ops->vidioc_prepare_buf <v4l2_ioctl_ops>`\  handler in driver.

.. _`vb2_qbuf`:

vb2_qbuf
========

.. c:function:: int vb2_qbuf(struct vb2_queue *q, struct v4l2_buffer *b)

    Queue a buffer from userspace

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param struct v4l2_buffer \*b:
        buffer structure passed from userspace to
        \ :c:type:`v4l2_ioctl_ops->vidioc_qbuf <v4l2_ioctl_ops>`\  handler in driver

.. _`vb2_qbuf.description`:

Description
-----------

Should be called from \ :c:type:`v4l2_ioctl_ops->vidioc_qbuf <v4l2_ioctl_ops>`\  handler of a driver.

.. _`vb2_qbuf.this-function`:

This function
-------------


#) verifies the passed buffer;
#) if necessary, calls \ :c:type:`vb2_ops->buf_prepare <vb2_ops>`\  callback in the driver
   (if provided), in which driver-specific buffer initialization can
   be performed;
#) if streaming is on, queues the buffer in driver by the means of
   \ :c:type:`vb2_ops->buf_queue <vb2_ops>`\  callback for processing.

The return values from this function are intended to be directly returned
from \ :c:type:`v4l2_ioctl_ops->vidioc_qbuf <v4l2_ioctl_ops>`\  handler in driver.

.. _`vb2_expbuf`:

vb2_expbuf
==========

.. c:function:: int vb2_expbuf(struct vb2_queue *q, struct v4l2_exportbuffer *eb)

    Export a buffer as a file descriptor

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param struct v4l2_exportbuffer \*eb:
        export buffer structure passed from userspace to
        \ :c:type:`v4l2_ioctl_ops->vidioc_expbuf <v4l2_ioctl_ops>`\  handler in driver

.. _`vb2_expbuf.description`:

Description
-----------

The return values from this function are intended to be directly returned
from \ :c:type:`v4l2_ioctl_ops->vidioc_expbuf <v4l2_ioctl_ops>`\  handler in driver.

.. _`vb2_dqbuf`:

vb2_dqbuf
=========

.. c:function:: int vb2_dqbuf(struct vb2_queue *q, struct v4l2_buffer *b, bool nonblocking)

    Dequeue a buffer to the userspace

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param struct v4l2_buffer \*b:
        buffer structure passed from userspace to
        \ :c:type:`v4l2_ioctl_ops->vidioc_dqbuf <v4l2_ioctl_ops>`\  handler in driver

    :param bool nonblocking:
        if true, this call will not sleep waiting for a buffer if no
        buffers ready for dequeuing are present. Normally the driver
        would be passing (&file->f_flags & \ ``O_NONBLOCK``\ ) here

.. _`vb2_dqbuf.description`:

Description
-----------

Should be called from \ :c:type:`v4l2_ioctl_ops->vidioc_dqbuf <v4l2_ioctl_ops>`\  ioctl handler
of a driver.

.. _`vb2_dqbuf.this-function`:

This function
-------------


#) verifies the passed buffer;
#) calls \ :c:type:`vb2_ops->buf_finish <vb2_ops>`\  callback in the driver (if provided), in which
   driver can perform any additional operations that may be required before
   returning the buffer to userspace, such as cache sync;
#) the buffer struct members are filled with relevant information for
   the userspace.

The return values from this function are intended to be directly returned
from \ :c:type:`v4l2_ioctl_ops->vidioc_dqbuf <v4l2_ioctl_ops>`\  handler in driver.

.. _`vb2_streamon`:

vb2_streamon
============

.. c:function:: int vb2_streamon(struct vb2_queue *q, enum v4l2_buf_type type)

    start streaming

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param enum v4l2_buf_type type:
        type argument passed from userspace to vidioc_streamon handler,
        as defined by \ :c:type:`enum v4l2_buf_type <v4l2_buf_type>`\ .

.. _`vb2_streamon.description`:

Description
-----------

Should be called from \ :c:type:`v4l2_ioctl_ops->vidioc_streamon <v4l2_ioctl_ops>`\  handler of a driver.

.. _`vb2_streamon.this-function`:

This function
-------------


1) verifies current state
2) passes any previously queued buffers to the driver and starts streaming

The return values from this function are intended to be directly returned
from \ :c:type:`v4l2_ioctl_ops->vidioc_streamon <v4l2_ioctl_ops>`\  handler in the driver.

.. _`vb2_streamoff`:

vb2_streamoff
=============

.. c:function:: int vb2_streamoff(struct vb2_queue *q, enum v4l2_buf_type type)

    stop streaming

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param enum v4l2_buf_type type:
        type argument passed from userspace to vidioc_streamoff handler

.. _`vb2_streamoff.description`:

Description
-----------

Should be called from vidioc_streamoff handler of a driver.

.. _`vb2_streamoff.this-function`:

This function
-------------


#) verifies current state,
#) stop streaming and dequeues any queued buffers, including those previously
   passed to the driver (after waiting for the driver to finish).

This call can be used for pausing playback.
The return values from this function are intended to be directly returned
from vidioc_streamoff handler in the driver

.. _`vb2_queue_init`:

vb2_queue_init
==============

.. c:function:: int vb2_queue_init(struct vb2_queue *q)

    initialize a videobuf2 queue

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

.. _`vb2_queue_init.description`:

Description
-----------

The vb2_queue structure should be allocated by the driver. The driver is
responsible of clearing it's content and setting initial values for some
required entries before calling this function.
q->ops, q->mem_ops, q->type and q->io_modes are mandatory. Please refer
to the struct vb2_queue description in include/media/videobuf2-core.h
for more information.

.. _`vb2_queue_release`:

vb2_queue_release
=================

.. c:function:: void vb2_queue_release(struct vb2_queue *q)

    stop streaming, release the queue and free memory

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

.. _`vb2_queue_release.description`:

Description
-----------

This function stops streaming and performs necessary clean ups, including
freeing video buffer memory. The driver is responsible for freeing
the vb2_queue structure itself.

.. _`vb2_poll`:

vb2_poll
========

.. c:function:: __poll_t vb2_poll(struct vb2_queue *q, struct file *file, poll_table *wait)

    implements poll userspace operation

    :param struct vb2_queue \*q:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\  with videobuf2 queue.

    :param struct file \*file:
        file argument passed to the poll file operation handler

    :param poll_table \*wait:
        wait argument passed to the poll file operation handler

.. _`vb2_poll.description`:

Description
-----------

This function implements poll file operation handler for a driver.
For CAPTURE queues, if a buffer is ready to be dequeued, the userspace will
be informed that the file descriptor of a video device is available for
reading.
For OUTPUT queues, if a buffer is ready to be dequeued, the file descriptor
will be reported as available for writing.

If the driver uses struct v4l2_fh, then \ :c:func:`vb2_poll`\  will also check for any
pending events.

The return values from this function are intended to be directly returned
from poll handler in driver.

.. _`vb2_ops_wait_prepare`:

vb2_ops_wait_prepare
====================

.. c:function:: void vb2_ops_wait_prepare(struct vb2_queue *vq)

    helper function to lock a struct \ :c:type:`struct vb2_queue <vb2_queue>`\ 

    :param struct vb2_queue \*vq:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\ 

.. _`vb2_ops_wait_prepare.description`:

Description
-----------

..note:: only use if vq->lock is non-NULL.

.. _`vb2_ops_wait_finish`:

vb2_ops_wait_finish
===================

.. c:function:: void vb2_ops_wait_finish(struct vb2_queue *vq)

    helper function to unlock a struct \ :c:type:`struct vb2_queue <vb2_queue>`\ 

    :param struct vb2_queue \*vq:
        pointer to \ :c:type:`struct vb2_queue <vb2_queue>`\ 

.. _`vb2_ops_wait_finish.description`:

Description
-----------

..note:: only use if vq->lock is non-NULL.

.. This file was automatic generated / don't edit.

