.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/ccids/ccid3.c

.. _`ccid3_update_send_interval`:

ccid3_update_send_interval
==========================

.. c:function:: void ccid3_update_send_interval(struct ccid3_hc_tx_sock *hc)

    Calculate new t_ipi = s / X_inst This respects the granularity of X_inst (64 \* bytes/second).

    :param struct ccid3_hc_tx_sock \*hc:
        *undescribed*

.. _`ccid3_hc_tx_update_x`:

ccid3_hc_tx_update_x
====================

.. c:function:: void ccid3_hc_tx_update_x(struct sock *sk, ktime_t *stamp)

    Update allowed sending rate X

    :param struct sock \*sk:
        *undescribed*

    :param ktime_t \*stamp:
        most recent time if available - can be left NULL.

.. _`ccid3_hc_tx_update_x.description`:

Description
-----------

This function tracks draft rfc3448bis, check there for latest details.

.. _`ccid3_hc_tx_update_x.note`:

Note
----

X and X_recv are both stored in units of 64 \* bytes/second, to support
fine-grained resolution of sending rates. This requires scaling by 2^6
throughout the code. Only X_calc is unscaled (in bytes/second).

.. _`ccid3_hc_tx_update_s`:

ccid3_hc_tx_update_s
====================

.. c:function:: void ccid3_hc_tx_update_s(struct ccid3_hc_tx_sock *hc, int len)

    Track the mean packet size \`s'

    :param struct ccid3_hc_tx_sock \*hc:
        *undescribed*

    :param int len:
        DCCP packet payload size in bytes

.. _`ccid3_hc_tx_update_s.description`:

Description
-----------

cf. RFC 4342, 5.3 and  RFC 3448, 4.1

.. _`ccid3_hc_tx_send_packet`:

ccid3_hc_tx_send_packet
=======================

.. c:function:: int ccid3_hc_tx_send_packet(struct sock *sk, struct sk_buff *skb)

    Delay-based dequeueing of TX packets

    :param struct sock \*sk:
        *undescribed*

    :param struct sk_buff \*skb:
        next packet candidate to send on \ ``sk``\ 

.. _`ccid3_hc_tx_send_packet.description`:

Description
-----------

This function uses the convention of \ :c:func:`ccid_packet_dequeue_eval`\  and
returns a millisecond-delay value between 0 and t_mbi = 64000 msec.

.. _`ccid3_first_li`:

ccid3_first_li
==============

.. c:function:: u32 ccid3_first_li(struct sock *sk)

    Implements [RFC 5348, 6.3.1]

    :param struct sock \*sk:
        *undescribed*

.. _`ccid3_first_li.description`:

Description
-----------

Determine the length of the first loss interval via inverse lookup.
Assume that X_recv can be computed by the throughput equation
s
X_recv = --------
R \* fval
Find some p such that f(p) = fval; return 1/p (scaled).

.. This file was automatic generated / don't edit.

