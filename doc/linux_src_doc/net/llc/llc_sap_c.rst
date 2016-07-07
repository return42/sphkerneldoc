.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/llc/llc_sap.c

.. _`llc_alloc_frame`:

llc_alloc_frame
===============

.. c:function:: struct sk_buff *llc_alloc_frame(struct sock *sk, struct net_device *dev, u8 type, u32 data_size)

    allocates sk_buff for frame

    :param struct sock \*sk:
        *undescribed*

    :param struct net_device \*dev:
        network device this skb will be sent over

    :param u8 type:
        pdu type to allocate

    :param u32 data_size:
        data size to allocate

.. _`llc_alloc_frame.description`:

Description
-----------

Allocates an sk_buff for frame and initializes sk_buff fields.
Returns allocated skb or \ ``NULL``\  when out of memory.

.. _`llc_sap_rtn_pdu`:

llc_sap_rtn_pdu
===============

.. c:function:: void llc_sap_rtn_pdu(struct llc_sap *sap, struct sk_buff *skb)

    Informs upper layer on rx of an UI, XID or TEST pdu.

    :param struct llc_sap \*sap:
        pointer to SAP

    :param struct sk_buff \*skb:
        received pdu

.. _`llc_find_sap_trans`:

llc_find_sap_trans
==================

.. c:function:: struct llc_sap_state_trans *llc_find_sap_trans(struct llc_sap *sap, struct sk_buff *skb)

    finds transition for event

    :param struct llc_sap \*sap:
        pointer to SAP

    :param struct sk_buff \*skb:
        happened event

.. _`llc_find_sap_trans.description`:

Description
-----------

This function finds transition that matches with happened event.
Returns the pointer to found transition on success or \ ``NULL``\  for
failure.

.. _`llc_exec_sap_trans_actions`:

llc_exec_sap_trans_actions
==========================

.. c:function:: int llc_exec_sap_trans_actions(struct llc_sap *sap, struct llc_sap_state_trans *trans, struct sk_buff *skb)

    execute actions related to event

    :param struct llc_sap \*sap:
        pointer to SAP

    :param struct llc_sap_state_trans \*trans:
        pointer to transition that it's actions must be performed

    :param struct sk_buff \*skb:
        happened event.

.. _`llc_exec_sap_trans_actions.description`:

Description
-----------

This function executes actions that is related to happened event.
Returns 0 for success and 1 for failure of at least one action.

.. _`llc_sap_next_state`:

llc_sap_next_state
==================

.. c:function:: int llc_sap_next_state(struct llc_sap *sap, struct sk_buff *skb)

    finds transition, execs actions & change SAP state

    :param struct llc_sap \*sap:
        pointer to SAP

    :param struct sk_buff \*skb:
        happened event

.. _`llc_sap_next_state.description`:

Description
-----------

This function finds transition that matches with happened event, then
executes related actions and finally changes state of SAP. It returns
0 on success and 1 for failure.

.. _`llc_sap_state_process`:

llc_sap_state_process
=====================

.. c:function:: void llc_sap_state_process(struct llc_sap *sap, struct sk_buff *skb)

    sends event to SAP state machine

    :param struct llc_sap \*sap:
        sap to use

    :param struct sk_buff \*skb:
        pointer to occurred event

.. _`llc_sap_state_process.description`:

Description
-----------

After executing actions of the event, upper layer will be indicated
if needed(on receiving an UI frame). sk can be null for the
datalink_proto case.

.. _`llc_build_and_send_test_pkt`:

llc_build_and_send_test_pkt
===========================

.. c:function:: void llc_build_and_send_test_pkt(struct llc_sap *sap, struct sk_buff *skb, u8 *dmac, u8 dsap)

    TEST interface for upper layers.

    :param struct llc_sap \*sap:
        sap to use

    :param struct sk_buff \*skb:
        packet to send

    :param u8 \*dmac:
        destination mac address

    :param u8 dsap:
        destination sap

.. _`llc_build_and_send_test_pkt.description`:

Description
-----------

This function is called when upper layer wants to send a TEST pdu.
Returns 0 for success, 1 otherwise.

.. _`llc_build_and_send_xid_pkt`:

llc_build_and_send_xid_pkt
==========================

.. c:function:: void llc_build_and_send_xid_pkt(struct llc_sap *sap, struct sk_buff *skb, u8 *dmac, u8 dsap)

    XID interface for upper layers

    :param struct llc_sap \*sap:
        sap to use

    :param struct sk_buff \*skb:
        packet to send

    :param u8 \*dmac:
        destination mac address

    :param u8 dsap:
        destination sap

.. _`llc_build_and_send_xid_pkt.description`:

Description
-----------

This function is called when upper layer wants to send a XID pdu.
Returns 0 for success, 1 otherwise.

.. _`llc_sap_rcv`:

llc_sap_rcv
===========

.. c:function:: void llc_sap_rcv(struct llc_sap *sap, struct sk_buff *skb, struct sock *sk)

    sends received pdus to the sap state machine

    :param struct llc_sap \*sap:
        current sap component structure.

    :param struct sk_buff \*skb:
        received frame.

    :param struct sock \*sk:
        *undescribed*

.. _`llc_sap_rcv.description`:

Description
-----------

Sends received pdus to the sap state machine.

.. _`llc_lookup_dgram`:

llc_lookup_dgram
================

.. c:function:: struct sock *llc_lookup_dgram(struct llc_sap *sap, const struct llc_addr *laddr)

    Finds dgram socket for the local sap/mac

    :param struct llc_sap \*sap:
        SAP

    :param const struct llc_addr \*laddr:
        address of local LLC (MAC + SAP)

.. _`llc_lookup_dgram.description`:

Description
-----------

Search socket list of the SAP and finds connection using the local
mac, and local sap. Returns pointer for socket found, \ ``NULL``\  otherwise.

.. _`llc_sap_mcast`:

llc_sap_mcast
=============

.. c:function:: void llc_sap_mcast(struct llc_sap *sap, const struct llc_addr *laddr, struct sk_buff *skb)

    Deliver multicast PDU's to all matching datagram sockets.

    :param struct llc_sap \*sap:
        SAP

    :param const struct llc_addr \*laddr:
        address of local LLC (MAC + SAP)

    :param struct sk_buff \*skb:
        *undescribed*

.. _`llc_sap_mcast.description`:

Description
-----------

Search socket list of the SAP and finds connections with same sap.
Deliver clone to each.

.. This file was automatic generated / don't edit.

