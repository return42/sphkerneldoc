.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/qat/qat_common/adf_sriov.c

.. _`adf_disable_sriov`:

adf_disable_sriov
=================

.. c:function:: void adf_disable_sriov(struct adf_accel_dev *accel_dev)

    Disable SRIOV for the device

    :param accel_dev:
        Pointer to accel device.
    :type accel_dev: struct adf_accel_dev \*

.. _`adf_disable_sriov.description`:

Description
-----------

Function disables SRIOV for the accel device.

.. _`adf_disable_sriov.return`:

Return
------

0 on success, error code otherwise.

.. _`adf_sriov_configure`:

adf_sriov_configure
===================

.. c:function:: int adf_sriov_configure(struct pci_dev *pdev, int numvfs)

    Enable SRIOV for the device

    :param pdev:
        Pointer to pci device.
    :type pdev: struct pci_dev \*

    :param numvfs:
        *undescribed*
    :type numvfs: int

.. _`adf_sriov_configure.description`:

Description
-----------

Function enables SRIOV for the pci device.

.. _`adf_sriov_configure.return`:

Return
------

0 on success, error code otherwise.

.. This file was automatic generated / don't edit.

