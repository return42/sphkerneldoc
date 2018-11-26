.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/appletalk/ddp.c

.. _`atalk_find_or_insert_socket`:

atalk_find_or_insert_socket
===========================

.. c:function:: struct sock *atalk_find_or_insert_socket(struct sock *sk, struct sockaddr_at *sat)

    Try to find a socket matching ADDR

    :param sk:
        socket to insert in the list if it is not there already
    :type sk: struct sock \*

    :param sat:
        address to search for
    :type sat: struct sockaddr_at \*

.. _`atalk_find_or_insert_socket.description`:

Description
-----------

Try to find a socket matching ADDR in the socket list, if found then return
it. If not, insert SK into the socket list.

This entire operation must execute atomically.

.. _`atalk_pick_and_bind_port`:

atalk_pick_and_bind_port
========================

.. c:function:: int atalk_pick_and_bind_port(struct sock *sk, struct sockaddr_at *sat)

    Pick a source port when one is not given

    :param sk:
        socket to insert into the tables
    :type sk: struct sock \*

    :param sat:
        address to search for
    :type sat: struct sockaddr_at \*

.. _`atalk_pick_and_bind_port.description`:

Description
-----------

Pick a source port when one is not given. If we can find a suitable free
one, we insert the socket into the tables using it.

This whole operation must be atomic.

.. _`atalk_rcv`:

atalk_rcv
=========

.. c:function:: int atalk_rcv(struct sk_buff *skb, struct net_device *dev, struct packet_type *pt, struct net_device *orig_dev)

    Receive a packet (in skb) from device dev \ ``skb``\  - packet received \ ``dev``\  - network device where the packet comes from \ ``pt``\  - packet type

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

    :param pt:
        *undescribed*
    :type pt: struct packet_type \*

    :param orig_dev:
        *undescribed*
    :type orig_dev: struct net_device \*

.. _`atalk_rcv.description`:

Description
-----------

Receive a packet (in skb) from device dev. This has come from the SNAP
decoder, and on entry skb->transport_header is the DDP header, skb->len
is the DDP header, skb->len is the DDP length. The physical headers
have been extracted. PPP should probably pass frames marked as for this
layer.  [ie ARPHRD_ETHERTALK]

.. This file was automatic generated / don't edit.

