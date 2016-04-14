.. -*- coding: utf-8; mode: rst -*-

===========
gen_stats.c
===========

.. _`gnet_stats_start_copy_compat`:

gnet_stats_start_copy_compat
============================

.. c:function:: int gnet_stats_start_copy_compat (struct sk_buff *skb, int type, int tc_stats_type, int xstats_type, spinlock_t *lock, struct gnet_dump *d)

    start dumping procedure in compatibility mode

    :param struct sk_buff \*skb:
        socket buffer to put statistics TLVs into

    :param int type:
        TLV type for top level statistic TLV

    :param int tc_stats_type:
        TLV type for backward compatibility struct tc_stats TLV

    :param int xstats_type:
        TLV type for backward compatibility xstats TLV

    :param spinlock_t \*lock:
        statistics lock

    :param struct gnet_dump \*d:
        dumping handle


.. _`gnet_stats_start_copy_compat.description`:

Description
-----------

Initializes the dumping handle, grabs the statistic lock and appends
an empty TLV header to the socket buffer for use a container for all
other statistic TLVS.

The dumping handle is marked to be in backward compatibility mode telling
all :c:func:`gnet_stats_copy_XXX` functions to fill a local copy of struct tc_stats.

Returns 0 on success or -1 if the room in the socket buffer was not sufficient.


.. _`gnet_stats_start_copy`:

gnet_stats_start_copy
=====================

.. c:function:: int gnet_stats_start_copy (struct sk_buff *skb, int type, spinlock_t *lock, struct gnet_dump *d)

    start dumping procedure in compatibility mode

    :param struct sk_buff \*skb:
        socket buffer to put statistics TLVs into

    :param int type:
        TLV type for top level statistic TLV

    :param spinlock_t \*lock:
        statistics lock

    :param struct gnet_dump \*d:
        dumping handle


.. _`gnet_stats_start_copy.description`:

Description
-----------

Initializes the dumping handle, grabs the statistic lock and appends
an empty TLV header to the socket buffer for use a container for all
other statistic TLVS.

Returns 0 on success or -1 if the room in the socket buffer was not sufficient.


.. _`gnet_stats_copy_basic`:

gnet_stats_copy_basic
=====================

.. c:function:: int gnet_stats_copy_basic (struct gnet_dump *d, struct gnet_stats_basic_cpu __percpu *cpu, struct gnet_stats_basic_packed *b)

    copy basic statistics into statistic TLV

    :param struct gnet_dump \*d:
        dumping handle

    :param struct gnet_stats_basic_cpu __percpu \*cpu:
        copy statistic per cpu

    :param struct gnet_stats_basic_packed \*b:
        basic statistics


.. _`gnet_stats_copy_basic.description`:

Description
-----------

Appends the basic statistics to the top level TLV created by
:c:func:`gnet_stats_start_copy`.

Returns 0 on success or -1 with the statistic lock released
if the room in the socket buffer was not sufficient.


.. _`gnet_stats_copy_rate_est`:

gnet_stats_copy_rate_est
========================

.. c:function:: int gnet_stats_copy_rate_est (struct gnet_dump *d, const struct gnet_stats_basic_packed *b, struct gnet_stats_rate_est64 *r)

    copy rate estimator statistics into statistics TLV

    :param struct gnet_dump \*d:
        dumping handle

    :param const struct gnet_stats_basic_packed \*b:
        basic statistics

    :param struct gnet_stats_rate_est64 \*r:
        rate estimator statistics


.. _`gnet_stats_copy_rate_est.description`:

Description
-----------

Appends the rate estimator statistics to the top level TLV created by
:c:func:`gnet_stats_start_copy`.

Returns 0 on success or -1 with the statistic lock released
if the room in the socket buffer was not sufficient.


.. _`gnet_stats_copy_queue`:

gnet_stats_copy_queue
=====================

.. c:function:: int gnet_stats_copy_queue (struct gnet_dump *d, struct gnet_stats_queue __percpu *cpu_q, struct gnet_stats_queue *q, __u32 qlen)

    copy queue statistics into statistics TLV

    :param struct gnet_dump \*d:
        dumping handle

    :param struct gnet_stats_queue __percpu \*cpu_q:
        per cpu queue statistics

    :param struct gnet_stats_queue \*q:
        queue statistics

    :param __u32 qlen:
        queue length statistics


.. _`gnet_stats_copy_queue.description`:

Description
-----------

Appends the queue statistics to the top level TLV created by
:c:func:`gnet_stats_start_copy`. Using per cpu queue statistics if
they are available.

Returns 0 on success or -1 with the statistic lock released
if the room in the socket buffer was not sufficient.


.. _`gnet_stats_copy_app`:

gnet_stats_copy_app
===================

.. c:function:: int gnet_stats_copy_app (struct gnet_dump *d, void *st, int len)

    copy application specific statistics into statistics TLV

    :param struct gnet_dump \*d:
        dumping handle

    :param void \*st:
        application specific statistics data

    :param int len:
        length of data


.. _`gnet_stats_copy_app.description`:

Description
-----------

Appends the application specific statistics to the top level TLV created by
:c:func:`gnet_stats_start_copy` and remembers the data for XSTATS if the dumping
handle is in backward compatibility mode.

Returns 0 on success or -1 with the statistic lock released
if the room in the socket buffer was not sufficient.


.. _`gnet_stats_finish_copy`:

gnet_stats_finish_copy
======================

.. c:function:: int gnet_stats_finish_copy (struct gnet_dump *d)

    finish dumping procedure

    :param struct gnet_dump \*d:
        dumping handle


.. _`gnet_stats_finish_copy.description`:

Description
-----------

Corrects the length of the top level TLV to include all TLVs added
by :c:func:`gnet_stats_copy_XXX` calls. Adds the backward compatibility TLVs
if :c:func:`gnet_stats_start_copy_compat` was used and releases the statistics
lock.

Returns 0 on success or -1 with the statistic lock released
if the room in the socket buffer was not sufficient.

