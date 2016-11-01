.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/arm64/iort.c

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

.. _`iort_dev_find_its_id`:

iort_dev_find_its_id
====================

.. c:function:: int iort_dev_find_its_id(struct device *dev, u32 req_id, unsigned int idx, int *its_id)

    Find the ITS identifier for a device

    :param struct device \*dev:
        The device.

    :param u32 req_id:
        *undescribed*

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

.. This file was automatic generated / don't edit.

