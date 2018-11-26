.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_hmc.c

.. _`i40e_add_sd_table_entry`:

i40e_add_sd_table_entry
=======================

.. c:function:: i40e_status i40e_add_sd_table_entry(struct i40e_hw *hw, struct i40e_hmc_info *hmc_info, u32 sd_index, enum i40e_sd_entry_type type, u64 direct_mode_sz)

    Adds a segment descriptor to the table

    :param hw:
        pointer to our hw struct
    :type hw: struct i40e_hw \*

    :param hmc_info:
        pointer to the HMC configuration information struct
    :type hmc_info: struct i40e_hmc_info \*

    :param sd_index:
        segment descriptor index to manipulate
    :type sd_index: u32

    :param type:
        what type of segment descriptor we're manipulating
    :type type: enum i40e_sd_entry_type

    :param direct_mode_sz:
        size to alloc in direct mode
    :type direct_mode_sz: u64

.. _`i40e_add_pd_table_entry`:

i40e_add_pd_table_entry
=======================

.. c:function:: i40e_status i40e_add_pd_table_entry(struct i40e_hw *hw, struct i40e_hmc_info *hmc_info, u32 pd_index, struct i40e_dma_mem *rsrc_pg)

    Adds page descriptor to the specified table

    :param hw:
        pointer to our HW structure
    :type hw: struct i40e_hw \*

    :param hmc_info:
        pointer to the HMC configuration information structure
    :type hmc_info: struct i40e_hmc_info \*

    :param pd_index:
        which page descriptor index to manipulate
    :type pd_index: u32

    :param rsrc_pg:
        if not NULL, use preallocated page instead of allocating new one.
    :type rsrc_pg: struct i40e_dma_mem \*

.. _`i40e_add_pd_table_entry.this-function`:

This function
-------------

1. Initializes the pd entry
2. Adds pd_entry in the pd_table
3. Mark the entry valid in i40e_hmc_pd_entry structure
4. Initializes the pd_entry's ref count to 1

.. _`i40e_add_pd_table_entry.assumptions`:

assumptions
-----------

1. The memory for pd should be pinned down, physically contiguous and
aligned on 4K boundary and zeroed memory.
2. It should be 4K in size.

.. _`i40e_remove_pd_bp`:

i40e_remove_pd_bp
=================

.. c:function:: i40e_status i40e_remove_pd_bp(struct i40e_hw *hw, struct i40e_hmc_info *hmc_info, u32 idx)

    remove a backing page from a page descriptor

    :param hw:
        pointer to our HW structure
    :type hw: struct i40e_hw \*

    :param hmc_info:
        pointer to the HMC configuration information structure
    :type hmc_info: struct i40e_hmc_info \*

    :param idx:
        the page index
    :type idx: u32

.. _`i40e_remove_pd_bp.this-function`:

This function
-------------

1. Marks the entry in pd tabe (for paged address mode) or in sd table
(for direct address mode) invalid.
2. Write to register PMPDINV to invalidate the backing page in FV cache
3. Decrement the ref count for the pd \_entry

.. _`i40e_remove_pd_bp.assumptions`:

assumptions
-----------

1. Caller can deallocate the memory used by backing storage after this
function returns.

.. _`i40e_prep_remove_sd_bp`:

i40e_prep_remove_sd_bp
======================

.. c:function:: i40e_status i40e_prep_remove_sd_bp(struct i40e_hmc_info *hmc_info, u32 idx)

    Prepares to remove a backing page from a sd entry

    :param hmc_info:
        pointer to the HMC configuration information structure
    :type hmc_info: struct i40e_hmc_info \*

    :param idx:
        the page index
    :type idx: u32

.. _`i40e_remove_sd_bp_new`:

i40e_remove_sd_bp_new
=====================

.. c:function:: i40e_status i40e_remove_sd_bp_new(struct i40e_hw *hw, struct i40e_hmc_info *hmc_info, u32 idx, bool is_pf)

    Removes a backing page from a segment descriptor

    :param hw:
        pointer to our hw struct
    :type hw: struct i40e_hw \*

    :param hmc_info:
        pointer to the HMC configuration information structure
    :type hmc_info: struct i40e_hmc_info \*

    :param idx:
        the page index
    :type idx: u32

    :param is_pf:
        used to distinguish between VF and PF
    :type is_pf: bool

.. _`i40e_prep_remove_pd_page`:

i40e_prep_remove_pd_page
========================

.. c:function:: i40e_status i40e_prep_remove_pd_page(struct i40e_hmc_info *hmc_info, u32 idx)

    Prepares to remove a PD page from sd entry.

    :param hmc_info:
        pointer to the HMC configuration information structure
    :type hmc_info: struct i40e_hmc_info \*

    :param idx:
        segment descriptor index to find the relevant page descriptor
    :type idx: u32

.. _`i40e_remove_pd_page_new`:

i40e_remove_pd_page_new
=======================

.. c:function:: i40e_status i40e_remove_pd_page_new(struct i40e_hw *hw, struct i40e_hmc_info *hmc_info, u32 idx, bool is_pf)

    Removes a PD page from sd entry.

    :param hw:
        pointer to our hw struct
    :type hw: struct i40e_hw \*

    :param hmc_info:
        pointer to the HMC configuration information structure
    :type hmc_info: struct i40e_hmc_info \*

    :param idx:
        segment descriptor index to find the relevant page descriptor
    :type idx: u32

    :param is_pf:
        used to distinguish between VF and PF
    :type is_pf: bool

.. This file was automatic generated / don't edit.

