.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/ccids/ccid3.h

.. _`ccid3_hc_tx_sock`:

struct ccid3_hc_tx_sock
=======================

.. c:type:: struct ccid3_hc_tx_sock

    CCID3 sender half-connection socket

.. _`ccid3_hc_tx_sock.definition`:

Definition
----------

.. code-block:: c

    struct ccid3_hc_tx_sock {
        u64 tx_x;
        u64 tx_x_recv;
        u32 tx_x_calc;
        u32 tx_rtt;
        u32 tx_p;
        u32 tx_t_rto;
        u32 tx_t_ipi;
        u16 tx_s;
        enum ccid3_hc_tx_states tx_state:8;
        u8 tx_last_win_count;
        ktime_t tx_t_last_win_count;
        struct timer_list tx_no_feedback_timer;
        ktime_t tx_t_ld;
        ktime_t tx_t_nom;
        struct tfrc_tx_hist_entry *tx_hist;
    }

.. _`ccid3_hc_tx_sock.members`:

Members
-------

tx_x
    Current sending rate in 64 \* bytes per second

tx_x_recv
    Receive rate in 64 \* bytes per second

tx_x_calc
    Calculated rate in bytes per second

tx_rtt
    Estimate of current round trip time in usecs

tx_p
    Current loss event rate (0-1) scaled by 1000000

tx_t_rto
    Nofeedback Timer setting in usecs

tx_t_ipi
    Interpacket (send) interval (RFC 3448, 4.6) in usecs

tx_s
    Packet size in bytes

tx_state
    Sender state, one of \ ``ccid3_hc_tx_states``\ 

tx_last_win_count
    Last window counter sent

tx_t_last_win_count
    Timestamp of earliest packet
    with last_win_count value sent

tx_no_feedback_timer
    Handle to no feedback timer

tx_t_ld
    Time last doubled during slow start

tx_t_nom
    Nominal send time of next packet

tx_hist
    Packet history

.. _`ccid3_hc_rx_sock`:

struct ccid3_hc_rx_sock
=======================

.. c:type:: struct ccid3_hc_rx_sock

    CCID3 receiver half-connection socket

.. _`ccid3_hc_rx_sock.definition`:

Definition
----------

.. code-block:: c

    struct ccid3_hc_rx_sock {
        u8 rx_last_counter:4;
        enum ccid3_hc_rx_states rx_state:8;
        u32 rx_bytes_recv;
        u32 rx_x_recv;
        u32 rx_rtt;
        ktime_t rx_tstamp_last_feedback;
        struct tfrc_rx_hist rx_hist;
        struct tfrc_loss_hist rx_li_hist;
        u16 rx_s;
        #define rx_pinv rx_li_hist.i_mean
    }

.. _`ccid3_hc_rx_sock.members`:

Members
-------

rx_last_counter
    Tracks window counter (RFC 4342, 8.1)

rx_state
    Receiver state, one of \ ``ccid3_hc_rx_states``\ 

rx_bytes_recv
    Total sum of DCCP payload bytes

rx_x_recv
    Receiver estimate of send rate (RFC 3448, sec. 4.3)

rx_rtt
    Receiver estimate of RTT

rx_tstamp_last_feedback
    Time at which last feedback was sent

rx_hist
    Packet history (loss detection + RTT sampling)

rx_li_hist
    Loss Interval database

rx_s
    Received packet size in bytes

.. This file was automatic generated / don't edit.

