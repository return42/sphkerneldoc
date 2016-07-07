.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/bat_v_ogm.c

.. _`batadv_v_ogm_orig_get`:

batadv_v_ogm_orig_get
=====================

.. c:function:: struct batadv_orig_node *batadv_v_ogm_orig_get(struct batadv_priv *bat_priv, const u8 *addr)

    retrieve and possibly create an originator node

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param const u8 \*addr:
        the address of the originator

.. _`batadv_v_ogm_orig_get.return`:

Return
------

the orig_node corresponding to the specified address. If such object
does not exist it is allocated here. In case of allocation failure returns
NULL.

.. _`batadv_v_ogm_start_timer`:

batadv_v_ogm_start_timer
========================

.. c:function:: void batadv_v_ogm_start_timer(struct batadv_priv *bat_priv)

    restart the OGM sending timer

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_v_ogm_send_to_if`:

batadv_v_ogm_send_to_if
=======================

.. c:function:: void batadv_v_ogm_send_to_if(struct sk_buff *skb, struct batadv_hard_iface *hard_iface)

    send a batman ogm using a given interface

    :param struct sk_buff \*skb:
        the OGM to send

    :param struct batadv_hard_iface \*hard_iface:
        the interface to use to send the OGM

.. _`batadv_v_ogm_send`:

batadv_v_ogm_send
=================

.. c:function:: void batadv_v_ogm_send(struct work_struct *work)

    periodic worker broadcasting the own OGM

    :param struct work_struct \*work:
        work queue item

.. _`batadv_v_ogm_iface_enable`:

batadv_v_ogm_iface_enable
=========================

.. c:function:: int batadv_v_ogm_iface_enable(struct batadv_hard_iface *hard_iface)

    prepare an interface for B.A.T.M.A.N. V

    :param struct batadv_hard_iface \*hard_iface:
        the interface to prepare

.. _`batadv_v_ogm_iface_enable.description`:

Description
-----------

Takes care of scheduling own OGM sending routine for this interface.

.. _`batadv_v_ogm_iface_enable.return`:

Return
------

0 on success or a negative error code otherwise

.. _`batadv_v_ogm_primary_iface_set`:

batadv_v_ogm_primary_iface_set
==============================

.. c:function:: void batadv_v_ogm_primary_iface_set(struct batadv_hard_iface *primary_iface)

    set a new primary interface

    :param struct batadv_hard_iface \*primary_iface:
        the new primary interface

.. _`batadv_v_forward_penalty`:

batadv_v_forward_penalty
========================

.. c:function:: u32 batadv_v_forward_penalty(struct batadv_priv *bat_priv, struct batadv_hard_iface *if_incoming, struct batadv_hard_iface *if_outgoing, u32 throughput)

    apply a penalty to the throughput metric forwarded with B.A.T.M.A.N. V OGMs

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_hard_iface \*if_incoming:
        the interface where the OGM has been received

    :param struct batadv_hard_iface \*if_outgoing:
        the interface where the OGM has to be forwarded to

    :param u32 throughput:
        the current throughput

.. _`batadv_v_forward_penalty.description`:

Description
-----------

Apply a penalty on the current throughput metric value based on the
characteristic of the interface where the OGM has been received. The return

.. _`batadv_v_forward_penalty.value-is-computed-as-follows`:

value is computed as follows
----------------------------

- throughput \* 50%          if the incoming and outgoing interface are the
same WiFi interface and the throughput is above
1MBit/s
- throughput                if the outgoing interface is the default
interface (i.e. this OGM is processed for the
internal table and not forwarded)
- throughput \* hop penalty  otherwise

.. _`batadv_v_forward_penalty.return`:

Return
------

the penalised throughput metric.

.. _`batadv_v_ogm_forward`:

batadv_v_ogm_forward
====================

.. c:function:: void batadv_v_ogm_forward(struct batadv_priv *bat_priv, const struct batadv_ogm2_packet *ogm_received, struct batadv_orig_node *orig_node, struct batadv_neigh_node *neigh_node, struct batadv_hard_iface *if_incoming, struct batadv_hard_iface *if_outgoing)

    check conditions and forward an OGM to the given outgoing interface

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param const struct batadv_ogm2_packet \*ogm_received:
        previously received OGM to be forwarded

    :param struct batadv_orig_node \*orig_node:
        the originator which has been updated

    :param struct batadv_neigh_node \*neigh_node:
        the neigh_node through with the OGM has been received

    :param struct batadv_hard_iface \*if_incoming:
        the interface on which this OGM was received on

    :param struct batadv_hard_iface \*if_outgoing:
        the interface to which the OGM has to be forwarded to

.. _`batadv_v_ogm_forward.description`:

Description
-----------

Forward an OGM to an interface after having altered the throughput metric and
the TTL value contained in it. The original OGM isn't modified.

.. _`batadv_v_ogm_metric_update`:

batadv_v_ogm_metric_update
==========================

.. c:function:: int batadv_v_ogm_metric_update(struct batadv_priv *bat_priv, const struct batadv_ogm2_packet *ogm2, struct batadv_orig_node *orig_node, struct batadv_neigh_node *neigh_node, struct batadv_hard_iface *if_incoming, struct batadv_hard_iface *if_outgoing)

    update route metric based on OGM

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param const struct batadv_ogm2_packet \*ogm2:
        OGM2 structure

    :param struct batadv_orig_node \*orig_node:
        Originator structure for which the OGM has been received

    :param struct batadv_neigh_node \*neigh_node:
        the neigh_node through with the OGM has been received

    :param struct batadv_hard_iface \*if_incoming:
        the interface where this packet was received

    :param struct batadv_hard_iface \*if_outgoing:
        the interface for which the packet should be considered

.. _`batadv_v_ogm_metric_update.return`:

Return
------

1  if the OGM is new,
0  if it is not new but valid,
<0 on error (e.g. old OGM)

.. _`batadv_v_ogm_route_update`:

batadv_v_ogm_route_update
=========================

.. c:function:: bool batadv_v_ogm_route_update(struct batadv_priv *bat_priv, const struct ethhdr *ethhdr, const struct batadv_ogm2_packet *ogm2, struct batadv_orig_node *orig_node, struct batadv_neigh_node *neigh_node, struct batadv_hard_iface *if_incoming, struct batadv_hard_iface *if_outgoing)

    update routes based on OGM

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param const struct ethhdr \*ethhdr:
        the Ethernet header of the OGM2

    :param const struct batadv_ogm2_packet \*ogm2:
        OGM2 structure

    :param struct batadv_orig_node \*orig_node:
        Originator structure for which the OGM has been received

    :param struct batadv_neigh_node \*neigh_node:
        the neigh_node through with the OGM has been received

    :param struct batadv_hard_iface \*if_incoming:
        the interface where this packet was received

    :param struct batadv_hard_iface \*if_outgoing:
        the interface for which the packet should be considered

.. _`batadv_v_ogm_route_update.return`:

Return
------

true if the packet should be forwarded, false otherwise

.. _`batadv_v_ogm_process_per_outif`:

batadv_v_ogm_process_per_outif
==============================

.. c:function:: void batadv_v_ogm_process_per_outif(struct batadv_priv *bat_priv, const struct ethhdr *ethhdr, const struct batadv_ogm2_packet *ogm2, struct batadv_orig_node *orig_node, struct batadv_neigh_node *neigh_node, struct batadv_hard_iface *if_incoming, struct batadv_hard_iface *if_outgoing)

    process a batman v OGM for an outgoing if

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param const struct ethhdr \*ethhdr:
        the Ethernet header of the OGM2

    :param const struct batadv_ogm2_packet \*ogm2:
        OGM2 structure

    :param struct batadv_orig_node \*orig_node:
        Originator structure for which the OGM has been received

    :param struct batadv_neigh_node \*neigh_node:
        the neigh_node through with the OGM has been received

    :param struct batadv_hard_iface \*if_incoming:
        the interface where this packet was received

    :param struct batadv_hard_iface \*if_outgoing:
        the interface for which the packet should be considered

.. _`batadv_v_ogm_aggr_packet`:

batadv_v_ogm_aggr_packet
========================

.. c:function:: bool batadv_v_ogm_aggr_packet(int buff_pos, int packet_len, __be16 tvlv_len)

    checks if there is another OGM aggregated

    :param int buff_pos:
        current position in the skb

    :param int packet_len:
        total length of the skb

    :param __be16 tvlv_len:
        tvlv length of the previously considered OGM

.. _`batadv_v_ogm_aggr_packet.return`:

Return
------

true if there is enough space for another OGM, false otherwise.

.. _`batadv_v_ogm_process`:

batadv_v_ogm_process
====================

.. c:function:: void batadv_v_ogm_process(const struct sk_buff *skb, int ogm_offset, struct batadv_hard_iface *if_incoming)

    process an incoming batman v OGM

    :param const struct sk_buff \*skb:
        the skb containing the OGM

    :param int ogm_offset:
        offset to the OGM which should be processed (for aggregates)

    :param struct batadv_hard_iface \*if_incoming:
        the interface where this packet was receved

.. _`batadv_v_ogm_packet_recv`:

batadv_v_ogm_packet_recv
========================

.. c:function:: int batadv_v_ogm_packet_recv(struct sk_buff *skb, struct batadv_hard_iface *if_incoming)

    OGM2 receiving handler

    :param struct sk_buff \*skb:
        the received OGM

    :param struct batadv_hard_iface \*if_incoming:
        the interface where this OGM has been received

.. _`batadv_v_ogm_packet_recv.return`:

Return
------

NET_RX_SUCCESS and consume the skb on success or returns NET_RX_DROP
(without freeing the skb) on failure

.. _`batadv_v_ogm_init`:

batadv_v_ogm_init
=================

.. c:function:: int batadv_v_ogm_init(struct batadv_priv *bat_priv)

    initialise the OGM2 engine

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_v_ogm_init.return`:

Return
------

0 on success or a negative error code in case of failure

.. _`batadv_v_ogm_free`:

batadv_v_ogm_free
=================

.. c:function:: void batadv_v_ogm_free(struct batadv_priv *bat_priv)

    free OGM private resources

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. This file was automatic generated / don't edit.

