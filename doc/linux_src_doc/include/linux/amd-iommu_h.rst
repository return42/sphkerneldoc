.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/amd-iommu.h

.. _`amd_pri_dev_erratum_enable_reset`:

AMD_PRI_DEV_ERRATUM_ENABLE_RESET
================================

.. c:function::  AMD_PRI_DEV_ERRATUM_ENABLE_RESET()

    Enable erratum workaround for device in the IOMMUv2 driver

.. _`amd_pri_dev_erratum_enable_reset.description`:

Description
-----------

The function needs to be called before \ :c:func:`amd_iommu_init_device`\ .

.. _`amd_pri_dev_erratum_enable_reset.possible-values-for-the-erratum-number-are-for-now`:

Possible values for the erratum number are for now
--------------------------------------------------

- AMD_PRI_DEV_ERRATUM_ENABLE_RESET - Reset PRI capability when PRI
is enabled
- AMD_PRI_DEV_ERRATUM_LIMIT_REQ_ONE - Limit number of outstanding PRI
requests to one

.. _`amd_iommu_init_device`:

amd_iommu_init_device
=====================

.. c:function:: int amd_iommu_init_device(struct pci_dev *pdev, int pasids)

    Init device for use with IOMMUv2 driver

    :param struct pci_dev \*pdev:
        The PCI device to initialize

    :param int pasids:
        Number of PASIDs to support for this device

.. _`amd_iommu_init_device.description`:

Description
-----------

This function does all setup for the device pdev so that it can be
used with IOMMUv2.
Returns 0 on success or negative value on error.

.. _`amd_iommu_free_device`:

amd_iommu_free_device
=====================

.. c:function:: void amd_iommu_free_device(struct pci_dev *pdev)

    Free all IOMMUv2 related device resources and disable IOMMUv2 usage for this device

    :param struct pci_dev \*pdev:
        The PCI device to disable IOMMUv2 usage for'

.. _`amd_iommu_bind_pasid`:

amd_iommu_bind_pasid
====================

.. c:function:: int amd_iommu_bind_pasid(struct pci_dev *pdev, int pasid, struct task_struct *task)

    Bind a given task to a PASID on a device

    :param struct pci_dev \*pdev:
        The PCI device to bind the task to

    :param int pasid:
        The PASID on the device the task should be bound to

    :param struct task_struct \*task:
        the task to bind

.. _`amd_iommu_bind_pasid.description`:

Description
-----------

The function returns 0 on success or a negative value on error.

.. _`amd_iommu_unbind_pasid`:

amd_iommu_unbind_pasid
======================

.. c:function:: void amd_iommu_unbind_pasid(struct pci_dev *pdev, int pasid)

    Unbind a PASID from its task on a device

    :param struct pci_dev \*pdev:
        The device of the PASID

    :param int pasid:
        The PASID to unbind

.. _`amd_iommu_unbind_pasid.description`:

Description
-----------

When this function returns the device is no longer using the PASID
and the PASID is no longer bound to its task.

.. _`amd_iommu_inv_pri_rsp_success`:

AMD_IOMMU_INV_PRI_RSP_SUCCESS
=============================

.. c:function::  AMD_IOMMU_INV_PRI_RSP_SUCCESS()

    Register a call-back for failed PRI requests

.. _`amd_iommu_inv_pri_rsp_success.description`:

Description
-----------

The IOMMUv2 driver invokes this call-back when it is unable to
successfully handle a PRI request. The device driver can then decide
which PRI response the device should see. Possible return values for
the call-back are:

- AMD_IOMMU_INV_PRI_RSP_SUCCESS - Send SUCCESS back to the device
- AMD_IOMMU_INV_PRI_RSP_INVALID - Send INVALID back to the device
- AMD_IOMMU_INV_PRI_RSP_FAIL    - Send Failure back to the device,
the device is required to disable
PRI when it receives this response

The function returns 0 on success or negative value on error.

.. _`amd_iommu_device_flag_ats_sup`:

AMD_IOMMU_DEVICE_FLAG_ATS_SUP
=============================

.. c:function::  AMD_IOMMU_DEVICE_FLAG_ATS_SUP()

    Get information about IOMMUv2 support of a PCI device

.. _`amd_iommu_device_flag_ats_sup.description`:

Description
-----------

Returns 0 on success, negative value on error

.. _`amd_iommu_invalidate_ctx`:

amd_iommu_invalidate_ctx
========================

.. c:function:: void amd_iommu_invalidate_ctx(struct pci_dev *pdev, int pasid)

    Register a call-back for invalidating a pasid context. This call-back is invoked when the IOMMUv2 driver needs to invalidate a PASID context, for example because the task that is bound to that context is about to exit.

    :param struct pci_dev \*pdev:
        The PCI device the call-back should be registered for

    :param int pasid:
        *undescribed*

.. This file was automatic generated / don't edit.

