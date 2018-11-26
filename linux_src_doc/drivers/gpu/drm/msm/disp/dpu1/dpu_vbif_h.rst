.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_vbif.h

.. _`dpu_vbif_set_qos_params`:

struct dpu_vbif_set_qos_params
==============================

.. c:type:: struct dpu_vbif_set_qos_params

    QoS remapper parameter

.. _`dpu_vbif_set_qos_params.definition`:

Definition
----------

.. code-block:: c

    struct dpu_vbif_set_qos_params {
        u32 vbif_idx;
        u32 xin_id;
        u32 clk_ctrl;
        u32 num;
        bool is_rt;
    }

.. _`dpu_vbif_set_qos_params.members`:

Members
-------

vbif_idx
    vbif identifier

xin_id
    client interface identifier

clk_ctrl
    clock control identifier of the xin

num
    pipe identifier (debug only)

is_rt
    true if pipe is used in real-time use case

.. _`dpu_vbif_set_ot_limit`:

dpu_vbif_set_ot_limit
=====================

.. c:function:: void dpu_vbif_set_ot_limit(struct dpu_kms *dpu_kms, struct dpu_vbif_set_ot_params *params)

    set OT limit for vbif client

    :param dpu_kms:
        DPU handler
    :type dpu_kms: struct dpu_kms \*

    :param params:
        Pointer to OT configuration parameters
    :type params: struct dpu_vbif_set_ot_params \*

.. _`dpu_vbif_set_qos_remap`:

dpu_vbif_set_qos_remap
======================

.. c:function:: void dpu_vbif_set_qos_remap(struct dpu_kms *dpu_kms, struct dpu_vbif_set_qos_params *params)

    set QoS priority level remap

    :param dpu_kms:
        DPU handler
    :type dpu_kms: struct dpu_kms \*

    :param params:
        Pointer to QoS configuration parameters
    :type params: struct dpu_vbif_set_qos_params \*

.. _`dpu_vbif_clear_errors`:

dpu_vbif_clear_errors
=====================

.. c:function:: void dpu_vbif_clear_errors(struct dpu_kms *dpu_kms)

    clear any vbif errors

    :param dpu_kms:
        DPU handler
    :type dpu_kms: struct dpu_kms \*

.. _`dpu_vbif_init_memtypes`:

dpu_vbif_init_memtypes
======================

.. c:function:: void dpu_vbif_init_memtypes(struct dpu_kms *dpu_kms)

    initialize xin memory types for vbif

    :param dpu_kms:
        DPU handler
    :type dpu_kms: struct dpu_kms \*

.. This file was automatic generated / don't edit.

