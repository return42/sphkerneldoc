.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_virtchnl.c

.. _`vchnl_vf_send_get_ver_req`:

vchnl_vf_send_get_ver_req
=========================

.. c:function:: enum i40iw_status_code vchnl_vf_send_get_ver_req(struct i40iw_sc_dev *dev, struct i40iw_virtchnl_req *vchnl_req)

    Request Channel version

    :param dev:
        IWARP device pointer
    :type dev: struct i40iw_sc_dev \*

    :param vchnl_req:
        Virtual channel message request pointer
    :type vchnl_req: struct i40iw_virtchnl_req \*

.. _`vchnl_vf_send_get_hmc_fcn_req`:

vchnl_vf_send_get_hmc_fcn_req
=============================

.. c:function:: enum i40iw_status_code vchnl_vf_send_get_hmc_fcn_req(struct i40iw_sc_dev *dev, struct i40iw_virtchnl_req *vchnl_req)

    Request HMC Function from VF

    :param dev:
        IWARP device pointer
    :type dev: struct i40iw_sc_dev \*

    :param vchnl_req:
        Virtual channel message request pointer
    :type vchnl_req: struct i40iw_virtchnl_req \*

.. _`vchnl_vf_send_get_pe_stats_req`:

vchnl_vf_send_get_pe_stats_req
==============================

.. c:function:: enum i40iw_status_code vchnl_vf_send_get_pe_stats_req(struct i40iw_sc_dev *dev, struct i40iw_virtchnl_req *vchnl_req)

    Request PE stats from VF

    :param dev:
        IWARP device pointer
    :type dev: struct i40iw_sc_dev \*

    :param vchnl_req:
        Virtual channel message request pointer
    :type vchnl_req: struct i40iw_virtchnl_req \*

.. _`vchnl_vf_send_add_hmc_objs_req`:

vchnl_vf_send_add_hmc_objs_req
==============================

.. c:function:: enum i40iw_status_code vchnl_vf_send_add_hmc_objs_req(struct i40iw_sc_dev *dev, struct i40iw_virtchnl_req *vchnl_req, enum i40iw_hmc_rsrc_type rsrc_type, u32 start_index, u32 rsrc_count)

    Add HMC objects

    :param dev:
        IWARP device pointer
    :type dev: struct i40iw_sc_dev \*

    :param vchnl_req:
        Virtual channel message request pointer
    :type vchnl_req: struct i40iw_virtchnl_req \*

    :param rsrc_type:
        *undescribed*
    :type rsrc_type: enum i40iw_hmc_rsrc_type

    :param start_index:
        *undescribed*
    :type start_index: u32

    :param rsrc_count:
        *undescribed*
    :type rsrc_count: u32

.. _`vchnl_vf_send_del_hmc_objs_req`:

vchnl_vf_send_del_hmc_objs_req
==============================

.. c:function:: enum i40iw_status_code vchnl_vf_send_del_hmc_objs_req(struct i40iw_sc_dev *dev, struct i40iw_virtchnl_req *vchnl_req, enum i40iw_hmc_rsrc_type rsrc_type, u32 start_index, u32 rsrc_count)

    del HMC objects

    :param dev:
        IWARP device pointer
    :type dev: struct i40iw_sc_dev \*

    :param vchnl_req:
        Virtual channel message request pointer
        \ ````\  rsrc_type - resource type to delete
        \ ````\  start_index - starting index for resource
        \ ````\  rsrc_count - number of resource type to delete
    :type vchnl_req: struct i40iw_virtchnl_req \*

    :param rsrc_type:
        *undescribed*
    :type rsrc_type: enum i40iw_hmc_rsrc_type

    :param start_index:
        *undescribed*
    :type start_index: u32

    :param rsrc_count:
        *undescribed*
    :type rsrc_count: u32

.. _`vchnl_pf_send_get_ver_resp`:

vchnl_pf_send_get_ver_resp
==========================

.. c:function:: void vchnl_pf_send_get_ver_resp(struct i40iw_sc_dev *dev, u32 vf_id, struct i40iw_virtchnl_op_buf *vchnl_msg)

    Send channel version to VF

    :param dev:
        IWARP device pointer
    :type dev: struct i40iw_sc_dev \*

    :param vf_id:
        Virtual function ID associated with the message
    :type vf_id: u32

    :param vchnl_msg:
        Virtual channel message buffer pointer
    :type vchnl_msg: struct i40iw_virtchnl_op_buf \*

.. _`vchnl_pf_send_get_hmc_fcn_resp`:

vchnl_pf_send_get_hmc_fcn_resp
==============================

.. c:function:: void vchnl_pf_send_get_hmc_fcn_resp(struct i40iw_sc_dev *dev, u32 vf_id, struct i40iw_virtchnl_op_buf *vchnl_msg, u16 hmc_fcn)

    Send HMC Function to VF

    :param dev:
        IWARP device pointer
    :type dev: struct i40iw_sc_dev \*

    :param vf_id:
        Virtual function ID associated with the message
    :type vf_id: u32

    :param vchnl_msg:
        Virtual channel message buffer pointer
    :type vchnl_msg: struct i40iw_virtchnl_op_buf \*

    :param hmc_fcn:
        *undescribed*
    :type hmc_fcn: u16

.. _`vchnl_pf_send_get_pe_stats_resp`:

vchnl_pf_send_get_pe_stats_resp
===============================

.. c:function:: void vchnl_pf_send_get_pe_stats_resp(struct i40iw_sc_dev *dev, u32 vf_id, struct i40iw_virtchnl_op_buf *vchnl_msg, struct i40iw_dev_hw_stats *hw_stats)

    Send PE Stats to VF

    :param dev:
        IWARP device pointer
    :type dev: struct i40iw_sc_dev \*

    :param vf_id:
        Virtual function ID associated with the message
    :type vf_id: u32

    :param vchnl_msg:
        Virtual channel message buffer pointer
    :type vchnl_msg: struct i40iw_virtchnl_op_buf \*

    :param hw_stats:
        HW Stats struct
    :type hw_stats: struct i40iw_dev_hw_stats \*

.. _`vchnl_pf_send_error_resp`:

vchnl_pf_send_error_resp
========================

.. c:function:: void vchnl_pf_send_error_resp(struct i40iw_sc_dev *dev, u32 vf_id, struct i40iw_virtchnl_op_buf *vchnl_msg, u16 op_ret_code)

    Send an error response to VF

    :param dev:
        IWARP device pointer
    :type dev: struct i40iw_sc_dev \*

    :param vf_id:
        Virtual function ID associated with the message
    :type vf_id: u32

    :param vchnl_msg:
        Virtual channel message buffer pointer
    :type vchnl_msg: struct i40iw_virtchnl_op_buf \*

    :param op_ret_code:
        *undescribed*
    :type op_ret_code: u16

.. _`pf_cqp_get_hmc_fcn_callback`:

pf_cqp_get_hmc_fcn_callback
===========================

.. c:function:: void pf_cqp_get_hmc_fcn_callback(struct i40iw_sc_dev *dev, void *callback_param, struct i40iw_ccq_cqe_info *cqe_info)

    Callback for Get HMC Fcn

    :param dev:
        *undescribed*
    :type dev: struct i40iw_sc_dev \*

    :param callback_param:
        *undescribed*
    :type callback_param: void \*

    :param cqe_info:
        *undescribed*
    :type cqe_info: struct i40iw_ccq_cqe_info \*

.. _`pf_add_hmc_obj_callback`:

pf_add_hmc_obj_callback
=======================

.. c:function:: void pf_add_hmc_obj_callback(void *work_vf_dev)

    Callback for Add HMC Object

    :param work_vf_dev:
        *undescribed*
    :type work_vf_dev: void \*

.. _`pf_del_hmc_obj_callback`:

pf_del_hmc_obj_callback
=======================

.. c:function:: void pf_del_hmc_obj_callback(void *work_vf_dev)

    Callback for delete HMC Object

    :param work_vf_dev:
        pointer to the VF Device
    :type work_vf_dev: void \*

.. _`i40iw_vf_init_pestat`:

i40iw_vf_init_pestat
====================

.. c:function:: void i40iw_vf_init_pestat(struct i40iw_sc_dev *dev, struct i40iw_vsi_pestat *stats, u16 index)

    Initialize stats for VF \ ``devL``\  pointer to the VF Device

    :param dev:
        *undescribed*
    :type dev: struct i40iw_sc_dev \*

    :param stats:
        Statistics structure pointer
    :type stats: struct i40iw_vsi_pestat \*

    :param index:
        Stats index
    :type index: u16

.. _`i40iw_vchnl_recv_pf`:

i40iw_vchnl_recv_pf
===================

.. c:function:: enum i40iw_status_code i40iw_vchnl_recv_pf(struct i40iw_sc_dev *dev, u32 vf_id, u8 *msg, u16 len)

    Receive PF virtual channel messages

    :param dev:
        IWARP device pointer
    :type dev: struct i40iw_sc_dev \*

    :param vf_id:
        Virtual function ID associated with the message
    :type vf_id: u32

    :param msg:
        Virtual channel message buffer pointer
    :type msg: u8 \*

    :param len:
        Length of the virtual channels message
    :type len: u16

.. _`i40iw_vchnl_recv_vf`:

i40iw_vchnl_recv_vf
===================

.. c:function:: enum i40iw_status_code i40iw_vchnl_recv_vf(struct i40iw_sc_dev *dev, u32 vf_id, u8 *msg, u16 len)

    Receive VF virtual channel messages

    :param dev:
        IWARP device pointer
    :type dev: struct i40iw_sc_dev \*

    :param vf_id:
        Virtual function ID associated with the message
    :type vf_id: u32

    :param msg:
        Virtual channel message buffer pointer
    :type msg: u8 \*

    :param len:
        Length of the virtual channels message
    :type len: u16

.. _`i40iw_vchnl_vf_get_ver`:

i40iw_vchnl_vf_get_ver
======================

.. c:function:: enum i40iw_status_code i40iw_vchnl_vf_get_ver(struct i40iw_sc_dev *dev, u32 *vchnl_ver)

    Request Channel version

    :param dev:
        IWARP device pointer
    :type dev: struct i40iw_sc_dev \*

    :param vchnl_ver:
        Virtual channel message version pointer
    :type vchnl_ver: u32 \*

.. _`i40iw_vchnl_vf_get_hmc_fcn`:

i40iw_vchnl_vf_get_hmc_fcn
==========================

.. c:function:: enum i40iw_status_code i40iw_vchnl_vf_get_hmc_fcn(struct i40iw_sc_dev *dev, u16 *hmc_fcn)

    Request HMC Function

    :param dev:
        IWARP device pointer
    :type dev: struct i40iw_sc_dev \*

    :param hmc_fcn:
        HMC function index pointer
    :type hmc_fcn: u16 \*

.. _`i40iw_vchnl_vf_add_hmc_objs`:

i40iw_vchnl_vf_add_hmc_objs
===========================

.. c:function:: enum i40iw_status_code i40iw_vchnl_vf_add_hmc_objs(struct i40iw_sc_dev *dev, enum i40iw_hmc_rsrc_type rsrc_type, u32 start_index, u32 rsrc_count)

    Add HMC Object

    :param dev:
        IWARP device pointer
    :type dev: struct i40iw_sc_dev \*

    :param rsrc_type:
        HMC Resource type
    :type rsrc_type: enum i40iw_hmc_rsrc_type

    :param start_index:
        Starting index of the objects to be added
    :type start_index: u32

    :param rsrc_count:
        Number of resources to be added
    :type rsrc_count: u32

.. _`i40iw_vchnl_vf_del_hmc_obj`:

i40iw_vchnl_vf_del_hmc_obj
==========================

.. c:function:: enum i40iw_status_code i40iw_vchnl_vf_del_hmc_obj(struct i40iw_sc_dev *dev, enum i40iw_hmc_rsrc_type rsrc_type, u32 start_index, u32 rsrc_count)

    del HMC obj

    :param dev:
        IWARP device pointer
    :type dev: struct i40iw_sc_dev \*

    :param rsrc_type:
        HMC Resource type
    :type rsrc_type: enum i40iw_hmc_rsrc_type

    :param start_index:
        Starting index of the object to delete
    :type start_index: u32

    :param rsrc_count:
        Number of resources to be delete
    :type rsrc_count: u32

.. _`i40iw_vchnl_vf_get_pe_stats`:

i40iw_vchnl_vf_get_pe_stats
===========================

.. c:function:: enum i40iw_status_code i40iw_vchnl_vf_get_pe_stats(struct i40iw_sc_dev *dev, struct i40iw_dev_hw_stats *hw_stats)

    Get PE stats

    :param dev:
        IWARP device pointer
    :type dev: struct i40iw_sc_dev \*

    :param hw_stats:
        HW stats struct
    :type hw_stats: struct i40iw_dev_hw_stats \*

.. This file was automatic generated / don't edit.

