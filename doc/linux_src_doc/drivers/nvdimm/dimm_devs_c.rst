.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvdimm/dimm_devs.c

.. _`nvdimm_init_nsarea`:

nvdimm_init_nsarea
==================

.. c:function:: int nvdimm_init_nsarea(struct nvdimm_drvdata *ndd)

    determine the geometry of a dimm's namespace area

    :param struct nvdimm_drvdata \*ndd:
        *undescribed*

.. _`nd_blk_available_dpa`:

nd_blk_available_dpa
====================

.. c:function:: resource_size_t nd_blk_available_dpa(struct nd_mapping *nd_mapping)

    account the unused dpa of BLK region

    :param struct nd_mapping \*nd_mapping:
        container of dpa-resource-root + labels

.. _`nd_blk_available_dpa.description`:

Description
-----------

Unlike PMEM, BLK namespaces can occupy discontiguous DPA ranges.

.. _`nd_pmem_available_dpa`:

nd_pmem_available_dpa
=====================

.. c:function:: resource_size_t nd_pmem_available_dpa(struct nd_region *nd_region, struct nd_mapping *nd_mapping, resource_size_t *overlap)

    for the given dimm+region account unallocated dpa

    :param struct nd_region \*nd_region:
        constrain available space check to this reference region

    :param struct nd_mapping \*nd_mapping:
        container of dpa-resource-root + labels

    :param resource_size_t \*overlap:
        calculate available space assuming this level of overlap

.. _`nd_pmem_available_dpa.description`:

Description
-----------

Validate that a PMEM label, if present, aligns with the start of an
interleave set and truncate the available size at the lowest BLK
overlap point.

The expectation is that this routine is called multiple times as it
probes for the largest BLK encroachment for any single member DIMM of
the interleave set.  Once that value is determined the PMEM-limit for
the set can be established.

.. _`nvdimm_allocated_dpa`:

nvdimm_allocated_dpa
====================

.. c:function:: resource_size_t nvdimm_allocated_dpa(struct nvdimm_drvdata *ndd, struct nd_label_id *label_id)

    sum up the dpa currently allocated to this label_id

    :param struct nvdimm_drvdata \*ndd:
        *undescribed*

    :param struct nd_label_id \*label_id:
        dpa resource name of the form {pmem\|blk}-<human readable uuid>

.. This file was automatic generated / don't edit.

