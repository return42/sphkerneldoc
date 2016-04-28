.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-spi-statistics:

=====================
struct spi_statistics
=====================

*man struct spi_statistics(9)*

*4.6.0-rc5*

statistics for spi transfers


Synopsis
========

.. code-block:: c

    struct spi_statistics {
      spinlock_t lock;
      unsigned long messages;
      unsigned long transfers;
      unsigned long errors;
      unsigned long timedout;
      unsigned long spi_sync;
      unsigned long spi_sync_immediate;
      unsigned long spi_async;
      unsigned long long bytes;
      unsigned long long bytes_rx;
      unsigned long long bytes_tx;
    #define SPI_STATISTICS_HISTO_SIZE 17
      unsigned long transfer_bytes_histo[SPI_STATISTICS_HISTO_SIZE];
      unsigned long transfers_split_maxsize;
    };


Members
=======

lock
    lock protecting this structure

messages
    number of spi-messages handled

transfers
    number of spi_transfers handled

errors
    number of errors during spi_transfer

timedout
    number of timeouts during spi_transfer

spi_sync
    number of times spi_sync is used

spi_sync_immediate
    number of times spi_sync is executed immediately in calling context
    without queuing and scheduling

spi_async
    number of times spi_async is used

bytes
    number of bytes transferred to/from device

bytes_rx
    number of bytes received from device

bytes_tx
    number of bytes sent to device

transfer_bytes_histo[SPI_STATISTICS_HISTO_SIZE]
    transfer bytes histogramm

transfers_split_maxsize
    number of transfers that have been split because of maxsize limit


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
