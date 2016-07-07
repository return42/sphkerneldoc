.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw_vf.c

.. _`i40iw_manage_vf_pble_bp`:

i40iw_manage_vf_pble_bp
=======================

.. c:function:: enum i40iw_status_code i40iw_manage_vf_pble_bp(struct i40iw_sc_cqp *cqp, struct i40iw_manage_vf_pble_info *info, u64 scratch, bool post_sq)

    manage vf pble

    :param struct i40iw_sc_cqp \*cqp:
        cqp for cqp' sq wqe

    :param struct i40iw_manage_vf_pble_info \*info:
        pble info

    :param u64 scratch:
        pointer for completion

    :param bool post_sq:
        to post and ring

.. This file was automatic generated / don't edit.

