.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/arm64/iort.c

.. _`iort_set_fwnode`:

iort_set_fwnode
===============

.. c:function:: int iort_set_fwnode(struct acpi_iort_node *iort_node, struct fwnode_handle *fwnode)

    Create iort_fwnode and use it to register iommu data in the iort_fwnode_list

    :param struct acpi_iort_node \*iort_node:
        *undescribed*

    :param struct fwnode_handle \*fwnode:
        fwnode associated with the IORT node

.. _`iort_set_fwnode.return`:

Return
------

0 on success
<0 on failure

.. _`iort_get_fwnode`:

iort_get_fwnode
===============

.. c:function:: struct fwnode_handle *iort_get_fwnode(struct acpi_iort_node *node)

    Retrieve fwnode associated with an IORT node

    :param struct acpi_iort_node \*node:
        IORT table node to be looked-up

.. _`iort_get_fwnode.return`:

Return
------

fwnode_handle pointer on success, NULL on failure

.. _`iort_delete_fwnode`:

iort_delete_fwnode
==================

.. c:function:: void iort_delete_fwnode(struct acpi_iort_node *node)

    Delete fwnode associated with an IORT node

    :param struct acpi_iort_node \*node:
        IORT table node associated with fwnode to delete

.. _`iort_register_domain_token`:

iort_register_domain_token
==========================

.. c:function:: int iort_register_domain_token(int trans_id, struct fwnode_handle *fw_node)

    register domain token and related ITS ID to the list from where we can get it back later on.

    :param int trans_id:
        ITS ID.

    :param struct fwnode_handle \*fw_node:
        Domain token.

.. _`iort_register_domain_token.return`:

Return
------

0 on success, -ENOMEM if no memory when allocating list element

.. _`iort_deregister_domain_token`:

iort_deregister_domain_token
============================

.. c:function:: void iort_deregister_domain_token(int trans_id)

    Deregister domain token based on ITS ID

    :param int trans_id:
        ITS ID.

.. _`iort_deregister_domain_token.return`:

Return
------

none.

.. _`iort_find_domain_token`:

iort_find_domain_token
======================

.. c:function:: struct fwnode_handle *iort_find_domain_token(int trans_id)

    Find domain token based on given ITS ID

    :param int trans_id:
        ITS ID.

.. _`iort_find_domain_token.return`:

Return
------

domain token when find on the list, NULL otherwise

.. _`iort_msi_map_rid`:

iort_msi_map_rid
================

.. c:function:: u32 iort_msi_map_rid(struct device *dev, u32 req_id)

    Map a MSI requester ID for a device

    :param struct device \*dev:
        The device for which the mapping is to be done.

    :param u32 req_id:
        The device requester ID.

.. _`iort_msi_map_rid.return`:

Return
------

mapped MSI RID on success, input requester ID otherwise

.. _`iort_pmsi_get_dev_id`:

iort_pmsi_get_dev_id
====================

.. c:function:: int iort_pmsi_get_dev_id(struct device *dev, u32 *dev_id)

    Get the device id for a device

    :param struct device \*dev:
        The device for which the mapping is to be done.

    :param u32 \*dev_id:
        The device ID found.

.. _`iort_pmsi_get_dev_id.return`:

Return
------

0 for successful find a dev id, -ENODEV on error

.. _`iort_dev_find_its_id`:

iort_dev_find_its_id
====================

.. c:function:: int iort_dev_find_its_id(struct device *dev, u32 req_id, unsigned int idx, int *its_id)

    Find the ITS identifier for a device

    :param struct device \*dev:
        The device.

    :param u32 req_id:
        Device's requester ID

    :param unsigned int idx:
        Index of the ITS identifier list.

    :param int \*its_id:
        ITS identifier.

.. _`iort_dev_find_its_id.return`:

Return
------

0 on success, appropriate error value otherwise

.. _`iort_get_device_domain`:

iort_get_device_domain
======================

.. c:function:: struct irq_domain *iort_get_device_domain(struct device *dev, u32 req_id)

    Find MSI domain related to a device

    :param struct device \*dev:
        The device.

    :param u32 req_id:
        Requester ID for the device.

.. _`iort_get_device_domain.return`:

Return
------

the MSI domain for this device, NULL otherwise

.. _`iort_get_platform_device_domain`:

iort_get_platform_device_domain
===============================

.. c:function:: struct irq_domain *iort_get_platform_device_domain(struct device *dev)

    Find MSI domain related to a platform device

    :param struct device \*dev:
        the dev pointer associated with the platform device

.. _`iort_get_platform_device_domain.return`:

Return
------

the MSI domain for this device, NULL otherwise

.. _`iort_set_dma_mask`:

iort_set_dma_mask
=================

.. c:function:: void iort_set_dma_mask(struct device *dev)

    Set-up dma mask for a device.

    :param struct device \*dev:
        device to configure

.. _`iort_iommu_configure`:

iort_iommu_configure
====================

.. c:function:: const struct iommu_ops *iort_iommu_configure(struct device *dev)

    Set-up IOMMU configuration for a device.

    :param struct device \*dev:
        device to configure

.. _`iort_iommu_configure.return`:

Return
------

iommu_ops pointer on configuration success
NULL on configuration failure

.. _`iort_add_smmu_platform_device`:

iort_add_smmu_platform_device
=============================

.. c:function:: int iort_add_smmu_platform_device(struct acpi_iort_node *node)

    Allocate a platform device for SMMU

    :param struct acpi_iort_node \*node:
        Pointer to SMMU ACPI IORT node

.. _`iort_add_smmu_platform_device.return`:

Return
------

0 on success, <0 failure

.. This file was automatic generated / don't edit.

