.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/nes/nes.c

.. _`nes_inetaddr_event`:

nes_inetaddr_event
==================

.. c:function:: int nes_inetaddr_event(struct notifier_block *notifier, unsigned long event, void *ptr)

    :param notifier:
        *undescribed*
    :type notifier: struct notifier_block \*

    :param event:
        *undescribed*
    :type event: unsigned long

    :param ptr:
        *undescribed*
    :type ptr: void \*

.. _`nes_net_event`:

nes_net_event
=============

.. c:function:: int nes_net_event(struct notifier_block *notifier, unsigned long event, void *ptr)

    :param notifier:
        *undescribed*
    :type notifier: struct notifier_block \*

    :param event:
        *undescribed*
    :type event: unsigned long

    :param ptr:
        *undescribed*
    :type ptr: void \*

.. _`nes_add_ref`:

nes_add_ref
===========

.. c:function:: void nes_add_ref(struct ib_qp *ibqp)

    :param ibqp:
        *undescribed*
    :type ibqp: struct ib_qp \*

.. _`nes_rem_ref`:

nes_rem_ref
===========

.. c:function:: void nes_rem_ref(struct ib_qp *ibqp)

    :param ibqp:
        *undescribed*
    :type ibqp: struct ib_qp \*

.. _`nes_get_qp`:

nes_get_qp
==========

.. c:function:: struct ib_qp *nes_get_qp(struct ib_device *device, int qpn)

    :param device:
        *undescribed*
    :type device: struct ib_device \*

    :param qpn:
        *undescribed*
    :type qpn: int

.. _`nes_print_macaddr`:

nes_print_macaddr
=================

.. c:function:: void nes_print_macaddr(struct net_device *netdev)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

.. _`nes_interrupt`:

nes_interrupt
=============

.. c:function:: irqreturn_t nes_interrupt(int irq, void *dev_id)

    handle interrupts

    :param irq:
        *undescribed*
    :type irq: int

    :param dev_id:
        *undescribed*
    :type dev_id: void \*

.. _`nes_probe`:

nes_probe
=========

.. c:function:: int nes_probe(struct pci_dev *pcidev, const struct pci_device_id *ent)

    Device initialization

    :param pcidev:
        *undescribed*
    :type pcidev: struct pci_dev \*

    :param ent:
        *undescribed*
    :type ent: const struct pci_device_id \*

.. _`nes_remove`:

nes_remove
==========

.. c:function:: void nes_remove(struct pci_dev *pcidev)

    unload from kernel

    :param pcidev:
        *undescribed*
    :type pcidev: struct pci_dev \*

.. _`nes_init_module`:

nes_init_module
===============

.. c:function:: int nes_init_module( void)

    module initialization entry point

    :param void:
        no arguments
    :type void: 

.. _`nes_exit_module`:

nes_exit_module
===============

.. c:function:: void __exit nes_exit_module( void)

    module unload entry point

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

