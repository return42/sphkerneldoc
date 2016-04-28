.. -*- coding: utf-8; mode: rst -*-

.. _API-mipi-dsi-create-packet:

======================
mipi_dsi_create_packet
======================

*man mipi_dsi_create_packet(9)*

*4.6.0-rc5*

create a packet from a message according to the DSI protocol


Synopsis
========

.. c:function:: int mipi_dsi_create_packet( struct mipi_dsi_packet * packet, const struct mipi_dsi_msg * msg )

Arguments
=========

``packet``
    pointer to a DSI packet structure

``msg``
    message to translate into a packet


Return
======

0 on success or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
