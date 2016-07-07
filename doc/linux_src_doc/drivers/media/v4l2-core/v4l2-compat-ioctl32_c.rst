.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/v4l2-core/v4l2-compat-ioctl32.c

.. _`v4l2_create_buffers32`:

struct v4l2_create_buffers32
============================

.. c:type:: struct v4l2_create_buffers32

    VIDIOC_CREATE_BUFS32 argument

.. _`v4l2_create_buffers32.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_create_buffers32 {
        __u32 index;
        __u32 count;
        __u32 memory;
        struct v4l2_format32 format;
        __u32 reserved[8];
    }

.. _`v4l2_create_buffers32.members`:

Members
-------

index
    on return, index of the first created buffer

count
    entry: number of requested buffers,
    return: number of created buffers

memory
    buffer memory type

format
    frame format, for which buffers are requested

reserved
    future extensions

.. This file was automatic generated / don't edit.

