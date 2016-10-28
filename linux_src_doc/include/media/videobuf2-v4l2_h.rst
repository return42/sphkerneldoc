.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/videobuf2-v4l2.h

.. _`vb2_v4l2_buffer`:

struct vb2_v4l2_buffer
======================

.. c:type:: struct vb2_v4l2_buffer

    video buffer information for v4l2

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
    video buffer 2

flags
    buffer informational flags

field
    enum v4l2_field; field order of the image in the buffer

timecode
    frame timecode

sequence
    sequence count of this frame
    Should contain enough information to be able to cover all the fields
    of struct v4l2_buffer at videodev2.h

.. This file was automatic generated / don't edit.

