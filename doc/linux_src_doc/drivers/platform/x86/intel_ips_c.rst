.. -*- coding: utf-8; mode: rst -*-

===========
intel_ips.c
===========


.. _`ips_cpu_busy`:

ips_cpu_busy
============

.. c:function:: bool ips_cpu_busy (struct ips_driver *ips)

    is CPU busy?

    :param struct ips_driver \*ips:
        IPS driver struct



.. _`ips_cpu_busy.description`:

Description
-----------

Check CPU for load to see whether we should increase its thermal budget.



.. _`ips_cpu_busy.returns`:

RETURNS
-------

True if the CPU could use more power, false otherwise.



.. _`ips_cpu_raise`:

ips_cpu_raise
=============

.. c:function:: void ips_cpu_raise (struct ips_driver *ips)

    raise CPU power clamp

    :param struct ips_driver \*ips:
        IPS driver struct



.. _`ips_cpu_raise.description`:

Description
-----------

Raise the CPU power clamp by ``IPS_CPU_STEP``\ , in accordance with TDP for
this platform.

We do this by adjusting the TURBO_POWER_CURRENT_LIMIT MSR upwards (as
long as we haven't hit the TDP limit for the SKU).



.. _`ips_cpu_lower`:

ips_cpu_lower
=============

.. c:function:: void ips_cpu_lower (struct ips_driver *ips)

    lower CPU power clamp

    :param struct ips_driver \*ips:
        IPS driver struct



.. _`ips_cpu_lower.description`:

Description
-----------

Lower CPU power clamp b ``IPS_CPU_STEP`` if possible.

We do this by adjusting the TURBO_POWER_CURRENT_LIMIT MSR down, going
as low as the platform limits will allow (though we could go lower there
wouldn't be much point).



.. _`do_enable_cpu_turbo`:

do_enable_cpu_turbo
===================

.. c:function:: void do_enable_cpu_turbo (void *data)

    internal turbo enable function

    :param void \*data:
        unused



.. _`do_enable_cpu_turbo.description`:

Description
-----------

Internal function for actually updating MSRs.  When we enable/disable
turbo, we need to do it on each CPU; this function is the one called
by :c:func:`on_each_cpu` when needed.



.. _`ips_enable_cpu_turbo`:

ips_enable_cpu_turbo
====================

.. c:function:: void ips_enable_cpu_turbo (struct ips_driver *ips)

    enable turbo mode on all CPUs

    :param struct ips_driver \*ips:
        IPS driver struct



.. _`ips_enable_cpu_turbo.description`:

Description
-----------

Enable turbo mode by clearing the disable bit in IA32_PERF_CTL on
all logical threads.



.. _`do_disable_cpu_turbo`:

do_disable_cpu_turbo
====================

.. c:function:: void do_disable_cpu_turbo (void *data)

    internal turbo disable function

    :param void \*data:
        unused



.. _`do_disable_cpu_turbo.description`:

Description
-----------

Internal function for actually updating MSRs.  When we enable/disable
turbo, we need to do it on each CPU; this function is the one called
by :c:func:`on_each_cpu` when needed.



.. _`ips_disable_cpu_turbo`:

ips_disable_cpu_turbo
=====================

.. c:function:: void ips_disable_cpu_turbo (struct ips_driver *ips)

    disable turbo mode on all CPUs

    :param struct ips_driver \*ips:
        IPS driver struct



.. _`ips_disable_cpu_turbo.description`:

Description
-----------

Disable turbo mode by setting the disable bit in IA32_PERF_CTL on
all logical threads.



.. _`ips_gpu_busy`:

ips_gpu_busy
============

.. c:function:: bool ips_gpu_busy (struct ips_driver *ips)

    is GPU busy?

    :param struct ips_driver \*ips:
        IPS driver struct



.. _`ips_gpu_busy.description`:

Description
-----------

Check GPU for load to see whether we should increase its thermal budget.
We need to call into the i915 driver in this case.



.. _`ips_gpu_busy.returns`:

RETURNS
-------

True if the GPU could use more power, false otherwise.



.. _`ips_gpu_raise`:

ips_gpu_raise
=============

.. c:function:: void ips_gpu_raise (struct ips_driver *ips)

    raise GPU power clamp

    :param struct ips_driver \*ips:
        IPS driver struct



.. _`ips_gpu_raise.description`:

Description
-----------

Raise the GPU frequency/power if possible.  We need to call into the
i915 driver in this case.



.. _`ips_gpu_lower`:

ips_gpu_lower
=============

.. c:function:: void ips_gpu_lower (struct ips_driver *ips)

    lower GPU power clamp

    :param struct ips_driver \*ips:
        IPS driver struct



.. _`ips_gpu_lower.description`:

Description
-----------

Lower GPU frequency/power if possible.  Need to call i915.



.. _`ips_enable_gpu_turbo`:

ips_enable_gpu_turbo
====================

.. c:function:: void ips_enable_gpu_turbo (struct ips_driver *ips)

    notify the gfx driver turbo is available

    :param struct ips_driver \*ips:
        IPS driver struct



.. _`ips_enable_gpu_turbo.description`:

Description
-----------

Call into the graphics driver indicating that it can safely use
turbo mode.



.. _`ips_disable_gpu_turbo`:

ips_disable_gpu_turbo
=====================

.. c:function:: void ips_disable_gpu_turbo (struct ips_driver *ips)

    notify the gfx driver to disable turbo mode

    :param struct ips_driver \*ips:
        IPS driver struct



.. _`ips_disable_gpu_turbo.description`:

Description
-----------

Request that the graphics driver disable turbo mode.



.. _`mcp_exceeded`:

mcp_exceeded
============

.. c:function:: bool mcp_exceeded (struct ips_driver *ips)

    check whether we're outside our thermal & power limits

    :param struct ips_driver \*ips:
        IPS driver struct



.. _`mcp_exceeded.description`:

Description
-----------

Check whether the MCP is over its thermal or power budget.



.. _`cpu_exceeded`:

cpu_exceeded
============

.. c:function:: bool cpu_exceeded (struct ips_driver *ips, int cpu)

    check whether a CPU core is outside its limits

    :param struct ips_driver \*ips:
        IPS driver struct

    :param int cpu:
        CPU number to check



.. _`cpu_exceeded.description`:

Description
-----------

Check a given CPU's average temp or power is over its limit.



.. _`mch_exceeded`:

mch_exceeded
============

.. c:function:: bool mch_exceeded (struct ips_driver *ips)

    check whether the GPU is over budget

    :param struct ips_driver \*ips:
        IPS driver struct



.. _`mch_exceeded.description`:

Description
-----------

Check the MCH temp & power against their maximums.



.. _`verify_limits`:

verify_limits
=============

.. c:function:: void verify_limits (struct ips_driver *ips)

    verify BIOS provided limits

    :param struct ips_driver \*ips:
        IPS structure



.. _`verify_limits.description`:

Description
-----------

BIOS can optionally provide non-default limits for power and temp.  Check
them here and use the defaults if the BIOS values are not provided or
are otherwise unusable.



.. _`update_turbo_limits`:

update_turbo_limits
===================

.. c:function:: void update_turbo_limits (struct ips_driver *ips)

    get various limits & settings from regs

    :param struct ips_driver \*ips:
        IPS driver struct



.. _`update_turbo_limits.description`:

Description
-----------

Update the IPS power & temp limits, along with turbo enable flags,
based on latest register contents.

Used at init time and for runtime BIOS support, which requires polling
the regs for updates (as a result of AC->DC transition for example).



.. _`update_turbo_limits.locking`:

LOCKING
-------

Caller must hold turbo_status_lock (outside of init)



.. _`ips_adjust`:

ips_adjust
==========

.. c:function:: int ips_adjust (void *data)

    adjust power clamp based on thermal state

    :param void \*data:
        ips driver structure



.. _`ips_adjust.description`:

Description
-----------

Wake up every 5s or so and check whether we should adjust the power clamp.
Check CPU and GPU load to determine which needs adjustment.  There are



.. _`ips_adjust.several-things-to-consider-here`:

several things to consider here
-------------------------------

- do we need to adjust up or down?
- is CPU busy?
- is GPU busy?
- is CPU in turbo?
- is GPU in turbo?
- is CPU or GPU preferred? (CPU is default)

So, given the above, we do the following:
- up (TDP available)

  - CPU not busy, GPU not busy - nothing
  - CPU busy, GPU not busy - adjust CPU up
  - CPU not busy, GPU busy - adjust GPU up
  - CPU busy, GPU busy - adjust preferred unit up, taking headroom from
    non-preferred unit if necessary

- down (at TDP limit)

  - adjust both CPU and GPU down if possible



.. _`ips_monitor`:

ips_monitor
===========

.. c:function:: int ips_monitor (void *data)

    temp/power monitoring thread

    :param void \*data:
        ips driver structure



.. _`ips_monitor.description`:

Description
-----------

This is the main function for the IPS driver.  It monitors power and
tempurature in the MCP and adjusts CPU and GPU power clams accordingly.

We keep a 5s moving average of power consumption and tempurature.  Using
that data, along with CPU vs GPU preference, we adjust the power clamps
up or down.



.. _`ips_irq_handler`:

ips_irq_handler
===============

.. c:function:: irqreturn_t ips_irq_handler (int irq, void *arg)

    handle temperature triggers and other IPS events

    :param int irq:
        irq number

    :param void \*arg:
        unused



.. _`ips_irq_handler.description`:

Description
-----------

Handle temperature limit trigger events, generally by lowering the clamps.
If we're at a critical limit, we clamp back to the lowest possible value
to prevent emergency shutdown.



.. _`ips_detect_cpu`:

ips_detect_cpu
==============

.. c:function:: struct ips_mcp_limits *ips_detect_cpu (struct ips_driver *ips)

    detect whether CPU supports IPS

    :param struct ips_driver \*ips:

        *undescribed*



.. _`ips_detect_cpu.description`:

Description
-----------


Walk our list and see if we're on a supported CPU.  If we find one,
return the limits for it.



.. _`ips_get_i915_syms`:

ips_get_i915_syms
=================

.. c:function:: bool ips_get_i915_syms (struct ips_driver *ips)

    try to get GPU control methods from i915 driver

    :param struct ips_driver \*ips:
        IPS driver



.. _`ips_get_i915_syms.description`:

Description
-----------

The i915 driver exports several interfaces to allow the IPS driver to
monitor and control graphics turbo mode.  If we can find them, we can
enable graphics turbo, otherwise we must disable it to avoid exceeding
thermal and power limits in the MCP.

