
.. _API-struct-vb2-buffer:

=================
struct vb2_buffer
=================

*man struct vb2_buffer(9)*

*4.6.0-rc1*

represents a video buffer


Synopsis
========

.. code-block:: c

    struct vb2_buffer {
      struct vb2_queue * vb2_queue;
      unsigned int index;
      unsigned int type;
      unsigned int memory;
      unsigned int num_planes;
      struct vb2_plane planes[VB2_MAX_PLANES];
      u64 timestamp;
    };


Members
=======

vb2_queue
    the queue to which this driver belongs

index
    id number of the buffer

type
    buffer type

memory
    the method, in which the actual data is passed

num_planes
    number of planes in the buffer on an internal driver queue

planes[VB2_MAX_PLANES]
    private per-plane information; do not change

timestamp
    frame timestamp in ns
