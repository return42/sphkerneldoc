.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/ccree/cc_driver.h

.. _`cc_drvdata`:

struct cc_drvdata
=================

.. c:type:: struct cc_drvdata

    driver private data context

.. _`cc_drvdata.definition`:

Definition
----------

.. code-block:: c

    struct cc_drvdata {
        void __iomem *cc_base;
        int irq;
        u32 irq_mask;
        u32 fw_ver;
        struct completion hw_queue_avail;
        struct platform_device *plat_dev;
        cc_sram_addr_t mlli_sram_addr;
        void *buff_mgr_handle;
        void *cipher_handle;
        void *hash_handle;
        void *aead_handle;
        void *request_mgr_handle;
        void *fips_handle;
        void *ivgen_handle;
        void *sram_mgr_handle;
        void *debugfs;
        struct clk *clk;
        bool coherent;
        char *hw_rev_name;
        enum cc_hw_rev hw_rev;
        u32 hash_len_sz;
        u32 axim_mon_offset;
        u32 sig_offset;
        u32 ver_offset;
    }

.. _`cc_drvdata.members`:

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

hw_queue_avail
    *undescribed*

plat_dev
    *undescribed*

mlli_sram_addr
    *undescribed*

buff_mgr_handle
    *undescribed*

cipher_handle
    *undescribed*

hash_handle
    *undescribed*

aead_handle
    *undescribed*

request_mgr_handle
    *undescribed*

fips_handle
    *undescribed*

ivgen_handle
    *undescribed*

sram_mgr_handle
    *undescribed*

debugfs
    *undescribed*

clk
    *undescribed*

coherent
    *undescribed*

hw_rev_name
    *undescribed*

hw_rev
    *undescribed*

hash_len_sz
    *undescribed*

axim_mon_offset
    *undescribed*

sig_offset
    *undescribed*

ver_offset
    *undescribed*

.. This file was automatic generated / don't edit.

