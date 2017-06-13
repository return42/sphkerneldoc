.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/pci-me.c

.. _`mei_me_quirk_probe`:

mei_me_quirk_probe
==================

.. c:function:: bool mei_me_quirk_probe(struct pci_dev *pdev, const struct mei_cfg *cfg)

    probe for devices that doesn't valid ME interface

    :param struct pci_dev \*pdev:
        PCI device structure

    :param const struct mei_cfg \*cfg:
        per generation config

.. _`mei_me_quirk_probe.return`:

Return
------

true if ME Interface is valid, false otherwise

.. _`mei_me_probe`:

mei_me_probe
============

.. c:function:: int mei_me_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param struct pci_dev \*pdev:
        PCI device structure

    :param const struct pci_device_id \*ent:
        entry in kcs_pci_tbl

.. _`mei_me_probe.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_me_shutdown`:

mei_me_shutdown
===============

.. c:function:: void mei_me_shutdown(struct pci_dev *pdev)

    Device Removal Routine

    :param struct pci_dev \*pdev:
        PCI device structure

.. _`mei_me_shutdown.description`:

Description
-----------

mei_me_shutdown is called from the reboot notifier
it's a simplified version of remove so we go down
faster.

.. _`mei_me_remove`:

mei_me_remove
=============

.. c:function:: void mei_me_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param struct pci_dev \*pdev:
        PCI device structure

.. _`mei_me_remove.description`:

Description
-----------

mei_me_remove is called by the PCI subsystem to alert the driver
that it should release a PCI device.

.. _`mei_me_set_pm_domain`:

mei_me_set_pm_domain
====================

.. c:function:: void mei_me_set_pm_domain(struct mei_device *dev)

    fill and set pm domain structure for device

    :param struct mei_device \*dev:
        mei_device

.. _`mei_me_unset_pm_domain`:

mei_me_unset_pm_domain
======================

.. c:function:: void mei_me_unset_pm_domain(struct mei_device *dev)

    clean pm domain structure for device

    :param struct mei_device \*dev:
        mei_device

.. This file was automatic generated / don't edit.

