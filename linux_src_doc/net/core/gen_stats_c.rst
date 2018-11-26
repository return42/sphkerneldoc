.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/gen_stats.c

.. _`gnet_stats_start_copy_compat`:

gnet_stats_start_copy_compat
============================

.. c:function:: int gnet_stats_start_copy_compat(struct sk_buff *skb, int type, int tc_stats_type, int xstats_type, spinlock_t *lock, struct gnet_dump *d, int padattr)

    start dumping procedure in compatibility mode

    :param skb:
        socket buffer to put statistics TLVs into
    :type skb: struct sk_buff \*

    :param type:
        TLV type for top level statistic TLV
    :type type: int

    :param tc_stats_type:
        TLV type for backward compatibility struct tc_stats TLV
    :type tc_stats_type: int

    :param xstats_type:
        TLV type for backward compatibility xstats TLV
    :type xstats_type: int

    :param lock:
        statistics lock
    :type lock: spinlock_t \*

    :param d:
        dumping handle
    :type d: struct gnet_dump \*

    :param padattr:
        padding attribute
    :type padattr: int

.. _`gnet_stats_start_copy_compat.description`:

Description
-----------

Initializes the dumping handle, grabs the statistic lock and appends
an empty TLV header to the socket buffer for use a container for all
other statistic TLVS.

The dumping handle is marked to be in backward compatibility mode telling
all \ :c:func:`gnet_stats_copy_XXX`\  functions to fill a local copy of struct tc_stats.

Returns 0 on success or -1 if the room in the socket buffer was not sufficient.

.. _`gnet_stats_start_copy`:

gnet_stats_start_copy
=====================

.. c:function:: int gnet_stats_start_copy(struct sk_buff *skb, int type, spinlock_t *lock, struct gnet_dump *d, int padattr)

    start dumping procedure in compatibility mode

    :param skb:
        socket buffer to put statistics TLVs into
    :type skb: struct sk_buff \*

    :param type:
        TLV type for top level statistic TLV
    :type type: int

    :param lock:
        statistics lock
    :type lock: spinlock_t \*

    :param d:
        dumping handle
    :type d: struct gnet_dump \*

    :param padattr:
        padding attribute
    :type padattr: int

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

.. c:function:: int gnet_stats_copy_basic(const seqcount_t *running, struct gnet_dump *d, struct gnet_stats_basic_cpu __percpu *cpu, struct gnet_stats_basic_packed *b)

    copy basic statistics into statistic TLV

    :param running:
        seqcount_t pointer
    :type running: const seqcount_t \*

    :param d:
        dumping handle
    :type d: struct gnet_dump \*

    :param cpu:
        copy statistic per cpu
    :type cpu: struct gnet_stats_basic_cpu __percpu \*

    :param b:
        basic statistics
    :type b: struct gnet_stats_basic_packed \*

.. _`gnet_stats_copy_basic.description`:

Description
-----------

Appends the basic statistics to the top level TLV created by
\ :c:func:`gnet_stats_start_copy`\ .

Returns 0 on success or -1 with the statistic lock released
if the room in the socket buffer was not sufficient.

.. _`gnet_stats_copy_basic_hw`:

gnet_stats_copy_basic_hw
========================

.. c:function:: int gnet_stats_copy_basic_hw(const seqcount_t *running, struct gnet_dump *d, struct gnet_stats_basic_cpu __percpu *cpu, struct gnet_stats_basic_packed *b)

    copy basic hw statistics into statistic TLV

    :param running:
        seqcount_t pointer
    :type running: const seqcount_t \*

    :param d:
        dumping handle
    :type d: struct gnet_dump \*

    :param cpu:
        copy statistic per cpu
    :type cpu: struct gnet_stats_basic_cpu __percpu \*

    :param b:
        basic statistics
    :type b: struct gnet_stats_basic_packed \*

.. _`gnet_stats_copy_basic_hw.description`:

Description
-----------

Appends the basic statistics to the top level TLV created by
\ :c:func:`gnet_stats_start_copy`\ .

Returns 0 on success or -1 with the statistic lock released
if the room in the socket buffer was not sufficient.

.. _`gnet_stats_copy_rate_est`:

gnet_stats_copy_rate_est
========================

.. c:function:: int gnet_stats_copy_rate_est(struct gnet_dump *d, struct net_rate_estimator __rcu **rate_est)

    copy rate estimator statistics into statistics TLV

    :param d:
        dumping handle
    :type d: struct gnet_dump \*

    :param rate_est:
        rate estimator
    :type rate_est: struct net_rate_estimator __rcu \*\*

.. _`gnet_stats_copy_rate_est.description`:

Description
-----------

Appends the rate estimator statistics to the top level TLV created by
\ :c:func:`gnet_stats_start_copy`\ .

Returns 0 on success or -1 with the statistic lock released
if the room in the socket buffer was not sufficient.

.. _`gnet_stats_copy_queue`:

gnet_stats_copy_queue
=====================

.. c:function:: int gnet_stats_copy_queue(struct gnet_dump *d, struct gnet_stats_queue __percpu *cpu_q, struct gnet_stats_queue *q, __u32 qlen)

    copy queue statistics into statistics TLV

    :param d:
        dumping handle
    :type d: struct gnet_dump \*

    :param cpu_q:
        per cpu queue statistics
    :type cpu_q: struct gnet_stats_queue __percpu \*

    :param q:
        queue statistics
    :type q: struct gnet_stats_queue \*

    :param qlen:
        queue length statistics
    :type qlen: __u32

.. _`gnet_stats_copy_queue.description`:

Description
-----------

Appends the queue statistics to the top level TLV created by
\ :c:func:`gnet_stats_start_copy`\ . Using per cpu queue statistics if
they are available.

Returns 0 on success or -1 with the statistic lock released
if the room in the socket buffer was not sufficient.

.. _`gnet_stats_copy_app`:

gnet_stats_copy_app
===================

.. c:function:: int gnet_stats_copy_app(struct gnet_dump *d, void *st, int len)

    copy application specific statistics into statistics TLV

    :param d:
        dumping handle
    :type d: struct gnet_dump \*

    :param st:
        application specific statistics data
    :type st: void \*

    :param len:
        length of data
    :type len: int

.. _`gnet_stats_copy_app.description`:

Description
-----------

Appends the application specific statistics to the top level TLV created by
\ :c:func:`gnet_stats_start_copy`\  and remembers the data for XSTATS if the dumping
handle is in backward compatibility mode.

Returns 0 on success or -1 with the statistic lock released
if the room in the socket buffer was not sufficient.

.. _`gnet_stats_finish_copy`:

gnet_stats_finish_copy
======================

.. c:function:: int gnet_stats_finish_copy(struct gnet_dump *d)

    finish dumping procedure

    :param d:
        dumping handle
    :type d: struct gnet_dump \*

.. _`gnet_stats_finish_copy.description`:

Description
-----------

Corrects the length of the top level TLV to include all TLVs added
by \ :c:func:`gnet_stats_copy_XXX`\  calls. Adds the backward compatibility TLVs
if \ :c:func:`gnet_stats_start_copy_compat`\  was used and releases the statistics
lock.

Returns 0 on success or -1 with the statistic lock released
if the room in the socket buffer was not sufficient.

.. This file was automatic generated / don't edit.

