.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/eeh_cache.c

.. _`eeh_addr_cache_get_dev`:

eeh_addr_cache_get_dev
======================

.. c:function:: struct eeh_dev *eeh_addr_cache_get_dev(unsigned long addr)

    Get device, given only address

    :param unsigned long addr:
        mmio (PIO) phys address or i/o port number

.. _`eeh_addr_cache_get_dev.description`:

Description
-----------

Given an mmio phys address, or a port number, find a pci device
that implements this address.  I/O port numbers are assumed to be offset
from zero (that is, they do \*not\* have pci_io_addr added in).
It is safe to call this function within an interrupt.

.. _`eeh_addr_cache_insert_dev`:

eeh_addr_cache_insert_dev
=========================

.. c:function:: void eeh_addr_cache_insert_dev(struct pci_dev *dev)

    Add a device to the address cache

    :param struct pci_dev \*dev:
        PCI device whose I/O addresses we are interested in.

.. _`eeh_addr_cache_insert_dev.description`:

Description
-----------

In order to support the fast lookup of devices based on addresses,
we maintain a cache of devices that can be quickly searched.
This routine adds a device to that cache.

.. _`eeh_addr_cache_rmv_dev`:

eeh_addr_cache_rmv_dev
======================

.. c:function:: void eeh_addr_cache_rmv_dev(struct pci_dev *dev)

    remove pci device from addr cache

    :param struct pci_dev \*dev:
        device to remove

.. _`eeh_addr_cache_rmv_dev.description`:

Description
-----------

Remove a device from the addr-cache tree.
This is potentially expensive, since it will walk
the tree multiple times (once per resource).
But so what; device removal doesn't need to be that fast.

.. _`eeh_addr_cache_build`:

eeh_addr_cache_build
====================

.. c:function:: void eeh_addr_cache_build( void)

    Build a cache of I/O addresses

    :param  void:
        no arguments

.. _`eeh_addr_cache_build.description`:

Description
-----------

Build a cache of pci i/o addresses.  This cache will be used to
find the pci device that corresponds to a given address.
This routine scans all pci busses to build the cache.
Must be run late in boot process, after the pci controllers
have been scanned for devices (after all device resources are known).

.. This file was automatic generated / don't edit.

