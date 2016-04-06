
.. _API-mipi-dsi-packet-format-is-short:

===============================
mipi_dsi_packet_format_is_short
===============================

*man mipi_dsi_packet_format_is_short(9)*

*4.6.0-rc1*

check if a packet is of the short format


Synopsis
========

.. c:function:: bool mipi_dsi_packet_format_is_short( u8 type )

Arguments
=========

``type``
    MIPI DSI data type of the packet


Return
======

true if the packet for the given data type is a short packet, false otherwise.
