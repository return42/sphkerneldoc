.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/lock_dlm.c

.. _`gfs2_update_stats`:

gfs2_update_stats
=================

.. c:function:: void gfs2_update_stats(struct gfs2_lkstats *s, unsigned index, s64 sample)

    Update time based stats

    :param struct gfs2_lkstats \*s:
        *undescribed*

    :param unsigned index:
        *undescribed*

    :param s64 sample:
        New data to include

.. _`gfs2_update_stats.description`:

Description
-----------

@delta is the difference between the current rtt sample and the
running average srtt. We add 1/8 of that to the srtt in order to
update the current srtt estimate. The variance estimate is a bit
more complicated. We subtract the abs value of the \ ``delta``\  from
the current variance estimate and add 1/4 of that to the running
total.

Note that the index points at the array entry containing the smoothed
mean value, and the variance is always in the following entry

.. _`gfs2_update_stats.reference`:

Reference
---------

TCP/IP Illustrated, vol 2, p. 831,832
All times are in units of integer nanoseconds. Unlike the TCP/IP case,
they are not scaled fixed point.

.. _`gfs2_update_reply_times`:

gfs2_update_reply_times
=======================

.. c:function:: void gfs2_update_reply_times(struct gfs2_glock *gl)

    Update locking statistics

    :param struct gfs2_glock \*gl:
        The glock to update

.. _`gfs2_update_reply_times.description`:

Description
-----------

This assumes that gl->gl_dstamp has been set earlier.

The rtt (lock round trip time) is an estimate of the time
taken to perform a dlm lock request. We update it on each
reply from the dlm.

The blocking flag is set on the glock for all dlm requests
which may potentially block due to lock requests from other nodes.
DLM requests where the current lock state is exclusive, the
requested state is null (or unlocked) or where the TRY or
TRY_1CB flags are set are classified as non-blocking. All
other DLM requests are counted as (potentially) blocking.

.. _`gfs2_update_request_times`:

gfs2_update_request_times
=========================

.. c:function:: void gfs2_update_request_times(struct gfs2_glock *gl)

    Update locking statistics

    :param struct gfs2_glock \*gl:
        The glock to update

.. _`gfs2_update_request_times.description`:

Description
-----------

The irt (lock inter-request times) measures the average time
between requests to the dlm. It is updated immediately before
each dlm call.

.. This file was automatic generated / don't edit.

