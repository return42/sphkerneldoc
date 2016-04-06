
.. _API-struct-mipi-dsi-msg:

===================
struct mipi_dsi_msg
===================

*man struct mipi_dsi_msg(9)*

*4.6.0-rc1*

read/write DSI buffer


Synopsis
========

.. code-block:: c

    struct mipi_dsi_msg {
      u8 channel;
      u8 type;
      u16 flags;
      size_t tx_len;
      const void * tx_buf;
      size_t rx_len;
      void * rx_buf;
    };


Members
=======

channel
    virtual channel id

type
    payload data type

flags
    flags controlling this message transmission

tx_len
    length of ``tx_buf``

tx_buf
    data to be written

rx_len
    length of ``rx_buf``

rx_buf
    data to be read, or NULL
