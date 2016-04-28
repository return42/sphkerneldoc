.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-spi-driver:

=================
struct spi_driver
=================

*man struct spi_driver(9)*

*4.6.0-rc5*

Host side “protocol” driver


Synopsis
========

.. code-block:: c

    struct spi_driver {
      const struct spi_device_id * id_table;
      int (* probe) (struct spi_device *spi);
      int (* remove) (struct spi_device *spi);
      void (* shutdown) (struct spi_device *spi);
      struct device_driver driver;
    };


Members
=======

id_table
    List of SPI devices supported by this driver

probe
    Binds this driver to the spi device. Drivers can verify that the
    device is actually present, and may need to configure
    characteristics (such as bits_per_word) which weren't needed for
    the initial configuration done during system setup.

remove
    Unbinds this driver from the spi device

shutdown
    Standard shutdown callback used during system state transitions such
    as powerdown/halt and kexec

driver
    SPI device drivers should initialize the name and owner field of
    this structure.


Description
===========

This represents the kind of device driver that uses SPI messages to
interact with the hardware at the other end of a SPI link. It's called a
“protocol” driver because it works through messages rather than talking
directly to SPI hardware (which is what the underlying SPI controller
driver does to pass those messages). These protocols are defined in the
specification for the device(s) supported by the driver.

As a rule, those device protocols represent the lowest level interface
supported by a driver, and it will support upper level interfaces too.
Examples of such upper levels include frameworks like MTD, networking,
MMC, RTC, filesystem character device nodes, and hardware monitoring.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
