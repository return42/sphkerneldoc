.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/parisc/iosapic.c

.. _`iosapic_load_irt`:

iosapic_load_irt
================

.. c:function:: int iosapic_load_irt(unsigned long cell_num, struct irt_entry **irt)

    Fill in the interrupt routing table

    :param unsigned long cell_num:
        The cell number of the CPU we're currently executing on

    :param struct irt_entry \*\*irt:
        The address to place the new IRT at
        \ ``return``\  The number of entries found

.. _`iosapic_load_irt.description`:

Description
-----------

The "Get PCI INT Routing Table Size" option returns the number of
entries in the PCI interrupt routing table for the cell specified
in the cell_number argument.  The cell number must be for a cell
within the caller's protection domain.

The "Get PCI INT Routing Table" option returns, for the cell
specified in the cell_number argument, the PCI interrupt routing
table in the caller allocated memory pointed to by mem_addr.
We assume the IRT only contains entries for I/O SAPIC and
calculate the size based on the size of I/O sapic entries.

The PCI interrupt routing table entry format is derived from the
IA64 SAL Specification 2.4.   The PCI interrupt routing table defines
the routing of PCI interrupt signals between the PCI device output
"pins" and the IO SAPICs' input "lines" (including core I/O PCI
devices).  This table does NOT include information for devices/slots
behind PCI to PCI bridges. See PCI to PCI Bridge Architecture Spec.
for the architected method of routing of IRQ's behind PPB's.

.. This file was automatic generated / don't edit.

