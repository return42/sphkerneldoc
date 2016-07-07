.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/eeh_dev.c

.. _`eeh_dev_init`:

eeh_dev_init
============

.. c:function:: void *eeh_dev_init(struct pci_dn *pdn, void *data)

    Create EEH device according to OF node

    :param struct pci_dn \*pdn:
        PCI device node

    :param void \*data:
        PHB

.. _`eeh_dev_init.description`:

Description
-----------

It will create EEH device according to the given OF node. The function
might be called by PCI emunation, DR, PHB hotplug.

.. _`eeh_dev_phb_init_dynamic`:

eeh_dev_phb_init_dynamic
========================

.. c:function:: void eeh_dev_phb_init_dynamic(struct pci_controller *phb)

    Create EEH devices for devices included in PHB

    :param struct pci_controller \*phb:
        PHB

.. _`eeh_dev_phb_init_dynamic.description`:

Description
-----------

Scan the PHB OF node and its child association, then create the
EEH devices accordingly

.. _`eeh_dev_phb_init`:

eeh_dev_phb_init
================

.. c:function:: int eeh_dev_phb_init( void)

    Create EEH devices for devices included in existing PHBs

    :param  void:
        no arguments

.. _`eeh_dev_phb_init.description`:

Description
-----------

Scan all the existing PHBs and create EEH devices for their OF
nodes and their children OF nodes

.. This file was automatic generated / don't edit.

