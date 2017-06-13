.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/fsmc_nand.c

.. _`fsmc_nand_data`:

struct fsmc_nand_data
=====================

.. c:type:: struct fsmc_nand_data

    structure for FSMC NAND device state

.. _`fsmc_nand_data.definition`:

Definition
----------

.. code-block:: c

    struct fsmc_nand_data {
        u32 pid;
        struct nand_chip nand;
        unsigned int bank;
        struct device *dev;
        enum access_mode mode;
        struct clk *clk;
        struct dma_chan *read_dma_chan;
        struct dma_chan *write_dma_chan;
        struct completion dma_access_complete;
        struct fsmc_nand_timings *dev_timings;
        dma_addr_t data_pa;
        void __iomem *data_va;
        void __iomem *cmd_va;
        void __iomem *addr_va;
        void __iomem *regs_va;
    }

.. _`fsmc_nand_data.members`:

Members
-------

pid
    Part ID on the AMBA PrimeCell format

nand
    Chip related info for a NAND flash.

bank
    Bank number for probed device.

dev
    *undescribed*

mode
    *undescribed*

clk
    Clock structure for FSMC.

read_dma_chan
    DMA channel for read access

write_dma_chan
    DMA channel for write access to NAND

dma_access_complete
    Completion structure

dev_timings
    *undescribed*

data_pa
    NAND Physical port for Data.

data_va
    NAND port for Data.

cmd_va
    NAND port for Command.

addr_va
    NAND port for Address.

regs_va
    FSMC regs base address.

.. This file was automatic generated / don't edit.

