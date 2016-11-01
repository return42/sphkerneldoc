.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/pci_dn.c

.. _`pci_devs_phb_init_dynamic`:

pci_devs_phb_init_dynamic
=========================

.. c:function:: void pci_devs_phb_init_dynamic(struct pci_controller *phb)

    setup pci devices under this PHB

    :param struct pci_controller \*phb:
        *undescribed*

.. _`pci_devs_phb_init_dynamic.phb`:

phb
---

pci-to-host bridge (top-level bridge connecting to cpu)

This routine is called both during boot, (before the memory
subsystem is set up, before kmalloc is valid) and during the
dynamic lpar operation of adding a PHB to a running system.

.. _`pci_devs_phb_init`:

pci_devs_phb_init
=================

.. c:function:: int pci_devs_phb_init( void)

    Initialize phbs and pci devs under them.

    :param  void:
        no arguments

.. _`pci_devs_phb_init.description`:

Description
-----------

This routine walks over all phb's (pci-host bridges) on the
system, and sets up assorted pci-related structures
(including pci info in the device node structs) for each
pci device found underneath.  This routine runs once,
early in the boot sequence.

.. This file was automatic generated / don't edit.

