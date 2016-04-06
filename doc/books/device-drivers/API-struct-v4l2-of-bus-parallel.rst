
.. _API-struct-v4l2-of-bus-parallel:

===========================
struct v4l2_of_bus_parallel
===========================

*man struct v4l2_of_bus_parallel(9)*

*4.6.0-rc1*

parallel data bus data structure


Synopsis
========

.. code-block:: c

    struct v4l2_of_bus_parallel {
      unsigned int flags;
      unsigned char bus_width;
      unsigned char data_shift;
    };


Members
=======

flags
    media bus (V4L2_MBUS_⋆) flags

bus_width
    bus width in bits

data_shift
    data shift in bits
