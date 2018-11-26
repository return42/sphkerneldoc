.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_hw_interrupts.c

.. _`mdp_sspp_top0_off`:

MDP_SSPP_TOP0_OFF
=================

.. c:function::  MDP_SSPP_TOP0_OFF()

    w.r.t. to the MDP base

.. _`dpu_intr_wb_0_done`:

DPU_INTR_WB_0_DONE
==================

.. c:function::  DPU_INTR_WB_0_DONE()

.. _`dpu_intr_wd_timer_0_done`:

DPU_INTR_WD_TIMER_0_DONE
========================

.. c:function::  DPU_INTR_WD_TIMER_0_DONE()

.. _`dpu_intr_ping_pong_0_done`:

DPU_INTR_PING_PONG_0_DONE
=========================

.. c:function::  DPU_INTR_PING_PONG_0_DONE()

.. _`dpu_intr_intf_0_underrun`:

DPU_INTR_INTF_0_UNDERRUN
========================

.. c:function::  DPU_INTR_INTF_0_UNDERRUN()

.. _`dpu_intr_ping_pong_s0_autorefresh_done`:

DPU_INTR_PING_PONG_S0_AUTOREFRESH_DONE
======================================

.. c:function::  DPU_INTR_PING_PONG_S0_AUTOREFRESH_DONE()

.. _`dpu_intr_ping_pong_0_tear_detected`:

DPU_INTR_PING_PONG_0_TEAR_DETECTED
==================================

.. c:function::  DPU_INTR_PING_PONG_0_TEAR_DETECTED()

.. _`dpu_intr_ping_pong_0_te_detected`:

DPU_INTR_PING_PONG_0_TE_DETECTED
================================

.. c:function::  DPU_INTR_PING_PONG_0_TE_DETECTED()

.. _`dpu_intr_ctl_0_start`:

DPU_INTR_CTL_0_START
====================

.. c:function::  DPU_INTR_CTL_0_START()

.. _`dpu_intr_cwb_2_overflow`:

DPU_INTR_CWB_2_OVERFLOW
=======================

.. c:function::  DPU_INTR_CWB_2_OVERFLOW()

.. _`dpu_intr_hist_vig_0_done`:

DPU_INTR_HIST_VIG_0_DONE
========================

.. c:function::  DPU_INTR_HIST_VIG_0_DONE()

.. _`dpu_intr_hist_vig_0_rstseq_done`:

DPU_INTR_HIST_VIG_0_RSTSEQ_DONE
===============================

.. c:function::  DPU_INTR_HIST_VIG_0_RSTSEQ_DONE()

.. _`dpu_intr_hist_dspp_0_done`:

DPU_INTR_HIST_DSPP_0_DONE
=========================

.. c:function::  DPU_INTR_HIST_DSPP_0_DONE()

.. _`dpu_intr_hist_dspp_0_rstseq_done`:

DPU_INTR_HIST_DSPP_0_RSTSEQ_DONE
================================

.. c:function::  DPU_INTR_HIST_DSPP_0_RSTSEQ_DONE()

.. _`dpu_intr_video_into_static`:

DPU_INTR_VIDEO_INTO_STATIC
==========================

.. c:function::  DPU_INTR_VIDEO_INTO_STATIC()

.. _`dpu_intr_brightpr_updated`:

DPU_INTR_BRIGHTPR_UPDATED
=========================

.. c:function::  DPU_INTR_BRIGHTPR_UPDATED()

.. _`dpu_intr_reg`:

struct dpu_intr_reg
===================

.. c:type:: struct dpu_intr_reg

    array of DPU register sets

.. _`dpu_intr_reg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_intr_reg {
        u32 clr_off;
        u32 en_off;
        u32 status_off;
    }

.. _`dpu_intr_reg.members`:

Members
-------

clr_off
    offset to CLEAR reg

en_off
    offset to ENABLE reg

status_off
    offset to STATUS reg

.. _`dpu_irq_type`:

struct dpu_irq_type
===================

.. c:type:: struct dpu_irq_type

    maps each irq with i/f

.. _`dpu_irq_type.definition`:

Definition
----------

.. code-block:: c

    struct dpu_irq_type {
        u32 intr_type;
        u32 instance_idx;
        u32 irq_mask;
        u32 reg_idx;
    }

.. _`dpu_irq_type.members`:

Members
-------

intr_type
    type of interrupt listed in dpu_intr_type

instance_idx
    instance index of the associated HW block in DPU

irq_mask
    corresponding bit in the interrupt status reg

reg_idx
    which reg set to use

.. This file was automatic generated / don't edit.

