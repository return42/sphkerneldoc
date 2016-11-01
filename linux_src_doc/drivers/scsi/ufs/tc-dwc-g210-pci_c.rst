.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/ufs/tc-dwc-g210-pci.c

.. _`tc_dwc_g210_pci_shutdown`:

tc_dwc_g210_pci_shutdown
========================

.. c:function:: void tc_dwc_g210_pci_shutdown(struct pci_dev *pdev)

    main function to put the controller in reset state

    :param struct pci_dev \*pdev:
        pointer to PCI device handle

.. _`tc_dwc_g210_pci_remove`:

tc_dwc_g210_pci_remove
======================

.. c:function:: void tc_dwc_g210_pci_remove(struct pci_dev *pdev)

    de-allocate PCI/SCSI host and host memory space data structure memory \ ``pdev``\  - pointer to PCI handle

    :param struct pci_dev \*pdev:
        *undescribed*

.. _`tc_dwc_g210_pci_probe`:

tc_dwc_g210_pci_probe
=====================

.. c:function:: int tc_dwc_g210_pci_probe(struct pci_dev *pdev, const struct pci_device_id *id)

    probe routine of the driver

    :param struct pci_dev \*pdev:
        pointer to PCI device handle

    :param const struct pci_device_id \*id:
        PCI device id

.. _`tc_dwc_g210_pci_probe.description`:

Description
-----------

Returns 0 on success, non-zero value on failure

.. This file was automatic generated / don't edit.

