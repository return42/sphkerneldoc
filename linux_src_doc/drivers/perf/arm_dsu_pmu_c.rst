.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/perf/arm_dsu_pmu.c

.. _`dsu_pmu_set_event_period`:

dsu_pmu_set_event_period
========================

.. c:function:: void dsu_pmu_set_event_period(struct perf_event *event)

    Set the period for the counter.

    :param event:
        *undescribed*
    :type event: struct perf_event \*

.. _`dsu_pmu_set_event_period.description`:

Description
-----------

All DSU PMU event counters, except the cycle counter are 32bit
counters. To handle cases of extreme interrupt latency, we program
the counter with half of the max count for the counters.

.. _`dsu_pmu_dt_get_cpus`:

dsu_pmu_dt_get_cpus
===================

.. c:function:: int dsu_pmu_dt_get_cpus(struct device_node *dev, cpumask_t *mask)

    Get the list of CPUs in the cluster.

    :param dev:
        *undescribed*
    :type dev: struct device_node \*

    :param mask:
        *undescribed*
    :type mask: cpumask_t \*

.. This file was automatic generated / don't edit.

