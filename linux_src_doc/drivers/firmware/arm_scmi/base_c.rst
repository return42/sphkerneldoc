.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/arm_scmi/base.c

.. _`scmi_base_attributes_get`:

scmi_base_attributes_get
========================

.. c:function:: int scmi_base_attributes_get(const struct scmi_handle *handle)

    gets the implementation details that are associated with the base protocol.

    :param handle:
        SCMI entity handle
    :type handle: const struct scmi_handle \*

.. _`scmi_base_attributes_get.return`:

Return
------

0 on success, else appropriate SCMI error.

.. _`scmi_base_vendor_id_get`:

scmi_base_vendor_id_get
=======================

.. c:function:: int scmi_base_vendor_id_get(const struct scmi_handle *handle, bool sub_vendor)

    gets vendor/subvendor identifier ASCII string.

    :param handle:
        SCMI entity handle
    :type handle: const struct scmi_handle \*

    :param sub_vendor:
        specify true if sub-vendor ID is needed
    :type sub_vendor: bool

.. _`scmi_base_vendor_id_get.return`:

Return
------

0 on success, else appropriate SCMI error.

.. _`scmi_base_implementation_version_get`:

scmi_base_implementation_version_get
====================================

.. c:function:: int scmi_base_implementation_version_get(const struct scmi_handle *handle)

    gets a vendor-specific implementation 32-bit version. The format of the version number is vendor-specific

    :param handle:
        SCMI entity handle
    :type handle: const struct scmi_handle \*

.. _`scmi_base_implementation_version_get.return`:

Return
------

0 on success, else appropriate SCMI error.

.. _`scmi_base_implementation_list_get`:

scmi_base_implementation_list_get
=================================

.. c:function:: int scmi_base_implementation_list_get(const struct scmi_handle *handle, u8 *protocols_imp)

    gets the list of protocols it is OSPM is allowed to access

    :param handle:
        SCMI entity handle
    :type handle: const struct scmi_handle \*

    :param protocols_imp:
        pointer to hold the list of protocol identifiers
    :type protocols_imp: u8 \*

.. _`scmi_base_implementation_list_get.return`:

Return
------

0 on success, else appropriate SCMI error.

.. _`scmi_base_discover_agent_get`:

scmi_base_discover_agent_get
============================

.. c:function:: int scmi_base_discover_agent_get(const struct scmi_handle *handle, int id, char *name)

    discover the name of an agent

    :param handle:
        SCMI entity handle
    :type handle: const struct scmi_handle \*

    :param id:
        Agent identifier
    :type id: int

    :param name:
        Agent identifier ASCII string
    :type name: char \*

.. _`scmi_base_discover_agent_get.description`:

Description
-----------

An agent id of 0 is reserved to identify the platform itself.
Generally operating system is represented as "OSPM"

.. _`scmi_base_discover_agent_get.return`:

Return
------

0 on success, else appropriate SCMI error.

.. This file was automatic generated / don't edit.

