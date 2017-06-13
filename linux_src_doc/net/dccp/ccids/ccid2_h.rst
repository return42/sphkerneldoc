.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/ccids/ccid2.h

.. _`ccid2_hc_tx_sock`:

struct ccid2_hc_tx_sock
=======================

.. c:type:: struct ccid2_hc_tx_sock

    CCID2 TX half connection

.. _`ccid2_hc_tx_sock.definition`:

Definition
----------

.. code-block:: c

    struct ccid2_hc_tx_sock {
        u32 tx_cwnd;
        u32 tx_ssthresh;
        u32 tx_pipe;
        u32 tx_packets_acked;
        struct ccid2_seq  *tx_seqbuf;
        int tx_seqbufc;
        struct ccid2_seq *tx_seqh;
        struct ccid2_seq *tx_seqt;
        u32 tx_srtt;
        u32 tx_mdev;
        u32 tx_mdev_max;
        u32 tx_rttvar;
        u32 tx_rto;
        u64 tx_rtt_seq:48;
        struct timer_list tx_rtotimer;
        u32 tx_cwnd_used;
        u32 tx_expected_wnd;
        u32 tx_cwnd_stamp;
        u32 tx_lsndtime;
        u64 tx_rpseq;
        int tx_rpdupack;
        u32 tx_last_cong;
        u64 tx_high_ack;
        struct list_head tx_av_chunks;
    }

.. _`ccid2_hc_tx_sock.members`:

Members
-------

tx_cwnd
    *undescribed*

tx_ssthresh
    *undescribed*

tx_pipe
    *undescribed*

tx_packets_acked
    Ack counter for deriving cwnd growth (RFC 3465)

tx_seqbuf
    *undescribed*

tx_seqbufc
    *undescribed*

tx_seqh
    *undescribed*

tx_seqt
    *undescribed*

tx_srtt
    smoothed RTT estimate, scaled by 2^3

tx_mdev
    smoothed RTT variation, scaled by 2^2

tx_mdev_max
    maximum of \ ``mdev``\  during one flight

tx_rttvar
    moving average/maximum of \ ``mdev_max``\ 

tx_rto
    RTO value deriving from SRTT and RTTVAR (RFC 2988)

tx_rtt_seq
    to decay RTTVAR at most once per flight

tx_rtotimer
    *undescribed*

tx_cwnd_used
    actually used cwnd, W_used of RFC 2861

tx_expected_wnd
    moving average of \ ``tx_cwnd_used``\ 

tx_cwnd_stamp
    to track idle periods in CWV

tx_lsndtime
    last time (in jiffies) a data packet was sent

tx_rpseq
    last consecutive seqno

tx_rpdupack
    dupacks since rpseq

tx_last_cong
    *undescribed*

tx_high_ack
    *undescribed*

tx_av_chunks
    list of Ack Vectors received on current skb

.. _`ccid2_hc_rx_sock`:

struct ccid2_hc_rx_sock
=======================

.. c:type:: struct ccid2_hc_rx_sock

    Receiving end of CCID-2 half-connection

.. _`ccid2_hc_rx_sock.definition`:

Definition
----------

.. code-block:: c

    struct ccid2_hc_rx_sock {
        u32 rx_num_data_pkts;
    }

.. _`ccid2_hc_rx_sock.members`:

Members
-------

rx_num_data_pkts
    number of data packets received since last feedback

.. This file was automatic generated / don't edit.

