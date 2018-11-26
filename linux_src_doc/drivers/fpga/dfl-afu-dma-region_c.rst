.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fpga/dfl-afu-dma-region.c

.. _`afu_dma_adjust_locked_vm`:

afu_dma_adjust_locked_vm
========================

.. c:function:: int afu_dma_adjust_locked_vm(struct device *dev, long npages, bool incr)

    adjust locked memory

    :param dev:
        port device
    :type dev: struct device \*

    :param npages:
        number of pages
    :type npages: long

    :param incr:
        increase or decrease locked memory
    :type incr: bool

.. _`afu_dma_adjust_locked_vm.description`:

Description
-----------

Increase or decrease the locked memory size with npages input.

Return 0 on success.
Return -ENOMEM if locked memory size is over the limit and no CAP_IPC_LOCK.

.. _`afu_dma_pin_pages`:

afu_dma_pin_pages
=================

.. c:function:: int afu_dma_pin_pages(struct dfl_feature_platform_data *pdata, struct dfl_afu_dma_region *region)

    pin pages of given dma memory region

    :param pdata:
        feature device platform data
    :type pdata: struct dfl_feature_platform_data \*

    :param region:
        dma memory region to be pinned
    :type region: struct dfl_afu_dma_region \*

.. _`afu_dma_pin_pages.description`:

Description
-----------

Pin all the pages of given dfl_afu_dma_region.
Return 0 for success or negative error code.

.. _`afu_dma_unpin_pages`:

afu_dma_unpin_pages
===================

.. c:function:: void afu_dma_unpin_pages(struct dfl_feature_platform_data *pdata, struct dfl_afu_dma_region *region)

    unpin pages of given dma memory region

    :param pdata:
        feature device platform data
    :type pdata: struct dfl_feature_platform_data \*

    :param region:
        dma memory region to be unpinned
    :type region: struct dfl_afu_dma_region \*

.. _`afu_dma_unpin_pages.description`:

Description
-----------

Unpin all the pages of given dfl_afu_dma_region.
Return 0 for success or negative error code.

.. _`afu_dma_check_continuous_pages`:

afu_dma_check_continuous_pages
==============================

.. c:function:: bool afu_dma_check_continuous_pages(struct dfl_afu_dma_region *region)

    check if pages are continuous

    :param region:
        dma memory region
    :type region: struct dfl_afu_dma_region \*

.. _`afu_dma_check_continuous_pages.description`:

Description
-----------

Return true if pages of given dma memory region have continuous physical
address, otherwise return false.

.. _`dma_region_check_iova`:

dma_region_check_iova
=====================

.. c:function:: bool dma_region_check_iova(struct dfl_afu_dma_region *region, u64 iova, u64 size)

    check if memory area is fully contained in the region

    :param region:
        dma memory region
    :type region: struct dfl_afu_dma_region \*

    :param iova:
        address of the dma memory area
    :type iova: u64

    :param size:
        size of the dma memory area
    :type size: u64

.. _`dma_region_check_iova.description`:

Description
-----------

Compare the dma memory area defined by \ ``iova``\  and \ ``size``\  with given dma region.
Return true if memory area is fully contained in the region, otherwise false.

.. _`afu_dma_region_add`:

afu_dma_region_add
==================

.. c:function:: int afu_dma_region_add(struct dfl_feature_platform_data *pdata, struct dfl_afu_dma_region *region)

    add given dma region to rbtree

    :param pdata:
        feature device platform data
    :type pdata: struct dfl_feature_platform_data \*

    :param region:
        dma region to be added
    :type region: struct dfl_afu_dma_region \*

.. _`afu_dma_region_add.description`:

Description
-----------

Return 0 for success, -EEXIST if dma region has already been added.

Needs to be called with pdata->lock heold.

.. _`afu_dma_region_remove`:

afu_dma_region_remove
=====================

.. c:function:: void afu_dma_region_remove(struct dfl_feature_platform_data *pdata, struct dfl_afu_dma_region *region)

    remove given dma region from rbtree

    :param pdata:
        feature device platform data
    :type pdata: struct dfl_feature_platform_data \*

    :param region:
        dma region to be removed
    :type region: struct dfl_afu_dma_region \*

.. _`afu_dma_region_remove.description`:

Description
-----------

Needs to be called with pdata->lock heold.

.. _`afu_dma_region_destroy`:

afu_dma_region_destroy
======================

.. c:function:: void afu_dma_region_destroy(struct dfl_feature_platform_data *pdata)

    destroy all regions in rbtree

    :param pdata:
        feature device platform data
    :type pdata: struct dfl_feature_platform_data \*

.. _`afu_dma_region_destroy.description`:

Description
-----------

Needs to be called with pdata->lock heold.

.. _`afu_dma_region_find`:

afu_dma_region_find
===================

.. c:function:: struct dfl_afu_dma_region *afu_dma_region_find(struct dfl_feature_platform_data *pdata, u64 iova, u64 size)

    find the dma region from rbtree based on iova and size

    :param pdata:
        feature device platform data
    :type pdata: struct dfl_feature_platform_data \*

    :param iova:
        address of the dma memory area
    :type iova: u64

    :param size:
        size of the dma memory area
    :type size: u64

.. _`afu_dma_region_find.description`:

Description
-----------

It finds the dma region from the rbtree based on \ ``iova``\  and \ ``size``\ :
- if \ ``size``\  == 0, it finds the dma region which starts from \ ``iova``\ 
- otherwise, it finds the dma region which fully contains
[@iova, \ ``iova``\ +size)
If nothing is matched returns NULL.

Needs to be called with pdata->lock held.

.. _`afu_dma_region_find_iova`:

afu_dma_region_find_iova
========================

.. c:function:: struct dfl_afu_dma_region *afu_dma_region_find_iova(struct dfl_feature_platform_data *pdata, u64 iova)

    find the dma region from rbtree by iova

    :param pdata:
        feature device platform data
    :type pdata: struct dfl_feature_platform_data \*

    :param iova:
        address of the dma region
    :type iova: u64

.. _`afu_dma_region_find_iova.description`:

Description
-----------

Needs to be called with pdata->lock held.

.. _`afu_dma_map_region`:

afu_dma_map_region
==================

.. c:function:: int afu_dma_map_region(struct dfl_feature_platform_data *pdata, u64 user_addr, u64 length, u64 *iova)

    map memory region for dma

    :param pdata:
        feature device platform data
    :type pdata: struct dfl_feature_platform_data \*

    :param user_addr:
        address of the memory region
    :type user_addr: u64

    :param length:
        size of the memory region
    :type length: u64

    :param iova:
        pointer of iova address
    :type iova: u64 \*

.. _`afu_dma_map_region.description`:

Description
-----------

Map memory region defined by \ ``user_addr``\  and \ ``length``\ , and return dma address
of the memory region via \ ``iova``\ .
Return 0 for success, otherwise error code.

.. _`afu_dma_unmap_region`:

afu_dma_unmap_region
====================

.. c:function:: int afu_dma_unmap_region(struct dfl_feature_platform_data *pdata, u64 iova)

    unmap dma memory region

    :param pdata:
        feature device platform data
    :type pdata: struct dfl_feature_platform_data \*

    :param iova:
        dma address of the region
    :type iova: u64

.. _`afu_dma_unmap_region.description`:

Description
-----------

Unmap dma memory region based on \ ``iova``\ .
Return 0 for success, otherwise error code.

.. This file was automatic generated / don't edit.

