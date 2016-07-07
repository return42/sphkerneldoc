.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/host/mmci.c

.. _`variant_data`:

struct variant_data
===================

.. c:type:: struct variant_data

    MMCI variant-specific quirks

.. _`variant_data.definition`:

Definition
----------

.. code-block:: c

    struct variant_data {
        unsigned int clkreg;
        unsigned int clkreg_enable;
        unsigned int clkreg_8bit_bus_enable;
        unsigned int clkreg_neg_edge_enable;
        unsigned int datalength_bits;
        unsigned int fifosize;
        unsigned int fifohalfsize;
        unsigned int data_cmd_enable;
        unsigned int datactrl_mask_ddrmode;
        unsigned int datactrl_mask_sdio;
        bool st_sdio;
        bool st_clkdiv;
        bool blksz_datactrl16;
        bool blksz_datactrl4;
        u32 pwrreg_powerup;
        u32 f_max;
        bool signal_direction;
        bool pwrreg_clkgate;
        bool busy_detect;
        bool pwrreg_nopower;
        bool explicit_mclk_control;
        bool qcom_fifo;
        bool qcom_dml;
        bool reversed_irq_handling;
    }

.. _`variant_data.members`:

Members
-------

clkreg
    default value for MCICLOCK register

clkreg_enable
    enable value for MMCICLOCK register

clkreg_8bit_bus_enable
    enable value for 8 bit bus

clkreg_neg_edge_enable
    enable value for inverted data/cmd output

datalength_bits
    number of bits in the MMCIDATALENGTH register

fifosize
    number of bytes that can be written when MMCI_TXFIFOEMPTY
    is asserted (likewise for RX)

fifohalfsize
    number of bytes that can be written when MCI_TXFIFOHALFEMPTY
    is asserted (likewise for RX)

data_cmd_enable
    enable value for data commands.

datactrl_mask_ddrmode
    ddr mode mask in datactrl register.

datactrl_mask_sdio
    SDIO enable mask in datactrl register

st_sdio
    enable ST specific SDIO logic

st_clkdiv
    true if using a ST-specific clock divider algorithm

blksz_datactrl16
    true if Block size is at b16..b30 position in datactrl register

blksz_datactrl4
    true if Block size is at b4..b16 position in datactrl
    register

pwrreg_powerup
    power up value for MMCIPOWER register

f_max
    maximum clk frequency supported by the controller.

signal_direction
    input/out direction of bus signals can be indicated

pwrreg_clkgate
    MMCIPOWER register must be used to gate the clock

busy_detect
    true if busy detection on dat0 is supported

pwrreg_nopower
    bits in MMCIPOWER don't controls ext. power supply

explicit_mclk_control
    enable explicit mclk control in driver.

qcom_fifo
    enables qcom specific fifo pio read logic.

qcom_dml
    enables qcom specific dma glue for dma transfers.

reversed_irq_handling
    handle data irq before cmd irq.

.. This file was automatic generated / don't edit.

