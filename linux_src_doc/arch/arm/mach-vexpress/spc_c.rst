.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-vexpress/spc.c

.. _`ve_spc_global_wakeup_irq`:

ve_spc_global_wakeup_irq
========================

.. c:function:: void ve_spc_global_wakeup_irq(bool set)

    :param set:
        if true, global wake-up IRQs are set, if false they are cleared
    :type set: bool

.. _`ve_spc_global_wakeup_irq.description`:

Description
-----------

Function to set/clear global wakeup IRQs. Not protected by locking since
it might be used in code paths where normal cacheable locks are not
working. Locking must be provided by the caller to ensure atomicity.

.. _`ve_spc_cpu_wakeup_irq`:

ve_spc_cpu_wakeup_irq
=====================

.. c:function:: void ve_spc_cpu_wakeup_irq(u32 cluster, u32 cpu, bool set)

    :param cluster:
        mpidr[15:8] bitfield describing cluster affinity level
    :type cluster: u32

    :param cpu:
        mpidr[7:0] bitfield describing cpu affinity level
    :type cpu: u32

    :param set:
        if true, wake-up IRQs are set, if false they are cleared
    :type set: bool

.. _`ve_spc_cpu_wakeup_irq.description`:

Description
-----------

Function to set/clear per-CPU wake-up IRQs. Not protected by locking since
it might be used in code paths where normal cacheable locks are not
working. Locking must be provided by the caller to ensure atomicity.

.. _`ve_spc_set_resume_addr`:

ve_spc_set_resume_addr
======================

.. c:function:: void ve_spc_set_resume_addr(u32 cluster, u32 cpu, u32 addr)

    set the jump address used for warm boot

    :param cluster:
        mpidr[15:8] bitfield describing cluster affinity level
    :type cluster: u32

    :param cpu:
        mpidr[7:0] bitfield describing cpu affinity level
    :type cpu: u32

    :param addr:
        physical resume address
    :type addr: u32

.. _`ve_spc_powerdown`:

ve_spc_powerdown
================

.. c:function:: void ve_spc_powerdown(u32 cluster, bool enable)

    :param cluster:
        mpidr[15:8] bitfield describing cluster affinity level
    :type cluster: u32

    :param enable:
        if true enables powerdown, if false disables it
    :type enable: bool

.. _`ve_spc_powerdown.description`:

Description
-----------

Function to enable/disable cluster powerdown. Not protected by locking
since it might be used in code paths where normal cacheable locks are not
working. Locking must be provided by the caller to ensure atomicity.

.. _`ve_spc_cpu_in_wfi`:

ve_spc_cpu_in_wfi
=================

.. c:function:: int ve_spc_cpu_in_wfi(u32 cpu, u32 cluster)

    :param cpu:
        mpidr[7:0] bitfield describing CPU affinity level within cluster
    :type cpu: u32

    :param cluster:
        mpidr[15:8] bitfield describing cluster affinity level
    :type cluster: u32

.. _`ve_spc_cpu_in_wfi.take-care-when-interpreting-the-result-of-this-function`:

Take care when interpreting the result of this function
-------------------------------------------------------

a CPU might
be in WFI temporarily due to idle, and is not necessarily safely
parked.

.. This file was automatic generated / don't edit.

