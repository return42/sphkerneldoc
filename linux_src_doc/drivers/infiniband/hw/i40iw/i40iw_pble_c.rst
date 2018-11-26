.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_pble.c

.. _`i40iw_destroy_pble_pool`:

i40iw_destroy_pble_pool
=======================

.. c:function:: void i40iw_destroy_pble_pool(struct i40iw_sc_dev *dev, struct i40iw_hmc_pble_rsrc *pble_rsrc)

    destroy pool during module unload

    :param dev:
        *undescribed*
    :type dev: struct i40iw_sc_dev \*

    :param pble_rsrc:
        pble resources
    :type pble_rsrc: struct i40iw_hmc_pble_rsrc \*

.. _`i40iw_hmc_init_pble`:

i40iw_hmc_init_pble
===================

.. c:function:: enum i40iw_status_code i40iw_hmc_init_pble(struct i40iw_sc_dev *dev, struct i40iw_hmc_pble_rsrc *pble_rsrc)

    Initialize pble resources during module load

    :param dev:
        i40iw_sc_dev struct
    :type dev: struct i40iw_sc_dev \*

    :param pble_rsrc:
        pble resources
    :type pble_rsrc: struct i40iw_hmc_pble_rsrc \*

.. _`get_sd_pd_idx`:

get_sd_pd_idx
=============

.. c:function:: void get_sd_pd_idx(struct i40iw_hmc_pble_rsrc *pble_rsrc, struct sd_pd_idx *idx)

    Returns sd index, pd index and rel_pd_idx from fpm address \ ````\  pble_rsrc: structure containing fpm address \ ````\  idx: where to return indexes

    :param pble_rsrc:
        *undescribed*
    :type pble_rsrc: struct i40iw_hmc_pble_rsrc \*

    :param idx:
        *undescribed*
    :type idx: struct sd_pd_idx \*

.. _`add_sd_direct`:

add_sd_direct
=============

.. c:function:: enum i40iw_status_code add_sd_direct(struct i40iw_sc_dev *dev, struct i40iw_hmc_pble_rsrc *pble_rsrc, struct i40iw_add_page_info *info)

    add sd direct for pble

    :param dev:
        hardware control device structure
    :type dev: struct i40iw_sc_dev \*

    :param pble_rsrc:
        pble resource ptr
    :type pble_rsrc: struct i40iw_hmc_pble_rsrc \*

    :param info:
        page info for sd
    :type info: struct i40iw_add_page_info \*

.. _`i40iw_free_vmalloc_mem`:

i40iw_free_vmalloc_mem
======================

.. c:function:: void i40iw_free_vmalloc_mem(struct i40iw_hw *hw, struct i40iw_chunk *chunk)

    free vmalloc during close

    :param hw:
        hw struct
    :type hw: struct i40iw_hw \*

    :param chunk:
        chunk information for vmalloc
    :type chunk: struct i40iw_chunk \*

.. _`i40iw_get_vmalloc_mem`:

i40iw_get_vmalloc_mem
=====================

.. c:function:: enum i40iw_status_code i40iw_get_vmalloc_mem(struct i40iw_hw *hw, struct i40iw_chunk *chunk, int pg_cnt)

    get 2M page for sd

    :param hw:
        hardware address
    :type hw: struct i40iw_hw \*

    :param chunk:
        chunk to adf
    :type chunk: struct i40iw_chunk \*

    :param pg_cnt:
        #of 4 K pages
    :type pg_cnt: int

.. _`fpm_to_idx`:

fpm_to_idx
==========

.. c:function:: u32 fpm_to_idx(struct i40iw_hmc_pble_rsrc *pble_rsrc, u64 addr)

    given fpm address, get pble index

    :param pble_rsrc:
        pble resource management
    :type pble_rsrc: struct i40iw_hmc_pble_rsrc \*

    :param addr:
        fpm address for index
    :type addr: u64

.. _`add_bp_pages`:

add_bp_pages
============

.. c:function:: enum i40iw_status_code add_bp_pages(struct i40iw_sc_dev *dev, struct i40iw_hmc_pble_rsrc *pble_rsrc, struct i40iw_add_page_info *info)

    add backing pages for sd

    :param dev:
        hardware control device structure
    :type dev: struct i40iw_sc_dev \*

    :param pble_rsrc:
        pble resource management
    :type pble_rsrc: struct i40iw_hmc_pble_rsrc \*

    :param info:
        page info for sd
    :type info: struct i40iw_add_page_info \*

.. _`add_pble_pool`:

add_pble_pool
=============

.. c:function:: enum i40iw_status_code add_pble_pool(struct i40iw_sc_dev *dev, struct i40iw_hmc_pble_rsrc *pble_rsrc)

    add a sd entry for pble resoure

    :param dev:
        hardware control device structure
    :type dev: struct i40iw_sc_dev \*

    :param pble_rsrc:
        pble resource management
    :type pble_rsrc: struct i40iw_hmc_pble_rsrc \*

.. _`free_lvl2`:

free_lvl2
=========

.. c:function:: void free_lvl2(struct i40iw_hmc_pble_rsrc *pble_rsrc, struct i40iw_pble_alloc *palloc)

    fee level 2 pble

    :param pble_rsrc:
        pble resource management
    :type pble_rsrc: struct i40iw_hmc_pble_rsrc \*

    :param palloc:
        level 2 pble allocation
    :type palloc: struct i40iw_pble_alloc \*

.. _`get_lvl2_pble`:

get_lvl2_pble
=============

.. c:function:: enum i40iw_status_code get_lvl2_pble(struct i40iw_hmc_pble_rsrc *pble_rsrc, struct i40iw_pble_alloc *palloc, struct gen_pool *pool)

    get level 2 pble resource

    :param pble_rsrc:
        pble resource management
    :type pble_rsrc: struct i40iw_hmc_pble_rsrc \*

    :param palloc:
        level 2 pble allocation
    :type palloc: struct i40iw_pble_alloc \*

    :param pool:
        pool pointer
    :type pool: struct gen_pool \*

.. _`get_lvl1_pble`:

get_lvl1_pble
=============

.. c:function:: enum i40iw_status_code get_lvl1_pble(struct i40iw_sc_dev *dev, struct i40iw_hmc_pble_rsrc *pble_rsrc, struct i40iw_pble_alloc *palloc)

    get level 1 pble resource

    :param dev:
        hardware control device structure
    :type dev: struct i40iw_sc_dev \*

    :param pble_rsrc:
        pble resource management
    :type pble_rsrc: struct i40iw_hmc_pble_rsrc \*

    :param palloc:
        level 1 pble allocation
    :type palloc: struct i40iw_pble_alloc \*

.. _`get_lvl1_lvl2_pble`:

get_lvl1_lvl2_pble
==================

.. c:function:: enum i40iw_status_code get_lvl1_lvl2_pble(struct i40iw_sc_dev *dev, struct i40iw_hmc_pble_rsrc *pble_rsrc, struct i40iw_pble_alloc *palloc, struct gen_pool *pool)

    calls get_lvl1 and get_lvl2 pble routine

    :param dev:
        i40iw_sc_dev struct
    :type dev: struct i40iw_sc_dev \*

    :param pble_rsrc:
        pble resources
    :type pble_rsrc: struct i40iw_hmc_pble_rsrc \*

    :param palloc:
        contains all inforamtion regarding pble (idx + pble addr)
    :type palloc: struct i40iw_pble_alloc \*

    :param pool:
        pointer to general purpose special memory pool descriptor
    :type pool: struct gen_pool \*

.. _`i40iw_get_pble`:

i40iw_get_pble
==============

.. c:function:: enum i40iw_status_code i40iw_get_pble(struct i40iw_sc_dev *dev, struct i40iw_hmc_pble_rsrc *pble_rsrc, struct i40iw_pble_alloc *palloc, u32 pble_cnt)

    allocate pbles from the pool

    :param dev:
        i40iw_sc_dev struct
    :type dev: struct i40iw_sc_dev \*

    :param pble_rsrc:
        pble resources
    :type pble_rsrc: struct i40iw_hmc_pble_rsrc \*

    :param palloc:
        contains all inforamtion regarding pble (idx + pble addr)
    :type palloc: struct i40iw_pble_alloc \*

    :param pble_cnt:
        #of pbles requested
    :type pble_cnt: u32

.. _`i40iw_free_pble`:

i40iw_free_pble
===============

.. c:function:: void i40iw_free_pble(struct i40iw_hmc_pble_rsrc *pble_rsrc, struct i40iw_pble_alloc *palloc)

    put pbles back into pool

    :param pble_rsrc:
        pble resources
    :type pble_rsrc: struct i40iw_hmc_pble_rsrc \*

    :param palloc:
        contains all inforamtion regarding pble resource being freed
    :type palloc: struct i40iw_pble_alloc \*

.. This file was automatic generated / don't edit.

