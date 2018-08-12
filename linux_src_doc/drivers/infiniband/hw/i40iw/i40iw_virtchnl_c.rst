.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_virtchnl.c

.. _`vchnl_vf_send_get_ver_req`:

vchnl_vf_send_get_ver_req
=========================

.. c:function:: enum i40iw_status_code vchnl_vf_send_get_ver_req(struct i40iw_sc_dev *dev, struct i40iw_virtchnl_req *vchnl_req)

    Request Channel version

    :param struct i40iw_sc_dev \*dev:
        IWARP device pointer

    :param struct i40iw_virtchnl_req \*vchnl_req:
        Virtual channel message request pointer

.. _`vchnl_vf_send_get_hmc_fcn_req`:

vchnl_vf_send_get_hmc_fcn_req
=============================

.. c:function:: enum i40iw_status_code vchnl_vf_send_get_hmc_fcn_req(struct i40iw_sc_dev *dev, struct i40iw_virtchnl_req *vchnl_req)

    Request HMC Function from VF

    :param struct i40iw_sc_dev \*dev:
        IWARP device pointer

    :param struct i40iw_virtchnl_req \*vchnl_req:
        Virtual channel message request pointer

.. _`vchnl_vf_send_get_pe_stats_req`:

vchnl_vf_send_get_pe_stats_req
==============================

.. c:function:: enum i40iw_status_code vchnl_vf_send_get_pe_stats_req(struct i40iw_sc_dev *dev, struct i40iw_virtchnl_req *vchnl_req)

    Request PE stats from VF

    :param struct i40iw_sc_dev \*dev:
        IWARP device pointer

    :param struct i40iw_virtchnl_req \*vchnl_req:
        Virtual channel message request pointer

.. _`vchnl_vf_send_add_hmc_objs_req`:

vchnl_vf_send_add_hmc_objs_req
==============================

.. c:function:: enum i40iw_status_code vchnl_vf_send_add_hmc_objs_req(struct i40iw_sc_dev *dev, struct i40iw_virtchnl_req *vchnl_req, enum i40iw_hmc_rsrc_type rsrc_type, u32 start_index, u32 rsrc_count)

    Add HMC objects

    :param struct i40iw_sc_dev \*dev:
        IWARP device pointer

    :param struct i40iw_virtchnl_req \*vchnl_req:
        Virtual channel message request pointer

    :param enum i40iw_hmc_rsrc_type rsrc_type:
        *undescribed*

    :param u32 start_index:
        *undescribed*

    :param u32 rsrc_count:
        *undescribed*

.. _`vchnl_vf_send_del_hmc_objs_req`:

vchnl_vf_send_del_hmc_objs_req
==============================

.. c:function:: enum i40iw_status_code vchnl_vf_send_del_hmc_objs_req(struct i40iw_sc_dev *dev, struct i40iw_virtchnl_req *vchnl_req, enum i40iw_hmc_rsrc_type rsrc_type, u32 start_index, u32 rsrc_count)

    del HMC objects

    :param struct i40iw_sc_dev \*dev:
        IWARP device pointer

    :param struct i40iw_virtchnl_req \*vchnl_req:
        Virtual channel message request pointer
        \ ````\  rsrc_type - resource type to delete
        \ ````\  start_index - starting index for resource
        \ ````\  rsrc_count - number of resource type to delete

    :param enum i40iw_hmc_rsrc_type rsrc_type:
        *undescribed*

    :param u32 start_index:
        *undescribed*

    :param u32 rsrc_count:
        *undescribed*

.. _`vchnl_pf_send_get_ver_resp`:

vchnl_pf_send_get_ver_resp
==========================

.. c:function:: void vchnl_pf_send_get_ver_resp(struct i40iw_sc_dev *dev, u32 vf_id, struct i40iw_virtchnl_op_buf *vchnl_msg)

    Send channel version to VF

    :param struct i40iw_sc_dev \*dev:
        IWARP device pointer

    :param u32 vf_id:
        Virtual function ID associated with the message

    :param struct i40iw_virtchnl_op_buf \*vchnl_msg:
        Virtual channel message buffer pointer

.. _`vchnl_pf_send_get_hmc_fcn_resp`:

vchnl_pf_send_get_hmc_fcn_resp
==============================

.. c:function:: void vchnl_pf_send_get_hmc_fcn_resp(struct i40iw_sc_dev *dev, u32 vf_id, struct i40iw_virtchnl_op_buf *vchnl_msg, u16 hmc_fcn)

    Send HMC Function to VF

    :param struct i40iw_sc_dev \*dev:
        IWARP device pointer

    :param u32 vf_id:
        Virtual function ID associated with the message

    :param struct i40iw_virtchnl_op_buf \*vchnl_msg:
        Virtual channel message buffer pointer

    :param u16 hmc_fcn:
        *undescribed*

.. _`vchnl_pf_send_get_pe_stats_resp`:

vchnl_pf_send_get_pe_stats_resp
===============================

.. c:function:: void vchnl_pf_send_get_pe_stats_resp(struct i40iw_sc_dev *dev, u32 vf_id, struct i40iw_virtchnl_op_buf *vchnl_msg, struct i40iw_dev_hw_stats *hw_stats)

    Send PE Stats to VF

    :param struct i40iw_sc_dev \*dev:
        IWARP device pointer

    :param u32 vf_id:
        Virtual function ID associated with the message

    :param struct i40iw_virtchnl_op_buf \*vchnl_msg:
        Virtual channel message buffer pointer

    :param struct i40iw_dev_hw_stats \*hw_stats:
        HW Stats struct

.. _`vchnl_pf_send_error_resp`:

vchnl_pf_send_error_resp
========================

.. c:function:: void vchnl_pf_send_error_resp(struct i40iw_sc_dev *dev, u32 vf_id, struct i40iw_virtchnl_op_buf *vchnl_msg, u16 op_ret_code)

    Send an error response to VF

    :param struct i40iw_sc_dev \*dev:
        IWARP device pointer

    :param u32 vf_id:
        Virtual function ID associated with the message

    :param struct i40iw_virtchnl_op_buf \*vchnl_msg:
        Virtual channel message buffer pointer

    :param u16 op_ret_code:
        *undescribed*

.. _`pf_cqp_get_hmc_fcn_callback`:

pf_cqp_get_hmc_fcn_callback
===========================

.. c:function:: void pf_cqp_get_hmc_fcn_callback(struct i40iw_sc_dev *dev, void *callback_param, struct i40iw_ccq_cqe_info *cqe_info)

    Callback for Get HMC Fcn

    :param struct i40iw_sc_dev \*dev:
        *undescribed*

    :param void \*callback_param:
        *undescribed*

    :param struct i40iw_ccq_cqe_info \*cqe_info:
        *undescribed*

.. _`pf_add_hmc_obj_callback`:

pf_add_hmc_obj_callback
=======================

.. c:function:: void pf_add_hmc_obj_callback(void *work_vf_dev)

    Callback for Add HMC Object

    :param void \*work_vf_dev:
        *undescribed*

.. _`pf_del_hmc_obj_callback`:

pf_del_hmc_obj_callback
=======================

.. c:function:: void pf_del_hmc_obj_callback(void *work_vf_dev)

    Callback for delete HMC Object

    :param void \*work_vf_dev:
        pointer to the VF Device

.. _`i40iw_vf_init_pestat`:

i40iw_vf_init_pestat
====================

.. c:function:: void i40iw_vf_init_pestat(struct i40iw_sc_dev *dev, struct i40iw_vsi_pestat *stats, u16 index)

    Initialize stats for VF \ ``devL``\  pointer to the VF Device

    :param struct i40iw_sc_dev \*dev:
        *undescribed*

    :param struct i40iw_vsi_pestat \*stats:
        Statistics structure pointer

    :param u16 index:
        Stats index

.. _`i40iw_vchnl_recv_pf`:

i40iw_vchnl_recv_pf
===================

.. c:function:: enum i40iw_status_code i40iw_vchnl_recv_pf(struct i40iw_sc_dev *dev, u32 vf_id, u8 *msg, u16 len)

    Receive PF virtual channel messages

    :param struct i40iw_sc_dev \*dev:
        IWARP device pointer

    :param u32 vf_id:
        Virtual function ID associated with the message

    :param u8 \*msg:
        Virtual channel message buffer pointer

    :param u16 len:
        Length of the virtual channels message

.. _`i40iw_vchnl_recv_vf`:

i40iw_vchnl_recv_vf
===================

.. c:function:: enum i40iw_status_code i40iw_vchnl_recv_vf(struct i40iw_sc_dev *dev, u32 vf_id, u8 *msg, u16 len)

    Receive VF virtual channel messages

    :param struct i40iw_sc_dev \*dev:
        IWARP device pointer

    :param u32 vf_id:
        Virtual function ID associated with the message

    :param u8 \*msg:
        Virtual channel message buffer pointer

    :param u16 len:
        Length of the virtual channels message

.. _`i40iw_vchnl_vf_get_ver`:

i40iw_vchnl_vf_get_ver
======================

.. c:function:: enum i40iw_status_code i40iw_vchnl_vf_get_ver(struct i40iw_sc_dev *dev, u32 *vchnl_ver)

    Request Channel version

    :param struct i40iw_sc_dev \*dev:
        IWARP device pointer

    :param u32 \*vchnl_ver:
        Virtual channel message version pointer

.. _`i40iw_vchnl_vf_get_hmc_fcn`:

i40iw_vchnl_vf_get_hmc_fcn
==========================

.. c:function:: enum i40iw_status_code i40iw_vchnl_vf_get_hmc_fcn(struct i40iw_sc_dev *dev, u16 *hmc_fcn)

    Request HMC Function

    :param struct i40iw_sc_dev \*dev:
        IWARP device pointer

    :param u16 \*hmc_fcn:
        HMC function index pointer

.. _`i40iw_vchnl_vf_add_hmc_objs`:

i40iw_vchnl_vf_add_hmc_objs
===========================

.. c:function:: enum i40iw_status_code i40iw_vchnl_vf_add_hmc_objs(struct i40iw_sc_dev *dev, enum i40iw_hmc_rsrc_type rsrc_type, u32 start_index, u32 rsrc_count)

    Add HMC Object

    :param struct i40iw_sc_dev \*dev:
        IWARP device pointer

    :param enum i40iw_hmc_rsrc_type rsrc_type:
        HMC Resource type

    :param u32 start_index:
        Starting index of the objects to be added

    :param u32 rsrc_count:
        Number of resources to be added

.. _`i40iw_vchnl_vf_del_hmc_obj`:

i40iw_vchnl_vf_del_hmc_obj
==========================

.. c:function:: enum i40iw_status_code i40iw_vchnl_vf_del_hmc_obj(struct i40iw_sc_dev *dev, enum i40iw_hmc_rsrc_type rsrc_type, u32 start_index, u32 rsrc_count)

    del HMC obj

    :param struct i40iw_sc_dev \*dev:
        IWARP device pointer

    :param enum i40iw_hmc_rsrc_type rsrc_type:
        HMC Resource type

    :param u32 start_index:
        Starting index of the object to delete

    :param u32 rsrc_count:
        Number of resources to be delete

.. _`i40iw_vchnl_vf_get_pe_stats`:

i40iw_vchnl_vf_get_pe_stats
===========================

.. c:function:: enum i40iw_status_code i40iw_vchnl_vf_get_pe_stats(struct i40iw_sc_dev *dev, struct i40iw_dev_hw_stats *hw_stats)

    Get PE stats

    :param struct i40iw_sc_dev \*dev:
        IWARP device pointer

    :param struct i40iw_dev_hw_stats \*hw_stats:
        HW stats struct

.. This file was automatic generated / don't edit.

