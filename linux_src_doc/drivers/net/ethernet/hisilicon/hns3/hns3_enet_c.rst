.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns3/hns3_enet.c

.. _`hns3_pci_sriov_configure`:

hns3_pci_sriov_configure
========================

.. c:function:: int hns3_pci_sriov_configure(struct pci_dev *pdev, int num_vfs)

    :param struct pci_dev \*pdev:
        pointer to a pci_dev structure

    :param int num_vfs:
        number of VFs to allocate

.. _`hns3_pci_sriov_configure.description`:

Description
-----------

Enable or change the number of VFs. Called when the user updates the number
of VFs in sysfs.

.. This file was automatic generated / don't edit.

