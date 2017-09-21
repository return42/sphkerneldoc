.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/perf/hv-24x7.c

.. _`get_count_from_result`:

get_count_from_result
=====================

.. c:function:: int get_count_from_result(struct perf_event *event, struct hv_24x7_data_result_buffer *resb, struct hv_24x7_result *res, u64 *countp, struct hv_24x7_result **next)

    get event count from all result elements in result

    :param struct perf_event \*event:
        Event associated with \ ``res``\ .

    :param struct hv_24x7_data_result_buffer \*resb:
        Result buffer containing \ ``res``\ .

    :param struct hv_24x7_result \*res:
        Result to work on.

    :param u64 \*countp:
        Output variable containing the event count.

    :param struct hv_24x7_result \*\*next:
        Optional output variable pointing to the next result in \ ``resb``\ .

.. _`get_count_from_result.description`:

Description
-----------

If the event corresponding to this result needs aggregation of the result
element values, then this function does that.

.. This file was automatic generated / don't edit.

