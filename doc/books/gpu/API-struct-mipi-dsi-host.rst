.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-mipi-dsi-host:

====================
struct mipi_dsi_host
====================

*man struct mipi_dsi_host(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
