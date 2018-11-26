.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_hmc.h

.. _`i40e_set_pf_sd_entry`:

I40E_SET_PF_SD_ENTRY
====================

.. c:function::  I40E_SET_PF_SD_ENTRY( hw,  pa,  sd_index,  type)

    marks the sd entry as valid in the hardware

    :param hw:
        pointer to our hw struct
    :type hw: 

    :param pa:
        pointer to physical address
    :type pa: 

    :param sd_index:
        segment descriptor index
    :type sd_index: 

    :param type:
        if sd entry is direct or paged
    :type type: 

.. _`i40e_clear_pf_sd_entry`:

I40E_CLEAR_PF_SD_ENTRY
======================

.. c:function::  I40E_CLEAR_PF_SD_ENTRY( hw,  sd_index,  type)

    marks the sd entry as invalid in the hardware

    :param hw:
        pointer to our hw struct
    :type hw: 

    :param sd_index:
        segment descriptor index
    :type sd_index: 

    :param type:
        if sd entry is direct or paged
    :type type: 

.. _`i40e_invalidate_pf_hmc_pd`:

I40E_INVALIDATE_PF_HMC_PD
=========================

.. c:function::  I40E_INVALIDATE_PF_HMC_PD( hw,  sd_idx,  pd_idx)

    Invalidates the pd cache in the hardware

    :param hw:
        pointer to our hw struct
    :type hw: 

    :param sd_idx:
        segment descriptor index
    :type sd_idx: 

    :param pd_idx:
        page descriptor index
    :type pd_idx: 

.. _`i40e_find_sd_index_limit`:

I40E_FIND_SD_INDEX_LIMIT
========================

.. c:function::  I40E_FIND_SD_INDEX_LIMIT( hmc_info,  type,  index,  cnt,  sd_idx,  sd_limit)

    finds segment descriptor index limit

    :param hmc_info:
        pointer to the HMC configuration information structure
    :type hmc_info: 

    :param type:
        type of HMC resources we're searching
    :type type: 

    :param index:
        starting index for the object
    :type index: 

    :param cnt:
        number of objects we're trying to create
    :type cnt: 

    :param sd_idx:
        pointer to return index of the segment descriptor in question
    :type sd_idx: 

    :param sd_limit:
        pointer to return the maximum number of segment descriptors
    :type sd_limit: 

.. _`i40e_find_sd_index_limit.description`:

Description
-----------

This function calculates the segment descriptor index and index limit
for the resource defined by i40e_hmc_rsrc_type.

.. _`i40e_find_pd_index_limit`:

I40E_FIND_PD_INDEX_LIMIT
========================

.. c:function::  I40E_FIND_PD_INDEX_LIMIT( hmc_info,  type,  idx,  cnt,  pd_index,  pd_limit)

    finds page descriptor index limit

    :param hmc_info:
        pointer to the HMC configuration information struct
    :type hmc_info: 

    :param type:
        HMC resource type we're examining
    :type type: 

    :param idx:
        starting index for the object
    :type idx: 

    :param cnt:
        number of objects we're trying to create
    :type cnt: 

    :param pd_index:
        pointer to return page descriptor index
    :type pd_index: 

    :param pd_limit:
        pointer to return page descriptor index limit
    :type pd_limit: 

.. _`i40e_find_pd_index_limit.description`:

Description
-----------

Calculates the page descriptor index and index limit for the resource
defined by i40e_hmc_rsrc_type.

.. This file was automatic generated / don't edit.

