.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/scheduler.c

.. _`intel_gvt_scan_and_shadow_workload`:

intel_gvt_scan_and_shadow_workload
==================================

.. c:function:: int intel_gvt_scan_and_shadow_workload(struct intel_vgpu_workload *workload)

    audit the workload by scanning and shadow it as well, include ringbuffer,wa_ctx and ctx.

    :param struct intel_vgpu_workload \*workload:
        an abstract entity for each execlist submission.

.. _`intel_gvt_scan_and_shadow_workload.description`:

Description
-----------

This function is called before the workload submitting to i915, to make
sure the content of the workload is valid.

.. This file was automatic generated / don't edit.

