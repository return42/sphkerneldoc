.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/memory/emif.c

.. _`emif_data`:

struct emif_data
================

.. c:type:: struct emif_data

    Per device static data for driver's use

.. _`emif_data.definition`:

Definition
----------

.. code-block:: c

    struct emif_data {
        u8 duplicate;
        u8 temperature_level;
        u8 lpmode;
        struct list_head node;
        unsigned long irq_state;
        void __iomem *base;
        struct device *dev;
        const struct lpddr2_addressing *addressing;
        struct emif_regs  *regs_cache[EMIF_MAX_NUM_FREQUENCIES];
        struct emif_regs *curr_regs;
        struct emif_platform_data *plat_data;
        struct dentry *debugfs_root;
        struct device_node *np_ddr;
    }

.. _`emif_data.members`:

Members
-------

duplicate
    Whether the DDR devices attached to this EMIF
    instance are exactly same as that on EMIF1. In
    this case we can save some memory and processing

temperature_level
    Maximum temperature of LPDDR2 devices attached
    to this EMIF - read from MR4 register. If there
    are two devices attached to this EMIF, this
    value is the maximum of the two temperature
    levels.

lpmode
    *undescribed*

node
    node in the device list

irq_state
    *undescribed*

base
    base address of memory-mapped IO registers.

dev
    device pointer.
    \ ``addressing``\                   table with addressing information from the spec

addressing
    *undescribed*

regs_cache
    An array of 'struct emif_regs' that stores
    calculated register values for different
    frequencies, to avoid re-calculating them on
    each DVFS transition.

curr_regs
    The set of register values used in the last
    frequency change (i.e. corresponding to the
    frequency in effect at the moment)

plat_data
    Pointer to saved platform data.

debugfs_root
    dentry to the root folder for EMIF in debugfs

np_ddr
    Pointer to ddr device tree node

.. This file was automatic generated / don't edit.

