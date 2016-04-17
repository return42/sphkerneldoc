.. -*- coding: utf-8; mode: rst -*-

=============
qcom_scm-64.c
=============


.. _`__qcom_scm_set_cold_boot_addr`:

__qcom_scm_set_cold_boot_addr
=============================

.. c:function:: int __qcom_scm_set_cold_boot_addr (void *entry, const cpumask_t *cpus)

    Set the cold boot address for cpus

    :param void \*entry:
        Entry point function for the cpus

    :param const cpumask_t \*cpus:
        The cpumask of cpus that will use the entry point



.. _`__qcom_scm_set_cold_boot_addr.description`:

Description
-----------

Set the cold boot address of the cpus. Any cpu outside the supported
range would be removed from the cpu present mask.



.. _`__qcom_scm_set_warm_boot_addr`:

__qcom_scm_set_warm_boot_addr
=============================

.. c:function:: int __qcom_scm_set_warm_boot_addr (void *entry, const cpumask_t *cpus)

    Set the warm boot address for cpus

    :param void \*entry:
        Entry point function for the cpus

    :param const cpumask_t \*cpus:
        The cpumask of cpus that will use the entry point



.. _`__qcom_scm_set_warm_boot_addr.description`:

Description
-----------

Set the Linux entry point for the SCM to transfer control to when coming
out of a power down. CPU power down may be executed on cpuidle or hotplug.



.. _`__qcom_scm_cpu_power_down`:

__qcom_scm_cpu_power_down
=========================

.. c:function:: void __qcom_scm_cpu_power_down (u32 flags)

    Power down the cpu @flags - Flags to flush cache

    :param u32 flags:

        *undescribed*



.. _`__qcom_scm_cpu_power_down.description`:

Description
-----------


This is an end point to power down cpu. If there was a pending interrupt,
the control would return from this function, otherwise, the cpu jumps to the
warm boot entry point set for this cpu upon reset.

