.. -*- coding: utf-8; mode: rst -*-

.. _API-mipi-dsi-packet-format-is-long:

==============================
mipi_dsi_packet_format_is_long
==============================

*man mipi_dsi_packet_format_is_long(9)*

*4.6.0-rc5*

check if a packet is of the long format


Synopsis
========

.. c:function:: bool mipi_dsi_packet_format_is_long( u8 type )

Arguments
=========

``type``
    MIPI DSI data type of the packet


Return
======

true if the packet for the given data type is a long packet, false
otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
