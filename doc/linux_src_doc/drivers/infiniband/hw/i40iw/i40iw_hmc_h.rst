.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_hmc.h

.. _`i40iw_invalidate_pf_hmc_pd`:

I40IW_INVALIDATE_PF_HMC_PD
==========================

.. c:function::  I40IW_INVALIDATE_PF_HMC_PD( hw,  sd_idx,  pd_idx)

    Invalidates the pd cache in the hardware

    :param  hw:
        pointer to our hw struct

    :param  sd_idx:
        segment descriptor index

    :param  pd_idx:
        page descriptor index

.. _`i40iw_invalidate_vf_hmc_pd`:

I40IW_INVALIDATE_VF_HMC_PD
==========================

.. c:function::  I40IW_INVALIDATE_VF_HMC_PD( hw,  sd_idx,  pd_idx,  hmc_fn_id)

    Invalidates the pd cache in the hardware

    :param  hw:
        pointer to our hw struct

    :param  sd_idx:
        segment descriptor index

    :param  pd_idx:
        page descriptor index

    :param  hmc_fn_id:
        VF's function id

.. This file was automatic generated / don't edit.

