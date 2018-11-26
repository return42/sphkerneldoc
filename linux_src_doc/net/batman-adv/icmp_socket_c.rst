.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/icmp_socket.c

.. _`batadv_socket_init`:

batadv_socket_init
==================

.. c:function:: void batadv_socket_init( void)

    Initialize soft interface independent socket data

    :param void:
        no arguments
    :type void: 

.. _`batadv_socket_setup`:

batadv_socket_setup
===================

.. c:function:: int batadv_socket_setup(struct batadv_priv *bat_priv)

    Create debugfs "socket" file

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. _`batadv_socket_setup.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_socket_add_packet`:

batadv_socket_add_packet
========================

.. c:function:: void batadv_socket_add_packet(struct batadv_socket_client *socket_client, struct batadv_icmp_header *icmph, size_t icmp_len)

    schedule an icmp packet to be sent to userspace on an icmp socket.

    :param socket_client:
        the socket this packet belongs to
    :type socket_client: struct batadv_socket_client \*

    :param icmph:
        pointer to the header of the icmp packet
    :type icmph: struct batadv_icmp_header \*

    :param icmp_len:
        total length of the icmp packet
    :type icmp_len: size_t

.. _`batadv_socket_receive_packet`:

batadv_socket_receive_packet
============================

.. c:function:: void batadv_socket_receive_packet(struct batadv_icmp_header *icmph, size_t icmp_len)

    schedule an icmp packet to be received locally and sent to userspace.

    :param icmph:
        pointer to the header of the icmp packet
    :type icmph: struct batadv_icmp_header \*

    :param icmp_len:
        total length of the icmp packet
    :type icmp_len: size_t

.. This file was automatic generated / don't edit.

