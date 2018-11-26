.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/can/af_can.c

.. _`can_send`:

can_send
========

.. c:function:: int can_send(struct sk_buff *skb, int loop)

    transmit a CAN frame (optional with local loopback)

    :param skb:
        pointer to socket buffer with CAN frame in data section
    :type skb: struct sk_buff \*

    :param loop:
        loopback for listeners on local CAN sockets (recommended default!)
    :type loop: int

.. _`can_send.description`:

Description
-----------

Due to the loopback this routine must not be called from hardirq context.

.. _`can_send.return`:

Return
------

0 on success
-ENETDOWN when the selected interface is down
-ENOBUFS on full driver queue (see \ :c:func:`net_xmit_errno`\ )
-ENOMEM when local loopback failed at calling \ :c:func:`skb_clone`\ 
-EPERM when trying to send on a non-CAN interface
-EMSGSIZE CAN frame size is bigger than CAN interface MTU
-EINVAL when the skb->data does not contain a valid CAN frame

.. _`effhash`:

effhash
=======

.. c:function:: unsigned int effhash(canid_t can_id)

    hash function for 29 bit CAN identifier reduction

    :param can_id:
        29 bit CAN identifier
    :type can_id: canid_t

.. _`effhash.description`:

Description
-----------

To reduce the linear traversal in one linked list of \_single\_ EFF CAN
frame subscriptions the 29 bit identifier is mapped to 10 bits.
(see CAN_EFF_RCV_HASH_BITS definition)

.. _`effhash.return`:

Return
------

Hash value from 0x000 - 0x3FF ( enforced by CAN_EFF_RCV_HASH_BITS mask )

.. _`find_rcv_list`:

find_rcv_list
=============

.. c:function:: struct hlist_head *find_rcv_list(canid_t *can_id, canid_t *mask, struct can_dev_rcv_lists *d)

    determine optimal filterlist inside device filter struct

    :param can_id:
        pointer to CAN identifier of a given can_filter
    :type can_id: canid_t \*

    :param mask:
        pointer to CAN mask of a given can_filter
    :type mask: canid_t \*

    :param d:
        pointer to the device filter struct
    :type d: struct can_dev_rcv_lists \*

.. _`find_rcv_list.description`:

Description
-----------

Returns the optimal filterlist to reduce the filter handling in the
receive path. This function is called by service functions that need
to register or unregister a can_filter in the filter lists.

A filter matches in general, when

<received_can_id> & mask == can_id & mask

so every bit set in the mask (even CAN_EFF_FLAG, CAN_RTR_FLAG) describe
relevant bits for the filter.

The filter can be inverted (CAN_INV_FILTER bit set in can_id) or it can
filter for error messages (CAN_ERR_FLAG bit set in mask). For error msg
frames there is a special filterlist and a special rx path filter handling.

.. _`find_rcv_list.return`:

Return
------

Pointer to optimal filterlist for the given can_id/mask pair.
Constistency checked mask.
Reduced can_id to have a preprocessed filter compare value.

.. _`can_rx_register`:

can_rx_register
===============

.. c:function:: int can_rx_register(struct net *net, struct net_device *dev, canid_t can_id, canid_t mask, void (*func)(struct sk_buff *, void *), void *data, char *ident, struct sock *sk)

    subscribe CAN frames from a specific interface

    :param net:
        *undescribed*
    :type net: struct net \*

    :param dev:
        pointer to netdevice (NULL => subcribe from 'all' CAN devices list)
    :type dev: struct net_device \*

    :param can_id:
        CAN identifier (see description)
    :type can_id: canid_t

    :param mask:
        CAN mask (see description)
    :type mask: canid_t

    :param void (\*func)(struct sk_buff \*, void \*):
        callback function on filter match

    :param data:
        returned parameter for callback function
    :type data: void \*

    :param ident:
        string for calling module identification
    :type ident: char \*

    :param sk:
        socket pointer (might be NULL)
    :type sk: struct sock \*

.. _`can_rx_register.description`:

Description
-----------

Invokes the callback function with the received sk_buff and the given
parameter 'data' on a matching receive filter. A filter matches, when

<received_can_id> & mask == can_id & mask

The filter can be inverted (CAN_INV_FILTER bit set in can_id) or it can
filter for error message frames (CAN_ERR_FLAG bit set in mask).

The provided pointer to the sk_buff is guaranteed to be valid as long as
the callback function is running. The callback function must \*not\* free
the given sk_buff while processing it's task. When the given sk_buff is
needed after the end of the callback function it must be cloned inside
the callback function with \ :c:func:`skb_clone`\ .

.. _`can_rx_register.return`:

Return
------

0 on success
-ENOMEM on missing cache mem to create subscription entry
-ENODEV unknown device

.. _`can_rx_unregister`:

can_rx_unregister
=================

.. c:function:: void can_rx_unregister(struct net *net, struct net_device *dev, canid_t can_id, canid_t mask, void (*func)(struct sk_buff *, void *), void *data)

    unsubscribe CAN frames from a specific interface

    :param net:
        *undescribed*
    :type net: struct net \*

    :param dev:
        pointer to netdevice (NULL => unsubscribe from 'all' CAN devices list)
    :type dev: struct net_device \*

    :param can_id:
        CAN identifier
    :type can_id: canid_t

    :param mask:
        CAN mask
    :type mask: canid_t

    :param void (\*func)(struct sk_buff \*, void \*):
        callback function on filter match

    :param data:
        returned parameter for callback function
    :type data: void \*

.. _`can_rx_unregister.description`:

Description
-----------

Removes subscription entry depending on given (subscription) values.

.. _`can_proto_register`:

can_proto_register
==================

.. c:function:: int can_proto_register(const struct can_proto *cp)

    register CAN transport protocol

    :param cp:
        pointer to CAN protocol structure
    :type cp: const struct can_proto \*

.. _`can_proto_register.return`:

Return
------

0 on success
-EINVAL invalid (out of range) protocol number
-EBUSY  protocol already in use
-ENOBUF if \ :c:func:`proto_register`\  fails

.. _`can_proto_unregister`:

can_proto_unregister
====================

.. c:function:: void can_proto_unregister(const struct can_proto *cp)

    unregister CAN transport protocol

    :param cp:
        pointer to CAN protocol structure
    :type cp: const struct can_proto \*

.. This file was automatic generated / don't edit.

