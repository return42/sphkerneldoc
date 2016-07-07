.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ipack/carriers/tpci200.h

.. _`slot_irq`:

struct slot_irq
===============

.. c:type:: struct slot_irq

    slot IRQ definition. \ ``vector``\       Vector number \ ``handler``\      Handler called when IRQ arrives \ ``arg``\          Handler argument

.. _`slot_irq.definition`:

Definition
----------

.. code-block:: c

    struct slot_irq {
        struct ipack_device *holder;
        int vector;
        irqreturn_t (* handler) (void *);
        void *arg;
    }

.. _`slot_irq.members`:

Members
-------

holder
    *undescribed*

vector
    *undescribed*

handler
    *undescribed*

arg
    *undescribed*

.. _`tpci200_slot`:

struct tpci200_slot
===================

.. c:type:: struct tpci200_slot

    data specific to the tpci200 slot. \ ``slot_id``\      Slot identification gived to external interface \ ``irq``\          Slot IRQ infos \ ``io_phys``\      IO physical base address register of the slot \ ``id_phys``\      ID physical base address register of the slot \ ``int_phys``\     INT physical base address register of the slot \ ``mem_phys``\     MEM physical base address register of the slot

.. _`tpci200_slot.definition`:

Definition
----------

.. code-block:: c

    struct tpci200_slot {
        struct slot_irq *irq;
    }

.. _`tpci200_slot.members`:

Members
-------

irq
    *undescribed*

.. _`tpci200_infos`:

struct tpci200_infos
====================

.. c:type:: struct tpci200_infos

    informations specific of the TPCI200 tpci200. \ ``pci_dev``\              PCI device \ ``interface_regs``\       Pointer to IP interface space (Bar 2) \ ``ioidint_space``\        Pointer to IP ID, IO and INT space (Bar 3) \ ``mem8_space``\           Pointer to MEM space (Bar 4)

.. _`tpci200_infos.definition`:

Definition
----------

.. code-block:: c

    struct tpci200_infos {
        struct pci_dev *pdev;
        struct pci_device_id *id_table;
        struct tpci200_regs __iomem *interface_regs;
        void __iomem *cfg_regs;
        struct ipack_bus_device *ipack_bus;
    }

.. _`tpci200_infos.members`:

Members
-------

pdev
    *undescribed*

id_table
    *undescribed*

interface_regs
    *undescribed*

cfg_regs
    *undescribed*

ipack_bus
    *undescribed*

.. This file was automatic generated / don't edit.

