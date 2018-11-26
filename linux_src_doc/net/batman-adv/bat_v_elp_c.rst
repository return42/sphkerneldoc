.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/bat_v_elp.c

.. _`batadv_v_elp_start_timer`:

batadv_v_elp_start_timer
========================

.. c:function:: void batadv_v_elp_start_timer(struct batadv_hard_iface *hard_iface)

    restart timer for ELP periodic work

    :param hard_iface:
        the interface for which the timer has to be reset
    :type hard_iface: struct batadv_hard_iface \*

.. _`batadv_v_elp_get_throughput`:

batadv_v_elp_get_throughput
===========================

.. c:function:: u32 batadv_v_elp_get_throughput(struct batadv_hardif_neigh_node *neigh)

    get the throughput towards a neighbour

    :param neigh:
        the neighbour for which the throughput has to be obtained
    :type neigh: struct batadv_hardif_neigh_node \*

.. _`batadv_v_elp_get_throughput.return`:

Return
------

The throughput towards the given neighbour in multiples of 100kpbs
(a value of '1' equals to 0.1Mbps, '10' equals 1Mbps, etc).

.. _`batadv_v_elp_throughput_metric_update`:

batadv_v_elp_throughput_metric_update
=====================================

.. c:function:: void batadv_v_elp_throughput_metric_update(struct work_struct *work)

    worker updating the throughput metric of a single hop neighbour

    :param work:
        the work queue item
    :type work: struct work_struct \*

.. _`batadv_v_elp_wifi_neigh_probe`:

batadv_v_elp_wifi_neigh_probe
=============================

.. c:function:: bool batadv_v_elp_wifi_neigh_probe(struct batadv_hardif_neigh_node *neigh)

    send link probing packets to a neighbour

    :param neigh:
        the neighbour to probe
    :type neigh: struct batadv_hardif_neigh_node \*

.. _`batadv_v_elp_wifi_neigh_probe.description`:

Description
-----------

Sends a predefined number of unicast wifi packets to a given neighbour in
order to trigger the throughput estimation on this link by the RC algorithm.
Packets are sent only if there there is not enough payload unicast traffic
towards this neighbour..

.. _`batadv_v_elp_wifi_neigh_probe.return`:

Return
------

True on success and false in case of error during skb preparation.

.. _`batadv_v_elp_periodic_work`:

batadv_v_elp_periodic_work
==========================

.. c:function:: void batadv_v_elp_periodic_work(struct work_struct *work)

    ELP periodic task per interface

    :param work:
        work queue item
    :type work: struct work_struct \*

.. _`batadv_v_elp_periodic_work.description`:

Description
-----------

Emits broadcast ELP message in regular intervals.

.. _`batadv_v_elp_iface_enable`:

batadv_v_elp_iface_enable
=========================

.. c:function:: int batadv_v_elp_iface_enable(struct batadv_hard_iface *hard_iface)

    setup the ELP interface private resources

    :param hard_iface:
        interface for which the data has to be prepared
    :type hard_iface: struct batadv_hard_iface \*

.. _`batadv_v_elp_iface_enable.return`:

Return
------

0 on success or a -ENOMEM in case of failure.

.. _`batadv_v_elp_iface_disable`:

batadv_v_elp_iface_disable
==========================

.. c:function:: void batadv_v_elp_iface_disable(struct batadv_hard_iface *hard_iface)

    release ELP interface private resources

    :param hard_iface:
        interface for which the resources have to be released
    :type hard_iface: struct batadv_hard_iface \*

.. _`batadv_v_elp_iface_activate`:

batadv_v_elp_iface_activate
===========================

.. c:function:: void batadv_v_elp_iface_activate(struct batadv_hard_iface *primary_iface, struct batadv_hard_iface *hard_iface)

    update the ELP buffer belonging to the given hard-interface

    :param primary_iface:
        the new primary interface
    :type primary_iface: struct batadv_hard_iface \*

    :param hard_iface:
        interface holding the to-be-updated buffer
    :type hard_iface: struct batadv_hard_iface \*

.. _`batadv_v_elp_primary_iface_set`:

batadv_v_elp_primary_iface_set
==============================

.. c:function:: void batadv_v_elp_primary_iface_set(struct batadv_hard_iface *primary_iface)

    change internal data to reflect the new primary interface

    :param primary_iface:
        the new primary interface
    :type primary_iface: struct batadv_hard_iface \*

.. _`batadv_v_elp_neigh_update`:

batadv_v_elp_neigh_update
=========================

.. c:function:: void batadv_v_elp_neigh_update(struct batadv_priv *bat_priv, u8 *neigh_addr, struct batadv_hard_iface *if_incoming, struct batadv_elp_packet *elp_packet)

    update an ELP neighbour node

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param neigh_addr:
        the neighbour interface address
    :type neigh_addr: u8 \*

    :param if_incoming:
        the interface the packet was received through
    :type if_incoming: struct batadv_hard_iface \*

    :param elp_packet:
        the received ELP packet
    :type elp_packet: struct batadv_elp_packet \*

.. _`batadv_v_elp_neigh_update.description`:

Description
-----------

Updates the ELP neighbour node state with the data received within the new
ELP packet.

.. _`batadv_v_elp_packet_recv`:

batadv_v_elp_packet_recv
========================

.. c:function:: int batadv_v_elp_packet_recv(struct sk_buff *skb, struct batadv_hard_iface *if_incoming)

    main ELP packet handler

    :param skb:
        the received packet
    :type skb: struct sk_buff \*

    :param if_incoming:
        the interface this packet was received through
    :type if_incoming: struct batadv_hard_iface \*

.. _`batadv_v_elp_packet_recv.return`:

Return
------

NET_RX_SUCCESS and consumes the skb if the packet was peoperly
processed or NET_RX_DROP in case of failure.

.. This file was automatic generated / don't edit.

