.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvdimm/label.c

.. _`preamble_index`:

preamble_index
==============

.. c:function:: bool preamble_index(struct nvdimm_drvdata *ndd, int idx, struct nd_namespace_index **nsindex_out, unsigned long **free, u32 *nslot)

    common variable initialization for nd_label\_\* routines

    :param ndd:
        dimm container for the relevant label set
    :type ndd: struct nvdimm_drvdata \*

    :param idx:
        namespace_index index
    :type idx: int

    :param nsindex_out:
        on return set to the currently active namespace index
    :type nsindex_out: struct nd_namespace_index \*\*

    :param free:
        on return set to the free label bitmap in the index
    :type free: unsigned long \*\*

    :param nslot:
        on return set to the number of slots in the label space
    :type nslot: u32 \*

.. This file was automatic generated / don't edit.

