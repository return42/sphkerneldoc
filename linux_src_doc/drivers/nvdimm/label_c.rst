.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvdimm/label.c

.. _`preamble_index`:

preamble_index
==============

.. c:function:: bool preamble_index(struct nvdimm_drvdata *ndd, int idx, struct nd_namespace_index **nsindex_out, unsigned long **free, u32 *nslot)

    common variable initialization for nd_label\_\* routines

    :param struct nvdimm_drvdata \*ndd:
        dimm container for the relevant label set

    :param int idx:
        namespace_index index

    :param struct nd_namespace_index \*\*nsindex_out:
        on return set to the currently active namespace index

    :param unsigned long \*\*free:
        on return set to the free label bitmap in the index

    :param u32 \*nslot:
        on return set to the number of slots in the label space

.. This file was automatic generated / don't edit.

