.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/yamon-dt.h

.. _`yamon_mem_region`:

struct yamon_mem_region
=======================

.. c:type:: struct yamon_mem_region

    Represents a contiguous range of physical RAM.

.. _`yamon_mem_region.definition`:

Definition
----------

.. code-block:: c

    struct yamon_mem_region {
        phys_addr_t start;
        phys_addr_t size;
        phys_addr_t discard;
    }

.. _`yamon_mem_region.members`:

Members
-------

start
    Start physical address.

size
    Maximum size of region.

discard
    Length of additional memory to discard after the region.

.. _`yamon_dt_append_cmdline`:

yamon_dt_append_cmdline
=======================

.. c:function:: int yamon_dt_append_cmdline(void *fdt)

    Append YAMON-provided command line to /chosen

    :param void \*fdt:
        the FDT blob

.. _`yamon_dt_append_cmdline.description`:

Description
-----------

Write the YAMON-provided command line to the bootargs property of the
/chosen node in \ ``fdt``\ .

.. _`yamon_dt_append_cmdline.return`:

Return
------

0 on success, else -errno

.. _`yamon_dt_append_memory`:

yamon_dt_append_memory
======================

.. c:function:: int yamon_dt_append_memory(void *fdt, const struct yamon_mem_region *regions)

    Append YAMON-provided memory info to /memory

    :param void \*fdt:
        the FDT blob

    :param const struct yamon_mem_region \*regions:
        zero size terminated array of physical memory regions

.. _`yamon_dt_append_memory.description`:

Description
-----------

Generate a /memory node in \ ``fdt``\  based upon memory size information provided
by YAMON in its environment and the \ ``regions``\  array.

.. _`yamon_dt_append_memory.return`:

Return
------

0 on success, else -errno

.. _`yamon_dt_serial_config`:

yamon_dt_serial_config
======================

.. c:function:: int yamon_dt_serial_config(void *fdt)

    Append YAMON-provided serial config to /chosen

    :param void \*fdt:
        the FDT blob

.. _`yamon_dt_serial_config.description`:

Description
-----------

Generate a stdout-path property in the /chosen node of \ ``fdt``\ , based upon
information provided in the YAMON environment about the UART configuration
of the system.

.. _`yamon_dt_serial_config.return`:

Return
------

0 on success, else -errno

.. This file was automatic generated / don't edit.

