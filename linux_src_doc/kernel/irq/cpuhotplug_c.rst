.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/cpuhotplug.c

.. _`irq_migrate_all_off_this_cpu`:

irq_migrate_all_off_this_cpu
============================

.. c:function:: void irq_migrate_all_off_this_cpu( void)

    Migrate irqs away from offline cpu

    :param  void:
        no arguments

.. _`irq_migrate_all_off_this_cpu.description`:

Description
-----------

The current CPU has been marked offline.  Migrate IRQs off this CPU.
If the affinity settings do not allow other CPUs, force them onto any
available CPU.

.. _`irq_migrate_all_off_this_cpu.note`:

Note
----

we must iterate over all IRQs, whether they have an attached
action structure or not, as we need to get chained interrupts too.

.. This file was automatic generated / don't edit.
