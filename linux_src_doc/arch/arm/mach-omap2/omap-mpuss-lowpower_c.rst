.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/omap-mpuss-lowpower.c

.. _`cpu_pm_ops`:

struct cpu_pm_ops
=================

.. c:type:: struct cpu_pm_ops

    CPU pm operations

.. _`cpu_pm_ops.definition`:

Definition
----------

.. code-block:: c

    struct cpu_pm_ops {
        int (*finish_suspend)(unsigned long cpu_state);
        void (*resume)(void);
        void (*scu_prepare)(unsigned int cpu_id, unsigned int cpu_state);
        void (*hotplug_restart)(void);
    }

.. _`cpu_pm_ops.members`:

Members
-------

finish_suspend
    CPU suspend finisher function pointer

resume
    CPU resume function pointer

scu_prepare
    CPU Snoop Control program function pointer

hotplug_restart
    CPU restart function pointer

.. _`cpu_pm_ops.description`:

Description
-----------

Structure holds functions pointer for CPU low power operations like
suspend, resume and scu programming.

.. _`omap4_enter_lowpower`:

omap4_enter_lowpower
====================

.. c:function:: int omap4_enter_lowpower(unsigned int cpu, unsigned int power_state)

    OMAP4 MPUSS Low Power Entry Function The purpose of this function is to manage low power programming of OMAP4 MPUSS subsystem

    :param unsigned int cpu:
        CPU ID

    :param unsigned int power_state:
        Low power state.

.. _`omap4_enter_lowpower.mpuss-states-for-the-context-save`:

MPUSS states for the context save
---------------------------------

save_state =
0 - Nothing lost and no need to save: MPUSS INACTIVE
1 - CPUx L1 and logic lost: MPUSS CSWR
2 - CPUx L1 and logic lost + GIC lost: MPUSS OSWR
3 - CPUx L1 and logic lost + GIC + L2 lost: DEVICE OFF

.. _`omap4_hotplug_cpu`:

omap4_hotplug_cpu
=================

.. c:function:: int omap4_hotplug_cpu(unsigned int cpu, unsigned int power_state)

    OMAP4 CPU hotplug entry

    :param unsigned int cpu:
        CPU ID

    :param unsigned int power_state:
        CPU low power state.

.. This file was automatic generated / don't edit.

