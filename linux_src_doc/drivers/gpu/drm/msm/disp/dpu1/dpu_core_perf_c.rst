.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_core_perf.c

.. _`dpu_perf_mode`:

enum dpu_perf_mode
==================

.. c:type:: enum dpu_perf_mode

    performance tuning mode

.. _`dpu_perf_mode.definition`:

Definition
----------

.. code-block:: c

    enum dpu_perf_mode {
        DPU_PERF_MODE_NORMAL,
        DPU_PERF_MODE_MINIMUM,
        DPU_PERF_MODE_FIXED,
        DPU_PERF_MODE_MAX
    };

.. _`dpu_perf_mode.constants`:

Constants
---------

DPU_PERF_MODE_NORMAL
    performance controlled by user mode client

DPU_PERF_MODE_MINIMUM
    performance bounded by minimum setting

DPU_PERF_MODE_FIXED
    performance bounded by fixed setting

DPU_PERF_MODE_MAX
    *undescribed*

.. This file was automatic generated / don't edit.

