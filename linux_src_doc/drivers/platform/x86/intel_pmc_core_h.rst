.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/x86/intel_pmc_core.h

.. _`pmc_reg_map`:

struct pmc_reg_map
==================

.. c:type:: struct pmc_reg_map

    Structure used to define parameter unique to a

.. _`pmc_reg_map.definition`:

Definition
----------

.. code-block:: c

    struct pmc_reg_map {
        const struct pmc_bit_map *pfear_sts;
        const struct pmc_bit_map *mphy_sts;
        const struct pmc_bit_map *pll_sts;
        const u32 slp_s0_offset;
        const u32 ltr_ignore_offset;
        const int regmap_length;
        const u32 ppfear0_offset;
        const int ppfear_buckets;
        const u32 pm_cfg_offset;
        const int pm_read_disable_bit;
    }

.. _`pmc_reg_map.members`:

Members
-------

pfear_sts
    Maps name of IP block to PPFEAR\* bit

mphy_sts
    Maps name of MPHY lane to MPHY status lane status bit

pll_sts
    Maps name of PLL to corresponding bit status

slp_s0_offset
    PWRMBASE offset to read SLP_S0 residency

ltr_ignore_offset
    PWRMBASE offset to read/write LTR ignore bit

regmap_length
    Length of memory to map from PWRMBASE address to access

ppfear0_offset
    PWRMBASE offset to to read PPFEAR\*

ppfear_buckets
    Number of 8 bits blocks to read all IP blocks from
    PPFEAR

pm_cfg_offset
    PWRMBASE offset to PM_CFG register

pm_read_disable_bit
    Bit index to read PMC_READ_DISABLE

.. _`pmc_reg_map.description`:

Description
-----------

Each PCH has unique set of register offsets and bit indexes. This structure
captures them to have a common implementation.

.. _`pmc_dev`:

struct pmc_dev
==============

.. c:type:: struct pmc_dev

    pmc device structure

.. _`pmc_dev.definition`:

Definition
----------

.. code-block:: c

    struct pmc_dev {
        u32 base_addr;
        void __iomem *regbase;
        const struct pmc_reg_map *map;
    #if IS_ENABLED(CONFIG_DEBUG_FS)
        struct dentry *dbgfs_dir;
    #endif
        int pmc_xram_read_bit;
        struct mutex lock;
    }

.. _`pmc_dev.members`:

Members
-------

base_addr
    contains pmc base address

regbase
    pointer to io-remapped memory location

map
    pointer to pmc_reg_map struct that contains platform
    specific attributes

dbgfs_dir
    path to debugfs interface

pmc_xram_read_bit
    flag to indicate whether PMC XRAM shadow registers
    used to read MPHY PG and PLL status are available

lock
    *undescribed*

.. _`pmc_dev.description`:

Description
-----------

pmc_dev contains info about power management controller device.

.. This file was automatic generated / don't edit.

