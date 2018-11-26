.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_lan_hmc.c

.. _`i40e_align_l2obj_base`:

i40e_align_l2obj_base
=====================

.. c:function:: u64 i40e_align_l2obj_base(u64 offset)

    aligns base object pointer to 512 bytes

    :param offset:
        base address offset needing alignment
    :type offset: u64

.. _`i40e_align_l2obj_base.description`:

Description
-----------

Aligns the layer 2 function private memory so it's 512-byte aligned.

.. _`i40e_calculate_l2fpm_size`:

i40e_calculate_l2fpm_size
=========================

.. c:function:: u64 i40e_calculate_l2fpm_size(u32 txq_num, u32 rxq_num, u32 fcoe_cntx_num, u32 fcoe_filt_num)

    calculates layer 2 FPM memory size

    :param txq_num:
        number of Tx queues needing backing context
    :type txq_num: u32

    :param rxq_num:
        number of Rx queues needing backing context
    :type rxq_num: u32

    :param fcoe_cntx_num:
        amount of FCoE statefull contexts needing backing context
    :type fcoe_cntx_num: u32

    :param fcoe_filt_num:
        number of FCoE filters needing backing context
    :type fcoe_filt_num: u32

.. _`i40e_calculate_l2fpm_size.description`:

Description
-----------

Calculates the maximum amount of memory for the function required, based
on the number of resources it must provide context for.

.. _`i40e_init_lan_hmc`:

i40e_init_lan_hmc
=================

.. c:function:: i40e_status i40e_init_lan_hmc(struct i40e_hw *hw, u32 txq_num, u32 rxq_num, u32 fcoe_cntx_num, u32 fcoe_filt_num)

    initialize i40e_hmc_info struct

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param txq_num:
        number of Tx queues needing backing context
    :type txq_num: u32

    :param rxq_num:
        number of Rx queues needing backing context
    :type rxq_num: u32

    :param fcoe_cntx_num:
        amount of FCoE statefull contexts needing backing context
    :type fcoe_cntx_num: u32

    :param fcoe_filt_num:
        number of FCoE filters needing backing context
    :type fcoe_filt_num: u32

.. _`i40e_init_lan_hmc.description`:

Description
-----------

This function will be called once per physical function initialization.
It will fill out the i40e_hmc_obj_info structure for LAN objects based on
the driver's provided input, as well as information from the HMC itself
loaded from NVRAM.

.. _`i40e_init_lan_hmc.assumptions`:

Assumptions
-----------

- HMC Resource Profile has been selected before calling this function.

.. _`i40e_remove_pd_page`:

i40e_remove_pd_page
===================

.. c:function:: i40e_status i40e_remove_pd_page(struct i40e_hw *hw, struct i40e_hmc_info *hmc_info, u32 idx)

    Remove a page from the page descriptor table

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param hmc_info:
        pointer to the HMC configuration information structure
    :type hmc_info: struct i40e_hmc_info \*

    :param idx:
        segment descriptor index to find the relevant page descriptor
    :type idx: u32

.. _`i40e_remove_pd_page.this-function`:

This function
-------------

1. Marks the entry in pd table (for paged address mode) invalid
2. write to register PMPDINV to invalidate the backing page in FV cache
3. Decrement the ref count for  pd_entry

.. _`i40e_remove_pd_page.assumptions`:

assumptions
-----------

1. caller can deallocate the memory used by pd after this function
returns.

.. _`i40e_remove_sd_bp`:

i40e_remove_sd_bp
=================

.. c:function:: i40e_status i40e_remove_sd_bp(struct i40e_hw *hw, struct i40e_hmc_info *hmc_info, u32 idx)

    remove a backing page from a segment descriptor

    :param hw:
        pointer to our HW structure
    :type hw: struct i40e_hw \*

    :param hmc_info:
        pointer to the HMC configuration information structure
    :type hmc_info: struct i40e_hmc_info \*

    :param idx:
        the page index
    :type idx: u32

.. _`i40e_remove_sd_bp.this-function`:

This function
-------------

1. Marks the entry in sd table (for direct address mode) invalid
2. write to register PMSDCMD, PMSDDATALOW(PMSDDATALOW.PMSDVALID set
to 0) and PMSDDATAHIGH to invalidate the sd page
3. Decrement the ref count for the sd_entry

.. _`i40e_remove_sd_bp.assumptions`:

assumptions
-----------

1. caller can deallocate the memory used by backing storage after this
function returns.

.. _`i40e_create_lan_hmc_object`:

i40e_create_lan_hmc_object
==========================

.. c:function:: i40e_status i40e_create_lan_hmc_object(struct i40e_hw *hw, struct i40e_hmc_lan_create_obj_info *info)

    allocate backing store for hmc objects

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param info:
        pointer to i40e_hmc_create_obj_info struct
    :type info: struct i40e_hmc_lan_create_obj_info \*

.. _`i40e_create_lan_hmc_object.description`:

Description
-----------

This will allocate memory for PDs and backing pages and populate
the sd and pd entries.

.. _`i40e_configure_lan_hmc`:

i40e_configure_lan_hmc
======================

.. c:function:: i40e_status i40e_configure_lan_hmc(struct i40e_hw *hw, enum i40e_hmc_model model)

    prepare the HMC backing store

    :param hw:
        pointer to the hw structure
    :type hw: struct i40e_hw \*

    :param model:
        the model for the layout of the SD/PD tables
    :type model: enum i40e_hmc_model

.. _`i40e_configure_lan_hmc.description`:

Description
-----------

- This function will be called once per physical function initialization.
- This function will be called after \ :c:func:`i40e_init_lan_hmc`\  and before
any LAN/FCoE HMC objects can be created.

.. _`i40e_delete_lan_hmc_object`:

i40e_delete_lan_hmc_object
==========================

.. c:function:: i40e_status i40e_delete_lan_hmc_object(struct i40e_hw *hw, struct i40e_hmc_lan_delete_obj_info *info)

    remove hmc objects

    :param hw:
        pointer to the HW structure
    :type hw: struct i40e_hw \*

    :param info:
        pointer to i40e_hmc_delete_obj_info struct
    :type info: struct i40e_hmc_lan_delete_obj_info \*

.. _`i40e_delete_lan_hmc_object.description`:

Description
-----------

This will de-populate the SDs and PDs.  It frees
the memory for PDS and backing storage.  After this function is returned,
caller should deallocate memory allocated previously for
book-keeping information about PDs and backing storage.

.. _`i40e_shutdown_lan_hmc`:

i40e_shutdown_lan_hmc
=====================

.. c:function:: i40e_status i40e_shutdown_lan_hmc(struct i40e_hw *hw)

    Remove HMC backing store, free allocated memory

    :param hw:
        pointer to the hw structure
    :type hw: struct i40e_hw \*

.. _`i40e_shutdown_lan_hmc.description`:

Description
-----------

This must be called by drivers as they are shutting down and being
removed from the OS.

.. _`i40e_write_byte`:

i40e_write_byte
===============

.. c:function:: void i40e_write_byte(u8 *hmc_bits, struct i40e_context_ele *ce_info, u8 *src)

    replace HMC context byte

    :param hmc_bits:
        pointer to the HMC memory
    :type hmc_bits: u8 \*

    :param ce_info:
        a description of the struct to be read from
    :type ce_info: struct i40e_context_ele \*

    :param src:
        the struct to be read from
    :type src: u8 \*

.. _`i40e_write_word`:

i40e_write_word
===============

.. c:function:: void i40e_write_word(u8 *hmc_bits, struct i40e_context_ele *ce_info, u8 *src)

    replace HMC context word

    :param hmc_bits:
        pointer to the HMC memory
    :type hmc_bits: u8 \*

    :param ce_info:
        a description of the struct to be read from
    :type ce_info: struct i40e_context_ele \*

    :param src:
        the struct to be read from
    :type src: u8 \*

.. _`i40e_write_dword`:

i40e_write_dword
================

.. c:function:: void i40e_write_dword(u8 *hmc_bits, struct i40e_context_ele *ce_info, u8 *src)

    replace HMC context dword

    :param hmc_bits:
        pointer to the HMC memory
    :type hmc_bits: u8 \*

    :param ce_info:
        a description of the struct to be read from
    :type ce_info: struct i40e_context_ele \*

    :param src:
        the struct to be read from
    :type src: u8 \*

.. _`i40e_write_qword`:

i40e_write_qword
================

.. c:function:: void i40e_write_qword(u8 *hmc_bits, struct i40e_context_ele *ce_info, u8 *src)

    replace HMC context qword

    :param hmc_bits:
        pointer to the HMC memory
    :type hmc_bits: u8 \*

    :param ce_info:
        a description of the struct to be read from
    :type ce_info: struct i40e_context_ele \*

    :param src:
        the struct to be read from
    :type src: u8 \*

.. _`i40e_clear_hmc_context`:

i40e_clear_hmc_context
======================

.. c:function:: i40e_status i40e_clear_hmc_context(struct i40e_hw *hw, u8 *context_bytes, enum i40e_hmc_lan_rsrc_type hmc_type)

    zero out the HMC context bits

    :param hw:
        the hardware struct
    :type hw: struct i40e_hw \*

    :param context_bytes:
        pointer to the context bit array (DMA memory)
    :type context_bytes: u8 \*

    :param hmc_type:
        the type of HMC resource
    :type hmc_type: enum i40e_hmc_lan_rsrc_type

.. _`i40e_set_hmc_context`:

i40e_set_hmc_context
====================

.. c:function:: i40e_status i40e_set_hmc_context(u8 *context_bytes, struct i40e_context_ele *ce_info, u8 *dest)

    replace HMC context bits

    :param context_bytes:
        pointer to the context bit array
    :type context_bytes: u8 \*

    :param ce_info:
        a description of the struct to be filled
    :type ce_info: struct i40e_context_ele \*

    :param dest:
        the struct to be filled
    :type dest: u8 \*

.. _`i40e_hmc_get_object_va`:

i40e_hmc_get_object_va
======================

.. c:function:: i40e_status i40e_hmc_get_object_va(struct i40e_hmc_info *hmc_info, u8 **object_base, enum i40e_hmc_lan_rsrc_type rsrc_type, u32 obj_idx)

    retrieves an object's virtual address

    :param hmc_info:
        pointer to i40e_hmc_info struct
    :type hmc_info: struct i40e_hmc_info \*

    :param object_base:
        pointer to u64 to get the va
    :type object_base: u8 \*\*

    :param rsrc_type:
        the hmc resource type
    :type rsrc_type: enum i40e_hmc_lan_rsrc_type

    :param obj_idx:
        hmc object index
    :type obj_idx: u32

.. _`i40e_hmc_get_object_va.description`:

Description
-----------

This function retrieves the object's virtual address from the object
base pointer.  This function is used for LAN Queue contexts.

.. _`i40e_clear_lan_tx_queue_context`:

i40e_clear_lan_tx_queue_context
===============================

.. c:function:: i40e_status i40e_clear_lan_tx_queue_context(struct i40e_hw *hw, u16 queue)

    clear the HMC context for the queue

    :param hw:
        the hardware struct
    :type hw: struct i40e_hw \*

    :param queue:
        the queue we care about
    :type queue: u16

.. _`i40e_set_lan_tx_queue_context`:

i40e_set_lan_tx_queue_context
=============================

.. c:function:: i40e_status i40e_set_lan_tx_queue_context(struct i40e_hw *hw, u16 queue, struct i40e_hmc_obj_txq *s)

    set the HMC context for the queue

    :param hw:
        the hardware struct
    :type hw: struct i40e_hw \*

    :param queue:
        the queue we care about
    :type queue: u16

    :param s:
        the struct to be filled
    :type s: struct i40e_hmc_obj_txq \*

.. _`i40e_clear_lan_rx_queue_context`:

i40e_clear_lan_rx_queue_context
===============================

.. c:function:: i40e_status i40e_clear_lan_rx_queue_context(struct i40e_hw *hw, u16 queue)

    clear the HMC context for the queue

    :param hw:
        the hardware struct
    :type hw: struct i40e_hw \*

    :param queue:
        the queue we care about
    :type queue: u16

.. _`i40e_set_lan_rx_queue_context`:

i40e_set_lan_rx_queue_context
=============================

.. c:function:: i40e_status i40e_set_lan_rx_queue_context(struct i40e_hw *hw, u16 queue, struct i40e_hmc_obj_rxq *s)

    set the HMC context for the queue

    :param hw:
        the hardware struct
    :type hw: struct i40e_hw \*

    :param queue:
        the queue we care about
    :type queue: u16

    :param s:
        the struct to be filled
    :type s: struct i40e_hmc_obj_rxq \*

.. This file was automatic generated / don't edit.

