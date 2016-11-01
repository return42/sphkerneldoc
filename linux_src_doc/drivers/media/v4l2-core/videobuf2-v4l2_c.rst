.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/v4l2-core/videobuf2-v4l2.c

.. _`__verify_planes_array`:

__verify_planes_array
=====================

.. c:function:: int __verify_planes_array(struct vb2_buffer *vb, const struct v4l2_buffer *b)

    verify that the planes array passed in struct v4l2_buffer from userspace can be safely used

    :param struct vb2_buffer \*vb:
        *undescribed*

    :param const struct v4l2_buffer \*b:
        *undescribed*

.. _`__verify_length`:

__verify_length
===============

.. c:function:: int __verify_length(struct vb2_buffer *vb, const struct v4l2_buffer *b)

    Verify that the bytesused value for each plane fits in the plane length and that the data offset doesn't exceed the bytesused value.

    :param struct vb2_buffer \*vb:
        *undescribed*

    :param const struct v4l2_buffer \*b:
        *undescribed*

.. _`__fill_v4l2_buffer`:

__fill_v4l2_buffer
==================

.. c:function:: void __fill_v4l2_buffer(struct vb2_buffer *vb, void *pb)

    fill in a struct v4l2_buffer with information to be returned to userspace

    :param struct vb2_buffer \*vb:
        *undescribed*

    :param void \*pb:
        *undescribed*

.. _`__fill_vb2_buffer`:

__fill_vb2_buffer
=================

.. c:function:: int __fill_vb2_buffer(struct vb2_buffer *vb, const void *pb, struct vb2_plane *planes)

    fill a vb2_buffer with information provided in a v4l2_buffer by the userspace. It also verifies that struct v4l2_buffer has a valid number of planes.

    :param struct vb2_buffer \*vb:
        *undescribed*

    :param const void \*pb:
        *undescribed*

    :param struct vb2_plane \*planes:
        *undescribed*

.. _`vb2_querybuf`:

vb2_querybuf
============

.. c:function:: int vb2_querybuf(struct vb2_queue *q, struct v4l2_buffer *b)

    query video buffer information

    :param struct vb2_queue \*q:
        videobuf queue

    :param struct v4l2_buffer \*b:
        buffer struct passed from userspace to vidioc_querybuf handler
        in driver

.. _`vb2_querybuf.description`:

Description
-----------

Should be called from vidioc_querybuf ioctl handler in driver.
This function will verify the passed v4l2_buffer structure and fill the
relevant information for the userspace.

The return values from this function are intended to be directly returned
from vidioc_querybuf handler in driver.

.. This file was automatic generated / don't edit.

