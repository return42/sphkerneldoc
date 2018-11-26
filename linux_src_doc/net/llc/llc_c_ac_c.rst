.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/llc/llc_c_ac.c

.. _`llc_conn_ac_send_ack_if_needed`:

llc_conn_ac_send_ack_if_needed
==============================

.. c:function:: int llc_conn_ac_send_ack_if_needed(struct sock *sk, struct sk_buff *skb)

    check if ack is needed

    :param sk:
        current connection structure
    :type sk: struct sock \*

    :param skb:
        current event
    :type skb: struct sk_buff \*

.. _`llc_conn_ac_send_ack_if_needed.description`:

Description
-----------

Checks number of received PDUs which have not been acknowledged, yet,
If number of them reaches to "npta"(Number of PDUs To Acknowledge) then
sends an RR response as acknowledgement for them.  Returns 0 for
success, 1 otherwise.

.. _`llc_conn_ac_rst_sendack_flag`:

llc_conn_ac_rst_sendack_flag
============================

.. c:function:: int llc_conn_ac_rst_sendack_flag(struct sock *sk, struct sk_buff *skb)

    resets ack_must_be_send flag

    :param sk:
        current connection structure
    :type sk: struct sock \*

    :param skb:
        current event
    :type skb: struct sk_buff \*

.. _`llc_conn_ac_rst_sendack_flag.description`:

Description
-----------

This action resets ack_must_be_send flag of given connection, this flag
indicates if there is any PDU which has not been acknowledged yet.
Returns 0 for success, 1 otherwise.

.. _`llc_conn_ac_send_i_rsp_f_set_ackpf`:

llc_conn_ac_send_i_rsp_f_set_ackpf
==================================

.. c:function:: int llc_conn_ac_send_i_rsp_f_set_ackpf(struct sock *sk, struct sk_buff *skb)

    acknowledge received PDUs

    :param sk:
        current connection structure
    :type sk: struct sock \*

    :param skb:
        current event
    :type skb: struct sk_buff \*

.. _`llc_conn_ac_send_i_rsp_f_set_ackpf.description`:

Description
-----------

Sends an I response PDU with f-bit set to ack_pf flag as acknowledge to
all received PDUs which have not been acknowledged, yet. ack_pf flag is
set to one if one PDU with p-bit set to one is received.  Returns 0 for
success, 1 otherwise.

.. _`llc_conn_ac_send_i_as_ack`:

llc_conn_ac_send_i_as_ack
=========================

.. c:function:: int llc_conn_ac_send_i_as_ack(struct sock *sk, struct sk_buff *skb)

    sends an I-format PDU to acknowledge rx PDUs

    :param sk:
        current connection structure.
    :type sk: struct sock \*

    :param skb:
        current event.
    :type skb: struct sk_buff \*

.. _`llc_conn_ac_send_i_as_ack.description`:

Description
-----------

This action sends an I-format PDU as acknowledge to received PDUs which
have not been acknowledged, yet, if there is any. By using of this
action number of acknowledgements decreases, this technic is called
piggy backing. Returns 0 for success, 1 otherwise.

.. _`llc_conn_ac_send_rr_rsp_f_set_ackpf`:

llc_conn_ac_send_rr_rsp_f_set_ackpf
===================================

.. c:function:: int llc_conn_ac_send_rr_rsp_f_set_ackpf(struct sock *sk, struct sk_buff *skb)

    ack all rx PDUs not yet acked

    :param sk:
        current connection structure.
    :type sk: struct sock \*

    :param skb:
        current event.
    :type skb: struct sk_buff \*

.. _`llc_conn_ac_send_rr_rsp_f_set_ackpf.description`:

Description
-----------

This action sends an RR response with f-bit set to ack_pf flag as
acknowledge to all received PDUs which have not been acknowledged, yet,
if there is any. ack_pf flag indicates if a PDU has been received with
p-bit set to one. Returns 0 for success, 1 otherwise.

.. _`llc_conn_ac_inc_npta_value`:

llc_conn_ac_inc_npta_value
==========================

.. c:function:: int llc_conn_ac_inc_npta_value(struct sock *sk, struct sk_buff *skb)

    tries to make value of npta greater

    :param sk:
        current connection structure.
    :type sk: struct sock \*

    :param skb:
        current event.
    :type skb: struct sk_buff \*

.. _`llc_conn_ac_inc_npta_value.description`:

Description
-----------

After "inc_cntr" times calling of this action, "npta" increase by one.
this action tries to make vale of "npta" greater as possible; number of
acknowledgements decreases by increasing of "npta". Returns 0 for
success, 1 otherwise.

.. _`llc_conn_ac_adjust_npta_by_rr`:

llc_conn_ac_adjust_npta_by_rr
=============================

.. c:function:: int llc_conn_ac_adjust_npta_by_rr(struct sock *sk, struct sk_buff *skb)

    decreases "npta" by one

    :param sk:
        current connection structure.
    :type sk: struct sock \*

    :param skb:
        current event.
    :type skb: struct sk_buff \*

.. _`llc_conn_ac_adjust_npta_by_rr.description`:

Description
-----------

After receiving "dec_cntr" times RR command, this action decreases
"npta" by one. Returns 0 for success, 1 otherwise.

.. _`llc_conn_ac_adjust_npta_by_rnr`:

llc_conn_ac_adjust_npta_by_rnr
==============================

.. c:function:: int llc_conn_ac_adjust_npta_by_rnr(struct sock *sk, struct sk_buff *skb)

    decreases "npta" by one

    :param sk:
        current connection structure.
    :type sk: struct sock \*

    :param skb:
        current event.
    :type skb: struct sk_buff \*

.. _`llc_conn_ac_adjust_npta_by_rnr.description`:

Description
-----------

After receiving "dec_cntr" times RNR command, this action decreases
"npta" by one. Returns 0 for success, 1 otherwise.

.. _`llc_conn_ac_dec_tx_win_size`:

llc_conn_ac_dec_tx_win_size
===========================

.. c:function:: int llc_conn_ac_dec_tx_win_size(struct sock *sk, struct sk_buff *skb)

    decreases tx window size

    :param sk:
        current connection structure.
    :type sk: struct sock \*

    :param skb:
        current event.
    :type skb: struct sk_buff \*

.. _`llc_conn_ac_dec_tx_win_size.description`:

Description
-----------

After receiving of a REJ command or response, transmit window size is
decreased by number of PDUs which are outstanding yet. Returns 0 for
success, 1 otherwise.

.. _`llc_conn_ac_inc_tx_win_size`:

llc_conn_ac_inc_tx_win_size
===========================

.. c:function:: int llc_conn_ac_inc_tx_win_size(struct sock *sk, struct sk_buff *skb)

    tx window size is inc by 1

    :param sk:
        current connection structure.
    :type sk: struct sock \*

    :param skb:
        current event.
    :type skb: struct sk_buff \*

.. _`llc_conn_ac_inc_tx_win_size.description`:

Description
-----------

After receiving an RR response with f-bit set to one, transmit window
size is increased by one. Returns 0 for success, 1 otherwise.

.. _`llc_conn_disc`:

llc_conn_disc
=============

.. c:function:: int llc_conn_disc(struct sock *sk, struct sk_buff *skb)

    removes connection from SAP list and frees it

    :param sk:
        closed connection
    :type sk: struct sock \*

    :param skb:
        occurred event
    :type skb: struct sk_buff \*

.. _`llc_conn_reset`:

llc_conn_reset
==============

.. c:function:: int llc_conn_reset(struct sock *sk, struct sk_buff *skb)

    resets connection

    :param sk:
        reseting connection.
    :type sk: struct sock \*

    :param skb:
        occurred event.
    :type skb: struct sk_buff \*

.. _`llc_conn_reset.description`:

Description
-----------

Stop all timers, empty all queues and reset all flags.

.. _`llc_circular_between`:

llc_circular_between
====================

.. c:function:: u8 llc_circular_between(u8 a, u8 b, u8 c)

    designates that b is between a and c or not

    :param a:
        lower bound
    :type a: u8

    :param b:
        element to see if is between a and b
    :type b: u8

    :param c:
        upper bound
    :type c: u8

.. _`llc_circular_between.description`:

Description
-----------

This function designates that b is between a and c or not (for example,
0 is between 127 and 1). Returns 1 if b is between a and c, 0
otherwise.

.. _`llc_process_tmr_ev`:

llc_process_tmr_ev
==================

.. c:function:: void llc_process_tmr_ev(struct sock *sk, struct sk_buff *skb)

    timer backend

    :param sk:
        active connection
    :type sk: struct sock \*

    :param skb:
        occurred event
    :type skb: struct sk_buff \*

.. _`llc_process_tmr_ev.description`:

Description
-----------

This function is called from timer callback functions. When connection
is busy (during sending a data frame) timer expiration event must be
queued. Otherwise this event can be sent to connection state machine.
Queued events will process by llc_backlog_rcv function after sending
data frame.

.. This file was automatic generated / don't edit.

