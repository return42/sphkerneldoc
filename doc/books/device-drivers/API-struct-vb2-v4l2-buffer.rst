
.. _API-struct-vb2-v4l2-buffer:

======================
struct vb2_v4l2_buffer
======================

*man struct vb2_v4l2_buffer(9)*

*4.6.0-rc1*

video buffer information for v4l2


Synopsis
========

.. code-block:: c

    struct vb2_v4l2_buffer {
      struct vb2_buffer vb2_buf;
      __u32 flags;
      __u32 field;
      struct v4l2_timecode timecode;
      __u32 sequence;
    };


Members
=======

vb2_buf
    video buffer 2

flags
    buffer informational flags

field
    enum v4l2_field; field order of the image in the buffer

timecode
    frame timecode

sequence
    sequence count of this frame Should contain enough information to be able to cover all the fields of struct v4l2_buffer at videodev2.h
