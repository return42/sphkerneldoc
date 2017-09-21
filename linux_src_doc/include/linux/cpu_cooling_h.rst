.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/cpu_cooling.h

.. _`cpufreq_cooling_register`:

cpufreq_cooling_register
========================

.. c:function:: struct thermal_cooling_device *cpufreq_cooling_register(struct cpufreq_policy *policy)

    function to create cpufreq cooling device.

    :param struct cpufreq_policy \*policy:
        cpufreq policy.

.. _`of_cpufreq_cooling_register`:

of_cpufreq_cooling_register
===========================

.. c:function:: struct thermal_cooling_device *of_cpufreq_cooling_register(struct device_node *np, struct cpufreq_policy *policy)

    create cpufreq cooling device based on DT.

    :param struct device_node \*np:
        a valid struct device_node to the cooling device device tree node.

    :param struct cpufreq_policy \*policy:
        cpufreq policy.

.. _`cpufreq_cooling_unregister`:

cpufreq_cooling_unregister
==========================

.. c:function:: void cpufreq_cooling_unregister(struct thermal_cooling_device *cdev)

    function to remove cpufreq cooling device.

    :param struct thermal_cooling_device \*cdev:
        thermal cooling device pointer.

.. This file was automatic generated / don't edit.

