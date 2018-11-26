.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/ufs/ufshcd-pci.c

.. _`ufshcd_pci_suspend`:

ufshcd_pci_suspend
==================

.. c:function:: int ufshcd_pci_suspend(struct device *dev)

    suspend power management function

    :param dev:
        pointer to PCI device handle
    :type dev: struct device \*

.. _`ufshcd_pci_suspend.description`:

Description
-----------

Returns 0 if successful
Returns non-zero otherwise

.. _`ufshcd_pci_resume`:

ufshcd_pci_resume
=================

.. c:function:: int ufshcd_pci_resume(struct device *dev)

    resume power management function

    :param dev:
        pointer to PCI device handle
    :type dev: struct device \*

.. _`ufshcd_pci_resume.description`:

Description
-----------

Returns 0 if successful
Returns non-zero otherwise

.. _`ufshcd_pci_shutdown`:

ufshcd_pci_shutdown
===================

.. c:function:: void ufshcd_pci_shutdown(struct pci_dev *pdev)

    main function to put the controller in reset state

    :param pdev:
        pointer to PCI device handle
    :type pdev: struct pci_dev \*

.. _`ufshcd_pci_remove`:

ufshcd_pci_remove
=================

.. c:function:: void ufshcd_pci_remove(struct pci_dev *pdev)

    de-allocate PCI/SCSI host and host memory space data structure memory

    :param pdev:
        pointer to PCI handle
    :type pdev: struct pci_dev \*

.. _`ufshcd_pci_probe`:

ufshcd_pci_probe
================

.. c:function:: int ufshcd_pci_probe(struct pci_dev *pdev, const struct pci_device_id *id)

    probe routine of the driver

    :param pdev:
        pointer to PCI device handle
    :type pdev: struct pci_dev \*

    :param id:
        PCI device id
    :type id: const struct pci_device_id \*

.. _`ufshcd_pci_probe.description`:

Description
-----------

Returns 0 on success, non-zero value on failure

.. This file was automatic generated / don't edit.

