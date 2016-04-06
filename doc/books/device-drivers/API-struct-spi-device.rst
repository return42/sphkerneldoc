
.. _API-struct-spi-device:

=================
struct spi_device
=================

*man struct spi_device(9)*

*4.6.0-rc1*

Master side proxy for an SPI slave device


Synopsis
========

.. code-block:: c

    struct spi_device {
      struct device dev;
      struct spi_master * master;
      u32 max_speed_hz;
      u8 chip_select;
      u8 bits_per_word;
      u16 mode;
    #define SPI_CPHA    0x01
    #define SPI_CPOL    0x02
    #define SPI_MODE_0  (0|0)
    #define SPI_MODE_1  (0|SPI_CPHA)
    #define SPI_MODE_2  (SPI_CPOL|0)
    #define SPI_MODE_3  (SPI_CPOL|SPI_CPHA)
    #define SPI_CS_HIGH 0x04
    #define SPI_LSB_FIRST   0x08
    #define SPI_3WIRE   0x10
    #define SPI_LOOP    0x20
    #define SPI_NO_CS   0x40
    #define SPI_READY   0x80
    #define SPI_TX_DUAL 0x100
    #define SPI_TX_QUAD 0x200
    #define SPI_RX_DUAL 0x400
    #define SPI_RX_QUAD 0x800
      int irq;
      void * controller_state;
      void * controller_data;
      char modalias[SPI_NAME_SIZE];
      int cs_gpio;
      struct spi_statistics statistics;
    };


Members
=======

dev
    Driver model representation of the device.

master
    SPI controller used with the device.

max_speed_hz
    Maximum clock rate to be used with this chip (on this board); may be changed by the device's driver. The spi_transfer.speed_hz can override this for each transfer.

chip_select
    Chipselect, distinguishing chips handled by ``master``.

bits_per_word
    Data transfers involve one or more words; word sizes like eight or 12 bits are common. In-memory wordsizes are powers of two bytes (e.g. 20 bit samples use 32 bits). This may
    be changed by the device's driver, or left at the default (0) indicating protocol words are eight bit bytes. The spi_transfer.bits_per_word can override this for each
    transfer.

mode
    The spi mode defines how data is clocked out and in. This may be changed by the device's driver. The “active low” default for chipselect mode can be overridden (by specifying
    SPI_CS_HIGH) as can the “MSB first” default for each word in a transfer (by specifying SPI_LSB_FIRST).

irq
    Negative, or the number passed to ``request_irq`` to receive interrupts from this device.

controller_state
    Controller's runtime state

controller_data
    Board-specific definitions for controller, such as FIFO initialization parameters; from board_info.controller_data

modalias[SPI_NAME_SIZE]
    Name of the driver to use with this device, or an alias for that name. This appears in the sysfs “modalias” attribute for driver coldplugging, and in uevents used for
    hotplugging

cs_gpio
    gpio number of the chipselect line (optional, -ENOENT when when not using a GPIO line)

statistics
    statistics for the spi_device


Description
===========

A ``spi_device`` is used to interchange data between an SPI slave (usually a discrete chip) and CPU memory.

In ``dev``, the platform_data is used to hold information about this device that's meaningful to the device's protocol driver, but not to its controller. One example might be an
identifier for a chip variant with slightly different functionality; another might be information about how this particular board wires the chip's pins.
