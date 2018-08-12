.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/controller/vmd.c

.. _`vmd_irq`:

struct vmd_irq
==============

.. c:type:: struct vmd_irq

    private data to map driver IRQ to the VMD shared vector

.. _`vmd_irq.definition`:

Definition
----------

.. code-block:: c

    struct vmd_irq {
        struct list_head node;
        struct vmd_irq_list *irq;
        bool enabled;
        unsigned int virq;
    }

.. _`vmd_irq.members`:

Members
-------

node
    list item for parent traversal.

irq
    back pointer to parent.

enabled
    true if driver enabled IRQ

virq
    the virtual IRQ value provided to the requesting driver.

.. _`vmd_irq.description`:

Description
-----------

Every MSI/MSI-X IRQ requested for a device in a VMD domain will be mapped to
a VMD IRQ using this structure.

.. _`vmd_irq_list`:

struct vmd_irq_list
===================

.. c:type:: struct vmd_irq_list

    list of driver requested IRQs mapping to a VMD vector

.. _`vmd_irq_list.definition`:

Definition
----------

.. code-block:: c

    struct vmd_irq_list {
        struct list_head irq_list;
        struct srcu_struct srcu;
        unsigned int count;
    }

.. _`vmd_irq_list.members`:

Members
-------

irq_list
    the list of irq's the VMD one demuxes to.

srcu
    SRCU struct for local synchronization.

count
    number of child IRQs assigned to this vector; used to track
    sharing.

.. This file was automatic generated / don't edit.

