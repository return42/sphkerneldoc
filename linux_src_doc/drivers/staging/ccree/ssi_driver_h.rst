.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/ccree/ssi_driver.h

.. _`ssi_drvdata`:

struct ssi_drvdata
==================

.. c:type:: struct ssi_drvdata

    driver private data context

.. _`ssi_drvdata.definition`:

Definition
----------

.. code-block:: c

    struct ssi_drvdata {
        void __iomem *cc_base;
        int irq;
        u32 irq_mask;
        u32 fw_ver;
        u32 monitor_null_cycles;
        struct platform_device *plat_dev;
        ssi_sram_addr_t mlli_sram_addr;
        void *buff_mgr_handle;
        void *hash_handle;
        void *aead_handle;
        void *blkcipher_handle;
        void *request_mgr_handle;
        void *fips_handle;
        void *ivgen_handle;
        void *sram_mgr_handle;
        struct clk *clk;
        bool coherent;
    }

.. _`ssi_drvdata.members`:

Members
-------

cc_base
    virt address of the CC registers

irq
    device IRQ number

irq_mask
    Interrupt mask shadow (1 for masked interrupts)

fw_ver
    SeP loaded firmware version

monitor_null_cycles
    *undescribed*

plat_dev
    *undescribed*

mlli_sram_addr
    *undescribed*

buff_mgr_handle
    *undescribed*

hash_handle
    *undescribed*

aead_handle
    *undescribed*

blkcipher_handle
    *undescribed*

request_mgr_handle
    *undescribed*

fips_handle
    *undescribed*

ivgen_handle
    *undescribed*

sram_mgr_handle
    *undescribed*

clk
    *undescribed*

coherent
    *undescribed*

.. This file was automatic generated / don't edit.

