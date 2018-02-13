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
        struct clk *clocks[SYSC_MAX_CLOCKS];
        const char *legacy_mode;
        const struct sysc_capabilities *cap;
        struct sysc_config cfg;
        const char *name;
        u32 revision;
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

legacy_mode
    configured for legacy mode if set

cap
    interconnect target module capabilities

cfg
    interconnect target module configuration

name
    name if available

revision
    interconnect target module revision

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

.. This file was automatic generated / don't edit.

