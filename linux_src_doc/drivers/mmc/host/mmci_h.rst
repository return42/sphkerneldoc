.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/host/mmci.h

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
        unsigned int cmdreg_cpsm_enable;
        unsigned int cmdreg_lrsp_crc;
        unsigned int cmdreg_srsp_crc;
        unsigned int cmdreg_srsp;
        unsigned int datalength_bits;
        unsigned int fifosize;
        unsigned int fifohalfsize;
        unsigned int data_cmd_enable;
        unsigned int datactrl_mask_ddrmode;
        unsigned int datactrl_mask_sdio;
        unsigned int datactrl_blocksz;
        unsigned int datactrl_dpsm_enable;
        u8 datactrl_first:1;
        u8 datacnt_useless:1;
        u8 st_sdio:1;
        u8 st_clkdiv:1;
        u8 stm32_clkdiv:1;
        u8 blksz_datactrl16:1;
        u8 blksz_datactrl4:1;
        u32 pwrreg_powerup;
        u32 f_max;
        u8 signal_direction:1;
        u8 pwrreg_clkgate:1;
        u8 busy_detect:1;
        u32 busy_dpsm_flag;
        u32 busy_detect_flag;
        u32 busy_detect_mask;
        u8 pwrreg_nopower:1;
        u8 explicit_mclk_control:1;
        u8 qcom_fifo:1;
        u8 qcom_dml:1;
        u8 reversed_irq_handling:1;
        u8 mmcimask1:1;
        unsigned int irq_pio_mask;
        u32 start_err;
        u32 opendrain;
        u8 dma_lli:1;
        u32 stm32_idmabsize_mask;
        void (*init)(struct mmci_host *host);
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

cmdreg_cpsm_enable
    enable value for CPSM

cmdreg_lrsp_crc
    enable value for long response with crc

cmdreg_srsp_crc
    enable value for short response with crc

cmdreg_srsp
    enable value for short response without crc

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

datactrl_blocksz
    *undescribed*

datactrl_dpsm_enable
    enable value for DPSM

datactrl_first
    true if data must be setup before send command

datacnt_useless
    true if you could not use datacnt register to read
    remaining data

st_sdio
    enable ST specific SDIO logic

st_clkdiv
    true if using a ST-specific clock divider algorithm

stm32_clkdiv
    true if using a STM32-specific clock divider algorithm

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
    true if the variant supports busy detection on DAT0.

busy_dpsm_flag
    bitmask enabling busy detection in the DPSM

busy_detect_flag
    bitmask identifying the bit in the MMCISTATUS register
    indicating that the card is busy

busy_detect_mask
    bitmask identifying the bit in the MMCIMASK0 to mask for
    getting busy end detection interrupts

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

mmcimask1
    true if variant have a MMCIMASK1 register.

irq_pio_mask
    bitmask used to manage interrupt pio transfert in mmcimask
    register

start_err
    bitmask identifying the STARTBITERR bit inside MMCISTATUS
    register.

opendrain
    bitmask identifying the OPENDRAIN bit inside MMCIPOWER register

dma_lli
    true if variant has dma link list feature.

stm32_idmabsize_mask
    stm32 sdmmc idma buffer size.

init
    *undescribed*

.. This file was automatic generated / don't edit.

