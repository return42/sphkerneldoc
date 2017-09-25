.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvdimm/nd-core.h

.. _`blk_alloc_info`:

struct blk_alloc_info
=====================

.. c:type:: struct blk_alloc_info

    tracking info for BLK dpa scanning

.. _`blk_alloc_info.definition`:

Definition
----------

.. code-block:: c

    struct blk_alloc_info {
        struct nd_mapping *nd_mapping;
        resource_size_t available, busy;
        struct resource *res;
    }

.. _`blk_alloc_info.members`:

Members
-------

nd_mapping
    blk region mapping boundaries

available
    decremented in alias_dpa_busy as aliased PMEM is scanned

busy
    decremented in blk_dpa_busy to account for ranges already
    handled by alias_dpa_busy

res
    alias_dpa_busy interprets this a free space range that needs to
    be truncated to the valid BLK allocation starting DPA, blk_dpa_busy
    treats it as a busy range that needs the aliased PMEM ranges
    truncated.

.. This file was automatic generated / don't edit.

