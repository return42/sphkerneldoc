
.. _API-mipi-dsi-packet-format-is-long:

==============================
mipi_dsi_packet_format_is_long
==============================

*man mipi_dsi_packet_format_is_long(9)*

*4.6.0-rc1*

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

true if the packet for the given data type is a long packet, false otherwise.
