.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-sync-transfer:

=================
spi_sync_transfer
=================

*man spi_sync_transfer(9)*

*4.6.0-rc5*

synchronous SPI data transfer


Synopsis
========

.. c:function:: int spi_sync_transfer( struct spi_device * spi, struct spi_transfer * xfers, unsigned int num_xfers )

Arguments
=========

``spi``
    device with which data will be exchanged

``xfers``
    An array of spi_transfers

``num_xfers``
    Number of items in the xfer array


Context
=======

can sleep


Description
===========

Does a synchronous SPI data transfer of the given spi_transfer array.

For more specific semantics see ``spi_sync``.


Return
======

Return: zero on success, else a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
