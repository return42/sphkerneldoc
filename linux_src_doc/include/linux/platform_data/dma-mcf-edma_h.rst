.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/dma-mcf-edma.h

.. _`mcf_edma_platform_data`:

struct mcf_edma_platform_data
=============================

.. c:type:: struct mcf_edma_platform_data

    platform specific data for eDMA engine

.. _`mcf_edma_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct mcf_edma_platform_data {
        int dma_channels;
        const struct dma_slave_map *slave_map;
        int slavecnt;
    }

.. _`mcf_edma_platform_data.members`:

Members
-------

dma_channels
    *undescribed*

slave_map
    *undescribed*

slavecnt
    *undescribed*

.. _`mcf_edma_platform_data.description`:

Description
-----------

\ ``ver``\                  The eDMA module version.
\ ``dma_channels``\         The number of eDMA channels.

.. This file was automatic generated / don't edit.

