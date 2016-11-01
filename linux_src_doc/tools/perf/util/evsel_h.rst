.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/evsel.h

.. _`perf_evsel__read_on_cpu`:

perf_evsel__read_on_cpu
=======================

.. c:function:: int perf_evsel__read_on_cpu(struct perf_evsel *evsel, int cpu, int thread)

    Read out the results on a CPU and thread

    :param struct perf_evsel \*evsel:
        *undescribed*

    :param int cpu:
        *undescribed*

    :param int thread:
        *undescribed*

.. _`perf_evsel__read_on_cpu.description`:

Description
-----------

@evsel - event selector to read value
\ ``cpu``\  - CPU of interest
\ ``thread``\  - thread of interest

.. _`perf_evsel__read_on_cpu_scaled`:

perf_evsel__read_on_cpu_scaled
==============================

.. c:function:: int perf_evsel__read_on_cpu_scaled(struct perf_evsel *evsel, int cpu, int thread)

    Read out the results on a CPU and thread, scaled

    :param struct perf_evsel \*evsel:
        *undescribed*

    :param int cpu:
        *undescribed*

    :param int thread:
        *undescribed*

.. _`perf_evsel__read_on_cpu_scaled.description`:

Description
-----------

@evsel - event selector to read value
\ ``cpu``\  - CPU of interest
\ ``thread``\  - thread of interest

.. _`perf_evsel__is_group_leader`:

perf_evsel__is_group_leader
===========================

.. c:function:: bool perf_evsel__is_group_leader(const struct perf_evsel *evsel)

    Return whether given evsel is a leader event

    :param const struct perf_evsel \*evsel:
        *undescribed*

.. _`perf_evsel__is_group_leader.description`:

Description
-----------

@evsel - evsel selector to be tested

Return \ ``true``\  if \ ``evsel``\  is a group leader or a stand-alone event

.. _`perf_evsel__is_group_event`:

perf_evsel__is_group_event
==========================

.. c:function:: bool perf_evsel__is_group_event(struct perf_evsel *evsel)

    Return whether given evsel is a group event

    :param struct perf_evsel \*evsel:
        *undescribed*

.. _`perf_evsel__is_group_event.description`:

Description
-----------

@evsel - evsel selector to be tested

Return \ ``true``\  iff event group view is enabled and \ ``evsel``\  is a actual group
leader which has other members in the group

.. This file was automatic generated / don't edit.

