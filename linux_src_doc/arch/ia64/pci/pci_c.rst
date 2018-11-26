.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/pci/pci.c

.. _`ia64_pci_get_legacy_mem`:

ia64_pci_get_legacy_mem
=======================

.. c:function:: char *ia64_pci_get_legacy_mem(struct pci_bus *bus)

    generic legacy mem routine

    :param bus:
        bus to get legacy memory base address for
    :type bus: struct pci_bus \*

.. _`ia64_pci_get_legacy_mem.description`:

Description
-----------

Find the base of legacy memory for \ ``bus``\ .  This is typically the first
megabyte of bus address space for \ ``bus``\  or is simply 0 on platforms whose
chipsets support legacy I/O and memory routing.  Returns the base address
or an error pointer if an error occurred.

This is the ia64 generic version of this routine.  Other platforms
are free to override it with a machine vector.

.. _`pci_mmap_legacy_page_range`:

pci_mmap_legacy_page_range
==========================

.. c:function:: int pci_mmap_legacy_page_range(struct pci_bus *bus, struct vm_area_struct *vma, enum pci_mmap_state mmap_state)

    map legacy memory space to userland

    :param bus:
        bus whose legacy space we're mapping
    :type bus: struct pci_bus \*

    :param vma:
        vma passed in by mmap
    :type vma: struct vm_area_struct \*

    :param mmap_state:
        *undescribed*
    :type mmap_state: enum pci_mmap_state

.. _`pci_mmap_legacy_page_range.description`:

Description
-----------

Map legacy memory space for this device back to userspace using a machine
vector to get the base address.

.. _`ia64_pci_legacy_read`:

ia64_pci_legacy_read
====================

.. c:function:: int ia64_pci_legacy_read(struct pci_bus *bus, u16 port, u32 *val, u8 size)

    read from legacy I/O space

    :param bus:
        bus to read
    :type bus: struct pci_bus \*

    :param port:
        legacy port value
    :type port: u16

    :param val:
        caller allocated storage for returned value
    :type val: u32 \*

    :param size:
        number of bytes to read
    :type size: u8

.. _`ia64_pci_legacy_read.description`:

Description
-----------

Simply reads \ ``size``\  bytes from \ ``port``\  and puts the result in \ ``val``\ .

Again, this (and the write routine) are generic versions that can be
overridden by the platform.  This is necessary on platforms that don't
support legacy I/O routing or that hard fail on legacy I/O timeouts.

.. _`ia64_pci_legacy_write`:

ia64_pci_legacy_write
=====================

.. c:function:: int ia64_pci_legacy_write(struct pci_bus *bus, u16 port, u32 val, u8 size)

    perform a legacy I/O write

    :param bus:
        bus pointer
    :type bus: struct pci_bus \*

    :param port:
        port to write
    :type port: u16

    :param val:
        value to write
    :type val: u32

    :param size:
        number of bytes to write from \ ``val``\ 
    :type size: u8

.. _`ia64_pci_legacy_write.description`:

Description
-----------

Simply writes \ ``size``\  bytes of \ ``val``\  to \ ``port``\ .

.. _`set_pci_dfl_cacheline_size`:

set_pci_dfl_cacheline_size
==========================

.. c:function:: void set_pci_dfl_cacheline_size( void)

    determine cacheline size for PCI devices

    :param void:
        no arguments
    :type void: 

.. _`set_pci_dfl_cacheline_size.description`:

Description
-----------

We want to use the line-size of the outer-most cache.  We assume
that this line-size is the same for all CPUs.

Code mostly taken from arch/ia64/kernel/palinfo.c:cache_info().

.. This file was automatic generated / don't edit.

