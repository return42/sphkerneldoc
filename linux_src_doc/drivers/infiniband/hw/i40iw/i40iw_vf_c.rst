.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_vf.c

.. _`i40iw_manage_vf_pble_bp`:

i40iw_manage_vf_pble_bp
=======================

.. c:function:: enum i40iw_status_code i40iw_manage_vf_pble_bp(struct i40iw_sc_cqp *cqp, struct i40iw_manage_vf_pble_info *info, u64 scratch, bool post_sq)

    manage vf pble

    :param cqp:
        cqp for cqp' sq wqe
    :type cqp: struct i40iw_sc_cqp \*

    :param info:
        pble info
    :type info: struct i40iw_manage_vf_pble_info \*

    :param scratch:
        pointer for completion
    :type scratch: u64

    :param post_sq:
        to post and ring
    :type post_sq: bool

.. This file was automatic generated / don't edit.

