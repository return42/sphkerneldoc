.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/arch/x86/tests/perf-time-to-tsc.c

.. _`test__perf_time_to_tsc`:

test__perf_time_to_tsc
======================

.. c:function:: int test__perf_time_to_tsc(int subtest __maybe_unused, int subtest __maybe_unused)

    test converting perf time to TSC.

    :param __maybe_unused:
        *undescribed*
    :type __maybe_unused: int subtest

    :param __maybe_unused:
        *undescribed*
    :type __maybe_unused: int subtest

.. _`test__perf_time_to_tsc.description`:

Description
-----------

This function implements a test that checks that the conversion of perf time
to and from TSC is consistent with the order of events.  If the test passes
\ ``0``\  is returned, otherwise \ ``-1``\  is returned.  If TSC conversion is not
supported then then the test passes but " (not supported)" is printed.

.. This file was automatic generated / don't edit.

