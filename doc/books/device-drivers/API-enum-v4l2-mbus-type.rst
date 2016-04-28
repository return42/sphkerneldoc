.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-v4l2-mbus-type:

===================
enum v4l2_mbus_type
===================

*man enum v4l2_mbus_type(9)*

*4.6.0-rc5*

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
    parallel interface with embedded synchronisation, can also be used
    for BT.1120

V4L2_MBUS_CSI2
    MIPI CSI-2 serial interface


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
