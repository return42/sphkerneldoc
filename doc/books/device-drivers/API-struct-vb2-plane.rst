
.. _API-struct-vb2-plane:

================
struct vb2_plane
================

*man struct vb2_plane(9)*

*4.6.0-rc1*

plane information


Synopsis
========

.. code-block:: c

    struct vb2_plane {
      void * mem_priv;
      struct dma_buf * dbuf;
      unsigned int dbuf_mapped;
      unsigned int bytesused;
      unsigned int length;
      unsigned int min_length;
      union m;
      unsigned int data_offset;
    };


Members
=======

mem_priv
    private data with this plane

dbuf
    dma_buf - shared buffer object

dbuf_mapped
    flag to show whether dbuf is mapped or not

bytesused
    number of bytes occupied by data in the plane (payload)

length
    size of this plane (NOT the payload) in bytes

min_length
    minimum required size of this plane (NOT the payload) in bytes. ``length`` is always greater or equal to ``min_length``.

m
    Union with memtype-specific data (``offset``, ``userptr`` or ``fd``).

data_offset
    offset in the plane to the start of data; usually 0, unless there is a header in front of the data Should contain enough information to be able to cover all the fields of
    struct v4l2_plane at videodev2.h
