.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/bus/ti-sysc.c

.. _`sysc`:

struct sysc
===========

.. c:type:: struct sysc

    TI sysc interconnect target module registers and capabilities

.. _`sysc.definition`:

Definition
----------

.. code-block:: c

    struct sysc {
        struct device *dev;
        u64 module_pa;
        u32 module_size;
        void __iomem *module_va;
        int offsets[SYSC_MAX_REGS];
        struct clk **clocks;
        const char **clock_roles;
        int nr_clocks;
        struct reset_control *rsts;
        const char *legacy_mode;
        const struct sysc_capabilities *cap;
        struct sysc_config cfg;
        struct ti_sysc_cookie cookie;
        const char *name;
        u32 revision;
        bool enabled;
        bool needs_resume;
        bool child_needs_resume;
        struct delayed_work idle_work;
    }

.. _`sysc.members`:

Members
-------

dev
    struct device pointer

module_pa
    physical address of the interconnect target module

module_size
    size of the interconnect target module

module_va
    virtual address of the interconnect target module

offsets
    register offsets from module base

clocks
    clocks used by the interconnect target module

clock_roles
    clock role names for the found clocks

nr_clocks
    number of clocks used by the interconnect target module

rsts
    *undescribed*

legacy_mode
    configured for legacy mode if set

cap
    interconnect target module capabilities

cfg
    interconnect target module configuration

cookie
    *undescribed*

name
    name if available

revision
    interconnect target module revision

enabled
    *undescribed*

needs_resume
    runtime resume needed on resume from suspend

child_needs_resume
    *undescribed*

idle_work
    *undescribed*

.. _`sysc_init_resets`:

sysc_init_resets
================

.. c:function:: int sysc_init_resets(struct sysc *ddata)

    reset module on init

    :param struct sysc \*ddata:
        device driver data

.. _`sysc_init_resets.description`:

Description
-----------

A module can have both OCP softreset control and external rstctrl.
If more complicated rstctrl resets are needed, please handle these
directly from the child device driver and map only the module reset
for the parent interconnect target module device.

Automatic reset of the module on init can be skipped with the
"ti,no-reset-on-init" device tree property.

.. _`sysc_parse_and_check_child_range`:

sysc_parse_and_check_child_range
================================

.. c:function:: int sysc_parse_and_check_child_range(struct sysc *ddata)

    parses module IO region from ranges

    :param struct sysc \*ddata:
        device driver data

.. _`sysc_parse_and_check_child_range.description`:

Description
-----------

In general we only need rev, syss, and sysc registers and not the whole
module range. But we do want the offsets for these registers from the
module base. This allows us to check them against the legacy hwmod
platform data. Let's also check the ranges are configured properly.

.. _`sysc_check_one_child`:

sysc_check_one_child
====================

.. c:function:: int sysc_check_one_child(struct sysc *ddata, struct device_node *np)

    check child configuration

    :param struct sysc \*ddata:
        device driver data

    :param struct device_node \*np:
        child device node

.. _`sysc_check_one_child.description`:

Description
-----------

Let's avoid messy situations where we have new interconnect target
node but children have "ti,hwmods". These belong to the interconnect
target node and are managed by this driver.

.. _`sysc_parse_one`:

sysc_parse_one
==============

.. c:function:: int sysc_parse_one(struct sysc *ddata, enum sysc_registers reg)

    parses the interconnect target module registers

    :param struct sysc \*ddata:
        device driver data

    :param enum sysc_registers reg:
        register to parse

.. _`sysc_check_registers`:

sysc_check_registers
====================

.. c:function:: int sysc_check_registers(struct sysc *ddata)

    check for misconfigured register overlaps

    :param struct sysc \*ddata:
        device driver data

.. _`sysc_ioremap`:

sysc_ioremap
============

.. c:function:: int sysc_ioremap(struct sysc *ddata)

    ioremap register space for the interconnect target module

    :param struct sysc \*ddata:
        deviec driver data

.. _`sysc_ioremap.description`:

Description
-----------

Note that the interconnect target module registers can be anywhere
within the first child device address space. For example, SGX has
them at offset 0x1fc00 in the 32MB module address space. We just
what we need around the interconnect target module registers.

.. _`sysc_map_and_check_registers`:

sysc_map_and_check_registers
============================

.. c:function:: int sysc_map_and_check_registers(struct sysc *ddata)

    ioremap and check device registers

    :param struct sysc \*ddata:
        device driver data

.. _`sysc_show_rev`:

sysc_show_rev
=============

.. c:function:: int sysc_show_rev(char *bufp, struct sysc *ddata)

    read and show interconnect target module revision

    :param char \*bufp:
        buffer to print the information to

    :param struct sysc \*ddata:
        device driver data

.. _`sysc_show_registers`:

sysc_show_registers
===================

.. c:function:: void sysc_show_registers(struct sysc *ddata)

    show information about interconnect target module

    :param struct sysc \*ddata:
        device driver data

.. _`sysc_legacy_idle_quirk`:

sysc_legacy_idle_quirk
======================

.. c:function:: void sysc_legacy_idle_quirk(struct sysc *ddata, struct device *child)

    handle children in omap_device compatible way

    :param struct sysc \*ddata:
        device driver data

    :param struct device \*child:
        child device driver

.. _`sysc_legacy_idle_quirk.description`:

Description
-----------

Allow idle for child devices as done with \_od_runtime_suspend().
Otherwise many child devices will not idle because of the permanent
parent usecount set in \ :c:func:`pm_runtime_irq_safe`\ .

Note that the long term solution is to just modify the child device
drivers to not set \ :c:func:`pm_runtime_irq_safe`\  and then this can be just
dropped.

.. This file was automatic generated / don't edit.

