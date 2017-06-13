.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi-s3c64xx.c

.. _`s3c64xx_spi_port_config`:

struct s3c64xx_spi_port_config
==============================

.. c:type:: struct s3c64xx_spi_port_config

    SPI Controller hardware info

.. _`s3c64xx_spi_port_config.definition`:

Definition
----------

.. code-block:: c

    struct s3c64xx_spi_port_config {
        int fifo_lvl_mask;
        int rx_lvl_offset;
        int tx_st_done;
        int quirks;
        bool high_speed;
        bool clk_from_cmu;
        bool clk_ioclk;
    }

.. _`s3c64xx_spi_port_config.members`:

Members
-------

fifo_lvl_mask
    Bit-mask for {TX\|RX}_FIFO_LVL bits in SPI_STATUS register.

rx_lvl_offset
    Bit offset of RX_FIFO_LVL bits in SPI_STATUS regiter.

tx_st_done
    Bit offset of TX_DONE bit in SPI_STATUS regiter.

quirks
    *undescribed*

high_speed
    True, if the controller supports HIGH_SPEED_EN bit.

clk_from_cmu
    True, if the controller does not include a clock mux and
    prescaler unit.

clk_ioclk
    *undescribed*

.. _`s3c64xx_spi_port_config.description`:

Description
-----------

The Samsung s3c64xx SPI controller are used on various Samsung SoC's but
differ in some aspects such as the size of the fifo and spi bus clock
setup. Such differences are specified to the driver using this structure
which is provided as driver data to the driver.

.. _`s3c64xx_spi_driver_data`:

struct s3c64xx_spi_driver_data
==============================

.. c:type:: struct s3c64xx_spi_driver_data

    Runtime info holder for SPI driver.

.. _`s3c64xx_spi_driver_data.definition`:

Definition
----------

.. code-block:: c

    struct s3c64xx_spi_driver_data {
        void __iomem *regs;
        struct clk *clk;
        struct clk *src_clk;
        struct clk *ioclk;
        struct platform_device *pdev;
        struct spi_master *master;
        struct s3c64xx_spi_info *cntrlr_info;
        struct spi_device *tgl_spi;
        spinlock_t lock;
        unsigned long sfr_start;
        struct completion xfer_completion;
        unsigned state;
        unsigned cur_mode;
        unsigned cur_bpw;
        unsigned cur_speed;
        struct s3c64xx_spi_dma_data rx_dma;
        struct s3c64xx_spi_dma_data tx_dma;
        struct s3c64xx_spi_port_config *port_conf;
        unsigned int port_id;
    }

.. _`s3c64xx_spi_driver_data.members`:

Members
-------

regs
    Pointer to ioremap'ed controller registers.

clk
    Pointer to the spi clock.

src_clk
    Pointer to the clock used to generate SPI signals.

ioclk
    Pointer to the i/o clock between master and slave

pdev
    *undescribed*

master
    Pointer to the SPI Protocol master.

cntrlr_info
    Platform specific data for the controller this driver manages.

tgl_spi
    Pointer to the last CS left untoggled by the cs_change hint.

lock
    Controller specific lock.

sfr_start
    BUS address of SPI controller regs.

xfer_completion
    To indicate completion of xfer task.

state
    Set of FLAGS to indicate status.

cur_mode
    Stores the active configuration of the controller.

cur_bpw
    Stores the active bits per word settings.

cur_speed
    Stores the active xfer clock speed.

rx_dma
    *undescribed*

tx_dma
    *undescribed*

port_conf
    *undescribed*

port_id
    *undescribed*

.. This file was automatic generated / don't edit.

