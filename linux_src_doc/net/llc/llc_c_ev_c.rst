.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/llc/llc_c_ev.c

.. _`llc_util_ns_inside_rx_window`:

llc_util_ns_inside_rx_window
============================

.. c:function:: u16 llc_util_ns_inside_rx_window(u8 ns, u8 vr, u8 rw)

    check if sequence number is in rx window

    :param u8 ns:
        sequence number of received pdu.

    :param u8 vr:
        sequence number which receiver expects to receive.

    :param u8 rw:
        receive window size of receiver.

.. _`llc_util_ns_inside_rx_window.description`:

Description
-----------

Checks if sequence number of received PDU is in range of receive
window. Returns 0 for success, 1 otherwise

.. _`llc_util_nr_inside_tx_window`:

llc_util_nr_inside_tx_window
============================

.. c:function:: u16 llc_util_nr_inside_tx_window(struct sock *sk, u8 nr)

    check if sequence number is in tx window

    :param struct sock \*sk:
        current connection.

    :param u8 nr:
        N(R) of received PDU.

.. _`llc_util_nr_inside_tx_window.description`:

Description
-----------

This routine checks if N(R) of received PDU is in range of transmit
window; on the other hand checks if received PDU acknowledges some
outstanding PDUs that are in transmit window. Returns 0 for success, 1
otherwise.

.. _`llc_conn_ev_qlfy_last_frame_eq_1`:

llc_conn_ev_qlfy_last_frame_eq_1
================================

.. c:function:: int llc_conn_ev_qlfy_last_frame_eq_1(struct sock *sk, struct sk_buff *skb)

    checks if frame is last in tx window

    :param struct sock \*sk:
        current connection structure.

    :param struct sk_buff \*skb:
        current event.

.. _`llc_conn_ev_qlfy_last_frame_eq_1.description`:

Description
-----------

This function determines when frame which is sent, is last frame of
transmit window, if it is then this function return zero else return
one.  This function is used for sending last frame of transmit window
as I-format command with p-bit set to one. Returns 0 if frame is last
frame, 1 otherwise.

.. _`llc_conn_ev_qlfy_last_frame_eq_0`:

llc_conn_ev_qlfy_last_frame_eq_0
================================

.. c:function:: int llc_conn_ev_qlfy_last_frame_eq_0(struct sock *sk, struct sk_buff *skb)

    checks if frame isn't last in tx window

    :param struct sock \*sk:
        current connection structure.

    :param struct sk_buff \*skb:
        current event.

.. _`llc_conn_ev_qlfy_last_frame_eq_0.description`:

Description
-----------

This function determines when frame which is sent, isn't last frame of
transmit window, if it isn't then this function return zero else return
one. Returns 0 if frame isn't last frame, 1 otherwise.

.. This file was automatic generated / don't edit.

