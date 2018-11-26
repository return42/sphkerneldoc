.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/ccids/ccid2.c

.. _`ccid2_update_used_window`:

ccid2_update_used_window
========================

.. c:function:: void ccid2_update_used_window(struct ccid2_hc_tx_sock *hc, u32 new_wnd)

    Track how much of cwnd is actually used This is done in addition to CWV. The sender needs to have an idea of how many packets may be in flight, to set the local Sequence Window value accordingly (RFC 4340, 7.5.2). The CWV mechanism is exploited to keep track of the maximum-used window. We use an EWMA low-pass filter to filter out noise.

    :param hc:
        *undescribed*
    :type hc: struct ccid2_hc_tx_sock \*

    :param new_wnd:
        *undescribed*
    :type new_wnd: u32

.. _`ccid2_rtt_estimator`:

ccid2_rtt_estimator
===================

.. c:function:: void ccid2_rtt_estimator(struct sock *sk, const long mrtt)

    Sample RTT and compute RTO using RFC2988 algorithm This code is almost identical with TCP's \ :c:func:`tcp_rtt_estimator`\ , since - it has a higher sampling frequency (recommended by RFC 1323), - the RTO does not collapse into RTT due to RTTVAR going towards zero, - it is simple (cf. more complex proposals such as Eifel timer or research which suggests that the gain should be set according to window size), - in tests it was found to work well with CCID2 [gerrit].

    :param sk:
        *undescribed*
    :type sk: struct sock \*

    :param mrtt:
        *undescribed*
    :type mrtt: const long

.. This file was automatic generated / don't edit.

