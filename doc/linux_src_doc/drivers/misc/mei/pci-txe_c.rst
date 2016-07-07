.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/pci-txe.c

.. _`mei_txe_probe`:

mei_txe_probe
=============

.. c:function:: int mei_txe_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param struct pci_dev \*pdev:
        PCI device structure

    :param const struct pci_device_id \*ent:
        entry in mei_txe_pci_tbl

.. _`mei_txe_probe.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_txe_remove`:

mei_txe_remove
==============

.. c:function:: void mei_txe_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param struct pci_dev \*pdev:
        PCI device structure

.. _`mei_txe_remove.description`:

Description
-----------

mei_remove is called by the PCI subsystem to alert the driver
that it should release a PCI device.

.. _`mei_txe_set_pm_domain`:

mei_txe_set_pm_domain
=====================

.. c:function:: void mei_txe_set_pm_domain(struct mei_device *dev)

    fill and set pm domain structure for device

    :param struct mei_device \*dev:
        mei_device

.. _`mei_txe_unset_pm_domain`:

mei_txe_unset_pm_domain
=======================

.. c:function:: void mei_txe_unset_pm_domain(struct mei_device *dev)

    clean pm domain structure for device

    :param struct mei_device \*dev:
        mei_device

.. This file was automatic generated / don't edit.

