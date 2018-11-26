.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_hw_intf.h

.. _`dpu_hw_intf_ops`:

struct dpu_hw_intf_ops
======================

.. c:type:: struct dpu_hw_intf_ops

    Interface to the interface Hw driver functions Assumption is these functions will be called after clocks are enabled \ ````\  setup_timing_gen : programs the timing engine \ ````\  setup_prog_fetch : enables/disables the programmable fetch logic \ ````\  enable_timing: enable/disable timing engine \ ````\  get_status: returns if timing engine is enabled or not \ ````\  get_line_count: reads current vertical line counter

.. _`dpu_hw_intf_ops.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_intf_ops {
        void (*setup_timing_gen)(struct dpu_hw_intf *intf,const struct intf_timing_params *p, const struct dpu_format *fmt);
        void (*setup_prg_fetch)(struct dpu_hw_intf *intf, const struct intf_prog_fetch *fetch);
        void (*enable_timing)(struct dpu_hw_intf *intf, u8 enable);
        void (*get_status)(struct dpu_hw_intf *intf, struct intf_status *status);
        u32 (*get_line_count)(struct dpu_hw_intf *intf);
    }

.. _`dpu_hw_intf_ops.members`:

Members
-------

setup_timing_gen
    *undescribed*

setup_prg_fetch
    *undescribed*

enable_timing
    *undescribed*

get_status
    *undescribed*

get_line_count
    *undescribed*

.. _`to_dpu_hw_intf`:

to_dpu_hw_intf
==============

.. c:function:: struct dpu_hw_intf *to_dpu_hw_intf(struct dpu_hw_blk *hw)

    convert base object dpu_hw_base to container

    :param hw:
        Pointer to base hardware block
    :type hw: struct dpu_hw_blk \*

.. _`to_dpu_hw_intf.return`:

Return
------

Pointer to hardware block container

.. _`dpu_hw_intf_init`:

dpu_hw_intf_init
================

.. c:function:: struct dpu_hw_intf *dpu_hw_intf_init(enum dpu_intf idx, void __iomem *addr, struct dpu_mdss_cfg *m)

    Initializes the intf driver for the passed interface idx.

    :param idx:
        interface index for which driver object is required
    :type idx: enum dpu_intf

    :param addr:
        mapped register io address of MDP
    :type addr: void __iomem \*

    :param m:
        pointer to mdss catalog data
    :type m: struct dpu_mdss_cfg \*

.. _`dpu_hw_intf_destroy`:

dpu_hw_intf_destroy
===================

.. c:function:: void dpu_hw_intf_destroy(struct dpu_hw_intf *intf)

    Destroys INTF driver context

    :param intf:
        Pointer to INTF driver context
    :type intf: struct dpu_hw_intf \*

.. This file was automatic generated / don't edit.

