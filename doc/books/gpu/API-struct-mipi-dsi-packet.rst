
.. _API-struct-mipi-dsi-packet:

======================
struct mipi_dsi_packet
======================

*man struct mipi_dsi_packet(9)*

*4.6.0-rc1*

represents a MIPI DSI packet in protocol format


Synopsis
========

.. code-block:: c

    struct mipi_dsi_packet {
      size_t size;
      u8 header[4];
      size_t payload_length;
      const u8 * payload;
    };


Members
=======

size
    size (in bytes) of the packet

header[4]
    the four bytes that make up the header (Data ID, Word Count or Packet Data, and ECC)

payload_length
    number of bytes in the payload

payload
    a pointer to a buffer containing the payload, if any
