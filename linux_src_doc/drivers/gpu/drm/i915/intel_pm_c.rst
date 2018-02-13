.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_pm.c

.. _`rc6`:

RC6
===

RC6 is a special power stage which allows the GPU to enter an very
low-voltage mode when idle, using down to 0V while at this stage.  This
stage is entered automatically when the GPU is idle when RC6 support is
enabled, and as soon as new workload arises GPU wakes up automatically as well.

There are different RC6 modes available in Intel GPU, which differentiate
among each other with the latency required to enter and leave RC6 and
voltage consumed by the GPU in different states.

The combination of the following flags define which states GPU is allowed
to enter, while RC6 is the normal RC6 state, RC6p is the deep RC6, and
RC6pp is deepest RC6. Their support by hardware varies according to the
GPU, BIOS, chipset and platform. RC6 is usually the safest one and the one
which brings the most power savings; deeper states save more power, but
require higher latency to switch to and wake up.

.. _`intel_set_memory_cxsr`:

intel_set_memory_cxsr
=====================

.. c:function:: bool intel_set_memory_cxsr(struct drm_i915_private *dev_priv, bool enable)

    Configure CxSR state

    :param struct drm_i915_private \*dev_priv:
        i915 device

    :param bool enable:
        Allow vs. disallow CxSR

.. _`intel_set_memory_cxsr.description`:

Description
-----------

Allow or disallow the system to enter a special CxSR
(C-state self refresh) state. What typically happens in CxSR mode
is that several display FIFOs may get combined into a single larger
FIFO for a particular plane (so called max FIFO mode) to allow the
system to defer memory fetches longer, and the memory will enter
self refresh.

Note that enabling CxSR does not guarantee that the system enter
this special mode, nor does it guarantee that the system stays
in that mode once entered. So this just allows/disallows the system
to autonomously utilize the CxSR mode. Other factors such as core
C-states will affect when/if the system actually enters/exits the
CxSR mode.

Note that on VLV/CHV this actually only controls the max FIFO mode,
and the system is free to enter/exit memory self refresh at any time
even when the use of CxSR has been disallowed.

While the system is actually in the CxSR/max FIFO mode, some plane
control registers will not get latched on vblank. Thus in order to
guarantee the system will respond to changes in the plane registers
we must always disallow CxSR prior to making changes to those registers.
Unfortunately the system will re-evaluate the CxSR conditions at
frame start which happens after vblank start (which is when the plane
registers would get latched), so we can't proceed with the plane update
during the same frame where we disallowed CxSR.

Certain platforms also have a deeper HPLL SR mode. Fortunately the
HPLL SR mode depends on CxSR itself, so we don't have to hand hold
the hardware w.r.t. HPLL SR when writing to plane registers.
Disallowing just CxSR is sufficient.

.. _`intel_wm_method1`:

intel_wm_method1
================

.. c:function:: unsigned int intel_wm_method1(unsigned int pixel_rate, unsigned int cpp, unsigned int latency)

    Method 1 / "small buffer" watermark formula

    :param unsigned int pixel_rate:
        Pipe pixel rate in kHz

    :param unsigned int cpp:
        Plane bytes per pixel

    :param unsigned int latency:
        Memory wakeup latency in 0.1us units

.. _`intel_wm_method1.description`:

Description
-----------

Compute the watermark using the method 1 or "small buffer"
formula. The caller may additonally add extra cachelines
to account for TLB misses and clock crossings.

This method is concerned with the short term drain rate
of the FIFO, ie. it does not account for blanking periods
which would effectively reduce the average drain rate across
a longer period. The name "small" refers to the fact the
FIFO is relatively small compared to the amount of data
fetched.

The FIFO level vs. time graph might look something like:

\|\   \|\
\| \  \| \
\__---__---_\_ (- plane active, _ blanking)
-> time

.. _`intel_wm_method1.or-perhaps-like-this`:

or perhaps like this
--------------------


\|\\|\  \|\\|\
\__----__----_\_ (- plane active, _ blanking)
-> time

.. _`intel_wm_method1.return`:

Return
------

The watermark in bytes

.. _`intel_wm_method2`:

intel_wm_method2
================

.. c:function:: unsigned int intel_wm_method2(unsigned int pixel_rate, unsigned int htotal, unsigned int width, unsigned int cpp, unsigned int latency)

    Method 2 / "large buffer" watermark formula

    :param unsigned int pixel_rate:
        Pipe pixel rate in kHz

    :param unsigned int htotal:
        Pipe horizontal total

    :param unsigned int width:
        Plane width in pixels

    :param unsigned int cpp:
        Plane bytes per pixel

    :param unsigned int latency:
        Memory wakeup latency in 0.1us units

.. _`intel_wm_method2.description`:

Description
-----------

Compute the watermark using the method 2 or "large buffer"
formula. The caller may additonally add extra cachelines
to account for TLB misses and clock crossings.

This method is concerned with the long term drain rate
of the FIFO, ie. it does account for blanking periods
which effectively reduce the average drain rate across
a longer period. The name "large" refers to the fact the
FIFO is relatively large compared to the amount of data
fetched.

The FIFO level vs. time graph might look something like:

\|\__\_       \|\___
\|    \__\_   \|    \___
\|        \  \|        \
_\_ --__--__--__--__--__--_\_ (- plane active, _ blanking)
-> time

.. _`intel_wm_method2.return`:

Return
------

The watermark in bytes

.. _`intel_calculate_wm`:

intel_calculate_wm
==================

.. c:function:: unsigned int intel_calculate_wm(int pixel_rate, const struct intel_watermark_params *wm, int fifo_size, int cpp, unsigned int latency_ns)

    calculate watermark level

    :param int pixel_rate:
        pixel clock

    :param const struct intel_watermark_params \*wm:
        chip FIFO params

    :param int fifo_size:
        *undescribed*

    :param int cpp:
        bytes per pixel

    :param unsigned int latency_ns:
        memory latency for the platform

.. _`intel_calculate_wm.description`:

Description
-----------

Calculate the watermark level (the level at which the display plane will
start fetching from memory again).  Each chip has a different display
FIFO size and allocation, so the caller needs to figure that out and pass
in the correct intel_watermark_params structure.

As the pixel clock runs, the FIFO will be drained at a rate that depends
on the pixel size.  When it reaches the watermark level, it'll start
fetching FIFO line sized based chunks from memory until the FIFO fills
past the watermark point.  If the FIFO drains completely, a FIFO underrun
will occur, and a display engine hang could result.

.. _`intel_update_watermarks`:

intel_update_watermarks
=======================

.. c:function:: void intel_update_watermarks(struct intel_crtc *crtc)

    update FIFO watermark values based on current modes

    :param struct intel_crtc \*crtc:
        *undescribed*

.. _`intel_update_watermarks.description`:

Description
-----------

Calculate watermark values for the various WM regs based on current mode
and plane configuration.

.. _`intel_update_watermarks.there-are-several-cases-to-deal-with-here`:

There are several cases to deal with here
-----------------------------------------

- normal (i.e. non-self-refresh)
- self-refresh (SR) mode
- lines are large relative to FIFO size (buffer can hold up to 2)
- lines are small relative to FIFO size (buffer can hold more than 2
lines), so need to account for TLB latency

.. _`intel_update_watermarks.the-normal-calculation-is`:

The normal calculation is
-------------------------

watermark = dotclock \* bytes per pixel \* latency
where latency is platform & configuration dependent (we assume pessimal
values here).

.. _`intel_update_watermarks.the-sr-calculation-is`:

The SR calculation is
---------------------

watermark = (trunc(latency/line time)+1) \* surface width \*
bytes per pixel
where
line time = htotal / dotclock
surface width = hdisplay for normal plane and 64 for cursor
and latency is assumed to be high, as above.

The final value programmed to the register should always be rounded up,
and include an extra 2 entries to account for clock crossings.

We don't use the sprite, so we can ignore that.  And on Crestline we have
to set the non-SR watermarks to 8.

.. _`i915_read_mch_val`:

i915_read_mch_val
=================

.. c:function:: unsigned long i915_read_mch_val( void)

    return value for IPS use

    :param  void:
        no arguments

.. _`i915_read_mch_val.description`:

Description
-----------

Calculate and return a value for the IPS driver to use when deciding whether
we have thermal and power headroom to increase CPU or GPU power budget.

.. _`i915_gpu_raise`:

i915_gpu_raise
==============

.. c:function:: bool i915_gpu_raise( void)

    raise GPU frequency limit

    :param  void:
        no arguments

.. _`i915_gpu_raise.description`:

Description
-----------

Raise the limit; IPS indicates we have thermal headroom.

.. _`i915_gpu_lower`:

i915_gpu_lower
==============

.. c:function:: bool i915_gpu_lower( void)

    lower GPU frequency limit

    :param  void:
        no arguments

.. _`i915_gpu_lower.description`:

Description
-----------

IPS indicates we're close to a thermal limit, so throttle back the GPU
frequency maximum.

.. _`i915_gpu_busy`:

i915_gpu_busy
=============

.. c:function:: bool i915_gpu_busy( void)

    indicate GPU business to IPS

    :param  void:
        no arguments

.. _`i915_gpu_busy.description`:

Description
-----------

Tell the IPS driver whether or not the GPU is busy.

.. _`i915_gpu_turbo_disable`:

i915_gpu_turbo_disable
======================

.. c:function:: bool i915_gpu_turbo_disable( void)

    disable graphics turbo

    :param  void:
        no arguments

.. _`i915_gpu_turbo_disable.description`:

Description
-----------

Disable graphics turbo by resetting the max frequency and setting the
current frequency to the default.

.. _`ips_ping_for_i915_load`:

ips_ping_for_i915_load
======================

.. c:function:: void ips_ping_for_i915_load( void)

    IPS got loaded first.

    :param  void:
        no arguments

.. _`ips_ping_for_i915_load.description`:

Description
-----------

This awkward dance is so that neither module has to depend on the
other in order for IPS to do the appropriate communication of
GPU turbo limits to i915.

.. _`intel_suspend_gt_powersave`:

intel_suspend_gt_powersave
==========================

.. c:function:: void intel_suspend_gt_powersave(struct drm_i915_private *dev_priv)

    suspend PM work and helper threads

    :param struct drm_i915_private \*dev_priv:
        i915 device

.. _`intel_suspend_gt_powersave.description`:

Description
-----------

We don't want to disable RC6 or other features here, we just want
to make sure any work we've queued has finished and won't bother
us while we're suspended.

.. _`intel_init_clock_gating_hooks`:

intel_init_clock_gating_hooks
=============================

.. c:function:: void intel_init_clock_gating_hooks(struct drm_i915_private *dev_priv)

    setup the clock gating hooks

    :param struct drm_i915_private \*dev_priv:
        device private

.. _`intel_init_clock_gating_hooks.description`:

Description
-----------

Setup the hooks that configure which clocks of a given platform can be
gated and also apply various GT and display specific workarounds for these
platforms. Note that some GT specific workarounds are applied separately
when GPU contexts or batchbuffers start their execution.

.. _`skl_pcode_request`:

skl_pcode_request
=================

.. c:function:: int skl_pcode_request(struct drm_i915_private *dev_priv, u32 mbox, u32 request, u32 reply_mask, u32 reply, int timeout_base_ms)

    send PCODE request until acknowledgment

    :param struct drm_i915_private \*dev_priv:
        device private

    :param u32 mbox:
        PCODE mailbox ID the request is targeted for

    :param u32 request:
        request ID

    :param u32 reply_mask:
        mask used to check for request acknowledgment

    :param u32 reply:
        value used to check for request acknowledgment

    :param int timeout_base_ms:
        timeout for polling with preemption enabled

.. _`skl_pcode_request.description`:

Description
-----------

Keep resending the \ ``request``\  to \ ``mbox``\  until PCODE acknowledges it, PCODE
reports an error or an overall timeout of \ ``timeout_base_ms``\ +50 ms expires.
The request is acknowledged once the PCODE reply dword equals \ ``reply``\  after
applying \ ``reply_mask``\ . Polling is first attempted with preemption enabled
for \ ``timeout_base_ms``\  and if this times out for another 50 ms with
preemption disabled.

Returns 0 on success, \ ``-ETIMEDOUT``\  in case of a timeout, <0 in case of some
other error as reported by PCODE.

.. This file was automatic generated / don't edit.

