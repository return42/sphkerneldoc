
.. _API-struct-mipi-dsi-device:

======================
struct mipi_dsi_device
======================

*man struct mipi_dsi_device(9)*

*4.6.0-rc1*

DSI peripheral device


Synopsis
========

.. code-block:: c

    struct mipi_dsi_device {
      struct mipi_dsi_host * host;
      struct device dev;
      char name[DSI_DEV_NAME_SIZE];
      unsigned int channel;
      unsigned int lanes;
      enum mipi_dsi_pixel_format format;
      unsigned long mode_flags;
    };


Members
=======

host
    DSI host for this peripheral

dev
    driver model device node for this peripheral

name[DSI_DEV_NAME_SIZE]
    DSI peripheral chip type

channel
    virtual channel assigned to the peripheral

lanes
    number of active data lanes

format
    pixel format for video mode

mode_flags
    DSI operation mode related flags
