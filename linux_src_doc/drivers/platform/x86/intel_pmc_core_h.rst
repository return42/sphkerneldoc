.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/x86/intel_pmc_core.h

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
    #if IS_ENABLEDCONFIG_DEBUG_FS
        struct dentry *dbgfs_dir;
    #endif
        bool has_slp_s0_res;
        int pmc_xram_read_bit;
        struct mutex lock;
    }

.. _`pmc_dev.members`:

Members
-------

base_addr
    comtains pmc base address

regbase
    pointer to io-remapped memory location

map
    *undescribed*

dbgfs_dir
    path to debug fs interface

has_slp_s0_res
    *undescribed*

pmc_xram_read_bit
    *undescribed*

lock
    *undescribed*

.. _`pmc_dev.description`:

Description
-----------

pmc_dev contains info about power management controller device.

.. This file was automatic generated / don't edit.

