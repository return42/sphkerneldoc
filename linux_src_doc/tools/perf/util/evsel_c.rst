.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/evsel.c

.. _`__perf_evsel__calc_id_pos`:

\__perf_evsel__calc_id_pos
==========================

.. c:function:: int __perf_evsel__calc_id_pos(u64 sample_type)

    calculate id_pos.

    :param sample_type:
        sample type
    :type sample_type: u64

.. _`__perf_evsel__calc_id_pos.description`:

Description
-----------

This function returns the position of the event id (PERF_SAMPLE_ID or
PERF_SAMPLE_IDENTIFIER) in a sample event i.e. in the array of struct
sample_event.

.. _`__perf_evsel__calc_is_pos`:

\__perf_evsel__calc_is_pos
==========================

.. c:function:: int __perf_evsel__calc_is_pos(u64 sample_type)

    calculate is_pos.

    :param sample_type:
        sample type
    :type sample_type: u64

.. _`__perf_evsel__calc_is_pos.description`:

Description
-----------

This function returns the position (counting backwards) of the event id
(PERF_SAMPLE_ID or PERF_SAMPLE_IDENTIFIER) in a non-sample event i.e. if
sample_id_all is used there is an id sample appended to non-sample events.

.. _`perf_evsel__is_function_event`:

perf_evsel__is_function_event
=============================

.. c:function:: bool perf_evsel__is_function_event(struct perf_evsel *evsel)

    Return whether given evsel is a function trace event

    :param evsel:
        *undescribed*
    :type evsel: struct perf_evsel \*

.. _`perf_evsel__is_function_event.description`:

Description
-----------

\ ``evsel``\  - evsel selector to be tested

Return \ ``true``\  if event is function trace event

.. This file was automatic generated / don't edit.

