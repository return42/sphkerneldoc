.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/ufs/tc-dwc-g210-pci.c

.. _`tc_dwc_g210_pci_shutdown`:

tc_dwc_g210_pci_shutdown
========================

.. c:function:: void tc_dwc_g210_pci_shutdown(struct pci_dev *pdev)

    main function to put the controller in reset state

    :param pdev:
        pointer to PCI device handle
    :type pdev: struct pci_dev \*

.. _`tc_dwc_g210_pci_remove`:

tc_dwc_g210_pci_remove
======================

.. c:function:: void tc_dwc_g210_pci_remove(struct pci_dev *pdev)

    de-allocate PCI/SCSI host and host memory space data structure memory

    :param pdev:
        pointer to PCI handle
    :type pdev: struct pci_dev \*

.. _`tc_dwc_g210_pci_probe`:

tc_dwc_g210_pci_probe
=====================

.. c:function:: int tc_dwc_g210_pci_probe(struct pci_dev *pdev, const struct pci_device_id *id)

    probe routine of the driver

    :param pdev:
        pointer to PCI device handle
    :type pdev: struct pci_dev \*

    :param id:
        PCI device id
    :type id: const struct pci_device_id \*

.. _`tc_dwc_g210_pci_probe.description`:

Description
-----------

Returns 0 on success, non-zero value on failure

.. This file was automatic generated / don't edit.

