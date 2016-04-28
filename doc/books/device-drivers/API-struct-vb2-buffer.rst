.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-vb2-buffer:

=================
struct vb2_buffer
=================

*man struct vb2_buffer(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
