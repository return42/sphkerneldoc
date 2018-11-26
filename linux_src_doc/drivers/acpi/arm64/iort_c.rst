.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/arm64/iort.c

.. _`iort_set_fwnode`:

iort_set_fwnode
===============

.. c:function:: int iort_set_fwnode(struct acpi_iort_node *iort_node, struct fwnode_handle *fwnode)

    Create iort_fwnode and use it to register iommu data in the iort_fwnode_list

    :param iort_node:
        *undescribed*
    :type iort_node: struct acpi_iort_node \*

    :param fwnode:
        fwnode associated with the IORT node
    :type fwnode: struct fwnode_handle \*

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

    :param node:
        IORT table node to be looked-up
    :type node: struct acpi_iort_node \*

.. _`iort_get_fwnode.return`:

Return
------

fwnode_handle pointer on success, NULL on failure

.. _`iort_delete_fwnode`:

iort_delete_fwnode
==================

.. c:function:: void iort_delete_fwnode(struct acpi_iort_node *node)

    Delete fwnode associated with an IORT node

    :param node:
        IORT table node associated with fwnode to delete
    :type node: struct acpi_iort_node \*

.. _`iort_get_iort_node`:

iort_get_iort_node
==================

.. c:function:: struct acpi_iort_node *iort_get_iort_node(struct fwnode_handle *fwnode)

    Retrieve iort_node associated with an fwnode

    :param fwnode:
        fwnode associated with device to be looked-up
    :type fwnode: struct fwnode_handle \*

.. _`iort_get_iort_node.return`:

Return
------

iort_node pointer on success, NULL on failure

.. _`iort_register_domain_token`:

iort_register_domain_token
==========================

.. c:function:: int iort_register_domain_token(int trans_id, phys_addr_t base, struct fwnode_handle *fw_node)

    register domain token along with related ITS ID and base address to the list from where we can get it back later on.

    :param trans_id:
        ITS ID.
    :type trans_id: int

    :param base:
        ITS base address.
    :type base: phys_addr_t

    :param fw_node:
        Domain token.
    :type fw_node: struct fwnode_handle \*

.. _`iort_register_domain_token.return`:

Return
------

0 on success, -ENOMEM if no memory when allocating list element

.. _`iort_deregister_domain_token`:

iort_deregister_domain_token
============================

.. c:function:: void iort_deregister_domain_token(int trans_id)

    Deregister domain token based on ITS ID

    :param trans_id:
        ITS ID.
    :type trans_id: int

.. _`iort_deregister_domain_token.return`:

Return
------

none.

.. _`iort_find_domain_token`:

iort_find_domain_token
======================

.. c:function:: struct fwnode_handle *iort_find_domain_token(int trans_id)

    Find domain token based on given ITS ID

    :param trans_id:
        ITS ID.
    :type trans_id: int

.. _`iort_find_domain_token.return`:

Return
------

domain token when find on the list, NULL otherwise

.. _`iort_msi_map_rid`:

iort_msi_map_rid
================

.. c:function:: u32 iort_msi_map_rid(struct device *dev, u32 req_id)

    Map a MSI requester ID for a device

    :param dev:
        The device for which the mapping is to be done.
    :type dev: struct device \*

    :param req_id:
        The device requester ID.
    :type req_id: u32

.. _`iort_msi_map_rid.return`:

Return
------

mapped MSI RID on success, input requester ID otherwise

.. _`iort_pmsi_get_dev_id`:

iort_pmsi_get_dev_id
====================

.. c:function:: int iort_pmsi_get_dev_id(struct device *dev, u32 *dev_id)

    Get the device id for a device

    :param dev:
        The device for which the mapping is to be done.
    :type dev: struct device \*

    :param dev_id:
        The device ID found.
    :type dev_id: u32 \*

.. _`iort_pmsi_get_dev_id.return`:

Return
------

0 for successful find a dev id, -ENODEV on error

.. _`iort_dev_find_its_id`:

iort_dev_find_its_id
====================

.. c:function:: int iort_dev_find_its_id(struct device *dev, u32 req_id, unsigned int idx, int *its_id)

    Find the ITS identifier for a device

    :param dev:
        The device.
    :type dev: struct device \*

    :param req_id:
        Device's requester ID
    :type req_id: u32

    :param idx:
        Index of the ITS identifier list.
    :type idx: unsigned int

    :param its_id:
        ITS identifier.
    :type its_id: int \*

.. _`iort_dev_find_its_id.return`:

Return
------

0 on success, appropriate error value otherwise

.. _`iort_get_device_domain`:

iort_get_device_domain
======================

.. c:function:: struct irq_domain *iort_get_device_domain(struct device *dev, u32 req_id)

    Find MSI domain related to a device

    :param dev:
        The device.
    :type dev: struct device \*

    :param req_id:
        Requester ID for the device.
    :type req_id: u32

.. _`iort_get_device_domain.return`:

Return
------

the MSI domain for this device, NULL otherwise

.. _`iort_get_platform_device_domain`:

iort_get_platform_device_domain
===============================

.. c:function:: struct irq_domain *iort_get_platform_device_domain(struct device *dev)

    Find MSI domain related to a platform device

    :param dev:
        the dev pointer associated with the platform device
    :type dev: struct device \*

.. _`iort_get_platform_device_domain.return`:

Return
------

the MSI domain for this device, NULL otherwise

.. _`iort_iommu_msi_get_resv_regions`:

iort_iommu_msi_get_resv_regions
===============================

.. c:function:: int iort_iommu_msi_get_resv_regions(struct device *dev, struct list_head *head)

    Reserved region driver helper

    :param dev:
        Device from \ :c:func:`iommu_get_resv_regions`\ 
    :type dev: struct device \*

    :param head:
        Reserved region list from \ :c:func:`iommu_get_resv_regions`\ 
    :type head: struct list_head \*

.. _`iort_iommu_msi_get_resv_regions.return`:

Return
------

Number of msi reserved regions on success (0 if platform
doesn't require the reservation or no associated msi regions),
appropriate error value otherwise. The ITS interrupt translation
spaces (ITS_base + SZ_64K, SZ_64K) associated with the device
are the msi reserved regions.

.. _`iort_dma_setup`:

iort_dma_setup
==============

.. c:function:: void iort_dma_setup(struct device *dev, u64 *dma_addr, u64 *dma_size)

    Set-up device DMA parameters.

    :param dev:
        device to configure
    :type dev: struct device \*

    :param dma_addr:
        device DMA address result pointer
    :type dma_addr: u64 \*

    :param dma_size:
        *undescribed*
    :type dma_size: u64 \*

.. _`iort_iommu_configure`:

iort_iommu_configure
====================

.. c:function:: const struct iommu_ops *iort_iommu_configure(struct device *dev)

    Set-up IOMMU configuration for a device.

    :param dev:
        device to configure
    :type dev: struct device \*

.. _`iort_iommu_configure.return`:

Return
------

iommu_ops pointer on configuration success
NULL on configuration failure

.. _`iort_add_platform_device`:

iort_add_platform_device
========================

.. c:function:: int iort_add_platform_device(struct acpi_iort_node *node, const struct iort_dev_config *ops)

    Allocate a platform device for IORT node

    :param node:
        Pointer to device ACPI IORT node
    :type node: struct acpi_iort_node \*

    :param ops:
        *undescribed*
    :type ops: const struct iort_dev_config \*

.. _`iort_add_platform_device.return`:

Return
------

0 on success, <0 failure

.. This file was automatic generated / don't edit.

