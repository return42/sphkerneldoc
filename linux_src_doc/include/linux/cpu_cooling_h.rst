.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/cpu_cooling.h

.. _`cpufreq_cooling_register`:

cpufreq_cooling_register
========================

.. c:function:: struct thermal_cooling_device *cpufreq_cooling_register(struct cpufreq_policy *policy)

    function to create cpufreq cooling device.

    :param policy:
        cpufreq policy.
    :type policy: struct cpufreq_policy \*

.. _`cpufreq_cooling_unregister`:

cpufreq_cooling_unregister
==========================

.. c:function:: void cpufreq_cooling_unregister(struct thermal_cooling_device *cdev)

    function to remove cpufreq cooling device.

    :param cdev:
        thermal cooling device pointer.
    :type cdev: struct thermal_cooling_device \*

.. _`of_cpufreq_cooling_register`:

of_cpufreq_cooling_register
===========================

.. c:function:: struct thermal_cooling_device *of_cpufreq_cooling_register(struct cpufreq_policy *policy)

    create cpufreq cooling device based on DT.

    :param policy:
        cpufreq policy.
    :type policy: struct cpufreq_policy \*

.. This file was automatic generated / don't edit.

