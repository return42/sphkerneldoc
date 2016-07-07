.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/iucv/af_iucv.c

.. _`afiucv_pm_freeze`:

afiucv_pm_freeze
================

.. c:function:: int afiucv_pm_freeze(struct device *dev)

    Freeze PM callback

    :param struct device \*dev:
        AFIUCV dummy device

.. _`afiucv_pm_freeze.description`:

Description
-----------

Sever all established IUCV communication pathes

.. _`afiucv_pm_restore_thaw`:

afiucv_pm_restore_thaw
======================

.. c:function:: int afiucv_pm_restore_thaw(struct device *dev)

    Thaw and restore PM callback

    :param struct device \*dev:
        AFIUCV dummy device

.. _`afiucv_pm_restore_thaw.description`:

Description
-----------

socket clean up after freeze

.. _`iucv_msg_length`:

iucv_msg_length
===============

.. c:function:: size_t iucv_msg_length(struct iucv_message *msg)

    Returns the length of an iucv message.

    :param struct iucv_message \*msg:
        Pointer to struct iucv_message, MUST NOT be NULL

.. _`iucv_msg_length.description`:

Description
-----------

The function returns the length of the specified iucv message \ ``msg``\  of data
stored in a buffer and of data stored in the parameter list (PRMDATA).

For IUCV_IPRMDATA, AF_IUCV uses the following convention to transport socket

.. _`iucv_msg_length.data`:

data
----

PRMDATA[0..6]   socket data (max 7 bytes);
PRMDATA[7]      socket data length value (len is 0xff - PRMDATA[7])

The socket data length is computed by subtracting the socket data length
value from 0xFF.
If the socket data len is greater 7, then PRMDATA can be used for special
notifications (see iucv_sock_shutdown); and further,
if the socket data len is > 7, the function returns 8.

Use this function to allocate socket buffers to store iucv message data.

.. _`iucv_sock_in_state`:

iucv_sock_in_state
==================

.. c:function:: int iucv_sock_in_state(struct sock *sk, int state, int state2)

    check for specific states

    :param struct sock \*sk:
        sock structure

    :param int state:
        second iucv sk state

    :param int state2:
        *undescribed*

.. _`iucv_sock_in_state.description`:

Description
-----------

Returns true if the socket in either in the first or second state.

.. _`iucv_below_msglim`:

iucv_below_msglim
=================

.. c:function:: int iucv_below_msglim(struct sock *sk)

    function to check if messages can be sent

    :param struct sock \*sk:
        sock structure

.. _`iucv_below_msglim.description`:

Description
-----------

Returns true if the send queue length is lower than the message limit.
Always returns true if the socket is not connected (no iucv path for
checking the message limit).

.. _`iucv_sock_wake_msglim`:

iucv_sock_wake_msglim
=====================

.. c:function:: void iucv_sock_wake_msglim(struct sock *sk)

    Wake up thread waiting on msg limit

    :param struct sock \*sk:
        *undescribed*

.. _`afiucv_hs_send`:

afiucv_hs_send
==============

.. c:function:: int afiucv_hs_send(struct iucv_message *imsg, struct sock *sock, struct sk_buff *skb, u8 flags)

    send a message through HiperSockets transport

    :param struct iucv_message \*imsg:
        *undescribed*

    :param struct sock \*sock:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

    :param u8 flags:
        *undescribed*

.. _`iucv_send_iprm`:

iucv_send_iprm
==============

.. c:function:: int iucv_send_iprm(struct iucv_path *path, struct iucv_message *msg, struct sk_buff *skb)

    Send socket data in parameter list of an iucv message.

    :param struct iucv_path \*path:
        IUCV path

    :param struct iucv_message \*msg:
        Pointer to a struct iucv_message

    :param struct sk_buff \*skb:
        The socket data to send, skb->len MUST BE <= 7

.. _`iucv_send_iprm.description`:

Description
-----------

Send the socket data in the parameter list in the iucv message
(IUCV_IPRMDATA). The socket data is stored at index 0 to 6 in the parameter
list and the socket data len at index 7 (last byte).
See also \ :c:func:`iucv_msg_length`\ .

Returns the error code from the \ :c:func:`iucv_message_send`\  call.

.. _`afiucv_hs_callback_syn`:

afiucv_hs_callback_syn
======================

.. c:function:: int afiucv_hs_callback_syn(struct sock *sk, struct sk_buff *skb)

    react on received SYN

    :param struct sock \*sk:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. _`afiucv_hs_callback_synack`:

afiucv_hs_callback_synack
=========================

.. c:function:: int afiucv_hs_callback_synack(struct sock *sk, struct sk_buff *skb)

    react on received SYN-ACK

    :param struct sock \*sk:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. _`afiucv_hs_callback_synfin`:

afiucv_hs_callback_synfin
=========================

.. c:function:: int afiucv_hs_callback_synfin(struct sock *sk, struct sk_buff *skb)

    react on received SYN_FIN

    :param struct sock \*sk:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. _`afiucv_hs_callback_fin`:

afiucv_hs_callback_fin
======================

.. c:function:: int afiucv_hs_callback_fin(struct sock *sk, struct sk_buff *skb)

    react on received FIN

    :param struct sock \*sk:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. _`afiucv_hs_callback_win`:

afiucv_hs_callback_win
======================

.. c:function:: int afiucv_hs_callback_win(struct sock *sk, struct sk_buff *skb)

    react on received WIN

    :param struct sock \*sk:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. _`afiucv_hs_callback_rx`:

afiucv_hs_callback_rx
=====================

.. c:function:: int afiucv_hs_callback_rx(struct sock *sk, struct sk_buff *skb)

    react on received data

    :param struct sock \*sk:
        *undescribed*

    :param struct sk_buff \*skb:
        *undescribed*

.. _`afiucv_hs_rcv`:

afiucv_hs_rcv
=============

.. c:function:: int afiucv_hs_rcv(struct sk_buff *skb, struct net_device *dev, struct packet_type *pt, struct net_device *orig_dev)

    base function for arriving data through HiperSockets transport called from netif RX softirq

    :param struct sk_buff \*skb:
        *undescribed*

    :param struct net_device \*dev:
        *undescribed*

    :param struct packet_type \*pt:
        *undescribed*

    :param struct net_device \*orig_dev:
        *undescribed*

.. _`afiucv_hs_callback_txnotify`:

afiucv_hs_callback_txnotify
===========================

.. c:function:: void afiucv_hs_callback_txnotify(struct sk_buff *skb, enum iucv_tx_notify n)

    handle send notifcations from HiperSockets transport

    :param struct sk_buff \*skb:
        *undescribed*

    :param enum iucv_tx_notify n:
        *undescribed*

.. This file was automatic generated / don't edit.

