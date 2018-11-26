.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_hmc.c

.. _`i40iw_find_sd_index_limit`:

i40iw_find_sd_index_limit
=========================

.. c:function:: void i40iw_find_sd_index_limit(struct i40iw_hmc_info *hmc_info, u32 type, u32 idx, u32 cnt, u32 *sd_idx, u32 *sd_limit)

    finds segment descriptor index limit

    :param hmc_info:
        pointer to the HMC configuration information structure
    :type hmc_info: struct i40iw_hmc_info \*

    :param type:
        type of HMC resources we're searching
    :type type: u32

    :param idx:
        *undescribed*
    :type idx: u32

    :param cnt:
        number of objects we're trying to create
    :type cnt: u32

    :param sd_idx:
        pointer to return index of the segment descriptor in question
    :type sd_idx: u32 \*

    :param sd_limit:
        pointer to return the maximum number of segment descriptors
    :type sd_limit: u32 \*

.. _`i40iw_find_sd_index_limit.description`:

Description
-----------

This function calculates the segment descriptor index and index limit
for the resource defined by i40iw_hmc_rsrc_type.

.. _`i40iw_find_pd_index_limit`:

i40iw_find_pd_index_limit
=========================

.. c:function:: void i40iw_find_pd_index_limit(struct i40iw_hmc_info *hmc_info, u32 type, u32 idx, u32 cnt, u32 *pd_idx, u32 *pd_limit)

    finds page descriptor index limit

    :param hmc_info:
        pointer to the HMC configuration information struct
    :type hmc_info: struct i40iw_hmc_info \*

    :param type:
        HMC resource type we're examining
    :type type: u32

    :param idx:
        starting index for the object
    :type idx: u32

    :param cnt:
        number of objects we're trying to create
    :type cnt: u32

    :param pd_idx:
        *undescribed*
    :type pd_idx: u32 \*

    :param pd_limit:
        pointer to return page descriptor index limit
    :type pd_limit: u32 \*

.. _`i40iw_find_pd_index_limit.description`:

Description
-----------

Calculates the page descriptor index and index limit for the resource
defined by i40iw_hmc_rsrc_type.

.. _`i40iw_set_sd_entry`:

i40iw_set_sd_entry
==================

.. c:function:: void i40iw_set_sd_entry(u64 pa, u32 idx, enum i40iw_sd_entry_type type, struct update_sd_entry *entry)

    setup entry for sd programming

    :param pa:
        physical addr
    :type pa: u64

    :param idx:
        sd index
    :type idx: u32

    :param type:
        paged or direct sd
    :type type: enum i40iw_sd_entry_type

    :param entry:
        sd entry ptr
    :type entry: struct update_sd_entry \*

.. _`i40iw_clr_sd_entry`:

i40iw_clr_sd_entry
==================

.. c:function:: void i40iw_clr_sd_entry(u32 idx, enum i40iw_sd_entry_type type, struct update_sd_entry *entry)

    setup entry for sd clear

    :param idx:
        sd index
    :type idx: u32

    :param type:
        paged or direct sd
    :type type: enum i40iw_sd_entry_type

    :param entry:
        sd entry ptr
    :type entry: struct update_sd_entry \*

.. _`i40iw_hmc_sd_one`:

i40iw_hmc_sd_one
================

.. c:function:: enum i40iw_status_code i40iw_hmc_sd_one(struct i40iw_sc_dev *dev, u8 hmc_fn_id, u64 pa, u32 sd_idx, enum i40iw_sd_entry_type type, bool setsd)

    setup 1 sd entry for cqp

    :param dev:
        pointer to the device structure
    :type dev: struct i40iw_sc_dev \*

    :param hmc_fn_id:
        hmc's function id
    :type hmc_fn_id: u8

    :param pa:
        physical addr
    :type pa: u64

    :param sd_idx:
        sd index
    :type sd_idx: u32

    :param type:
        paged or direct sd
    :type type: enum i40iw_sd_entry_type

    :param setsd:
        flag to set or clear sd
    :type setsd: bool

.. _`i40iw_hmc_sd_grp`:

i40iw_hmc_sd_grp
================

.. c:function:: enum i40iw_status_code i40iw_hmc_sd_grp(struct i40iw_sc_dev *dev, struct i40iw_hmc_info *hmc_info, u32 sd_index, u32 sd_cnt, bool setsd)

    setup group od sd entries for cqp

    :param dev:
        pointer to the device structure
    :type dev: struct i40iw_sc_dev \*

    :param hmc_info:
        pointer to the HMC configuration information struct
    :type hmc_info: struct i40iw_hmc_info \*

    :param sd_index:
        sd index
    :type sd_index: u32

    :param sd_cnt:
        number of sd entries
    :type sd_cnt: u32

    :param setsd:
        flag to set or clear sd
    :type setsd: bool

.. _`i40iw_vfdev_from_fpm`:

i40iw_vfdev_from_fpm
====================

.. c:function:: struct i40iw_vfdev *i40iw_vfdev_from_fpm(struct i40iw_sc_dev *dev, u8 hmc_fn_id)

    return vf dev ptr for hmc function id

    :param dev:
        pointer to the device structure
    :type dev: struct i40iw_sc_dev \*

    :param hmc_fn_id:
        hmc's function id
    :type hmc_fn_id: u8

.. _`i40iw_vf_hmcinfo_from_fpm`:

i40iw_vf_hmcinfo_from_fpm
=========================

.. c:function:: struct i40iw_hmc_info *i40iw_vf_hmcinfo_from_fpm(struct i40iw_sc_dev *dev, u8 hmc_fn_id)

    get ptr to hmc for func_id

    :param dev:
        pointer to the device structure
    :type dev: struct i40iw_sc_dev \*

    :param hmc_fn_id:
        hmc's function id
    :type hmc_fn_id: u8

.. _`i40iw_hmc_finish_add_sd_reg`:

i40iw_hmc_finish_add_sd_reg
===========================

.. c:function:: enum i40iw_status_code i40iw_hmc_finish_add_sd_reg(struct i40iw_sc_dev *dev, struct i40iw_hmc_create_obj_info *info)

    program sd entries for objects

    :param dev:
        pointer to the device structure
    :type dev: struct i40iw_sc_dev \*

    :param info:
        create obj info
    :type info: struct i40iw_hmc_create_obj_info \*

.. _`i40iw_sc_create_hmc_obj`:

i40iw_sc_create_hmc_obj
=======================

.. c:function:: enum i40iw_status_code i40iw_sc_create_hmc_obj(struct i40iw_sc_dev *dev, struct i40iw_hmc_create_obj_info *info)

    allocate backing store for hmc objects

    :param dev:
        pointer to the device structure
    :type dev: struct i40iw_sc_dev \*

    :param info:
        pointer to i40iw_hmc_iw_create_obj_info struct
    :type info: struct i40iw_hmc_create_obj_info \*

.. _`i40iw_sc_create_hmc_obj.description`:

Description
-----------

This will allocate memory for PDs and backing pages and populate
the sd and pd entries.

.. _`i40iw_finish_del_sd_reg`:

i40iw_finish_del_sd_reg
=======================

.. c:function:: enum i40iw_status_code i40iw_finish_del_sd_reg(struct i40iw_sc_dev *dev, struct i40iw_hmc_del_obj_info *info, bool reset)

    delete sd entries for objects

    :param dev:
        pointer to the device structure
    :type dev: struct i40iw_sc_dev \*

    :param info:
        dele obj info
    :type info: struct i40iw_hmc_del_obj_info \*

    :param reset:
        true if called before reset
    :type reset: bool

.. _`i40iw_sc_del_hmc_obj`:

i40iw_sc_del_hmc_obj
====================

.. c:function:: enum i40iw_status_code i40iw_sc_del_hmc_obj(struct i40iw_sc_dev *dev, struct i40iw_hmc_del_obj_info *info, bool reset)

    remove pe hmc objects

    :param dev:
        pointer to the device structure
    :type dev: struct i40iw_sc_dev \*

    :param info:
        pointer to i40iw_hmc_del_obj_info struct
    :type info: struct i40iw_hmc_del_obj_info \*

    :param reset:
        true if called before reset
    :type reset: bool

.. _`i40iw_sc_del_hmc_obj.description`:

Description
-----------

This will de-populate the SDs and PDs.  It frees
the memory for PDS and backing storage.  After this function is returned,
caller should deallocate memory allocated previously for
book-keeping information about PDs and backing storage.

.. _`i40iw_add_sd_table_entry`:

i40iw_add_sd_table_entry
========================

.. c:function:: enum i40iw_status_code i40iw_add_sd_table_entry(struct i40iw_hw *hw, struct i40iw_hmc_info *hmc_info, u32 sd_index, enum i40iw_sd_entry_type type, u64 direct_mode_sz)

    Adds a segment descriptor to the table

    :param hw:
        pointer to our hw struct
    :type hw: struct i40iw_hw \*

    :param hmc_info:
        pointer to the HMC configuration information struct
    :type hmc_info: struct i40iw_hmc_info \*

    :param sd_index:
        segment descriptor index to manipulate
    :type sd_index: u32

    :param type:
        what type of segment descriptor we're manipulating
    :type type: enum i40iw_sd_entry_type

    :param direct_mode_sz:
        size to alloc in direct mode
    :type direct_mode_sz: u64

.. _`i40iw_add_pd_table_entry`:

i40iw_add_pd_table_entry
========================

.. c:function:: enum i40iw_status_code i40iw_add_pd_table_entry(struct i40iw_hw *hw, struct i40iw_hmc_info *hmc_info, u32 pd_index, struct i40iw_dma_mem *rsrc_pg)

    Adds page descriptor to the specified table

    :param hw:
        pointer to our HW structure
    :type hw: struct i40iw_hw \*

    :param hmc_info:
        pointer to the HMC configuration information structure
    :type hmc_info: struct i40iw_hmc_info \*

    :param pd_index:
        which page descriptor index to manipulate
    :type pd_index: u32

    :param rsrc_pg:
        if not NULL, use preallocated page instead of allocating new one.
    :type rsrc_pg: struct i40iw_dma_mem \*

.. _`i40iw_add_pd_table_entry.this-function`:

This function
-------------

1. Initializes the pd entry
2. Adds pd_entry in the pd_table
3. Mark the entry valid in i40iw_hmc_pd_entry structure
4. Initializes the pd_entry's ref count to 1

.. _`i40iw_add_pd_table_entry.assumptions`:

assumptions
-----------

1. The memory for pd should be pinned down, physically contiguous and
aligned on 4K boundary and zeroed memory.
2. It should be 4K in size.

.. _`i40iw_remove_pd_bp`:

i40iw_remove_pd_bp
==================

.. c:function:: enum i40iw_status_code i40iw_remove_pd_bp(struct i40iw_hw *hw, struct i40iw_hmc_info *hmc_info, u32 idx, bool is_pf)

    remove a backing page from a page descriptor

    :param hw:
        pointer to our HW structure
    :type hw: struct i40iw_hw \*

    :param hmc_info:
        pointer to the HMC configuration information structure
    :type hmc_info: struct i40iw_hmc_info \*

    :param idx:
        the page index
    :type idx: u32

    :param is_pf:
        distinguishes a VF from a PF
    :type is_pf: bool

.. _`i40iw_remove_pd_bp.this-function`:

This function
-------------

1. Marks the entry in pd table (for paged address mode) or in sd table
(for direct address mode) invalid.
2. Write to register PMPDINV to invalidate the backing page in FV cache
3. Decrement the ref count for the pd \_entry

.. _`i40iw_remove_pd_bp.assumptions`:

assumptions
-----------

1. Caller can deallocate the memory used by backing storage after this
function returns.

.. _`i40iw_prep_remove_sd_bp`:

i40iw_prep_remove_sd_bp
=======================

.. c:function:: enum i40iw_status_code i40iw_prep_remove_sd_bp(struct i40iw_hmc_info *hmc_info, u32 idx)

    Prepares to remove a backing page from a sd entry

    :param hmc_info:
        pointer to the HMC configuration information structure
    :type hmc_info: struct i40iw_hmc_info \*

    :param idx:
        the page index
    :type idx: u32

.. _`i40iw_prep_remove_pd_page`:

i40iw_prep_remove_pd_page
=========================

.. c:function:: enum i40iw_status_code i40iw_prep_remove_pd_page(struct i40iw_hmc_info *hmc_info, u32 idx)

    Prepares to remove a PD page from sd entry.

    :param hmc_info:
        pointer to the HMC configuration information structure
    :type hmc_info: struct i40iw_hmc_info \*

    :param idx:
        segment descriptor index to find the relevant page descriptor
    :type idx: u32

.. _`i40iw_pf_init_vfhmc`:

i40iw_pf_init_vfhmc
===================

.. c:function:: enum i40iw_status_code i40iw_pf_init_vfhmc(struct i40iw_sc_dev *dev, u8 vf_hmc_fn_id, u32 *vf_cnt_array)

    :param dev:
        pointer to i40iw_dev struct
    :type dev: struct i40iw_sc_dev \*

    :param vf_hmc_fn_id:
        hmc function id ofr vf driver
    :type vf_hmc_fn_id: u8

    :param vf_cnt_array:
        array of cnt values of iwarp hmc objects
    :type vf_cnt_array: u32 \*

.. _`i40iw_pf_init_vfhmc.description`:

Description
-----------

Called by pf driver to initialize hmc_info for vf driver instance.

.. This file was automatic generated / don't edit.

