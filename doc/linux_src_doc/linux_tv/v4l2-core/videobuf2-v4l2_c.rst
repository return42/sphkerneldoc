.. -*- coding: utf-8; mode: rst -*-

================
videobuf2-v4l2.c
================



.. _xref___verify_planes_array:

__verify_planes_array
=====================

.. c:function:: int __verify_planes_array (struct vb2_buffer * vb, const struct v4l2_buffer * b)

    verify that the planes array passed in struct v4l2_buffer from userspace can be safely used

    :param struct vb2_buffer * vb:

        _undescribed_

    :param const struct v4l2_buffer * b:

        _undescribed_




.. _xref___verify_length:

__verify_length
===============

.. c:function:: int __verify_length (struct vb2_buffer * vb, const struct v4l2_buffer * b)

    Verify that the bytesused value for each plane fits in the plane length and that the data offset doesn't exceed the bytesused value.

    :param struct vb2_buffer * vb:

        _undescribed_

    :param const struct v4l2_buffer * b:

        _undescribed_




.. _xref___fill_v4l2_buffer:

__fill_v4l2_buffer
==================

.. c:function:: void __fill_v4l2_buffer (struct vb2_buffer * vb, void * pb)

    fill in a struct v4l2_buffer with information to be returned to userspace

    :param struct vb2_buffer * vb:

        _undescribed_

    :param void * pb:

        _undescribed_




.. _xref___fill_vb2_buffer:

__fill_vb2_buffer
=================

.. c:function:: int __fill_vb2_buffer (struct vb2_buffer * vb, const void * pb, struct vb2_plane * planes)

    fill a vb2_buffer with information provided in a v4l2_buffer by the userspace. It also verifies that struct v4l2_buffer has a valid number of planes.

    :param struct vb2_buffer * vb:

        _undescribed_

    :param const void * pb:

        _undescribed_

    :param struct vb2_plane * planes:

        _undescribed_




.. _xref_vb2_querybuf:

vb2_querybuf
============

.. c:function:: int vb2_querybuf (struct vb2_queue * q, struct v4l2_buffer * b)

    query video buffer information

    :param struct vb2_queue * q:
        videobuf queue

    :param struct v4l2_buffer * b:
        buffer struct passed from userspace to vidioc_querybuf handler
        		in driver



Description
-----------

Should be called from vidioc_querybuf ioctl handler in driver.
This function will verify the passed v4l2_buffer structure and fill the
relevant information for the userspace.


The return values from this function are intended to be directly returned
from vidioc_querybuf handler in driver.




.. _xref_vb2_reqbufs:

vb2_reqbufs
===========

.. c:function:: int vb2_reqbufs (struct vb2_queue * q, struct v4l2_requestbuffers * req)

    Wrapper for vb2_core_reqbufs() that also verifies the memory and type values.

    :param struct vb2_queue * q:
        videobuf2 queue

    :param struct v4l2_requestbuffers * req:
        struct passed from userspace to vidioc_reqbufs handler
        		in driver




.. _xref_vb2_prepare_buf:

vb2_prepare_buf
===============

.. c:function:: int vb2_prepare_buf (struct vb2_queue * q, struct v4l2_buffer * b)

    Pass ownership of a buffer from userspace to the kernel

    :param struct vb2_queue * q:
        videobuf2 queue

    :param struct v4l2_buffer * b:
        buffer structure passed from userspace to vidioc_prepare_buf
        		handler in driver



Description
-----------

Should be called from vidioc_prepare_buf ioctl handler of a driver.



This function
-------------

1) verifies the passed buffer,
2) calls buf_prepare callback in the driver (if provided), in which
   driver-specific buffer initialization can be performed,


The return values from this function are intended to be directly returned
from vidioc_prepare_buf handler in driver.




.. _xref_vb2_create_bufs:

vb2_create_bufs
===============

.. c:function:: int vb2_create_bufs (struct vb2_queue * q, struct v4l2_create_buffers * create)

    Wrapper for vb2_core_create_bufs() that also verifies the memory and type values.

    :param struct vb2_queue * q:
        videobuf2 queue

    :param struct v4l2_create_buffers * create:
        creation parameters, passed from userspace to vidioc_create_bufs
        		handler in driver




.. _xref_vb2_qbuf:

vb2_qbuf
========

.. c:function:: int vb2_qbuf (struct vb2_queue * q, struct v4l2_buffer * b)

    Queue a buffer from userspace

    :param struct vb2_queue * q:
        videobuf2 queue

    :param struct v4l2_buffer * b:
        buffer structure passed from userspace to vidioc_qbuf handler
        		in driver



Description
-----------

Should be called from vidioc_qbuf ioctl handler of a driver.



This function
-------------

1) verifies the passed buffer,
2) if necessary, calls buf_prepare callback in the driver (if provided), in
   which driver-specific buffer initialization can be performed,
3) if streaming is on, queues the buffer in driver by the means of buf_queue
   callback for processing.


The return values from this function are intended to be directly returned
from vidioc_qbuf handler in driver.




.. _xref_vb2_dqbuf:

vb2_dqbuf
=========

.. c:function:: int vb2_dqbuf (struct vb2_queue * q, struct v4l2_buffer * b, bool nonblocking)

    Dequeue a buffer to the userspace

    :param struct vb2_queue * q:
        videobuf2 queue

    :param struct v4l2_buffer * b:
        buffer structure passed from userspace to vidioc_dqbuf handler
        		in driver

    :param bool nonblocking:
        if true, this call will not sleep waiting for a buffer if no
        		 buffers ready for dequeuing are present. Normally the driver
        		 would be passing (file->f_flags & O_NONBLOCK) here



Description
-----------

Should be called from vidioc_dqbuf ioctl handler of a driver.



This function
-------------

1) verifies the passed buffer,
2) calls buf_finish callback in the driver (if provided), in which
   driver can perform any additional operations that may be required before
   returning the buffer to userspace, such as cache sync,
3) the buffer struct members are filled with relevant information for
   the userspace.


The return values from this function are intended to be directly returned
from vidioc_dqbuf handler in driver.




.. _xref_vb2_streamon:

vb2_streamon
============

.. c:function:: int vb2_streamon (struct vb2_queue * q, enum v4l2_buf_type type)

    start streaming

    :param struct vb2_queue * q:
        videobuf2 queue

    :param enum v4l2_buf_type type:
        type argument passed from userspace to vidioc_streamon handler



Description
-----------

Should be called from vidioc_streamon handler of a driver.



This function
-------------

1) verifies current state
2) passes any previously queued buffers to the driver and starts streaming


The return values from this function are intended to be directly returned
from vidioc_streamon handler in the driver.




.. _xref_vb2_streamoff:

vb2_streamoff
=============

.. c:function:: int vb2_streamoff (struct vb2_queue * q, enum v4l2_buf_type type)

    stop streaming

    :param struct vb2_queue * q:
        videobuf2 queue

    :param enum v4l2_buf_type type:
        type argument passed from userspace to vidioc_streamoff handler



Description
-----------

Should be called from vidioc_streamoff handler of a driver.



This function
-------------

1) verifies current state,
2) stop streaming and dequeues any queued buffers, including those previously
   passed to the driver (after waiting for the driver to finish).


This call can be used for pausing playback.
The return values from this function are intended to be directly returned
from vidioc_streamoff handler in the driver




.. _xref_vb2_expbuf:

vb2_expbuf
==========

.. c:function:: int vb2_expbuf (struct vb2_queue * q, struct v4l2_exportbuffer * eb)

    Export a buffer as a file descriptor

    :param struct vb2_queue * q:
        videobuf2 queue

    :param struct v4l2_exportbuffer * eb:
        export buffer structure passed from userspace to vidioc_expbuf
        		handler in driver



Description
-----------

The return values from this function are intended to be directly returned
from vidioc_expbuf handler in driver.




.. _xref_vb2_queue_init:

vb2_queue_init
==============

.. c:function:: int vb2_queue_init (struct vb2_queue * q)

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




.. _xref_vb2_queue_release:

vb2_queue_release
=================

.. c:function:: void vb2_queue_release (struct vb2_queue * q)

    stop streaming, release the queue and free memory

    :param struct vb2_queue * q:
        videobuf2 queue



Description
-----------

This function stops streaming and performs necessary clean ups, including
freeing video buffer memory. The driver is responsible for freeing
the vb2_queue structure itself.




.. _xref_vb2_poll:

vb2_poll
========

.. c:function:: unsigned int vb2_poll (struct vb2_queue * q, struct file * file, poll_table * wait)

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


If the driver uses struct v4l2_fh, then :c:func:`vb2_poll` will also check for any
pending events.


The return values from this function are intended to be directly returned
from poll handler in driver.


