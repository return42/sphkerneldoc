.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/alpha/kernel/pci-sysfs.c

.. _`pci_mmap_resource`:

pci_mmap_resource
=================

.. c:function:: int pci_mmap_resource(struct kobject *kobj, struct bin_attribute *attr, struct vm_area_struct *vma, int sparse)

    map a PCI resource into user memory space

    :param kobj:
        kobject for mapping
    :type kobj: struct kobject \*

    :param attr:
        struct bin_attribute for the file being mapped
    :type attr: struct bin_attribute \*

    :param vma:
        struct vm_area_struct passed into the mmap
    :type vma: struct vm_area_struct \*

    :param sparse:
        address space type
    :type sparse: int

.. _`pci_mmap_resource.description`:

Description
-----------

Use the bus mapping routines to map a PCI resource into userspace.

.. _`pci_remove_resource_files`:

pci_remove_resource_files
=========================

.. c:function:: void pci_remove_resource_files(struct pci_dev *pdev)

    cleanup resource files

    :param pdev:
        *undescribed*
    :type pdev: struct pci_dev \*

.. _`pci_remove_resource_files.description`:

Description
-----------

If we created resource files for \ ``dev``\ , remove them from sysfs and
free their resources.

.. _`pci_create_resource_files`:

pci_create_resource_files
=========================

.. c:function:: int pci_create_resource_files(struct pci_dev *pdev)

    create resource files in sysfs for \ ``dev``\ 

    :param pdev:
        *undescribed*
    :type pdev: struct pci_dev \*

.. _`pci_create_resource_files.description`:

Description
-----------

Walk the resources in \ ``dev``\  creating files for each resource available.

.. _`pci_adjust_legacy_attr`:

pci_adjust_legacy_attr
======================

.. c:function:: void pci_adjust_legacy_attr(struct pci_bus *bus, enum pci_mmap_state mmap_type)

    adjustment of legacy file attributes

    :param bus:
        *undescribed*
    :type bus: struct pci_bus \*

    :param mmap_type:
        I/O port or memory
    :type mmap_type: enum pci_mmap_state

.. _`pci_adjust_legacy_attr.description`:

Description
-----------

Adjust file name and size for sparse mappings.

.. This file was automatic generated / don't edit.

