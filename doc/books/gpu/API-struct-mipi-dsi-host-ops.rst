.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-mipi-dsi-host-ops:

========================
struct mipi_dsi_host_ops
========================

*man struct mipi_dsi_host_ops(9)*

*4.6.0-rc5*

DSI bus operations


Synopsis
========

.. code-block:: c

    struct mipi_dsi_host_ops {
      int (* attach) (struct mipi_dsi_host *host,struct mipi_dsi_device *dsi);
      int (* detach) (struct mipi_dsi_host *host,struct mipi_dsi_device *dsi);
      ssize_t (* transfer) (struct mipi_dsi_host *host,const struct mipi_dsi_msg *msg);
    };


Members
=======

attach
    attach DSI device to DSI host

detach
    detach DSI device from DSI host

transfer
    transmit a DSI packet


Description
===========

DSI packets transmitted by .\ ``transfer`` are passed in as
mipi_dsi_msg structures. This structure contains information about the
type of packet being transmitted as well as the transmit and receive
buffers. When an error is encountered during transmission, this function
will return a negative error code. On success it shall return the number
of bytes transmitted for write packets or the number of bytes received
for read packets.

Note that typically DSI packet transmission is atomic, so the
.\ ``transfer`` function will seldomly return anything other than the
number of bytes contained in the transmit buffer on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
