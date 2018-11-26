.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/pci-sysfs.c

.. _`pci_read_legacy_io`:

pci_read_legacy_io
==================

.. c:function:: ssize_t pci_read_legacy_io(struct file *filp, struct kobject *kobj, struct bin_attribute *bin_attr, char *buf, loff_t off, size_t count)

    read byte(s) from legacy I/O port space

    :param filp:
        open sysfs file
    :type filp: struct file \*

    :param kobj:
        kobject corresponding to file to read from
    :type kobj: struct kobject \*

    :param bin_attr:
        struct bin_attribute for this file
    :type bin_attr: struct bin_attribute \*

    :param buf:
        buffer to store results
    :type buf: char \*

    :param off:
        offset into legacy I/O port space
    :type off: loff_t

    :param count:
        number of bytes to read
    :type count: size_t

.. _`pci_read_legacy_io.description`:

Description
-----------

Reads 1, 2, or 4 bytes from legacy I/O port space using an arch specific
callback routine (pci_legacy_read).

.. _`pci_write_legacy_io`:

pci_write_legacy_io
===================

.. c:function:: ssize_t pci_write_legacy_io(struct file *filp, struct kobject *kobj, struct bin_attribute *bin_attr, char *buf, loff_t off, size_t count)

    write byte(s) to legacy I/O port space

    :param filp:
        open sysfs file
    :type filp: struct file \*

    :param kobj:
        kobject corresponding to file to read from
    :type kobj: struct kobject \*

    :param bin_attr:
        struct bin_attribute for this file
    :type bin_attr: struct bin_attribute \*

    :param buf:
        buffer containing value to be written
    :type buf: char \*

    :param off:
        offset into legacy I/O port space
    :type off: loff_t

    :param count:
        number of bytes to write
    :type count: size_t

.. _`pci_write_legacy_io.description`:

Description
-----------

Writes 1, 2, or 4 bytes from legacy I/O port space using an arch specific
callback routine (pci_legacy_write).

.. _`pci_mmap_legacy_mem`:

pci_mmap_legacy_mem
===================

.. c:function:: int pci_mmap_legacy_mem(struct file *filp, struct kobject *kobj, struct bin_attribute *attr, struct vm_area_struct *vma)

    map legacy PCI memory into user memory space

    :param filp:
        open sysfs file
    :type filp: struct file \*

    :param kobj:
        kobject corresponding to device to be mapped
    :type kobj: struct kobject \*

    :param attr:
        struct bin_attribute for this file
    :type attr: struct bin_attribute \*

    :param vma:
        struct vm_area_struct passed to mmap
    :type vma: struct vm_area_struct \*

.. _`pci_mmap_legacy_mem.description`:

Description
-----------

Uses an arch specific callback, pci_mmap_legacy_mem_page_range, to mmap
legacy memory space (first meg of bus space) into application virtual
memory space.

.. _`pci_mmap_legacy_io`:

pci_mmap_legacy_io
==================

.. c:function:: int pci_mmap_legacy_io(struct file *filp, struct kobject *kobj, struct bin_attribute *attr, struct vm_area_struct *vma)

    map legacy PCI IO into user memory space

    :param filp:
        open sysfs file
    :type filp: struct file \*

    :param kobj:
        kobject corresponding to device to be mapped
    :type kobj: struct kobject \*

    :param attr:
        struct bin_attribute for this file
    :type attr: struct bin_attribute \*

    :param vma:
        struct vm_area_struct passed to mmap
    :type vma: struct vm_area_struct \*

.. _`pci_mmap_legacy_io.description`:

Description
-----------

Uses an arch specific callback, pci_mmap_legacy_io_page_range, to mmap
legacy IO space (first meg of bus space) into application virtual
memory space. Returns -ENOSYS if the operation isn't supported

.. _`pci_adjust_legacy_attr`:

pci_adjust_legacy_attr
======================

.. c:function:: void pci_adjust_legacy_attr(struct pci_bus *b, enum pci_mmap_state mmap_type)

    adjustment of legacy file attributes

    :param b:
        bus to create files under
    :type b: struct pci_bus \*

    :param mmap_type:
        I/O port or memory
    :type mmap_type: enum pci_mmap_state

.. _`pci_adjust_legacy_attr.description`:

Description
-----------

Stub implementation. Can be overridden by arch if necessary.

.. _`pci_create_legacy_files`:

pci_create_legacy_files
=======================

.. c:function:: void pci_create_legacy_files(struct pci_bus *b)

    create legacy I/O port and memory files

    :param b:
        bus to create files under
    :type b: struct pci_bus \*

.. _`pci_create_legacy_files.description`:

Description
-----------

Some platforms allow access to legacy I/O port and ISA memory space on
a per-bus basis.  This routine creates the files and ties them into
their associated read, write and mmap files from pci-sysfs.c

On error unwind, but don't propagate the error to the caller
as it is ok to set up the PCI bus without these files.

.. _`pci_mmap_resource`:

pci_mmap_resource
=================

.. c:function:: int pci_mmap_resource(struct kobject *kobj, struct bin_attribute *attr, struct vm_area_struct *vma, int write_combine)

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

    :param write_combine:
        1 for write_combine mapping
    :type write_combine: int

.. _`pci_mmap_resource.description`:

Description
-----------

Use the regular PCI mapping routines to map a PCI resource into userspace.

.. _`pci_remove_resource_files`:

pci_remove_resource_files
=========================

.. c:function:: void pci_remove_resource_files(struct pci_dev *pdev)

    cleanup resource files

    :param pdev:
        dev to cleanup
    :type pdev: struct pci_dev \*

.. _`pci_remove_resource_files.description`:

Description
-----------

If we created resource files for \ ``pdev``\ , remove them from sysfs and
free their resources.

.. _`pci_create_resource_files`:

pci_create_resource_files
=========================

.. c:function:: int pci_create_resource_files(struct pci_dev *pdev)

    create resource files in sysfs for \ ``dev``\ 

    :param pdev:
        dev in question
    :type pdev: struct pci_dev \*

.. _`pci_create_resource_files.description`:

Description
-----------

Walk the resources in \ ``pdev``\  creating files for each resource available.

.. _`pci_write_rom`:

pci_write_rom
=============

.. c:function:: ssize_t pci_write_rom(struct file *filp, struct kobject *kobj, struct bin_attribute *bin_attr, char *buf, loff_t off, size_t count)

    used to enable access to the PCI ROM display

    :param filp:
        sysfs file
    :type filp: struct file \*

    :param kobj:
        kernel object handle
    :type kobj: struct kobject \*

    :param bin_attr:
        struct bin_attribute for this file
    :type bin_attr: struct bin_attribute \*

    :param buf:
        user input
    :type buf: char \*

    :param off:
        file offset
    :type off: loff_t

    :param count:
        number of byte in input
    :type count: size_t

.. _`pci_write_rom.description`:

Description
-----------

writing anything except 0 enables it

.. _`pci_read_rom`:

pci_read_rom
============

.. c:function:: ssize_t pci_read_rom(struct file *filp, struct kobject *kobj, struct bin_attribute *bin_attr, char *buf, loff_t off, size_t count)

    read a PCI ROM

    :param filp:
        sysfs file
    :type filp: struct file \*

    :param kobj:
        kernel object handle
    :type kobj: struct kobject \*

    :param bin_attr:
        struct bin_attribute for this file
    :type bin_attr: struct bin_attribute \*

    :param buf:
        where to put the data we read from the ROM
    :type buf: char \*

    :param off:
        file offset
    :type off: loff_t

    :param count:
        number of bytes to read
    :type count: size_t

.. _`pci_read_rom.description`:

Description
-----------

Put \ ``count``\  bytes starting at \ ``off``\  into \ ``buf``\  from the ROM in the PCI
device corresponding to \ ``kobj``\ .

.. _`pci_remove_sysfs_dev_files`:

pci_remove_sysfs_dev_files
==========================

.. c:function:: void pci_remove_sysfs_dev_files(struct pci_dev *pdev)

    cleanup PCI specific sysfs files

    :param pdev:
        device whose entries we should free
    :type pdev: struct pci_dev \*

.. _`pci_remove_sysfs_dev_files.description`:

Description
-----------

Cleanup when \ ``pdev``\  is removed from sysfs.

.. This file was automatic generated / don't edit.

