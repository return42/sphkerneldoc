.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fpga/dfl-afu-region.c

.. _`afu_mmio_region_init`:

afu_mmio_region_init
====================

.. c:function:: void afu_mmio_region_init(struct dfl_feature_platform_data *pdata)

    init function for afu mmio region support

    :param pdata:
        afu platform device's pdata.
    :type pdata: struct dfl_feature_platform_data \*

.. _`afu_mmio_region_add`:

afu_mmio_region_add
===================

.. c:function:: int afu_mmio_region_add(struct dfl_feature_platform_data *pdata, u32 region_index, u64 region_size, u64 phys, u32 flags)

    add a mmio region to given feature dev.

    :param pdata:
        *undescribed*
    :type pdata: struct dfl_feature_platform_data \*

    :param region_index:
        region index.
    :type region_index: u32

    :param region_size:
        region size.
    :type region_size: u64

    :param phys:
        region's physical address of this region.
    :type phys: u64

    :param flags:
        region flags (access permission).
    :type flags: u32

.. _`afu_mmio_region_add.return`:

Return
------

0 on success, negative error code otherwise.

.. _`afu_mmio_region_destroy`:

afu_mmio_region_destroy
=======================

.. c:function:: void afu_mmio_region_destroy(struct dfl_feature_platform_data *pdata)

    destroy all mmio regions under given feature dev.

    :param pdata:
        afu platform device's pdata.
    :type pdata: struct dfl_feature_platform_data \*

.. _`afu_mmio_region_get_by_index`:

afu_mmio_region_get_by_index
============================

.. c:function:: int afu_mmio_region_get_by_index(struct dfl_feature_platform_data *pdata, u32 region_index, struct dfl_afu_mmio_region *pregion)

    find an afu region by index.

    :param pdata:
        afu platform device's pdata.
    :type pdata: struct dfl_feature_platform_data \*

    :param region_index:
        region index.
    :type region_index: u32

    :param pregion:
        ptr to region for result.
    :type pregion: struct dfl_afu_mmio_region \*

.. _`afu_mmio_region_get_by_index.return`:

Return
------

0 on success, negative error code otherwise.

.. _`afu_mmio_region_get_by_offset`:

afu_mmio_region_get_by_offset
=============================

.. c:function:: int afu_mmio_region_get_by_offset(struct dfl_feature_platform_data *pdata, u64 offset, u64 size, struct dfl_afu_mmio_region *pregion)

    find an afu mmio region by offset and size

    :param pdata:
        afu platform device's pdata.
    :type pdata: struct dfl_feature_platform_data \*

    :param offset:
        region offset from start of the device fd.
    :type offset: u64

    :param size:
        region size.
    :type size: u64

    :param pregion:
        ptr to region for result.
    :type pregion: struct dfl_afu_mmio_region \*

.. _`afu_mmio_region_get_by_offset.description`:

Description
-----------

Find the region which fully contains the region described by input
parameters (offset and size) from the feature dev's region linked list.

.. _`afu_mmio_region_get_by_offset.return`:

Return
------

0 on success, negative error code otherwise.

.. This file was automatic generated / don't edit.

