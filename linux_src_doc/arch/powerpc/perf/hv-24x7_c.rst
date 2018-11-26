.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/perf/hv-24x7.c

.. _`get_count_from_result`:

get_count_from_result
=====================

.. c:function:: int get_count_from_result(struct perf_event *event, struct hv_24x7_data_result_buffer *resb, struct hv_24x7_result *res, u64 *countp, struct hv_24x7_result **next)

    get event count from all result elements in result

    :param event:
        Event associated with \ ``res``\ .
    :type event: struct perf_event \*

    :param resb:
        Result buffer containing \ ``res``\ .
    :type resb: struct hv_24x7_data_result_buffer \*

    :param res:
        Result to work on.
    :type res: struct hv_24x7_result \*

    :param countp:
        Output variable containing the event count.
    :type countp: u64 \*

    :param next:
        Optional output variable pointing to the next result in \ ``resb``\ .
    :type next: struct hv_24x7_result \*\*

.. _`get_count_from_result.description`:

Description
-----------

If the event corresponding to this result needs aggregation of the result
element values, then this function does that.

.. This file was automatic generated / don't edit.

