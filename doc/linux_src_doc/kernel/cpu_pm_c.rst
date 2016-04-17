.. -*- coding: utf-8; mode: rst -*-

========
cpu_pm.c
========


.. _`cpu_pm_register_notifier`:

cpu_pm_register_notifier
========================

.. c:function:: int cpu_pm_register_notifier (struct notifier_block *nb)

    register a driver with cpu_pm

    :param struct notifier_block \*nb:
        notifier block to register



.. _`cpu_pm_register_notifier.description`:

Description
-----------

Add a driver to a list of drivers that are notified about
CPU and CPU cluster low power entry and exit.

This function may sleep, and has the same return conditions as
raw_notifier_chain_register.



.. _`cpu_pm_unregister_notifier`:

cpu_pm_unregister_notifier
==========================

.. c:function:: int cpu_pm_unregister_notifier (struct notifier_block *nb)

    unregister a driver with cpu_pm

    :param struct notifier_block \*nb:
        notifier block to be unregistered



.. _`cpu_pm_unregister_notifier.description`:

Description
-----------

Remove a driver from the CPU PM notifier list.

This function may sleep, and has the same return conditions as
raw_notifier_chain_unregister.



.. _`cpu_pm_enter`:

cpu_pm_enter
============

.. c:function:: int cpu_pm_enter ( void)

    CPU low power entry notifier

    :param void:
        no arguments



.. _`cpu_pm_enter.description`:

Description
-----------


Notifies listeners that a single CPU is entering a low power state that may
cause some blocks in the same power domain as the cpu to reset.

Must be called on the affected CPU with interrupts disabled.  Platform is
responsible for ensuring that cpu_pm_enter is not called twice on the same
CPU before cpu_pm_exit is called. Notified drivers can include VFP
co-processor, interrupt controller and its PM extensions, local CPU
timers context save/restore which shouldn't be interrupted. Hence it
must be called with interrupts disabled.

Return conditions are same as __raw_notifier_call_chain.



.. _`cpu_pm_exit`:

cpu_pm_exit
===========

.. c:function:: int cpu_pm_exit ( void)

    CPU low power exit notifier

    :param void:
        no arguments



.. _`cpu_pm_exit.description`:

Description
-----------


Notifies listeners that a single CPU is exiting a low power state that may
have caused some blocks in the same power domain as the cpu to reset.

Notified drivers can include VFP co-processor, interrupt controller
and its PM extensions, local CPU timers context save/restore which
shouldn't be interrupted. Hence it must be called with interrupts disabled.

Return conditions are same as __raw_notifier_call_chain.



.. _`cpu_cluster_pm_enter`:

cpu_cluster_pm_enter
====================

.. c:function:: int cpu_cluster_pm_enter ( void)

    CPU cluster low power entry notifier

    :param void:
        no arguments



.. _`cpu_cluster_pm_enter.description`:

Description
-----------


Notifies listeners that all cpus in a power domain are entering a low power
state that may cause some blocks in the same power domain to reset.

Must be called after cpu_pm_enter has been called on all cpus in the power
domain, and before cpu_pm_exit has been called on any cpu in the power
domain. Notified drivers can include VFP co-processor, interrupt controller
and its PM extensions, local CPU timers context save/restore which
shouldn't be interrupted. Hence it must be called with interrupts disabled.

Must be called with interrupts disabled.

Return conditions are same as __raw_notifier_call_chain.



.. _`cpu_cluster_pm_exit`:

cpu_cluster_pm_exit
===================

.. c:function:: int cpu_cluster_pm_exit ( void)

    CPU cluster low power exit notifier

    :param void:
        no arguments



.. _`cpu_cluster_pm_exit.description`:

Description
-----------


Notifies listeners that all cpus in a power domain are exiting form a
low power state that may have caused some blocks in the same power domain
to reset.

Must be called after cpu_cluster_pm_enter has been called for the power
domain, and before cpu_pm_exit has been called on any cpu in the power
domain. Notified drivers can include VFP co-processor, interrupt controller
and its PM extensions, local CPU timers context save/restore which
shouldn't be interrupted. Hence it must be called with interrupts disabled.

Return conditions are same as __raw_notifier_call_chain.

