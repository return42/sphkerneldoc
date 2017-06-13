.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/pci-epf.h

.. _`pci_epf_header`:

struct pci_epf_header
=====================

.. c:type:: struct pci_epf_header

    represents standard configuration header

.. _`pci_epf_header.definition`:

Definition
----------

.. code-block:: c

    struct pci_epf_header {
        u16 vendorid;
        u16 deviceid;
        u8 revid;
        u8 progif_code;
        u8 subclass_code;
        u8 baseclass_code;
        u8 cache_line_size;
        u16 subsys_vendor_id;
        u16 subsys_id;
        enum pci_interrupt_pin interrupt_pin;
    }

.. _`pci_epf_header.members`:

Members
-------

vendorid
    identifies device manufacturer

deviceid
    identifies a particular device

revid
    specifies a device-specific revision identifier

progif_code
    identifies a specific register-level programming interface

subclass_code
    identifies more specifically the function of the device

baseclass_code
    broadly classifies the type of function the device performs

cache_line_size
    specifies the system cacheline size in units of DWORDs

subsys_vendor_id
    vendor of the add-in card or subsystem

subsys_id
    id specific to vendor

interrupt_pin
    interrupt pin the device (or device function) uses

.. _`pci_epf_ops`:

struct pci_epf_ops
==================

.. c:type:: struct pci_epf_ops

    set of function pointers for performing EPF operations

.. _`pci_epf_ops.definition`:

Definition
----------

.. code-block:: c

    struct pci_epf_ops {
        int (*bind)(struct pci_epf *epf);
        void (*unbind)(struct pci_epf *epf);
        void (*linkup)(struct pci_epf *epf);
    }

.. _`pci_epf_ops.members`:

Members
-------

bind
    ops to perform when a EPC device has been bound to EPF device

unbind
    ops to perform when a binding has been lost between a EPC device
    and EPF device

linkup
    ops to perform when the EPC device has established a connection with
    a host system

.. _`pci_epf_driver`:

struct pci_epf_driver
=====================

.. c:type:: struct pci_epf_driver

    represents the PCI EPF driver

.. _`pci_epf_driver.definition`:

Definition
----------

.. code-block:: c

    struct pci_epf_driver {
        int (*probe)(struct pci_epf *epf);
        int (*remove)(struct pci_epf *epf);
        struct device_driver driver;
        struct pci_epf_ops *ops;
        struct module *owner;
        struct config_group *group;
        const struct pci_epf_device_id *id_table;
    }

.. _`pci_epf_driver.members`:

Members
-------

probe
    ops to perform when a new EPF device has been bound to the EPF driver

remove
    ops to perform when the binding between the EPF device and EPF
    driver is broken

driver
    PCI EPF driver

ops
    set of function pointers for performing EPF operations

owner
    the owner of the module that registers the PCI EPF driver

group
    configfs group corresponding to the PCI EPF driver

id_table
    identifies EPF devices for probing

.. _`pci_epf_bar`:

struct pci_epf_bar
==================

.. c:type:: struct pci_epf_bar

    represents the BAR of EPF device

.. _`pci_epf_bar.definition`:

Definition
----------

.. code-block:: c

    struct pci_epf_bar {
        dma_addr_t phys_addr;
        size_t size;
    }

.. _`pci_epf_bar.members`:

Members
-------

phys_addr
    physical address that should be mapped to the BAR

size
    the size of the address space present in BAR

.. _`pci_epf`:

struct pci_epf
==============

.. c:type:: struct pci_epf

    represents the PCI EPF device

.. _`pci_epf.definition`:

Definition
----------

.. code-block:: c

    struct pci_epf {
        struct device dev;
        const char *name;
        struct pci_epf_header *header;
        struct pci_epf_bar bar;
        u8 msi_interrupts;
        u8 func_no;
        struct pci_epc *epc;
        struct pci_epf_driver *driver;
        struct list_head list;
    }

.. _`pci_epf.members`:

Members
-------

dev
    the PCI EPF device

name
    the name of the PCI EPF device

header
    represents standard configuration header

bar
    represents the BAR of EPF device

msi_interrupts
    number of MSI interrupts required by this function

func_no
    unique function number within this endpoint device

epc
    the EPC device to which this EPF device is bound

driver
    the EPF driver to which this EPF device is bound

list
    to add pci_epf as a list of PCI endpoint functions to pci_epc

.. This file was automatic generated / don't edit.

