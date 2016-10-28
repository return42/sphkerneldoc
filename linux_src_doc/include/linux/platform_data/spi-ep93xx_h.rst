.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/spi-ep93xx.h

.. _`ep93xx_spi_info`:

struct ep93xx_spi_info
======================

.. c:type:: struct ep93xx_spi_info

    EP93xx specific SPI descriptor

.. _`ep93xx_spi_info.definition`:

Definition
----------

.. code-block:: c

    struct ep93xx_spi_info {
        int num_chipselect;
        bool use_dma;
    }

.. _`ep93xx_spi_info.members`:

Members
-------

num_chipselect
    number of chip selects on this board, must be
    at least one

use_dma
    use DMA for the transfers

.. _`ep93xx_spi_chip_ops`:

struct ep93xx_spi_chip_ops
==========================

.. c:type:: struct ep93xx_spi_chip_ops

    operation callbacks for SPI slave device

.. _`ep93xx_spi_chip_ops.definition`:

Definition
----------

.. code-block:: c

    struct ep93xx_spi_chip_ops {
        int (*setup)(struct spi_device *spi);
        void (*cleanup)(struct spi_device *spi);
        void (*cs_control)(struct spi_device *spi, int value);
    }

.. _`ep93xx_spi_chip_ops.members`:

Members
-------

setup
    setup the chip select mechanism

cleanup
    cleanup the chip select mechanism

cs_control
    control the device chip select

.. This file was automatic generated / don't edit.

