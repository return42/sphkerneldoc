.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pci/asihpi/hpicmn.c

.. _`hpi_validate_response`:

hpi_validate_response
=====================

.. c:function:: u16 hpi_validate_response(struct hpi_message *phm, struct hpi_response *phr)

    validate that the response has the correct fields filled in, i.e ObjectType, Function etc

    :param phm:
        *undescribed*
    :type phm: struct hpi_message \*

    :param phr:
        *undescribed*
    :type phr: struct hpi_response \*

.. _`hpi_find_adapter`:

hpi_find_adapter
================

.. c:function:: struct hpi_adapter_obj *hpi_find_adapter(u16 adapter_index)

    index wAdapterIndex in an HPI_ADAPTERS_LIST structure.

    :param adapter_index:
        *undescribed*
    :type adapter_index: u16

.. This file was automatic generated / don't edit.

