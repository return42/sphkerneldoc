
.. _API-struct-vb2-queue:

================
struct vb2_queue
================

*man struct vb2_queue(9)*

*4.6.0-rc1*

a videobuf queue


Synopsis
========

.. code-block:: c

    struct vb2_queue {
      unsigned int type;
      unsigned int io_modes;
      unsigned fileio_read_once:1;
      unsigned fileio_write_immediately:1;
      unsigned allow_zero_bytesused:1;
      struct mutex * lock;
      void * owner;
      const struct vb2_ops * ops;
      const struct vb2_mem_ops * mem_ops;
      const struct vb2_buf_ops * buf_ops;
      void * drv_priv;
      unsigned int buf_struct_size;
      u32 timestamp_flags;
      gfp_t gfp_flags;
      u32 min_buffers_needed;
    };


Members
=======

type
    private buffer type whose content is defined by the vb2-core caller. For example, for V4L2, it should match the V4L2_BUF_TYPE_⋆ in include/uapi/linux/videodev2.h

io_modes
    supported io methods (see vb2_io_modes enum)

fileio_read_once
    report EOF after reading the first buffer

fileio_write_immediately
    queue buffer after each ``write`` call

allow_zero_bytesused
    allow bytesused == 0 to be passed to the driver

lock
    pointer to a mutex that protects the vb2_queue struct. The driver can set this to a mutex to let the v4l2 core serialize the queuing ioctls. If the driver wants to handle
    locking itself, then this should be set to NULL. This lock is not used by the videobuf2 core API.

owner
    The filehandle that 'owns' the buffers, i.e. the filehandle that called reqbufs, create_buffers or started fileio. This field is not used by the videobuf2 core API, but it
    allows drivers to easily associate an owner filehandle with the queue.

ops
    driver-specific callbacks

mem_ops
    memory allocator specific callbacks

buf_ops
    callbacks to deliver buffer information between user-space and kernel-space

drv_priv
    driver private data

buf_struct_size
    size of the driver-specific buffer structure; “0” indicates the driver doesn't want to use a custom buffer structure type. for example, sizeof(struct vb2_v4l2_buffer) will be
    used for v4l2.

timestamp_flags
    Timestamp flags; V4L2_BUF_FLAG_TIMESTAMP_⋆ and V4L2_BUF_FLAG_TSTAMP_SRC_⋆

gfp_flags
    additional gfp flags used when allocating the buffers. Typically this is 0, but it may be e.g. GFP_DMA or __GFP_DMA32 to force the buffer allocation to a specific memory
    zone.

min_buffers_needed
    the minimum number of buffers needed before ``start_streaming`` can be called. Used when a DMA engine cannot be started unless at least this number of buffers have been queued
    into the driver.
