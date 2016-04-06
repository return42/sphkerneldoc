
.. _API-struct-mipi-dsi-host:

====================
struct mipi_dsi_host
====================

*man struct mipi_dsi_host(9)*

*4.6.0-rc1*

DSI host device


Synopsis
========

.. code-block:: c

    struct mipi_dsi_host {
      struct device * dev;
      const struct mipi_dsi_host_ops * ops;
      struct list_head list;
    };


Members
=======

dev
    driver model device node for this DSI host

ops
    DSI host operations

list
    list management
