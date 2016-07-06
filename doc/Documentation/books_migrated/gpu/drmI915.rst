.. -*- coding: utf-8; mode: rst -*-

.. _drmI915:

*************************
drm/i915 Intel GFX Driver
*************************

The drm/i915 driver supports all (with the exception of some very early
models) integrated GFX chipsets with both Intel display and rendering
blocks. This excludes a set of SoC platforms with an SGX rendering unit,
those have basic support through the gma500 drm driver.


Core Driver Infrastructure
==========================

This section covers core driver infrastructure used by both the display
and the GEM parts of the driver.


Runtime Power Management
------------------------


.. kernel-doc:: drivers/gpu/drm/i915/intel_runtime_pm.c
    :man-sect: 9
    :doc: runtime pm


.. kernel-doc:: drivers/gpu/drm/i915/intel_runtime_pm.c
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/gpu/drm/i915/intel_uncore.c
    :man-sect: 9
    :internal:


Interrupt Handling
------------------


.. kernel-doc:: drivers/gpu/drm/i915/i915_irq.c
    :man-sect: 9
    :doc: interrupt handling


.. kernel-doc:: drivers/gpu/drm/i915/i915_irq.c
    :man-sect: 9
    :functions: intel_irq_init intel_irq_init_hw intel_hpd_init


.. kernel-doc:: drivers/gpu/drm/i915/i915_irq.c
    :man-sect: 9
    :functions: intel_runtime_pm_disable_interrupts


.. kernel-doc:: drivers/gpu/drm/i915/i915_irq.c
    :man-sect: 9
    :functions: intel_runtime_pm_enable_interrupts


Intel GVT-g Guest Support(vGPU)
-------------------------------


.. kernel-doc:: drivers/gpu/drm/i915/i915_vgpu.c
    :man-sect: 9
    :doc: Intel GVT-g guest support


.. kernel-doc:: drivers/gpu/drm/i915/i915_vgpu.c
    :man-sect: 9
    :internal:


Display Hardware Handling
=========================

This section covers everything related to the display hardware including
the mode setting infrastructure, plane, sprite and cursor handling and
display, output probing and related topics.


Mode Setting Infrastructure
---------------------------

The i915 driver is thus far the only DRM driver which doesn't use the
common DRM helper code to implement mode setting sequences. Thus it has
its own tailor-made infrastructure for executing a display configuration
change.


Frontbuffer Tracking
--------------------


.. kernel-doc:: drivers/gpu/drm/i915/intel_frontbuffer.c
    :man-sect: 9
    :doc: frontbuffer tracking


.. kernel-doc:: drivers/gpu/drm/i915/intel_frontbuffer.c
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/gpu/drm/i915/i915_gem.c
    :man-sect: 9
    :functions: i915_gem_track_fb


Display FIFO Underrun Reporting
-------------------------------


.. kernel-doc:: drivers/gpu/drm/i915/intel_fifo_underrun.c
    :man-sect: 9
    :doc: fifo underrun handling


.. kernel-doc:: drivers/gpu/drm/i915/intel_fifo_underrun.c
    :man-sect: 9
    :internal:


Plane Configuration
-------------------

This section covers plane configuration and composition with the primary
plane, sprites, cursors and overlays. This includes the infrastructure
to do atomic vsync'ed updates of all this state and also tightly coupled
topics like watermark setup and computation, framebuffer compression and
panel self refresh.


Atomic Plane Helpers
--------------------


.. kernel-doc:: drivers/gpu/drm/i915/intel_atomic_plane.c
    :man-sect: 9
    :doc: atomic plane helpers


.. kernel-doc:: drivers/gpu/drm/i915/intel_atomic_plane.c
    :man-sect: 9
    :internal:


Output Probing
--------------

This section covers output probing and related infrastructure like the
hotplug interrupt storm detection and mitigation code. Note that the
i915 driver still uses most of the common DRM helper code for output
probing, so those sections fully apply.


Hotplug
-------


.. kernel-doc:: drivers/gpu/drm/i915/intel_hotplug.c
    :man-sect: 9
    :doc: Hotplug


.. kernel-doc:: drivers/gpu/drm/i915/intel_hotplug.c
    :man-sect: 9
    :internal:


High Definition Audio
---------------------


.. kernel-doc:: drivers/gpu/drm/i915/intel_audio.c
    :man-sect: 9
    :doc: High Definition Audio over HDMI and Display Port


.. kernel-doc:: drivers/gpu/drm/i915/intel_audio.c
    :man-sect: 9
    :internal:


.. kernel-doc:: include/drm/i915_component.h
    :man-sect: 9
    :internal:


Panel Self Refresh PSR (PSR/SRD)
--------------------------------


.. kernel-doc:: drivers/gpu/drm/i915/intel_psr.c
    :man-sect: 9
    :doc: Panel Self Refresh (PSR/SRD)


.. kernel-doc:: drivers/gpu/drm/i915/intel_psr.c
    :man-sect: 9
    :internal:


Frame Buffer Compression (FBC)
------------------------------


.. kernel-doc:: drivers/gpu/drm/i915/intel_fbc.c
    :man-sect: 9
    :doc: Frame Buffer Compression (FBC)


.. kernel-doc:: drivers/gpu/drm/i915/intel_fbc.c
    :man-sect: 9
    :internal:


Display Refresh Rate Switching (DRRS)
-------------------------------------


.. kernel-doc:: drivers/gpu/drm/i915/intel_dp.c
    :man-sect: 9
    :doc: Display Refresh Rate Switching (DRRS)


.. kernel-doc:: drivers/gpu/drm/i915/intel_dp.c
    :man-sect: 9
    :functions: intel_dp_set_drrs_state


.. kernel-doc:: drivers/gpu/drm/i915/intel_dp.c
    :man-sect: 9
    :functions: intel_edp_drrs_enable


.. kernel-doc:: drivers/gpu/drm/i915/intel_dp.c
    :man-sect: 9
    :functions: intel_edp_drrs_disable


.. kernel-doc:: drivers/gpu/drm/i915/intel_dp.c
    :man-sect: 9
    :functions: intel_edp_drrs_invalidate


.. kernel-doc:: drivers/gpu/drm/i915/intel_dp.c
    :man-sect: 9
    :functions: intel_edp_drrs_flush


.. kernel-doc:: drivers/gpu/drm/i915/intel_dp.c
    :man-sect: 9
    :functions: intel_dp_drrs_init


DPIO
----


.. kernel-doc:: drivers/gpu/drm/i915/i915_reg.h
    :man-sect: 9
    :doc: DPIO


CSR firmware support for DMC
----------------------------


.. kernel-doc:: drivers/gpu/drm/i915/intel_csr.c
    :man-sect: 9
    :doc: csr support for dmc


.. kernel-doc:: drivers/gpu/drm/i915/intel_csr.c
    :man-sect: 9
    :internal:


Video BIOS Table (VBT)
----------------------


.. kernel-doc:: drivers/gpu/drm/i915/intel_bios.c
    :man-sect: 9
    :doc: Video BIOS Table (VBT)


.. kernel-doc:: drivers/gpu/drm/i915/intel_bios.c
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/gpu/drm/i915/intel_vbt_defs.h
    :man-sect: 9
    :internal:


Memory Management and Command Submission
========================================

This sections covers all things related to the GEM implementation in the
i915 driver.


Batchbuffer Parsing
-------------------


.. kernel-doc:: drivers/gpu/drm/i915/i915_cmd_parser.c
    :man-sect: 9
    :doc: batch buffer command parser


.. kernel-doc:: drivers/gpu/drm/i915/i915_cmd_parser.c
    :man-sect: 9
    :internal:


Batchbuffer Pools
-----------------


.. kernel-doc:: drivers/gpu/drm/i915/i915_gem_batch_pool.c
    :man-sect: 9
    :doc: batch pool


.. kernel-doc:: drivers/gpu/drm/i915/i915_gem_batch_pool.c
    :man-sect: 9
    :internal:


Logical Rings, Logical Ring Contexts and Execlists
--------------------------------------------------


.. kernel-doc:: drivers/gpu/drm/i915/intel_lrc.c
    :man-sect: 9
    :doc: Logical Rings, Logical Ring Contexts and Execlists


.. kernel-doc:: drivers/gpu/drm/i915/intel_lrc.c
    :man-sect: 9
    :internal:


Global GTT views
----------------


.. kernel-doc:: drivers/gpu/drm/i915/i915_gem_gtt.c
    :man-sect: 9
    :doc: Global GTT views


.. kernel-doc:: drivers/gpu/drm/i915/i915_gem_gtt.c
    :man-sect: 9
    :internal:


GTT Fences and Swizzling
------------------------


.. kernel-doc:: drivers/gpu/drm/i915/i915_gem_fence.c
    :man-sect: 9
    :internal:


Global GTT Fence Handling
^^^^^^^^^^^^^^^^^^^^^^^^^


.. kernel-doc:: drivers/gpu/drm/i915/i915_gem_fence.c
    :man-sect: 9
    :doc: fence register handling


Hardware Tiling and Swizzling Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. kernel-doc:: drivers/gpu/drm/i915/i915_gem_fence.c
    :man-sect: 9
    :doc: tiling swizzling details


Object Tiling IOCTLs
--------------------


.. kernel-doc:: drivers/gpu/drm/i915/i915_gem_tiling.c
    :man-sect: 9
    :internal:


.. kernel-doc:: drivers/gpu/drm/i915/i915_gem_tiling.c
    :man-sect: 9
    :doc: buffer object tiling


Buffer Object Eviction
----------------------

This section documents the interface functions for evicting buffer
objects to make space available in the virtual gpu address spaces. Note
that this is mostly orthogonal to shrinking buffer objects caches, which
has the goal to make main memory (shared with the gpu through the
unified memory architecture) available.


.. kernel-doc:: drivers/gpu/drm/i915/i915_gem_evict.c
    :man-sect: 9
    :internal:


Buffer Object Memory Shrinking
------------------------------

This section documents the interface function for shrinking memory usage
of buffer object caches. Shrinking is used to make main memory
available. Note that this is mostly orthogonal to evicting buffer
objects, which has the goal to make space in gpu virtual address spaces.


.. kernel-doc:: drivers/gpu/drm/i915/i915_gem_shrinker.c
    :man-sect: 9
    :internal:


GuC
===


GuC-specific firmware loader
----------------------------


.. kernel-doc:: drivers/gpu/drm/i915/intel_guc_loader.c
    :man-sect: 9
    :doc: GuC-specific firmware loader


.. kernel-doc:: drivers/gpu/drm/i915/intel_guc_loader.c
    :man-sect: 9
    :internal:


GuC-based command submission
----------------------------


.. kernel-doc:: drivers/gpu/drm/i915/i915_guc_submission.c
    :man-sect: 9
    :doc: GuC-based command submission


.. kernel-doc:: drivers/gpu/drm/i915/i915_guc_submission.c
    :man-sect: 9
    :internal:


GuC Firmware Layout
-------------------


.. kernel-doc:: drivers/gpu/drm/i915/intel_guc_fwif.h
    :man-sect: 9
    :doc: GuC Firmware Layout


Tracing
=======

This sections covers all things related to the tracepoints implemented
in the i915 driver.


i915_ppgtt_create and i915_ppgtt_release
----------------------------------------


.. kernel-doc:: drivers/gpu/drm/i915/i915_trace.h
    :man-sect: 9
    :doc: i915_ppgtt_create and i915_ppgtt_release tracepoints


i915_context_create and i915_context_free
-----------------------------------------


.. kernel-doc:: drivers/gpu/drm/i915/i915_trace.h
    :man-sect: 9
    :doc: i915_context_create and i915_context_free tracepoints


switch_mm
---------


.. kernel-doc:: drivers/gpu/drm/i915/i915_trace.h
    :man-sect: 9
    :doc: switch_mm tracepoint




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
