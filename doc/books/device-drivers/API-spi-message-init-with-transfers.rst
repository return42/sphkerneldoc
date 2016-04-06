
.. _API-spi-message-init-with-transfers:

===============================
spi_message_init_with_transfers
===============================

*man spi_message_init_with_transfers(9)*

*4.6.0-rc1*

Initialize spi_message and append transfers


Synopsis
========

.. c:function:: void spi_message_init_with_transfers( struct spi_message * m, struct spi_transfer * xfers, unsigned int num_xfers )

Arguments
=========

``m``
    spi_message to be initialized

``xfers``
    An array of spi transfers

``num_xfers``
    Number of items in the xfer array


Description
===========

This function initializes the given spi_message and adds each spi_transfer in the given array to the message.
