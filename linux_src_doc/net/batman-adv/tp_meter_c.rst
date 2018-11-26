.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/tp_meter.c

.. _`batadv_tp_def_test_length`:

BATADV_TP_DEF_TEST_LENGTH
=========================

.. c:function::  BATADV_TP_DEF_TEST_LENGTH()

    Default test length if not specified by the user in milliseconds

.. _`batadv_tp_awnd`:

BATADV_TP_AWND
==============

.. c:function::  BATADV_TP_AWND()

    Advertised window by the receiver (in bytes)

.. _`batadv_tp_recv_timeout`:

BATADV_TP_RECV_TIMEOUT
======================

.. c:function::  BATADV_TP_RECV_TIMEOUT()

    Receiver activity timeout. If the receiver does not get anything for such amount of milliseconds, the connection is killed

.. _`batadv_tp_max_rto`:

BATADV_TP_MAX_RTO
=================

.. c:function::  BATADV_TP_MAX_RTO()

    Maximum sender timeout. If the sender RTO gets beyond such amound of milliseconds, the receiver is considered unreachable and the connection is killed

.. _`batadv_tp_first_seq`:

BATADV_TP_FIRST_SEQ
===================

.. c:function::  BATADV_TP_FIRST_SEQ()

    First seqno of each session. The number is rather high in order to immediately trigger a wrap around (test purposes)

.. _`batadv_tp_plen`:

BATADV_TP_PLEN
==============

.. c:function::  BATADV_TP_PLEN()

    length of the payload (data after the batadv_unicast header) to simulate

.. _`batadv_tp_session_cookie`:

batadv_tp_session_cookie
========================

.. c:function:: u32 batadv_tp_session_cookie(const u8 session, u8 icmp_uid)

    generate session cookie based on session ids

    :param session:
        TP session identifier
    :type session: const u8

    :param icmp_uid:
        icmp pseudo uid of the tp session
    :type icmp_uid: u8

.. _`batadv_tp_session_cookie.return`:

Return
------

32 bit tp_meter session cookie

.. _`batadv_tp_cwnd`:

batadv_tp_cwnd
==============

.. c:function:: u32 batadv_tp_cwnd(u32 base, u32 increment, u32 min)

    compute the new cwnd size

    :param base:
        base cwnd size value
    :type base: u32

    :param increment:
        the value to add to base to get the new size
    :type increment: u32

    :param min:
        minumim cwnd value (usually MSS)
    :type min: u32

.. _`batadv_tp_cwnd.description`:

Description
-----------

Return the new cwnd size and ensures it does not exceed the Advertised
Receiver Window size. It is wrap around safe.
For details refer to Section 3.1 of RFC5681

.. _`batadv_tp_cwnd.return`:

Return
------

new congestion window size in bytes

.. _`batadv_tp_update_cwnd`:

batadv_tp_update_cwnd
=====================

.. c:function:: void batadv_tp_update_cwnd(struct batadv_tp_vars *tp_vars, u32 mss)

    update the Congestion Windows

    :param tp_vars:
        the private data of the current TP meter session
    :type tp_vars: struct batadv_tp_vars \*

    :param mss:
        maximum segment size of transmission
    :type mss: u32

.. _`batadv_tp_update_cwnd.description`:

Description
-----------

1) if the session is in Slow Start, the CWND has to be increased by 1
MSS every unique received ACK
2) if the session is in Congestion Avoidance, the CWND has to be
increased by MSS \* MSS / CWND for every unique received ACK

.. _`batadv_tp_update_rto`:

batadv_tp_update_rto
====================

.. c:function:: void batadv_tp_update_rto(struct batadv_tp_vars *tp_vars, u32 new_rtt)

    calculate new retransmission timeout

    :param tp_vars:
        the private data of the current TP meter session
    :type tp_vars: struct batadv_tp_vars \*

    :param new_rtt:
        new roundtrip time in msec
    :type new_rtt: u32

.. _`batadv_tp_batctl_notify`:

batadv_tp_batctl_notify
=======================

.. c:function:: void batadv_tp_batctl_notify(enum batadv_tp_meter_reason reason, const u8 *dst, struct batadv_priv *bat_priv, unsigned long start_time, u64 total_sent, u32 cookie)

    send client status result to client

    :param reason:
        reason for tp meter session stop
    :type reason: enum batadv_tp_meter_reason

    :param dst:
        destination of tp_meter session
    :type dst: const u8 \*

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param start_time:
        start of transmission in jiffies
    :type start_time: unsigned long

    :param total_sent:
        bytes acked to the receiver
    :type total_sent: u64

    :param cookie:
        cookie of tp_meter session
    :type cookie: u32

.. _`batadv_tp_batctl_error_notify`:

batadv_tp_batctl_error_notify
=============================

.. c:function:: void batadv_tp_batctl_error_notify(enum batadv_tp_meter_reason reason, const u8 *dst, struct batadv_priv *bat_priv, u32 cookie)

    send client error result to client

    :param reason:
        reason for tp meter session stop
    :type reason: enum batadv_tp_meter_reason

    :param dst:
        destination of tp_meter session
    :type dst: const u8 \*

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param cookie:
        cookie of tp_meter session
    :type cookie: u32

.. _`batadv_tp_list_find`:

batadv_tp_list_find
===================

.. c:function:: struct batadv_tp_vars *batadv_tp_list_find(struct batadv_priv *bat_priv, const u8 *dst)

    find a tp_vars object in the global list

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param dst:
        the other endpoint MAC address to look for
    :type dst: const u8 \*

.. _`batadv_tp_list_find.description`:

Description
-----------

Look for a tp_vars object matching dst as end_point and return it after
having incremented the refcounter. Return NULL is not found

.. _`batadv_tp_list_find.return`:

Return
------

matching tp_vars or NULL when no tp_vars with \ ``dst``\  was found

.. _`batadv_tp_list_find_session`:

batadv_tp_list_find_session
===========================

.. c:function:: struct batadv_tp_vars *batadv_tp_list_find_session(struct batadv_priv *bat_priv, const u8 *dst, const u8 *session)

    find tp_vars session object in the global list

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param dst:
        the other endpoint MAC address to look for
    :type dst: const u8 \*

    :param session:
        session identifier
    :type session: const u8 \*

.. _`batadv_tp_list_find_session.description`:

Description
-----------

Look for a tp_vars object matching dst as end_point, session as tp meter
session and return it after having incremented the refcounter. Return NULL
is not found

.. _`batadv_tp_list_find_session.return`:

Return
------

matching tp_vars or NULL when no tp_vars was found

.. _`batadv_tp_vars_release`:

batadv_tp_vars_release
======================

.. c:function:: void batadv_tp_vars_release(struct kref *ref)

    release batadv_tp_vars from lists and queue for free after rcu grace period

    :param ref:
        kref pointer of the batadv_tp_vars
    :type ref: struct kref \*

.. _`batadv_tp_vars_put`:

batadv_tp_vars_put
==================

.. c:function:: void batadv_tp_vars_put(struct batadv_tp_vars *tp_vars)

    decrement the batadv_tp_vars refcounter and possibly release it

    :param tp_vars:
        the private data of the current TP meter session to be free'd
    :type tp_vars: struct batadv_tp_vars \*

.. _`batadv_tp_sender_cleanup`:

batadv_tp_sender_cleanup
========================

.. c:function:: void batadv_tp_sender_cleanup(struct batadv_priv *bat_priv, struct batadv_tp_vars *tp_vars)

    cleanup sender data and drop and timer

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param tp_vars:
        the private data of the current TP meter session to cleanup
    :type tp_vars: struct batadv_tp_vars \*

.. _`batadv_tp_sender_end`:

batadv_tp_sender_end
====================

.. c:function:: void batadv_tp_sender_end(struct batadv_priv *bat_priv, struct batadv_tp_vars *tp_vars)

    print info about ended session and inform client

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param tp_vars:
        the private data of the current TP meter session
    :type tp_vars: struct batadv_tp_vars \*

.. _`batadv_tp_sender_shutdown`:

batadv_tp_sender_shutdown
=========================

.. c:function:: void batadv_tp_sender_shutdown(struct batadv_tp_vars *tp_vars, enum batadv_tp_meter_reason reason)

    let sender thread/timer stop gracefully

    :param tp_vars:
        the private data of the current TP meter session
    :type tp_vars: struct batadv_tp_vars \*

    :param reason:
        reason for tp meter session stop
    :type reason: enum batadv_tp_meter_reason

.. _`batadv_tp_sender_finish`:

batadv_tp_sender_finish
=======================

.. c:function:: void batadv_tp_sender_finish(struct work_struct *work)

    stop sender session after test_length was reached

    :param work:
        delayed work reference of the related tp_vars
    :type work: struct work_struct \*

.. _`batadv_tp_reset_sender_timer`:

batadv_tp_reset_sender_timer
============================

.. c:function:: void batadv_tp_reset_sender_timer(struct batadv_tp_vars *tp_vars)

    reschedule the sender timer

    :param tp_vars:
        the private TP meter data for this session
    :type tp_vars: struct batadv_tp_vars \*

.. _`batadv_tp_reset_sender_timer.description`:

Description
-----------

Reschedule the timer using tp_vars->rto as delay

.. _`batadv_tp_sender_timeout`:

batadv_tp_sender_timeout
========================

.. c:function:: void batadv_tp_sender_timeout(struct timer_list *t)

    timer that fires in case of packet loss

    :param t:
        address to timer_list inside tp_vars
    :type t: struct timer_list \*

.. _`batadv_tp_sender_timeout.description`:

Description
-----------

If fired it means that there was packet loss.
Switch to Slow Start, set the ss_threshold to half of the current cwnd and
reset the cwnd to 3\*MSS

.. _`batadv_tp_fill_prerandom`:

batadv_tp_fill_prerandom
========================

.. c:function:: void batadv_tp_fill_prerandom(struct batadv_tp_vars *tp_vars, u8 *buf, size_t nbytes)

    Fill buffer with prefetched random bytes

    :param tp_vars:
        the private TP meter data for this session
    :type tp_vars: struct batadv_tp_vars \*

    :param buf:
        Buffer to fill with bytes
    :type buf: u8 \*

    :param nbytes:
        amount of pseudorandom bytes
    :type nbytes: size_t

.. _`batadv_tp_send_msg`:

batadv_tp_send_msg
==================

.. c:function:: int batadv_tp_send_msg(struct batadv_tp_vars *tp_vars, const u8 *src, struct batadv_orig_node *orig_node, u32 seqno, size_t len, const u8 *session, int uid, u32 timestamp)

    send a single message

    :param tp_vars:
        the private TP meter data for this session
    :type tp_vars: struct batadv_tp_vars \*

    :param src:
        source mac address
    :type src: const u8 \*

    :param orig_node:
        the originator of the destination
    :type orig_node: struct batadv_orig_node \*

    :param seqno:
        sequence number of this packet
    :type seqno: u32

    :param len:
        length of the entire packet
    :type len: size_t

    :param session:
        session identifier
    :type session: const u8 \*

    :param uid:
        local ICMP "socket" index
    :type uid: int

    :param timestamp:
        timestamp in jiffies which is replied in ack
    :type timestamp: u32

.. _`batadv_tp_send_msg.description`:

Description
-----------

Create and send a single TP Meter message.

.. _`batadv_tp_send_msg.return`:

Return
------

0 on success, BATADV_TP_REASON_DST_UNREACHABLE if the destination is
not reachable, BATADV_TP_REASON_MEMORY_ERROR if the packet couldn't be
allocated

.. _`batadv_tp_recv_ack`:

batadv_tp_recv_ack
==================

.. c:function:: void batadv_tp_recv_ack(struct batadv_priv *bat_priv, const struct sk_buff *skb)

    ACK receiving function

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param skb:
        the buffer containing the received packet
    :type skb: const struct sk_buff \*

.. _`batadv_tp_recv_ack.description`:

Description
-----------

Process a received TP ACK packet

.. _`batadv_tp_avail`:

batadv_tp_avail
===============

.. c:function:: bool batadv_tp_avail(struct batadv_tp_vars *tp_vars, size_t payload_len)

    check if congestion window is not full

    :param tp_vars:
        the private data of the current TP meter session
    :type tp_vars: struct batadv_tp_vars \*

    :param payload_len:
        size of the payload of a single message
    :type payload_len: size_t

.. _`batadv_tp_avail.return`:

Return
------

true when congestion window is not full, false otherwise

.. _`batadv_tp_wait_available`:

batadv_tp_wait_available
========================

.. c:function:: int batadv_tp_wait_available(struct batadv_tp_vars *tp_vars, size_t plen)

    wait until congestion window becomes free or timeout is reached

    :param tp_vars:
        the private data of the current TP meter session
    :type tp_vars: struct batadv_tp_vars \*

    :param plen:
        size of the payload of a single message
    :type plen: size_t

.. _`batadv_tp_wait_available.return`:

Return
------

0 if the condition evaluated to false after the timeout elapsed,
1 if the condition evaluated to true after the timeout elapsed, the
remaining jiffies (at least 1) if the condition evaluated to true before
the timeout elapsed, or -ERESTARTSYS if it was interrupted by a signal.

.. _`batadv_tp_send`:

batadv_tp_send
==============

.. c:function:: int batadv_tp_send(void *arg)

    main sending thread of a tp meter session

    :param arg:
        address of the related tp_vars
    :type arg: void \*

.. _`batadv_tp_send.return`:

Return
------

nothing, this function never returns

.. _`batadv_tp_start_kthread`:

batadv_tp_start_kthread
=======================

.. c:function:: void batadv_tp_start_kthread(struct batadv_tp_vars *tp_vars)

    start new thread which manages the tp meter sender

    :param tp_vars:
        the private data of the current TP meter session
    :type tp_vars: struct batadv_tp_vars \*

.. _`batadv_tp_start`:

batadv_tp_start
===============

.. c:function:: void batadv_tp_start(struct batadv_priv *bat_priv, const u8 *dst, u32 test_length, u32 *cookie)

    start a new tp meter session

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param dst:
        the receiver MAC address
    :type dst: const u8 \*

    :param test_length:
        test length in milliseconds
    :type test_length: u32

    :param cookie:
        session cookie
    :type cookie: u32 \*

.. _`batadv_tp_stop`:

batadv_tp_stop
==============

.. c:function:: void batadv_tp_stop(struct batadv_priv *bat_priv, const u8 *dst, u8 return_value)

    stop currently running tp meter session

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param dst:
        the receiver MAC address
    :type dst: const u8 \*

    :param return_value:
        reason for tp meter session stop
    :type return_value: u8

.. _`batadv_tp_reset_receiver_timer`:

batadv_tp_reset_receiver_timer
==============================

.. c:function:: void batadv_tp_reset_receiver_timer(struct batadv_tp_vars *tp_vars)

    reset the receiver shutdown timer

    :param tp_vars:
        the private data of the current TP meter session
    :type tp_vars: struct batadv_tp_vars \*

.. _`batadv_tp_reset_receiver_timer.description`:

Description
-----------

start the receiver shutdown timer or reset it if already started

.. _`batadv_tp_receiver_shutdown`:

batadv_tp_receiver_shutdown
===========================

.. c:function:: void batadv_tp_receiver_shutdown(struct timer_list *t)

    stop a tp meter receiver when timeout is reached without received ack

    :param t:
        address to timer_list inside tp_vars
    :type t: struct timer_list \*

.. _`batadv_tp_send_ack`:

batadv_tp_send_ack
==================

.. c:function:: int batadv_tp_send_ack(struct batadv_priv *bat_priv, const u8 *dst, u32 seq, __be32 timestamp, const u8 *session, int socket_index)

    send an ACK packet

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param dst:
        the mac address of the destination originator
    :type dst: const u8 \*

    :param seq:
        the sequence number to ACK
    :type seq: u32

    :param timestamp:
        the timestamp to echo back in the ACK
    :type timestamp: __be32

    :param session:
        session identifier
    :type session: const u8 \*

    :param socket_index:
        local ICMP socket identifier
    :type socket_index: int

.. _`batadv_tp_send_ack.return`:

Return
------

0 on success, a positive integer representing the reason of the
failure otherwise

.. _`batadv_tp_handle_out_of_order`:

batadv_tp_handle_out_of_order
=============================

.. c:function:: bool batadv_tp_handle_out_of_order(struct batadv_tp_vars *tp_vars, const struct sk_buff *skb)

    store an out of order packet

    :param tp_vars:
        the private data of the current TP meter session
    :type tp_vars: struct batadv_tp_vars \*

    :param skb:
        the buffer containing the received packet
    :type skb: const struct sk_buff \*

.. _`batadv_tp_handle_out_of_order.description`:

Description
-----------

Store the out of order packet in the unacked list for late processing. This
packets are kept in this list so that they can be ACKed at once as soon as
all the previous packets have been received

.. _`batadv_tp_handle_out_of_order.return`:

Return
------

true if the packed has been successfully processed, false otherwise

.. _`batadv_tp_ack_unordered`:

batadv_tp_ack_unordered
=======================

.. c:function:: void batadv_tp_ack_unordered(struct batadv_tp_vars *tp_vars)

    update number received bytes in current stream without gaps

    :param tp_vars:
        the private data of the current TP meter session
    :type tp_vars: struct batadv_tp_vars \*

.. _`batadv_tp_init_recv`:

batadv_tp_init_recv
===================

.. c:function:: struct batadv_tp_vars *batadv_tp_init_recv(struct batadv_priv *bat_priv, const struct batadv_icmp_tp_packet *icmp)

    return matching or create new receiver tp_vars

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param icmp:
        received icmp tp msg
    :type icmp: const struct batadv_icmp_tp_packet \*

.. _`batadv_tp_init_recv.return`:

Return
------

corresponding tp_vars or NULL on errors

.. _`batadv_tp_recv_msg`:

batadv_tp_recv_msg
==================

.. c:function:: void batadv_tp_recv_msg(struct batadv_priv *bat_priv, const struct sk_buff *skb)

    process a single data message

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param skb:
        the buffer containing the received packet
    :type skb: const struct sk_buff \*

.. _`batadv_tp_recv_msg.description`:

Description
-----------

Process a received TP MSG packet

.. _`batadv_tp_meter_recv`:

batadv_tp_meter_recv
====================

.. c:function:: void batadv_tp_meter_recv(struct batadv_priv *bat_priv, struct sk_buff *skb)

    main TP Meter receiving function

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param skb:
        the buffer containing the received packet
    :type skb: struct sk_buff \*

.. _`batadv_tp_meter_init`:

batadv_tp_meter_init
====================

.. c:function:: void batadv_tp_meter_init( void)

    initialize global tp_meter structures

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

