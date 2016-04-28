.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-v4l2-of-bus-mipi-csi2:

============================
struct v4l2_of_bus_mipi_csi2
============================

*man struct v4l2_of_bus_mipi_csi2(9)*

*4.6.0-rc5*

MIPI CSI-2 bus data structure


Synopsis
========

.. code-block:: c

    struct v4l2_of_bus_mipi_csi2 {
      unsigned int flags;
      unsigned char data_lanes[4];
      unsigned char clock_lane;
      unsigned short num_data_lanes;
      bool lane_polarities[5];
    };


Members
=======

flags
    media bus (V4L2_MBUS_*) flags

data_lanes[4]
    an array of physical data lane indexes

clock_lane
    physical lane index of the clock lane

num_data_lanes
    number of data lanes

lane_polarities[5]
    polarity of the lanes. The order is the same of the physical lanes.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
