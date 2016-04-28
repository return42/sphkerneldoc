.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-message-init-with-transfers:

===============================
spi_message_init_with_transfers
===============================

*man spi_message_init_with_transfers(9)*

*4.6.0-rc5*

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

This function initializes the given spi_message and adds each
spi_transfer in the given array to the message.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
