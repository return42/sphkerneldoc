.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/endpoint/pci-epc-mem.c

.. _`pci_epc_mem_get_order`:

pci_epc_mem_get_order
=====================

.. c:function:: int pci_epc_mem_get_order(struct pci_epc_mem *mem, size_t size)

    :param mem:
        *undescribed*
    :type mem: struct pci_epc_mem \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`pci_epc_mem_get_order.description`:

Description
-----------

Copyright (C) 2017 Texas Instruments

.. _`pci_epc_mem_get_order.author`:

Author
------

Kishon Vijay Abraham I <kishon@ti.com>

.. _`__pci_epc_mem_init`:

\__pci_epc_mem_init
===================

.. c:function:: int __pci_epc_mem_init(struct pci_epc *epc, phys_addr_t phys_base, size_t size, size_t page_size)

    initialize the pci_epc_mem structure

    :param epc:
        the EPC device that invoked pci_epc_mem_init
    :type epc: struct pci_epc \*

    :param phys_base:
        the physical address of the base
    :type phys_base: phys_addr_t

    :param size:
        the size of the address space
    :type size: size_t

    :param page_size:
        size of each page
    :type page_size: size_t

.. _`__pci_epc_mem_init.description`:

Description
-----------

Invoke to initialize the pci_epc_mem structure used by the
endpoint functions to allocate mapped PCI address.

.. _`pci_epc_mem_exit`:

pci_epc_mem_exit
================

.. c:function:: void pci_epc_mem_exit(struct pci_epc *epc)

    cleanup the pci_epc_mem structure

    :param epc:
        the EPC device that invoked pci_epc_mem_exit
    :type epc: struct pci_epc \*

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

    :param epc:
        the EPC device on which memory has to be allocated
    :type epc: struct pci_epc \*

    :param phys_addr:
        populate the allocated physical address here
    :type phys_addr: phys_addr_t \*

    :param size:
        the size of the address space that has to be allocated
    :type size: size_t

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

    :param epc:
        the EPC device on which memory was allocated
    :type epc: struct pci_epc \*

    :param phys_addr:
        the allocated physical address
    :type phys_addr: phys_addr_t

    :param virt_addr:
        virtual address of the allocated mem space
    :type virt_addr: void __iomem \*

    :param size:
        the size of the allocated address space
    :type size: size_t

.. _`pci_epc_mem_free_addr.description`:

Description
-----------

Invoke to free the memory allocated using pci_epc_mem_alloc_addr.

.. This file was automatic generated / don't edit.

