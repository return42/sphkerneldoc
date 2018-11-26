.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/trace/events/wbt.h

.. _`trace_wbt_stat`:

trace_wbt_stat
==============

.. c:function:: void trace_wbt_stat(struct backing_dev_info *bdi, struct blk_rq_stat *stat)

    trace stats for blk_wb

    :param bdi:
        *undescribed*
    :type bdi: struct backing_dev_info \*

    :param stat:
        array of read/write stats
    :type stat: struct blk_rq_stat \*

.. _`trace_wbt_lat`:

trace_wbt_lat
=============

.. c:function:: void trace_wbt_lat(struct backing_dev_info *bdi, unsigned long lat)

    trace latency event

    :param bdi:
        *undescribed*
    :type bdi: struct backing_dev_info \*

    :param lat:
        latency trigger
    :type lat: unsigned long

.. _`trace_wbt_step`:

trace_wbt_step
==============

.. c:function:: void trace_wbt_step(struct backing_dev_info *bdi, const char *msg, int step, unsigned long window, unsigned int bg, unsigned int normal, unsigned int max)

    trace wb event step

    :param bdi:
        *undescribed*
    :type bdi: struct backing_dev_info \*

    :param msg:
        context message
    :type msg: const char \*

    :param step:
        the current scale step count
    :type step: int

    :param window:
        the current monitoring window
    :type window: unsigned long

    :param bg:
        the current background queue limit
    :type bg: unsigned int

    :param normal:
        the current normal writeback limit
    :type normal: unsigned int

    :param max:
        the current max throughput writeback limit
    :type max: unsigned int

.. _`trace_wbt_timer`:

trace_wbt_timer
===============

.. c:function:: void trace_wbt_timer(struct backing_dev_info *bdi, unsigned int status, int step, unsigned int inflight)

    trace wb timer event

    :param bdi:
        *undescribed*
    :type bdi: struct backing_dev_info \*

    :param status:
        timer state status
    :type status: unsigned int

    :param step:
        the current scale step count
    :type step: int

    :param inflight:
        tracked writes inflight
    :type inflight: unsigned int

.. This file was automatic generated / don't edit.

