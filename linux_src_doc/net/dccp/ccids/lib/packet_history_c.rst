.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/ccids/lib/packet_history.c

.. _`tfrc_rx_handle_loss`:

tfrc_rx_handle_loss
===================

.. c:function:: int tfrc_rx_handle_loss(struct tfrc_rx_hist *h, struct tfrc_loss_hist *lh, struct sk_buff *skb, const u64 ndp, u32 (*calc_first_li)(struct sock *), struct sock *sk)

    Loss detection and further processing

    :param h:
        The non-empty RX history object
    :type h: struct tfrc_rx_hist \*

    :param lh:
        Loss Intervals database to update
    :type lh: struct tfrc_loss_hist \*

    :param skb:
        Currently received packet
    :type skb: struct sk_buff \*

    :param ndp:
        The NDP count belonging to \ ``skb``\ 
    :type ndp: const u64

    :param u32 (\*calc_first_li)(struct sock \*):
        Caller-dependent computation of first loss interval in \ ``lh``\ 

    :param sk:
        Used by \ ``calc_first_li``\  (see tfrc_lh_interval_add)
    :type sk: struct sock \*

.. _`tfrc_rx_handle_loss.description`:

Description
-----------

Chooses action according to pending loss, updates LI database when a new
loss was detected, and does required post-processing. Returns 1 when caller
should send feedback, 0 otherwise.
Since it also takes care of reordering during loss detection and updates the
records accordingly, the caller should not perform any more RX history
operations when loss_count is greater than 0 after calling this function.

.. _`tfrc_rx_hist_rtt_last_s`:

tfrc_rx_hist_rtt_last_s
=======================

.. c:function:: struct tfrc_rx_hist_entry *tfrc_rx_hist_rtt_last_s(const struct tfrc_rx_hist *h)

    reference entry to compute RTT samples against

    :param h:
        *undescribed*
    :type h: const struct tfrc_rx_hist \*

.. _`tfrc_rx_hist_rtt_prev_s`:

tfrc_rx_hist_rtt_prev_s
=======================

.. c:function:: struct tfrc_rx_hist_entry *tfrc_rx_hist_rtt_prev_s(const struct tfrc_rx_hist *h)

    previously suitable (wrt rtt_last_s) RTT-sampling entry

    :param h:
        *undescribed*
    :type h: const struct tfrc_rx_hist \*

.. _`tfrc_rx_hist_sample_rtt`:

tfrc_rx_hist_sample_rtt
=======================

.. c:function:: u32 tfrc_rx_hist_sample_rtt(struct tfrc_rx_hist *h, const struct sk_buff *skb)

    Sample RTT from timestamp / CCVal Based on ideas presented in RFC 4342, 8.1. Returns 0 if it was not able to compute a sample with given data - calling function should check this.

    :param h:
        *undescribed*
    :type h: struct tfrc_rx_hist \*

    :param skb:
        *undescribed*
    :type skb: const struct sk_buff \*

.. This file was automatic generated / don't edit.

