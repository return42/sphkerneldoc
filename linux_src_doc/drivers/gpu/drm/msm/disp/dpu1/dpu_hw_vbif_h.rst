.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_hw_vbif.h

.. _`dpu_hw_vbif_ops`:

struct dpu_hw_vbif_ops
======================

.. c:type:: struct dpu_hw_vbif_ops

    Interface to the VBIF hardware driver functions Assumption is these functions will be called after clocks are enabled

.. _`dpu_hw_vbif_ops.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_vbif_ops {
        void (*set_limit_conf)(struct dpu_hw_vbif *vbif, u32 xin_id, bool rd, u32 limit);
        u32 (*get_limit_conf)(struct dpu_hw_vbif *vbif, u32 xin_id, bool rd);
        void (*set_halt_ctrl)(struct dpu_hw_vbif *vbif, u32 xin_id, bool enable);
        bool (*get_halt_ctrl)(struct dpu_hw_vbif *vbif, u32 xin_id);
        void (*set_qos_remap)(struct dpu_hw_vbif *vbif, u32 xin_id, u32 level, u32 remap_level);
        void (*set_mem_type)(struct dpu_hw_vbif *vbif, u32 xin_id, u32 value);
        void (*clear_errors)(struct dpu_hw_vbif *vbif, u32 *pnd_errors, u32 *src_errors);
        void (*set_write_gather_en)(struct dpu_hw_vbif *vbif, u32 xin_id);
    }

.. _`dpu_hw_vbif_ops.members`:

Members
-------

set_limit_conf
    *undescribed*

get_limit_conf
    *undescribed*

set_halt_ctrl
    *undescribed*

get_halt_ctrl
    *undescribed*

set_qos_remap
    *undescribed*

set_mem_type
    *undescribed*

clear_errors
    *undescribed*

set_write_gather_en
    *undescribed*

.. _`dpu_hw_vbif_init`:

dpu_hw_vbif_init
================

.. c:function:: struct dpu_hw_vbif *dpu_hw_vbif_init(enum dpu_vbif idx, void __iomem *addr, const struct dpu_mdss_cfg *m)

    initializes the vbif driver for the passed interface idx

    :param idx:
        Interface index for which driver object is required
    :type idx: enum dpu_vbif

    :param addr:
        Mapped register io address of MDSS
    :type addr: void __iomem \*

    :param m:
        Pointer to mdss catalog data
    :type m: const struct dpu_mdss_cfg \*

.. This file was automatic generated / don't edit.

