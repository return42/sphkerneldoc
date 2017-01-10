.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/trace/events/wbt.h

.. _`trace_wbt_stat`:

trace_wbt_stat
==============

.. c:function:: void trace_wbt_stat(struct backing_dev_info *bdi, struct blk_rq_stat *stat)

    trace stats for blk_wb

    :param struct backing_dev_info \*bdi:
        *undescribed*

    :param struct blk_rq_stat \*stat:
        array of read/write stats

.. _`trace_wbt_lat`:

trace_wbt_lat
=============

.. c:function:: void trace_wbt_lat(struct backing_dev_info *bdi, unsigned long lat)

    trace latency event

    :param struct backing_dev_info \*bdi:
        *undescribed*

    :param unsigned long lat:
        latency trigger

.. _`trace_wbt_step`:

trace_wbt_step
==============

.. c:function:: void trace_wbt_step(struct backing_dev_info *bdi, const char *msg, int step, unsigned long window, unsigned int bg, unsigned int normal, unsigned int max)

    trace wb event step

    :param struct backing_dev_info \*bdi:
        *undescribed*

    :param const char \*msg:
        context message

    :param int step:
        the current scale step count

    :param unsigned long window:
        the current monitoring window

    :param unsigned int bg:
        the current background queue limit

    :param unsigned int normal:
        the current normal writeback limit

    :param unsigned int max:
        the current max throughput writeback limit

.. _`trace_wbt_timer`:

trace_wbt_timer
===============

.. c:function:: void trace_wbt_timer(struct backing_dev_info *bdi, unsigned int status, int step, unsigned int inflight)

    trace wb timer event

    :param struct backing_dev_info \*bdi:
        *undescribed*

    :param unsigned int status:
        timer state status

    :param int step:
        the current scale step count

    :param unsigned int inflight:
        tracked writes inflight

.. This file was automatic generated / don't edit.

