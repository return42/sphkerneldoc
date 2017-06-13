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
        int *chipselect;
        int num_chipselect;
        bool use_dma;
    }

.. _`ep93xx_spi_info.members`:

Members
-------

chipselect
    array of gpio numbers to use as chip selects

num_chipselect
    ARRAY_SIZE(chipselect)

use_dma
    use DMA for the transfers

.. This file was automatic generated / don't edit.

