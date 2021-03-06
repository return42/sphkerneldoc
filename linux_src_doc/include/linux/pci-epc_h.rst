.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/pci-epc.h

.. _`pci_epc_ops`:

struct pci_epc_ops
==================

.. c:type:: struct pci_epc_ops

    set of function pointers for performing EPC operations

.. _`pci_epc_ops.definition`:

Definition
----------

.. code-block:: c

    struct pci_epc_ops {
        int (*write_header)(struct pci_epc *epc, u8 func_no, struct pci_epf_header *hdr);
        int (*set_bar)(struct pci_epc *epc, u8 func_no, struct pci_epf_bar *epf_bar);
        void (*clear_bar)(struct pci_epc *epc, u8 func_no, struct pci_epf_bar *epf_bar);
        int (*map_addr)(struct pci_epc *epc, u8 func_no, phys_addr_t addr, u64 pci_addr, size_t size);
        void (*unmap_addr)(struct pci_epc *epc, u8 func_no, phys_addr_t addr);
        int (*set_msi)(struct pci_epc *epc, u8 func_no, u8 interrupts);
        int (*get_msi)(struct pci_epc *epc, u8 func_no);
        int (*set_msix)(struct pci_epc *epc, u8 func_no, u16 interrupts);
        int (*get_msix)(struct pci_epc *epc, u8 func_no);
        int (*raise_irq)(struct pci_epc *epc, u8 func_no, enum pci_epc_irq_type type, u16 interrupt_num);
        int (*start)(struct pci_epc *epc);
        void (*stop)(struct pci_epc *epc);
        struct module *owner;
    }

.. _`pci_epc_ops.members`:

Members
-------

write_header
    ops to populate configuration space header

set_bar
    ops to configure the BAR

clear_bar
    ops to reset the BAR

map_addr
    ops to map CPU address to PCI address

unmap_addr
    ops to unmap CPU address and PCI address

set_msi
    ops to set the requested number of MSI interrupts in the MSI
    capability register

get_msi
    ops to get the number of MSI interrupts allocated by the RC from
    the MSI capability register

set_msix
    ops to set the requested number of MSI-X interrupts in the
    MSI-X capability register

get_msix
    ops to get the number of MSI-X interrupts allocated by the RC
    from the MSI-X capability register

raise_irq
    ops to raise a legacy, MSI or MSI-X interrupt

start
    ops to start the PCI link

stop
    ops to stop the PCI link

owner
    the module owner containing the ops

.. _`pci_epc_mem`:

struct pci_epc_mem
==================

.. c:type:: struct pci_epc_mem

    address space of the endpoint controller

.. _`pci_epc_mem.definition`:

Definition
----------

.. code-block:: c

    struct pci_epc_mem {
        phys_addr_t phys_base;
        size_t size;
        unsigned long *bitmap;
        size_t page_size;
        int pages;
    }

.. _`pci_epc_mem.members`:

Members
-------

phys_base
    physical base address of the PCI address space

size
    the size of the PCI address space

bitmap
    bitmap to manage the PCI address space

page_size
    size of each page

pages
    number of bits representing the address region

.. _`pci_epc`:

struct pci_epc
==============

.. c:type:: struct pci_epc

    represents the PCI EPC device

.. _`pci_epc.definition`:

Definition
----------

.. code-block:: c

    struct pci_epc {
        struct device dev;
        struct list_head pci_epf;
        const struct pci_epc_ops *ops;
        struct pci_epc_mem *mem;
        u8 max_functions;
        struct config_group *group;
        spinlock_t lock;
        unsigned int features;
    }

.. _`pci_epc.members`:

Members
-------

dev
    PCI EPC device

pci_epf
    list of endpoint functions present in this EPC device

ops
    function pointers for performing endpoint operations

mem
    address space of the endpoint controller

max_functions
    max number of functions that can be configured in this EPC

group
    configfs group representing the PCI EPC device

lock
    spinlock to protect pci_epc ops

features
    *undescribed*

.. This file was automatic generated / don't edit.

