.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/pci-txe.c

.. _`mei_txe_probe`:

mei_txe_probe
=============

.. c:function:: int mei_txe_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

    :param ent:
        entry in mei_txe_pci_tbl
    :type ent: const struct pci_device_id \*

.. _`mei_txe_probe.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_txe_shutdown`:

mei_txe_shutdown
================

.. c:function:: void mei_txe_shutdown(struct pci_dev *pdev)

    Device Shutdown Routine

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

.. _`mei_txe_shutdown.description`:

Description
-----------

mei_txe_shutdown is called from the reboot notifier
it's a simplified version of remove so we go down
faster.

.. _`mei_txe_remove`:

mei_txe_remove
==============

.. c:function:: void mei_txe_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

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

    :param dev:
        mei_device
    :type dev: struct mei_device \*

.. _`mei_txe_unset_pm_domain`:

mei_txe_unset_pm_domain
=======================

.. c:function:: void mei_txe_unset_pm_domain(struct mei_device *dev)

    clean pm domain structure for device

    :param dev:
        mei_device
    :type dev: struct mei_device \*

.. This file was automatic generated / don't edit.

