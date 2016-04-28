.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-spi-board-info:

=====================
struct spi_board_info
=====================

*man struct spi_board_info(9)*

*4.6.0-rc5*

board-specific template for a SPI device


Synopsis
========

.. code-block:: c

    struct spi_board_info {
      char modalias[SPI_NAME_SIZE];
      const void * platform_data;
      void * controller_data;
      int irq;
      u32 max_speed_hz;
      u16 bus_num;
      u16 chip_select;
      u16 mode;
    };


Members
=======

modalias[SPI_NAME_SIZE]
    Initializes spi_device.modalias; identifies the driver.

platform_data
    Initializes spi_device.platform_data; the particular data stored
    there is driver-specific.

controller_data
    Initializes spi_device.controller_data; some controllers need
    hints about hardware setup, e.g. for DMA.

irq
    Initializes spi_device.irq; depends on how the board is wired.

max_speed_hz
    Initializes spi_device.max_speed_hz; based on limits from the
    chip datasheet and board-specific signal quality issues.

bus_num
    Identifies which spi_master parents the spi_device; unused by
    ``spi_new_device``, and otherwise depends on board wiring.

chip_select
    Initializes spi_device.chip_select; depends on how the board is
    wired.

mode
    Initializes spi_device.mode; based on the chip datasheet, board
    wiring (some devices support both 3WIRE and standard modes), and
    possibly presence of an inverter in the chipselect path.


Description
===========

When adding new SPI devices to the device tree, these structures serve
as a partial device template. They hold information which can't always
be determined by drivers. Information that ``probe`` can establish (such
as the default transfer wordsize) is not included here.

These structures are used in two places. Their primary role is to be
stored in tables of board-specific device descriptors, which are
declared early in board initialization and then used (much later) to
populate a controller's device tree after the that controller's driver
initializes. A secondary (and atypical) role is as a parameter to
``spi_new_device`` call, which happens after those controller drivers
are active in some dynamic board configuration models.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
