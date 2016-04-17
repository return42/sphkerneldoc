.. -*- coding: utf-8; mode: rst -*-

========
hpicmn.c
========


.. _`hpi_validate_response`:

hpi_validate_response
=====================

.. c:function:: u16 hpi_validate_response (struct hpi_message *phm, struct hpi_response *phr)

    :param struct hpi_message \*phm:

        *undescribed*

    :param struct hpi_response \*phr:

        *undescribed*



.. _`hpi_validate_response.description`:

Description
-----------

validate that the response has the correct fields filled in,
i.e ObjectType, Function etc



.. _`hpi_find_adapter`:

hpi_find_adapter
================

.. c:function:: struct hpi_adapter_obj *hpi_find_adapter (u16 adapter_index)

    :param u16 adapter_index:

        *undescribed*



.. _`hpi_find_adapter.description`:

Description
-----------

index wAdapterIndex in an HPI_ADAPTERS_LIST structure.

