.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/tests/switch-tracking.c

.. _`test__switch_tracking`:

test__switch_tracking
=====================

.. c:function:: int test__switch_tracking(int subtest __maybe_unused, int subtest __maybe_unused)

    test using sched_switch and tracking events.

    :param int subtest __maybe_unused:
        *undescribed*

    :param int subtest __maybe_unused:
        *undescribed*

.. _`test__switch_tracking.description`:

Description
-----------

This function implements a test that checks that sched_switch events and
tracking events can be recorded for a workload (current process) using the
evsel->system_wide and evsel->tracking flags (respectively) with other events
sometimes enabled or disabled.

.. This file was automatic generated / don't edit.

