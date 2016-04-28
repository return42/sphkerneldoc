.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-mipi-dsi-device-info:

===========================
struct mipi_dsi_device_info
===========================

*man struct mipi_dsi_device_info(9)*

*4.6.0-rc5*

template for creating a mipi_dsi_device


Synopsis
========

.. code-block:: c

    struct mipi_dsi_device_info {
      char type[DSI_DEV_NAME_SIZE];
      u32 channel;
      struct device_node * node;
    };


Members
=======

type[DSI_DEV_NAME_SIZE]
    DSI peripheral chip type

channel
    DSI virtual channel assigned to peripheral

node
    pointer to OF device node or NULL


Description
===========

This is populated and passed to mipi_dsi_device_new to create a new
DSI device


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
