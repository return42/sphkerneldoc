
.. _API-wimax-msg-send:

==============
wimax_msg_send
==============

*man wimax_msg_send(9)*

*4.6.0-rc1*

Send a pre-allocated message to user space


Synopsis
========

.. c:function:: int wimax_msg_send( struct wimax_dev * wimax_dev, struct sk_buff * skb )

Arguments
=========

``wimax_dev``
    WiMAX device descriptor

``skb``
    ``struct sk_buff`` returned by ``wimax_msg_alloc``. Note the ownership of ``skb`` is transferred to this function.


Returns
=======

0 if ok, < 0 errno code on error


Description
===========

Sends a free-form message that was preallocated with ``wimax_msg_alloc`` and filled up.

Assumes that once you pass an skb to this function for sending, it owns it and will release it when done (on success).


IMPORTANT
=========

Don't use ``skb_push``/``skb_pull``/``skb_reserve`` on the skb, as ``wimax_msg_send`` depends on skb->data being placed at the beginning of the user message.

Unlike other WiMAX stack calls, this call can be used way early, even before ``wimax_dev_add`` is called, as long as the wimax_dev->net_dev pointer is set to point to a proper
net_dev. This is so that drivers can use it early in case they need to send stuff around or communicate with user space.
