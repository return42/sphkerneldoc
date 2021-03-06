.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/ti-sysc.h

.. _`sysc_regbits`:

struct sysc_regbits
===================

.. c:type:: struct sysc_regbits

    TI OCP_SYSCONFIG register field offsets

.. _`sysc_regbits.definition`:

Definition
----------

.. code-block:: c

    struct sysc_regbits {
        s8 midle_shift;
        s8 clkact_shift;
        s8 sidle_shift;
        s8 enwkup_shift;
        s8 srst_shift;
        s8 autoidle_shift;
        s8 dmadisable_shift;
        s8 emufree_shift;
    }

.. _`sysc_regbits.members`:

Members
-------

midle_shift
    Offset of the midle bit

clkact_shift
    Offset of the clockactivity bit

sidle_shift
    Offset of the sidle bit

enwkup_shift
    Offset of the enawakeup bit

srst_shift
    Offset of the softreset bit

autoidle_shift
    Offset of the autoidle bit

dmadisable_shift
    Offset of the dmadisable bit
    \ ``emufree_shift``\ ; Offset of the emufree bit

emufree_shift
    *undescribed*

.. _`sysc_regbits.description`:

Description
-----------

Note that 0 is a valid shift, and for ti-sysc.c -ENODEV can be used if a
feature is not available.

.. _`sysc_capabilities`:

struct sysc_capabilities
========================

.. c:type:: struct sysc_capabilities

    capabilities for an interconnect target module

.. _`sysc_capabilities.definition`:

Definition
----------

.. code-block:: c

    struct sysc_capabilities {
        const enum ti_sysc_module_type type;
        const u32 sysc_mask;
        const struct sysc_regbits *regbits;
        const u32 mod_quirks;
    }

.. _`sysc_capabilities.members`:

Members
-------

type
    *undescribed*

sysc_mask
    bitmask of supported SYSCONFIG register bits

regbits
    bitmask of SYSCONFIG register bits

mod_quirks
    bitmask of module specific quirks

.. _`sysc_config`:

struct sysc_config
==================

.. c:type:: struct sysc_config

    configuration for an interconnect target module

.. _`sysc_config.definition`:

Definition
----------

.. code-block:: c

    struct sysc_config {
        u32 sysc_val;
        u32 syss_mask;
        u8 midlemodes;
        u8 sidlemodes;
        u8 srst_udelay;
        u32 quirks;
    }

.. _`sysc_config.members`:

Members
-------

sysc_val
    configured value for sysc register

syss_mask
    *undescribed*

midlemodes
    bitmask of supported master idle modes

sidlemodes
    bitmask of supported master idle modes

srst_udelay
    optional delay needed after OCP soft reset

quirks
    bitmask of enabled quirks

.. _`ti_sysc_module_data`:

struct ti_sysc_module_data
==========================

.. c:type:: struct ti_sysc_module_data

    ti-sysc to hwmod translation data for a module

.. _`ti_sysc_module_data.definition`:

Definition
----------

.. code-block:: c

    struct ti_sysc_module_data {
        const char *name;
        u64 module_pa;
        u32 module_size;
        int *offsets;
        int nr_offsets;
        const struct sysc_capabilities *cap;
        struct sysc_config *cfg;
    }

.. _`ti_sysc_module_data.members`:

Members
-------

name
    legacy "ti,hwmods" module name

module_pa
    physical address of the interconnect target module

module_size
    size of the interconnect target module

offsets
    array of register offsets as listed in enum sysc_registers

nr_offsets
    number of registers

cap
    interconnect target module capabilities

cfg
    interconnect target module configuration

.. _`ti_sysc_module_data.description`:

Description
-----------

This data is enough to allocate a new struct omap_hwmod_class_sysconfig
based on device tree data parsed by ti-sysc driver.

.. This file was automatic generated / don't edit.

