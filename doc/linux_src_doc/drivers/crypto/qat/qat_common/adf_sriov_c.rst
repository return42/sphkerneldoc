.. -*- coding: utf-8; mode: rst -*-

===========
adf_sriov.c
===========


.. _`adf_disable_sriov`:

adf_disable_sriov
=================

.. c:function:: void adf_disable_sriov (struct adf_accel_dev *accel_dev)

    Disable SRIOV for the device

    :param struct adf_accel_dev \*accel_dev:

        *undescribed*



.. _`adf_disable_sriov.description`:

Description
-----------

Function disables SRIOV for the pci device.



.. _`adf_disable_sriov.return`:

Return
------

0 on success, error code otherwise.



.. _`adf_sriov_configure`:

adf_sriov_configure
===================

.. c:function:: int adf_sriov_configure (struct pci_dev *pdev, int numvfs)

    Enable SRIOV for the device

    :param struct pci_dev \*pdev:
        Pointer to pci device.

    :param int numvfs:

        *undescribed*



.. _`adf_sriov_configure.description`:

Description
-----------

Function enables SRIOV for the pci device.



.. _`adf_sriov_configure.return`:

Return
------

0 on success, error code otherwise.

