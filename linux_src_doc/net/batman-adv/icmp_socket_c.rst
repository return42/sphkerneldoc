.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/icmp_socket.c

.. _`batadv_socket_add_packet`:

batadv_socket_add_packet
========================

.. c:function:: void batadv_socket_add_packet(struct batadv_socket_client *socket_client, struct batadv_icmp_header *icmph, size_t icmp_len)

    schedule an icmp packet to be sent to userspace on an icmp socket.

    :param struct batadv_socket_client \*socket_client:
        the socket this packet belongs to

    :param struct batadv_icmp_header \*icmph:
        pointer to the header of the icmp packet

    :param size_t icmp_len:
        total length of the icmp packet

.. _`batadv_socket_receive_packet`:

batadv_socket_receive_packet
============================

.. c:function:: void batadv_socket_receive_packet(struct batadv_icmp_header *icmph, size_t icmp_len)

    schedule an icmp packet to be received locally and sent to userspace.

    :param struct batadv_icmp_header \*icmph:
        pointer to the header of the icmp packet

    :param size_t icmp_len:
        total length of the icmp packet

.. This file was automatic generated / don't edit.
