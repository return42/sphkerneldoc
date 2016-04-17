.. -*- coding: utf-8; mode: rst -*-

=====
pci.c
=====


.. _`ia64_pci_get_legacy_mem`:

ia64_pci_get_legacy_mem
=======================

.. c:function:: char *ia64_pci_get_legacy_mem (struct pci_bus *bus)

    generic legacy mem routine

    :param struct pci_bus \*bus:
        bus to get legacy memory base address for



.. _`ia64_pci_get_legacy_mem.description`:

Description
-----------

Find the base of legacy memory for ``bus``\ .  This is typically the first
megabyte of bus address space for ``bus`` or is simply 0 on platforms whose
chipsets support legacy I/O and memory routing.  Returns the base address
or an error pointer if an error occurred.

This is the ia64 generic version of this routine.  Other platforms
are free to override it with a machine vector.



.. _`pci_mmap_legacy_page_range`:

pci_mmap_legacy_page_range
==========================

.. c:function:: int pci_mmap_legacy_page_range (struct pci_bus *bus, struct vm_area_struct *vma, enum pci_mmap_state mmap_state)

    map legacy memory space to userland

    :param struct pci_bus \*bus:
        bus whose legacy space we're mapping

    :param struct vm_area_struct \*vma:
        vma passed in by mmap

    :param enum pci_mmap_state mmap_state:

        *undescribed*



.. _`pci_mmap_legacy_page_range.description`:

Description
-----------

Map legacy memory space for this device back to userspace using a machine
vector to get the base address.



.. _`ia64_pci_legacy_read`:

ia64_pci_legacy_read
====================

.. c:function:: int ia64_pci_legacy_read (struct pci_bus *bus, u16 port, u32 *val, u8 size)

    read from legacy I/O space

    :param struct pci_bus \*bus:
        bus to read

    :param u16 port:
        legacy port value

    :param u32 \*val:
        caller allocated storage for returned value

    :param u8 size:
        number of bytes to read



.. _`ia64_pci_legacy_read.description`:

Description
-----------

Simply reads ``size`` bytes from ``port`` and puts the result in ``val``\ .

Again, this (and the write routine) are generic versions that can be
overridden by the platform.  This is necessary on platforms that don't
support legacy I/O routing or that hard fail on legacy I/O timeouts.



.. _`ia64_pci_legacy_write`:

ia64_pci_legacy_write
=====================

.. c:function:: int ia64_pci_legacy_write (struct pci_bus *bus, u16 port, u32 val, u8 size)

    perform a legacy I/O write

    :param struct pci_bus \*bus:
        bus pointer

    :param u16 port:
        port to write

    :param u32 val:
        value to write

    :param u8 size:
        number of bytes to write from ``val``



.. _`ia64_pci_legacy_write.description`:

Description
-----------

Simply writes ``size`` bytes of ``val`` to ``port``\ .



.. _`set_pci_dfl_cacheline_size`:

set_pci_dfl_cacheline_size
==========================

.. c:function:: void set_pci_dfl_cacheline_size ( void)

    determine cacheline size for PCI devices

    :param void:
        no arguments



.. _`set_pci_dfl_cacheline_size.description`:

Description
-----------


We want to use the line-size of the outer-most cache.  We assume
that this line-size is the same for all CPUs.

Code mostly taken from arch/ia64/kernel/palinfo.c::c:func:`cache_info`.

