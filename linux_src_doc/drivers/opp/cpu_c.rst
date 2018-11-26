.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/opp/cpu.c

.. _`dev_pm_opp_init_cpufreq_table`:

dev_pm_opp_init_cpufreq_table
=============================

.. c:function:: int dev_pm_opp_init_cpufreq_table(struct device *dev, struct cpufreq_frequency_table **table)

    create a cpufreq table for a device

    :param dev:
        device for which we do this operation
    :type dev: struct device \*

    :param table:
        Cpufreq table returned back to caller
    :type table: struct cpufreq_frequency_table \*\*

.. _`dev_pm_opp_init_cpufreq_table.description`:

Description
-----------

Generate a cpufreq table for a provided device- this assumes that the
opp table is already initialized and ready for usage.

This function allocates required memory for the cpufreq table. It is
expected that the caller does the required maintenance such as freeing
the table as required.

Returns -EINVAL for bad pointers, -ENODEV if the device is not found, -ENOMEM
if no memory available for the operation (table is not populated), returns 0
if successful and table is populated.

.. _`dev_pm_opp_init_cpufreq_table.warning`:

WARNING
-------

It is  important for the callers to ensure refreshing their copy of
the table if any of the mentioned functions have been invoked in the interim.

.. _`dev_pm_opp_free_cpufreq_table`:

dev_pm_opp_free_cpufreq_table
=============================

.. c:function:: void dev_pm_opp_free_cpufreq_table(struct device *dev, struct cpufreq_frequency_table **table)

    free the cpufreq table

    :param dev:
        device for which we do this operation
    :type dev: struct device \*

    :param table:
        table to free
    :type table: struct cpufreq_frequency_table \*\*

.. _`dev_pm_opp_free_cpufreq_table.description`:

Description
-----------

Free up the table allocated by dev_pm_opp_init_cpufreq_table

.. _`dev_pm_opp_cpumask_remove_table`:

dev_pm_opp_cpumask_remove_table
===============================

.. c:function:: void dev_pm_opp_cpumask_remove_table(const struct cpumask *cpumask)

    Removes OPP table for \ ``cpumask``\ 

    :param cpumask:
        cpumask for which OPP table needs to be removed
    :type cpumask: const struct cpumask \*

.. _`dev_pm_opp_cpumask_remove_table.description`:

Description
-----------

This removes the OPP tables for CPUs present in the \ ``cpumask``\ .
This should be used to remove all the OPPs entries associated with
the cpus in \ ``cpumask``\ .

.. _`dev_pm_opp_set_sharing_cpus`:

dev_pm_opp_set_sharing_cpus
===========================

.. c:function:: int dev_pm_opp_set_sharing_cpus(struct device *cpu_dev, const struct cpumask *cpumask)

    Mark OPP table as shared by few CPUs

    :param cpu_dev:
        CPU device for which we do this operation
    :type cpu_dev: struct device \*

    :param cpumask:
        cpumask of the CPUs which share the OPP table with \ ``cpu_dev``\ 
    :type cpumask: const struct cpumask \*

.. _`dev_pm_opp_set_sharing_cpus.description`:

Description
-----------

This marks OPP table of the \ ``cpu_dev``\  as shared by the CPUs present in
\ ``cpumask``\ .

Returns -ENODEV if OPP table isn't already present.

.. _`dev_pm_opp_get_sharing_cpus`:

dev_pm_opp_get_sharing_cpus
===========================

.. c:function:: int dev_pm_opp_get_sharing_cpus(struct device *cpu_dev, struct cpumask *cpumask)

    Get cpumask of CPUs sharing OPPs with \ ``cpu_dev``\ 

    :param cpu_dev:
        CPU device for which we do this operation
    :type cpu_dev: struct device \*

    :param cpumask:
        cpumask to update with information of sharing CPUs
    :type cpumask: struct cpumask \*

.. _`dev_pm_opp_get_sharing_cpus.description`:

Description
-----------

This updates the \ ``cpumask``\  with CPUs that are sharing OPPs with \ ``cpu_dev``\ .

Returns -ENODEV if OPP table isn't already present and -EINVAL if the OPP
table's status is access-unknown.

.. This file was automatic generated / don't edit.

