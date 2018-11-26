.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/llc/llc_if.c

.. _`llc_build_and_send_pkt`:

llc_build_and_send_pkt
======================

.. c:function:: int llc_build_and_send_pkt(struct sock *sk, struct sk_buff *skb)

    Connection data sending for upper layers.

    :param sk:
        connection
    :type sk: struct sock \*

    :param skb:
        packet to send
    :type skb: struct sk_buff \*

.. _`llc_build_and_send_pkt.description`:

Description
-----------

This function is called when upper layer wants to send data using
connection oriented communication mode. During sending data, connection
will be locked and received frames and expired timers will be queued.
Returns 0 for success, -ECONNABORTED when the connection already
closed and -EBUSY when sending data is not permitted in this state or
LLC has send an I pdu with p bit set to 1 and is waiting for it's
response.

.. _`llc_establish_connection`:

llc_establish_connection
========================

.. c:function:: int llc_establish_connection(struct sock *sk, u8 *lmac, u8 *dmac, u8 dsap)

    Called by upper layer to establish a conn

    :param sk:
        connection
    :type sk: struct sock \*

    :param lmac:
        local mac address
    :type lmac: u8 \*

    :param dmac:
        destination mac address
    :type dmac: u8 \*

    :param dsap:
        destination sap
    :type dsap: u8

.. _`llc_establish_connection.description`:

Description
-----------

Upper layer calls this to establish an LLC connection with a remote
machine. This function packages a proper event and sends it connection
component state machine. Success or failure of connection
establishment will inform to upper layer via calling it's confirm
function and passing proper information.

.. _`llc_send_disc`:

llc_send_disc
=============

.. c:function:: int llc_send_disc(struct sock *sk)

    Called by upper layer to close a connection

    :param sk:
        connection to be closed
    :type sk: struct sock \*

.. _`llc_send_disc.description`:

Description
-----------

Upper layer calls this when it wants to close an established LLC
connection with a remote machine. This function packages a proper event
and sends it to connection component state machine. Returns 0 for
success, 1 otherwise.

.. This file was automatic generated / don't edit.

