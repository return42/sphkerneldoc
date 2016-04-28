.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-vb2-buf-ops:

==================
struct vb2_buf_ops
==================

*man struct vb2_buf_ops(9)*

*4.6.0-rc5*

driver-specific callbacks


Synopsis
========

.. code-block:: c

    struct vb2_buf_ops {
      void (* fill_user_buffer) (struct vb2_buffer *vb, void *pb);
      int (* fill_vb2_buffer) (struct vb2_buffer *vb, const void *pb,struct vb2_plane *planes);
      void (* copy_timestamp) (struct vb2_buffer *vb, const void *pb);
    };


Members
=======

fill_user_buffer
    given a vb2_buffer fill in the userspace structure. For V4L2 this
    is a struct v4l2_buffer.

fill_vb2_buffer
    given a userspace structure, fill in the vb2_buffer. If the
    userspace structure is invalid, then this op will return an error.

copy_timestamp
    copy the timestamp from a userspace structure to the vb2_buffer
    struct.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
