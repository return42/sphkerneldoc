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
        struct resource *res_mem;
        struct resource *res_irq;
        void __iomem *cc_base;
    #ifdef DX_BASE_ENV_REGS
        void __iomem *env_base;
    #endif
        unsigned int irq;
        uint32_t irq_mask;
        uint32_t fw_ver;
        uint32_t monitor_null_cycles;
        struct platform_device *plat_dev;
        ssi_sram_addr_t mlli_sram_addr;
        struct completion icache_setup_completion;
        void *buff_mgr_handle;
        void *hash_handle;
        void *aead_handle;
        void *blkcipher_handle;
        void *request_mgr_handle;
        void *fips_handle;
        void *ivgen_handle;
        void *sram_mgr_handle;
    #ifdef ENABLE_CYCLE_COUNT
        cycles_t isr_exit_cycles;
    #endif
        uint32_t inflight_counter;
    }

.. _`ssi_drvdata.members`:

Members
-------

res_mem
    *undescribed*

res_irq
    *undescribed*

cc_base
    virt address of the CC registers

env_base
    *undescribed*

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

icache_setup_completion
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

isr_exit_cycles
    *undescribed*

inflight_counter
    *undescribed*

.. This file was automatic generated / don't edit.

