.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/llc/llc_conn.c

.. _`llc_conn_state_process`:

llc_conn_state_process
======================

.. c:function:: int llc_conn_state_process(struct sock *sk, struct sk_buff *skb)

    sends event to connection state machine

    :param struct sock \*sk:
        connection

    :param struct sk_buff \*skb:
        occurred event

.. _`llc_conn_state_process.description`:

Description
-----------

Sends an event to connection state machine. After processing event
(executing it's actions and changing state), upper layer will be
indicated or confirmed, if needed. Returns 0 for success, 1 for
failure. The socket lock has to be held before calling this function.

.. _`llc_conn_rtn_pdu`:

llc_conn_rtn_pdu
================

.. c:function:: void llc_conn_rtn_pdu(struct sock *sk, struct sk_buff *skb)

    sends received data pdu to upper layer

    :param struct sock \*sk:
        Active connection

    :param struct sk_buff \*skb:
        Received data frame

.. _`llc_conn_rtn_pdu.description`:

Description
-----------

Sends received data pdu to upper layer (by using indicate function).
Prepares service parameters (prim and prim_data). calling indication
function will be done in llc_conn_state_process.

.. _`llc_conn_resend_i_pdu_as_cmd`:

llc_conn_resend_i_pdu_as_cmd
============================

.. c:function:: void llc_conn_resend_i_pdu_as_cmd(struct sock *sk, u8 nr, u8 first_p_bit)

    resend all all unacknowledged I PDUs

    :param struct sock \*sk:
        active connection

    :param u8 nr:
        NR

    :param u8 first_p_bit:
        p_bit value of first pdu

.. _`llc_conn_resend_i_pdu_as_cmd.description`:

Description
-----------

Resend all unacknowledged I PDUs, starting with the NR; send first as
command PDU with P bit equal first_p_bit; if more than one send
subsequent as command PDUs with P bit equal zero (0).

.. _`llc_conn_resend_i_pdu_as_rsp`:

llc_conn_resend_i_pdu_as_rsp
============================

.. c:function:: void llc_conn_resend_i_pdu_as_rsp(struct sock *sk, u8 nr, u8 first_f_bit)

    Resend all unacknowledged I PDUs

    :param struct sock \*sk:
        active connection.

    :param u8 nr:
        NR

    :param u8 first_f_bit:
        f_bit value of first pdu.

.. _`llc_conn_resend_i_pdu_as_rsp.description`:

Description
-----------

Resend all unacknowledged I PDUs, starting with the NR; send first as
response PDU with F bit equal first_f_bit; if more than one send
subsequent as response PDUs with F bit equal zero (0).

.. _`llc_conn_remove_acked_pdus`:

llc_conn_remove_acked_pdus
==========================

.. c:function:: int llc_conn_remove_acked_pdus(struct sock *sk, u8 nr, u16 *how_many_unacked)

    Removes acknowledged pdus from tx queue

    :param struct sock \*sk:
        active connection
        nr: NR

    :param u8 nr:
        *undescribed*

    :param u16 \*how_many_unacked:
        *undescribed*

.. _`llc_conn_remove_acked_pdus.how_many_unacked`:

how_many_unacked
----------------

size of pdu_unack_q after removing acked pdus

Removes acknowledged pdus from transmit queue (pdu_unack_q). Returns
the number of pdus that removed from queue.

.. _`llc_conn_send_pdus`:

llc_conn_send_pdus
==================

.. c:function:: void llc_conn_send_pdus(struct sock *sk)

    Sends queued PDUs

    :param struct sock \*sk:
        active connection

.. _`llc_conn_send_pdus.description`:

Description
-----------

Sends queued pdus to MAC layer for transmission.

.. _`llc_conn_service`:

llc_conn_service
================

.. c:function:: int llc_conn_service(struct sock *sk, struct sk_buff *skb)

    finds transition and changes state of connection

    :param struct sock \*sk:
        connection

    :param struct sk_buff \*skb:
        happened event

.. _`llc_conn_service.description`:

Description
-----------

This function finds transition that matches with happened event, then
executes related actions and finally changes state of connection.
Returns 0 for success, 1 for failure.

.. _`llc_qualify_conn_ev`:

llc_qualify_conn_ev
===================

.. c:function:: struct llc_conn_state_trans *llc_qualify_conn_ev(struct sock *sk, struct sk_buff *skb)

    finds transition for event

    :param struct sock \*sk:
        connection

    :param struct sk_buff \*skb:
        happened event

.. _`llc_qualify_conn_ev.description`:

Description
-----------

This function finds transition that matches with happened event.
Returns pointer to found transition on success, \ ``NULL``\  otherwise.

.. _`llc_exec_conn_trans_actions`:

llc_exec_conn_trans_actions
===========================

.. c:function:: int llc_exec_conn_trans_actions(struct sock *sk, struct llc_conn_state_trans *trans, struct sk_buff *skb)

    executes related actions

    :param struct sock \*sk:
        connection

    :param struct llc_conn_state_trans \*trans:
        transition that it's actions must be performed

    :param struct sk_buff \*skb:
        event

.. _`llc_exec_conn_trans_actions.description`:

Description
-----------

Executes actions that is related to happened event. Returns 0 for
success, 1 to indicate failure of at least one action.

.. _`__llc_lookup_established`:

__llc_lookup_established
========================

.. c:function:: struct sock *__llc_lookup_established(struct llc_sap *sap, struct llc_addr *daddr, struct llc_addr *laddr)

    Finds connection for the remote/local sap/mac

    :param struct llc_sap \*sap:
        SAP

    :param struct llc_addr \*daddr:
        address of remote LLC (MAC + SAP)

    :param struct llc_addr \*laddr:
        address of local LLC (MAC + SAP)

.. _`__llc_lookup_established.description`:

Description
-----------

Search connection list of the SAP and finds connection using the remote
mac, remote sap, local mac, and local sap. Returns pointer for
connection found, \ ``NULL``\  otherwise.
Caller has to make sure local_bh is disabled.

.. _`llc_lookup_listener`:

llc_lookup_listener
===================

.. c:function:: struct sock *llc_lookup_listener(struct llc_sap *sap, struct llc_addr *laddr)

    Finds listener for local MAC + SAP

    :param struct llc_sap \*sap:
        SAP

    :param struct llc_addr \*laddr:
        address of local LLC (MAC + SAP)

.. _`llc_lookup_listener.description`:

Description
-----------

Search connection list of the SAP and finds connection listening on
local mac, and local sap. Returns pointer for parent socket found,
\ ``NULL``\  otherwise.
Caller has to make sure local_bh is disabled.

.. _`llc_data_accept_state`:

llc_data_accept_state
=====================

.. c:function:: u8 llc_data_accept_state(u8 state)

    designates if in this state data can be sent.

    :param u8 state:
        state of connection.

.. _`llc_data_accept_state.description`:

Description
-----------

Returns 0 if data can be sent, 1 otherwise.

.. _`llc_find_next_offset`:

llc_find_next_offset
====================

.. c:function:: u16 llc_find_next_offset(struct llc_conn_state *state, u16 offset)

    finds offset for next category of transitions

    :param struct llc_conn_state \*state:
        state table.

    :param u16 offset:
        start offset.

.. _`llc_find_next_offset.description`:

Description
-----------

Finds offset of next category of transitions in transition table.
Returns the start index of next category.

.. _`llc_build_offset_table`:

llc_build_offset_table
======================

.. c:function:: void llc_build_offset_table( void)

    builds offset table of connection

    :param  void:
        no arguments

.. _`llc_build_offset_table.description`:

Description
-----------

Fills offset table of connection state transition table
(llc_offset_table).

.. _`llc_find_offset`:

llc_find_offset
===============

.. c:function:: int llc_find_offset(int state, int ev_type)

    finds start offset of category of transitions

    :param int state:
        state of connection

    :param int ev_type:
        type of happened event

.. _`llc_find_offset.description`:

Description
-----------

Finds start offset of desired category of transitions. Returns the
desired start offset.

.. _`llc_sap_add_socket`:

llc_sap_add_socket
==================

.. c:function:: void llc_sap_add_socket(struct llc_sap *sap, struct sock *sk)

    adds a socket to a SAP

    :param struct llc_sap \*sap:
        SAP

    :param struct sock \*sk:
        socket

.. _`llc_sap_add_socket.description`:

Description
-----------

This function adds a socket to the hash tables of a SAP.

.. _`llc_sap_remove_socket`:

llc_sap_remove_socket
=====================

.. c:function:: void llc_sap_remove_socket(struct llc_sap *sap, struct sock *sk)

    removes a socket from SAP

    :param struct llc_sap \*sap:
        SAP

    :param struct sock \*sk:
        socket

.. _`llc_sap_remove_socket.description`:

Description
-----------

This function removes a connection from the hash tables of a SAP if
the connection was in this list.

.. _`llc_conn_rcv`:

llc_conn_rcv
============

.. c:function:: int llc_conn_rcv(struct sock *sk, struct sk_buff *skb)

    sends received pdus to the connection state machine

    :param struct sock \*sk:
        current connection structure.

    :param struct sk_buff \*skb:
        received frame.

.. _`llc_conn_rcv.description`:

Description
-----------

Sends received pdus to the connection state machine.

.. _`llc_backlog_rcv`:

llc_backlog_rcv
===============

.. c:function:: int llc_backlog_rcv(struct sock *sk, struct sk_buff *skb)

    Processes rx frames and expired timers.

    :param struct sock \*sk:
        LLC sock (p8022 connection)

    :param struct sk_buff \*skb:
        queued rx frame or event

.. _`llc_backlog_rcv.description`:

Description
-----------

This function processes frames that has received and timers that has
expired during sending an I pdu (refer to data_req_handler).  frames
queue by llc_rcv function (llc_mac.c) and timers queue by timer
callback functions(llc_c_ac.c).

.. _`llc_sk_init`:

llc_sk_init
===========

.. c:function:: void llc_sk_init(struct sock *sk)

    Initializes a socket with default llc values.

    :param struct sock \*sk:
        socket to initialize.

.. _`llc_sk_init.description`:

Description
-----------

Initializes a socket with default llc values.

.. _`llc_sk_alloc`:

llc_sk_alloc
============

.. c:function:: struct sock *llc_sk_alloc(struct net *net, int family, gfp_t priority, struct proto *prot, int kern)

    Allocates LLC sock

    :param struct net \*net:
        *undescribed*

    :param int family:
        upper layer protocol family

    :param gfp_t priority:
        for allocation (\ ``GFP_KERNEL``\ , \ ``GFP_ATOMIC``\ , etc)

    :param struct proto \*prot:
        *undescribed*

    :param int kern:
        *undescribed*

.. _`llc_sk_alloc.description`:

Description
-----------

Allocates a LLC sock and initializes it. Returns the new LLC sock
or \ ``NULL``\  if there's no memory available for one

.. _`llc_sk_free`:

llc_sk_free
===========

.. c:function:: void llc_sk_free(struct sock *sk)

    Frees a LLC socket \ ``sk``\  - socket to free

    :param struct sock \*sk:
        *undescribed*

.. _`llc_sk_free.description`:

Description
-----------

Frees a LLC socket

.. _`llc_sk_reset`:

llc_sk_reset
============

.. c:function:: void llc_sk_reset(struct sock *sk)

    resets a connection

    :param struct sock \*sk:
        LLC socket to reset

.. _`llc_sk_reset.description`:

Description
-----------

Resets a connection to the out of service state. Stops its timers
and frees any frames in the queues of the connection.

.. This file was automatic generated / don't edit.

