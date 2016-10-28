.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/spi/xilinx_spi.h

.. _`xspi_platform_data`:

struct xspi_platform_data
=========================

.. c:type:: struct xspi_platform_data

    Platform data of the Xilinx SPI driver

.. _`xspi_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct xspi_platform_data {
        u16 num_chipselect;
        u8 bits_per_word;
        struct spi_board_info *devices;
        u8 num_devices;
    }

.. _`xspi_platform_data.members`:

Members
-------

num_chipselect
    Number of chip select by the IP.

bits_per_word
    Number of bits per word.

devices
    Devices to add when the driver is probed.

num_devices
    Number of devices in the devices array.

.. This file was automatic generated / don't edit.

