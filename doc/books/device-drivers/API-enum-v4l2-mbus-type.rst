
.. _API-enum-v4l2-mbus-type:

===================
enum v4l2_mbus_type
===================

*man enum v4l2_mbus_type(9)*

*4.6.0-rc1*

media bus type


Synopsis
========

.. code-block:: c

    enum v4l2_mbus_type {
      V4L2_MBUS_PARALLEL,
      V4L2_MBUS_BT656,
      V4L2_MBUS_CSI2
    };


Constants
=========

V4L2_MBUS_PARALLEL
    parallel interface with hsync and vsync

V4L2_MBUS_BT656
    parallel interface with embedded synchronisation, can also be used for BT.1120

V4L2_MBUS_CSI2
    MIPI CSI-2 serial interface
