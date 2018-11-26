.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_drv.c

.. _`vramlimit--int-`:

vramlimit (int)
===============

Restrict the total amount of VRAM in MiB for testing.  The default is 0 (Use full VRAM).

.. _`vis_vramlimit--int-`:

vis_vramlimit (int)
===================

Restrict the amount of CPU visible VRAM in MiB for testing.  The default is 0 (Use full CPU visible VRAM).

.. _`gartsize--uint-`:

gartsize (uint)
===============

Restrict the size of GART in Mib (32, 64, etc.) for testing. The default is -1 (The size depends on asic).

.. _`gttsize--int-`:

gttsize (int)
=============

Restrict the size of GTT domain in MiB for testing. The default is -1 (It's VRAM size if 3GB < VRAM < 3/4 RAM,
otherwise 3/4 RAM size).

.. _`moverate--int-`:

moverate (int)
==============

Set maximum buffer migration rate in MB/s. The default is -1 (8 MB/s).

.. _`benchmark--int-`:

benchmark (int)
===============

Run benchmarks. The default is 0 (Skip benchmarks).

.. _`test--int-`:

test (int)
==========

Test BO GTT->VRAM and VRAM->GTT GPU copies. The default is 0 (Skip test, only set 1 to run test).

.. _`audio--int-`:

audio (int)
===========

Set HDMI/DPAudio. Only affects non-DC display handling. The default is -1 (Enabled), set 0 to disabled it.

.. _`disp_priority--int-`:

disp_priority (int)
===================

Set display Priority (1 = normal, 2 = high). Only affects non-DC display handling. The default is 0 (auto).

.. _`hw_i2c--int-`:

hw_i2c (int)
============

To enable hw i2c engine. Only affects non-DC display handling. The default is 0 (Disabled).

.. _`pcie_gen2--int-`:

pcie_gen2 (int)
===============

To disable PCIE Gen2/3 mode (0 = disable, 1 = enable). The default is -1 (auto, enabled).

.. _`msi--int-`:

msi (int)
=========

To disable Message Signaled Interrupts (MSI) functionality (1 = enable, 0 = disable). The default is -1 (auto, enabled).

.. _`lockup_timeout--int-`:

lockup_timeout (int)
====================

Set GPU scheduler timeout value in ms. Value 0 is invalidated, will be adjusted to 10000.
Negative values mean 'infinite timeout' (MAX_JIFFY_OFFSET). The default is 10000.

.. _`dpm--int-`:

dpm (int)
=========

Override for dynamic power management setting (1 = enable, 0 = disable). The default is -1 (auto).

.. _`fw_load_type--int-`:

fw_load_type (int)
==================

Set different firmware loading type for debugging (0 = direct, 1 = SMU, 2 = PSP). The default is -1 (auto).

.. _`aspm--int-`:

aspm (int)
==========

To disable ASPM (1 = enable, 0 = disable). The default is -1 (auto, enabled).

.. _`runpm--int-`:

runpm (int)
===========

Override for runtime power management control for dGPUs in PX/HG laptops. The amdgpu driver can dynamically power down
the dGPU on PX/HG laptops when it is idle. The default is -1 (auto enable). Setting the value to 0 disables this functionality.

.. _`ip_block_mask--uint-`:

ip_block_mask (uint)
====================

Override what IP blocks are enabled on the GPU. Each GPU is a collection of IP blocks (gfx, display, video, etc.).
Use this parameter to disable specific blocks. Note that the IP blocks do not have a fixed index. Some asics may not have
some IPs or may include multiple instances of an IP so the ordering various from asic to asic. See the driver output in
the kernel log for the list of IPs on the asic. The default is 0xffffffff (enable all blocks on a device).

.. _`bapm--int-`:

bapm (int)
==========

Bidirectional Application Power Management (BAPM) used to dynamically share TDP between CPU and GPU. Set value 0 to disable it.
The default -1 (auto, enabled)

.. _`deep_color--int-`:

deep_color (int)
================

Set 1 to enable Deep Color support. Only affects non-DC display handling. The default is 0 (disabled).

.. _`vm_size--int-`:

vm_size (int)
=============

Override the size of the GPU's per client virtual address space in GiB.  The default is -1 (automatic for each asic).

.. _`vm_fragment_size--int-`:

vm_fragment_size (int)
======================

Override VM fragment size in bits (4, 5, etc. 4 = 64K, 9 = 2M). The default is -1 (automatic for each asic).

.. _`vm_block_size--int-`:

vm_block_size (int)
===================

Override VM page table size in bits (default depending on vm_size and hw setup). The default is -1 (automatic for each asic).

.. _`vm_fault_stop--int-`:

vm_fault_stop (int)
===================

Stop on VM fault for debugging (0 = never, 1 = print first, 2 = always). The default is 0 (No stop).

.. _`vm_debug--int-`:

vm_debug (int)
==============

Debug VM handling (0 = disabled, 1 = enabled). The default is 0 (Disabled).

.. _`vm_update_mode--int-`:

vm_update_mode (int)
====================

Override VM update mode. VM updated by using CPU (0 = never, 1 = Graphics only, 2 = Compute only, 3 = Both). The default
is -1 (Only in large BAR(LB) systems Compute VM tables will be updated by CPU, otherwise 0, never).

.. _`vram_page_split--int-`:

vram_page_split (int)
=====================

Override the number of pages after we split VRAM allocations (default 512, -1 = disable). The default is 512.

.. _`exp_hw_support--int-`:

exp_hw_support (int)
====================

Enable experimental hw support (1 = enable). The default is 0 (disabled).

.. _`dc--int-`:

dc (int)
========

Disable/Enable Display Core driver for debugging (1 = enable, 0 = disable). The default is -1 (automatic for each asic).

.. _`sched_jobs--int-`:

sched_jobs (int)
================

Override the max number of jobs supported in the sw queue. The default is 32.

.. _`sched_hw_submission--int-`:

sched_hw_submission (int)
=========================

Override the max number of HW submissions. The default is 2.

.. _`ppfeaturemask--uint-`:

ppfeaturemask (uint)
====================

Override power features enabled. See enum PP_FEATURE_MASK in drivers/gpu/drm/amd/include/amd_shared.h.
The default is the current set of stable power features.

.. _`pcie_gen_cap--uint-`:

pcie_gen_cap (uint)
===================

Override PCIE gen speed capabilities. See the CAIL flags in drivers/gpu/drm/amd/include/amd_pcie.h.
The default is 0 (automatic for each asic).

.. _`pcie_lane_cap--uint-`:

pcie_lane_cap (uint)
====================

Override PCIE lanes capabilities. See the CAIL flags in drivers/gpu/drm/amd/include/amd_pcie.h.
The default is 0 (automatic for each asic).

.. _`cg_mask--uint-`:

cg_mask (uint)
==============

Override Clockgating features enabled on GPU (0 = disable clock gating). See the AMD_CG_SUPPORT flags in
drivers/gpu/drm/amd/include/amd_shared.h. The default is 0xffffffff (all enabled).

.. _`pg_mask--uint-`:

pg_mask (uint)
==============

Override Powergating features enabled on GPU (0 = disable power gating). See the AMD_PG_SUPPORT flags in
drivers/gpu/drm/amd/include/amd_shared.h. The default is 0xffffffff (all enabled).

.. _`sdma_phase_quantum--uint-`:

sdma_phase_quantum (uint)
=========================

Override SDMA context switch phase quantum (x 1K GPU clock cycles, 0 = no change). The default is 32.

.. _`disable_cu--charp-`:

disable_cu (charp)
==================

Set to disable CUs (It's set like se.sh.cu,...). The default is NULL.

.. _`virtual_display--charp-`:

virtual_display (charp)
=======================

Set to enable virtual display feature. This feature provides a virtual display hardware on headless boards
or in virtualized environments. It will be set like xxxx:xx:xx.x,x;xxxx:xx:xx.x,x. It's the pci address of
the device, plus the number of crtcs to expose. E.g., 0000:26:00.0,4 would enable 4 virtual crtcs on the pci
device at 26:00.0. The default is NULL.

.. _`ngg--int-`:

ngg (int)
=========

Set to enable Next Generation Graphics (1 = enable). The default is 0 (disabled).

.. _`prim_buf_per_se--int-`:

prim_buf_per_se (int)
=====================

Override the size of Primitive Buffer per Shader Engine in Byte. The default is 0 (depending on gfx).

.. _`pos_buf_per_se--int-`:

pos_buf_per_se (int)
====================

Override the size of Position Buffer per Shader Engine in Byte. The default is 0 (depending on gfx).

.. _`cntl_sb_buf_per_se--int-`:

cntl_sb_buf_per_se (int)
========================

Override the size of Control Sideband per Shader Engine in Byte. The default is 0 (depending on gfx).

.. _`param_buf_per_se--int-`:

param_buf_per_se (int)
======================

Override the size of Off-Chip Pramater Cache per Shader Engine in Byte. The default is 0 (depending on gfx).

.. _`job_hang_limit--int-`:

job_hang_limit (int)
====================

Set how much time allow a job hang and not drop it. The default is 0.

.. _`lbpw--int-`:

lbpw (int)
==========

Override Load Balancing Per Watt (LBPW) support (1 = enable, 0 = disable). The default is -1 (auto, enabled).

.. _`gpu_recovery--int-`:

gpu_recovery (int)
==================

Set to enable GPU recovery mechanism (1 = enable, 0 = disable). The default is -1 (auto, disabled except SRIOV).

.. _`emu_mode--int-`:

emu_mode (int)
==============

Set value 1 to enable emulation mode. This is only needed when running on an emulator. The default is 0 (disabled).

.. _`si_support--int-`:

si_support (int)
================

Set SI support driver. This parameter works after set config CONFIG_DRM_AMDGPU_SI. For SI asic, when radeon driver is enabled,
set value 0 to use radeon driver, while set value 1 to use amdgpu driver. The default is using radeon driver when it available,
otherwise using amdgpu driver.

.. _`cik_support--int-`:

cik_support (int)
=================

Set CIK support driver. This parameter works after set config CONFIG_DRM_AMDGPU_CIK. For CIK asic, when radeon driver is enabled,
set value 0 to use radeon driver, while set value 1 to use amdgpu driver. The default is using radeon driver when it available,
otherwise using amdgpu driver.

.. _`smu_memory_pool_size--uint-`:

smu_memory_pool_size (uint)
===========================

It is used to reserve gtt for smu debug usage, setting value 0 to disable it. The actual size is value * 256MiB.
E.g. 0x1 = 256Mbyte, 0x2 = 512Mbyte, 0x4 = 1 Gbyte, 0x8 = 2GByte. The default is 0 (disabled).

.. _`sched_policy--int-`:

sched_policy (int)
==================

Set scheduling policy. Default is HWS(hardware scheduling) with over-subscription.
Setting 1 disables over-subscription. Setting 2 disables HWS and statically
assigns queues to HQDs.

.. _`hws_max_conc_proc--int-`:

hws_max_conc_proc (int)
=======================

Maximum number of processes that HWS can schedule concurrently. The maximum is the
number of VMIDs assigned to the HWS, which is also the default.

.. _`cwsr_enable--int-`:

cwsr_enable (int)
=================

CWSR(compute wave store and resume) allows the GPU to preempt shader execution in
the middle of a compute wave. Default is 1 to enable this feature. Setting 0
disables it.

.. _`max_num_of_queues_per_device--int-`:

max_num_of_queues_per_device (int)
==================================

Maximum number of queues per device. Valid setting is between 1 and 4096. Default
is 4096.

.. _`send_sigterm--int-`:

send_sigterm (int)
==================

Send sigterm to HSA process on unhandled exceptions. Default is not to send sigterm
but just print errors on dmesg. Setting 1 enables sending sigterm.

.. _`debug_largebar--int-`:

debug_largebar (int)
====================

Set debug_largebar as 1 to enable simulating large-bar capability on non-large bar
system. This limits the VRAM size reported to ROCm applications to the visible
size, usually 256MB.
Default value is 0, diabled.

.. _`ignore_crat--int-`:

ignore_crat (int)
=================

Ignore CRAT table during KFD initialization. By default, KFD uses the ACPI CRAT
table to get information about AMD APUs. This option can serve as a workaround on
systems with a broken CRAT table.

.. _`noretry--int-`:

noretry (int)
=============

This parameter sets sh_mem_config.retry_disable. Default value, 0, enables retry.
Setting 1 disables retry.
Retry is needed for recoverable page faults.

.. _`halt_if_hws_hang--int-`:

halt_if_hws_hang (int)
======================

Halt if HWS hang is detected. Default value, 0, disables the halt on hang.
Setting 1 enables halt on hang.

.. _`dcfeaturemask--uint-`:

dcfeaturemask (uint)
====================

Override display features enabled. See enum DC_FEATURE_MASK in drivers/gpu/drm/amd/include/amd_shared.h.
The default is the current set of stable display features.

.. This file was automatic generated / don't edit.

