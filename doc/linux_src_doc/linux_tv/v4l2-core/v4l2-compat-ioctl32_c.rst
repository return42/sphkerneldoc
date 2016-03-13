.. -*- coding: utf-8; mode: rst -*-

=====================
v4l2-compat-ioctl32.c
=====================



.. _xref_struct_v4l2_create_buffers32:

struct v4l2_create_buffers32
============================

.. c:type:: struct v4l2_create_buffers32

    VIDIOC_CREATE_BUFS32 argument



Definition
----------

.. code-block:: c

  struct v4l2_create_buffers32 {
    __u32 index;
    __u32 count;
    __u32 memory;
    struct v4l2_format32 format;
    __u32 reserved[8];
  };



Members
-------

:``__u32 index``:
    on return, index of the first created buffer

:``__u32 count``:
    entry: number of requested buffers,

:``__u32 memory``:
    buffer memory type

:``struct v4l2_format32 format``:
    frame format, for which buffers are requested

:``__u32 reserved[8]``:
    future extensions




return
------

number of created buffers


