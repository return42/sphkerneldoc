.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/netlink.c

.. _`batadv_netlink_get_ifindex`:

batadv_netlink_get_ifindex
==========================

.. c:function:: int batadv_netlink_get_ifindex(const struct nlmsghdr *nlh, int attrtype)

    Extract an interface index from a message

    :param const struct nlmsghdr \*nlh:
        Message header

    :param int attrtype:
        Attribute which holds an interface index

.. _`batadv_netlink_get_ifindex.return`:

Return
------

interface index, or 0.

.. _`batadv_netlink_mesh_info_put`:

batadv_netlink_mesh_info_put
============================

.. c:function:: int batadv_netlink_mesh_info_put(struct sk_buff *msg, struct net_device *soft_iface)

    fill in generic information about mesh interface

    :param struct sk_buff \*msg:
        netlink message to be sent back

    :param struct net_device \*soft_iface:
        interface for which the data should be taken

.. _`batadv_netlink_mesh_info_put.return`:

Return
------

0 on success, < 0 on error

.. _`batadv_netlink_get_mesh_info`:

batadv_netlink_get_mesh_info
============================

.. c:function:: int batadv_netlink_get_mesh_info(struct sk_buff *skb, struct genl_info *info)

    handle incoming BATADV_CMD_GET_MESH_INFO netlink request

    :param struct sk_buff \*skb:
        received netlink message

    :param struct genl_info \*info:
        receiver information

.. _`batadv_netlink_get_mesh_info.return`:

Return
------

0 on success, < 0 on error

.. _`batadv_netlink_tp_meter_put`:

batadv_netlink_tp_meter_put
===========================

.. c:function:: int batadv_netlink_tp_meter_put(struct sk_buff *msg, u32 cookie)

    Fill information of started tp_meter session

    :param struct sk_buff \*msg:
        netlink message to be sent back

    :param u32 cookie:
        tp meter session cookie

.. _`batadv_netlink_tp_meter_put.return`:

Return
------

0 on success, < 0 on error

.. _`batadv_netlink_tpmeter_notify`:

batadv_netlink_tpmeter_notify
=============================

.. c:function:: int batadv_netlink_tpmeter_notify(struct batadv_priv *bat_priv, const u8 *dst, u8 result, u32 test_time, u64 total_bytes, u32 cookie)

    send tp_meter result via netlink to client

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param const u8 \*dst:
        destination of tp_meter session

    :param u8 result:
        reason for tp meter session stop

    :param u32 test_time:
        total time ot the tp_meter session

    :param u64 total_bytes:
        bytes acked to the receiver

    :param u32 cookie:
        cookie of tp_meter session

.. _`batadv_netlink_tpmeter_notify.return`:

Return
------

0 on success, < 0 on error

.. _`batadv_netlink_tp_meter_start`:

batadv_netlink_tp_meter_start
=============================

.. c:function:: int batadv_netlink_tp_meter_start(struct sk_buff *skb, struct genl_info *info)

    Start a new tp_meter session

    :param struct sk_buff \*skb:
        received netlink message

    :param struct genl_info \*info:
        receiver information

.. _`batadv_netlink_tp_meter_start.return`:

Return
------

0 on success, < 0 on error

.. _`batadv_netlink_tp_meter_cancel`:

batadv_netlink_tp_meter_cancel
==============================

.. c:function:: int batadv_netlink_tp_meter_cancel(struct sk_buff *skb, struct genl_info *info)

    Cancel a running tp_meter session

    :param struct sk_buff \*skb:
        received netlink message

    :param struct genl_info \*info:
        receiver information

.. _`batadv_netlink_tp_meter_cancel.return`:

Return
------

0 on success, < 0 on error

.. _`batadv_netlink_dump_hardif_entry`:

batadv_netlink_dump_hardif_entry
================================

.. c:function:: int batadv_netlink_dump_hardif_entry(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_hard_iface *hard_iface)

    Dump one hard interface into a message

    :param struct sk_buff \*msg:
        Netlink message to dump into

    :param u32 portid:
        Port making netlink request

    :param u32 seq:
        Sequence number of netlink message

    :param struct batadv_hard_iface \*hard_iface:
        Hard interface to dump

.. _`batadv_netlink_dump_hardif_entry.return`:

Return
------

error code, or 0 on success

.. _`batadv_netlink_dump_hardifs`:

batadv_netlink_dump_hardifs
===========================

.. c:function:: int batadv_netlink_dump_hardifs(struct sk_buff *msg, struct netlink_callback *cb)

    Dump all hard interface into a messages

    :param struct sk_buff \*msg:
        Netlink message to dump into

    :param struct netlink_callback \*cb:
        Parameters from query

.. _`batadv_netlink_dump_hardifs.return`:

Return
------

error code, or length of reply message on success

.. _`batadv_netlink_register`:

batadv_netlink_register
=======================

.. c:function:: void batadv_netlink_register( void)

    register batadv genl netlink family

    :param  void:
        no arguments

.. _`batadv_netlink_unregister`:

batadv_netlink_unregister
=========================

.. c:function:: void batadv_netlink_unregister( void)

    unregister batadv genl netlink family

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

