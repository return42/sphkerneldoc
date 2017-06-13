.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/endpoint/pci-epc-mem.c

.. _`pci_epc_mem_init`:

pci_epc_mem_init
================

.. c:function:: int pci_epc_mem_init(struct pci_epc *epc, phys_addr_t phys_base, size_t size)

    :param struct pci_epc \*epc:
        *undescribed*

    :param phys_addr_t phys_base:
        *undescribed*

    :param size_t size:
        *undescribed*

.. _`pci_epc_mem_init.description`:

Description
-----------

Copyright (C) 2017 Texas Instruments

.. _`pci_epc_mem_init.author`:

Author
------

Kishon Vijay Abraham I <kishon@ti.com>

.. _`pci_epc_mem_init.this-program-is-free-software`:

This program is free software
-----------------------------

you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2 of
the License as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

.. _`pci_epc_mem_exit`:

pci_epc_mem_exit
================

.. c:function:: void pci_epc_mem_exit(struct pci_epc *epc)

    cleanup the pci_epc_mem structure

    :param struct pci_epc \*epc:
        the EPC device that invoked pci_epc_mem_exit

.. _`pci_epc_mem_exit.description`:

Description
-----------

Invoke to cleanup the pci_epc_mem structure allocated in
\ :c:func:`pci_epc_mem_init`\ .

.. _`pci_epc_mem_alloc_addr`:

pci_epc_mem_alloc_addr
======================

.. c:function:: void __iomem *pci_epc_mem_alloc_addr(struct pci_epc *epc, phys_addr_t *phys_addr, size_t size)

    allocate memory address from EPC addr space

    :param struct pci_epc \*epc:
        the EPC device on which memory has to be allocated

    :param phys_addr_t \*phys_addr:
        populate the allocated physical address here

    :param size_t size:
        the size of the address space that has to be allocated

.. _`pci_epc_mem_alloc_addr.description`:

Description
-----------

Invoke to allocate memory address from the EPC address space. This
is usually done to map the remote RC address into the local system.

.. _`pci_epc_mem_free_addr`:

pci_epc_mem_free_addr
=====================

.. c:function:: void pci_epc_mem_free_addr(struct pci_epc *epc, phys_addr_t phys_addr, void __iomem *virt_addr, size_t size)

    free the allocated memory address

    :param struct pci_epc \*epc:
        the EPC device on which memory was allocated

    :param phys_addr_t phys_addr:
        the allocated physical address

    :param void __iomem \*virt_addr:
        virtual address of the allocated mem space

    :param size_t size:
        the size of the allocated address space

.. _`pci_epc_mem_free_addr.description`:

Description
-----------

Invoke to free the memory allocated using pci_epc_mem_alloc_addr.

.. This file was automatic generated / don't edit.

