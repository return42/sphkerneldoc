.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/spi-nor/intel-spi.c

.. _`intel_spi`:

struct intel_spi
================

.. c:type:: struct intel_spi

    Driver private data

.. _`intel_spi.definition`:

Definition
----------

.. code-block:: c

    struct intel_spi {
        struct device *dev;
        const struct intel_spi_boardinfo *info;
        struct spi_nor nor;
        void __iomem *base;
        void __iomem *pregs;
        void __iomem *sregs;
        size_t nregions;
        size_t pr_num;
        bool writeable;
        bool locked;
        bool swseq_reg;
        bool swseq_erase;
        bool erase_64k;
        u8 atomic_preopcode;
        u8 opcodes[8];
    }

.. _`intel_spi.members`:

Members
-------

dev
    Device pointer

info
    Pointer to board specific info

nor
    SPI NOR layer structure

base
    Beginning of MMIO space

pregs
    Start of protection registers

sregs
    Start of software sequencer registers

nregions
    Maximum number of regions

pr_num
    Maximum number of protected range registers

writeable
    Is the chip writeable

locked
    Is SPI setting locked

swseq_reg
    Use SW sequencer in register reads/writes

swseq_erase
    Use SW sequencer in erase operation

erase_64k
    64k erase supported

atomic_preopcode
    Holds preopcode when atomic sequence is requested

opcodes
    Opcodes which are supported. This are programmed by BIOS
    before it locks down the controller.

.. This file was automatic generated / don't edit.

