.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/decnet/dn_nsp_out.c

.. _`dn_nsp_clone_and_send`:

dn_nsp_clone_and_send
=====================

.. c:function:: unsigned int dn_nsp_clone_and_send(struct sk_buff *skb, gfp_t gfp)

    Send a data packet by cloning it

    :param struct sk_buff \*skb:
        The packet to clone and transmit

    :param gfp_t gfp:
        memory allocation flag

.. _`dn_nsp_clone_and_send.description`:

Description
-----------

Clone a queued data or other data packet and transmit it.

.. _`dn_nsp_clone_and_send.return`:

Return
------

The number of times the packet has been sent previously

.. _`dn_nsp_output`:

dn_nsp_output
=============

.. c:function:: void dn_nsp_output(struct sock *sk)

    Try and send something from socket queues

    :param struct sock \*sk:
        The socket whose queues are to be investigated

.. _`dn_nsp_output.description`:

Description
-----------

Try and send the packet on the end of the data and other data queues.
Other data gets priority over data, and if we retransmit a packet we
reduce the window by dividing it in two.

.. This file was automatic generated / don't edit.

