.. -*- coding: utf-8; mode: rst -*-

.. _spi:

=================================
Serial Peripheral Interface (SPI)
=================================

SPI is the "Serial Peripheral Interface", widely used with embedded
systems because it is a simple and efficient interface: basically a
multiplexed shift register. Its three signal wires hold a clock (SCK,
often in the range of 1-20 MHz), a "Master Out, Slave In" (MOSI) data
line, and a "Master In, Slave Out" (MISO) data line. SPI is a full
duplex protocol; for each bit shifted out the MOSI line (one per clock)
another is shifted in on the MISO line. Those bits are assembled into
words of various sizes on the way to and from system memory. An
additional chipselect line is usually active-low (nCS); four signals are
normally used for each peripheral, plus sometimes an interrupt.

The SPI bus facilities listed here provide a generalized interface to
declare SPI busses and devices, manage them according to the standard
Linux driver model, and perform input/output operations. At this time,
only "master" side interfaces are supported, where Linux talks to SPI
peripherals and does not implement such a peripheral itself. (Interfaces
to support implementing SPI slaves would necessarily look different.)

The programming interface is structured around two kinds of driver, and
two kinds of device. A "Controller Driver" abstracts the controller
hardware, which may be as simple as a set of GPIO pins or as complex as
a pair of FIFOs connected to dual DMA engines on the other side of the
SPI shift register (maximizing throughput). Such drivers bridge between
whatever bus they sit on (often the platform bus) and SPI, and expose
the SPI side of their device as a ``struct spi_master``. SPI devices are
children of that master, represented as a ``struct spi_device`` and
manufactured from ``struct spi_board_info`` descriptors which are
usually provided by board-specific initialization code. A
``struct spi_driver`` is called a "Protocol Driver", and is bound to a
spi_device using normal driver model calls.

The I/O model is a set of queued messages. Protocol drivers submit one
or more ``struct spi_message`` objects, which are processed and
completed asynchronously. (There are synchronous wrappers, however.)
Messages are built from one or more ``struct spi_transfer`` objects,
each of which wraps a full duplex SPI transfer. A variety of protocol
tweaking options are needed, because different chips adopt very
different policies for how they use the bits transferred with SPI.


.. toctree::
    :maxdepth: 1

    API-struct-spi-statistics
    API-struct-spi-device
    API-struct-spi-driver
    API-spi-unregister-driver
    API-module-spi-driver
    API-struct-spi-master
    API-struct-spi-res
    API-struct-spi-transfer
    API-struct-spi-message
    API-spi-message-init-with-transfers
    API-struct-spi-replaced-transfers
    API-spi-write
    API-spi-read
    API-spi-sync-transfer
    API-spi-w8r8
    API-spi-w8r16
    API-spi-w8r16be
    API-struct-spi-flash-read-message
    API-struct-spi-board-info
    API-spi-register-board-info
    API---spi-register-driver
    API-spi-alloc-device
    API-spi-add-device
    API-spi-new-device
    API-spi-unregister-device
    API-spi-finalize-current-transfer
    API-spi-get-next-queued-message
    API-spi-finalize-current-message
    API-spi-alloc-master
    API-spi-register-master
    API-devm-spi-register-master
    API-spi-unregister-master
    API-spi-busnum-to-master
    API-spi-res-alloc
    API-spi-res-free
    API-spi-res-add
    API-spi-res-release
    API-spi-replace-transfers
    API-spi-split-transfers-maxsize
    API-spi-setup
    API-spi-async
    API-spi-async-locked
    API-spi-sync
    API-spi-sync-locked
    API-spi-bus-lock
    API-spi-bus-unlock
    API-spi-write-then-read




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
