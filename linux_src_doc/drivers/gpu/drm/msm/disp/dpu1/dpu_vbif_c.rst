.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_vbif.c

.. _`_dpu_vbif_wait_for_xin_halt`:

\_dpu_vbif_wait_for_xin_halt
============================

.. c:function:: int _dpu_vbif_wait_for_xin_halt(struct dpu_hw_vbif *vbif, u32 xin_id)

    wait for the xin to halt

    :param vbif:
        Pointer to hardware vbif driver
    :type vbif: struct dpu_hw_vbif \*

    :param xin_id:
        Client interface identifier
    :type xin_id: u32

.. _`_dpu_vbif_apply_dynamic_ot_limit`:

\_dpu_vbif_apply_dynamic_ot_limit
=================================

.. c:function:: void _dpu_vbif_apply_dynamic_ot_limit(struct dpu_hw_vbif *vbif, u32 *ot_lim, struct dpu_vbif_set_ot_params *params)

    determine OT based on usecase parameters

    :param vbif:
        Pointer to hardware vbif driver
    :type vbif: struct dpu_hw_vbif \*

    :param ot_lim:
        Pointer to OT limit to be modified
    :type ot_lim: u32 \*

    :param params:
        Pointer to usecase parameters
    :type params: struct dpu_vbif_set_ot_params \*

.. _`_dpu_vbif_get_ot_limit`:

\_dpu_vbif_get_ot_limit
=======================

.. c:function:: u32 _dpu_vbif_get_ot_limit(struct dpu_hw_vbif *vbif, struct dpu_vbif_set_ot_params *params)

    get OT based on usecase & configuration parameters

    :param vbif:
        Pointer to hardware vbif driver
    :type vbif: struct dpu_hw_vbif \*

    :param params:
        Pointer to usecase parameters
    :type params: struct dpu_vbif_set_ot_params \*

.. _`dpu_vbif_set_ot_limit`:

dpu_vbif_set_ot_limit
=====================

.. c:function:: void dpu_vbif_set_ot_limit(struct dpu_kms *dpu_kms, struct dpu_vbif_set_ot_params *params)

    set OT based on usecase & configuration parameters

    :param dpu_kms:
        *undescribed*
    :type dpu_kms: struct dpu_kms \*

    :param params:
        Pointer to usecase parameters
    :type params: struct dpu_vbif_set_ot_params \*

.. _`dpu_vbif_set_ot_limit.description`:

Description
-----------

Note this function would block waiting for bus halt.

.. This file was automatic generated / don't edit.

