.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/spi-s3c64xx.h

.. _`s3c64xx_spi_csinfo`:

struct s3c64xx_spi_csinfo
=========================

.. c:type:: struct s3c64xx_spi_csinfo

    ChipSelect description

.. _`s3c64xx_spi_csinfo.definition`:

Definition
----------

.. code-block:: c

    struct s3c64xx_spi_csinfo {
        u8 fb_delay;
        unsigned line;
    }

.. _`s3c64xx_spi_csinfo.members`:

Members
-------

fb_delay
    Slave specific feedback delay.
    Refer to FB_CLK_SEL register definition in SPI chapter.

line
    Custom 'identity' of the CS line.

.. _`s3c64xx_spi_csinfo.description`:

Description
-----------

This is per SPI-Slave Chipselect information.
Allocate and initialize one in machine init code and make the
spi_board_info.controller_data point to it.

.. _`s3c64xx_spi_info`:

struct s3c64xx_spi_info
=======================

.. c:type:: struct s3c64xx_spi_info

    SPI Controller defining structure

.. _`s3c64xx_spi_info.definition`:

Definition
----------

.. code-block:: c

    struct s3c64xx_spi_info {
        int src_clk_nr;
        int num_cs;
        bool no_cs;
        int (*cfg_gpio)(void);
        dma_filter_fn filter;
        void *dma_tx;
        void *dma_rx;
    }

.. _`s3c64xx_spi_info.members`:

Members
-------

src_clk_nr
    Clock source index for the CLK_CFG[SPI_CLKSEL] field.

num_cs
    Number of CS this controller emulates.

no_cs
    *undescribed*

cfg_gpio
    Configure pins for this SPI controller.

filter
    *undescribed*

dma_tx
    *undescribed*

dma_rx
    *undescribed*

.. _`s3c64xx_spi0_set_platdata`:

s3c64xx_spi0_set_platdata
=========================

.. c:function:: void s3c64xx_spi0_set_platdata(int (*cfg_gpio)(void), int src_clk_nr, int num_cs)

    SPI Controller configure callback by the board initialization code.

    :param int (\*cfg_gpio)(void):
        Pointer to gpio setup function.

    :param int src_clk_nr:
        Clock the SPI controller is to use to generate SPI clocks.

    :param int num_cs:
        Number of elements in the 'cs' array.

.. _`s3c64xx_spi0_set_platdata.description`:

Description
-----------

Call this from machine init code for each SPI Controller that
has some chips attached to it.

.. This file was automatic generated / don't edit.

