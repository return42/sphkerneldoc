.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/netlink.c

.. _`batadv_netlink_get_ifindex`:

batadv_netlink_get_ifindex
==========================

.. c:function:: int batadv_netlink_get_ifindex(const struct nlmsghdr *nlh, int attrtype)

    Extract an interface index from a message

    :param nlh:
        Message header
    :type nlh: const struct nlmsghdr \*

    :param attrtype:
        Attribute which holds an interface index
    :type attrtype: int

.. _`batadv_netlink_get_ifindex.return`:

Return
------

interface index, or 0.

.. _`batadv_netlink_mesh_info_put`:

batadv_netlink_mesh_info_put
============================

.. c:function:: int batadv_netlink_mesh_info_put(struct sk_buff *msg, struct net_device *soft_iface)

    fill in generic information about mesh interface

    :param msg:
        netlink message to be sent back
    :type msg: struct sk_buff \*

    :param soft_iface:
        interface for which the data should be taken
    :type soft_iface: struct net_device \*

.. _`batadv_netlink_mesh_info_put.return`:

Return
------

0 on success, < 0 on error

.. _`batadv_netlink_get_mesh_info`:

batadv_netlink_get_mesh_info
============================

.. c:function:: int batadv_netlink_get_mesh_info(struct sk_buff *skb, struct genl_info *info)

    handle incoming BATADV_CMD_GET_MESH_INFO netlink request

    :param skb:
        received netlink message
    :type skb: struct sk_buff \*

    :param info:
        receiver information
    :type info: struct genl_info \*

.. _`batadv_netlink_get_mesh_info.return`:

Return
------

0 on success, < 0 on error

.. _`batadv_netlink_tp_meter_put`:

batadv_netlink_tp_meter_put
===========================

.. c:function:: int batadv_netlink_tp_meter_put(struct sk_buff *msg, u32 cookie)

    Fill information of started tp_meter session

    :param msg:
        netlink message to be sent back
    :type msg: struct sk_buff \*

    :param cookie:
        tp meter session cookie
    :type cookie: u32

.. _`batadv_netlink_tp_meter_put.return`:

Return
------

0 on success, < 0 on error

.. _`batadv_netlink_tpmeter_notify`:

batadv_netlink_tpmeter_notify
=============================

.. c:function:: int batadv_netlink_tpmeter_notify(struct batadv_priv *bat_priv, const u8 *dst, u8 result, u32 test_time, u64 total_bytes, u32 cookie)

    send tp_meter result via netlink to client

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param dst:
        destination of tp_meter session
    :type dst: const u8 \*

    :param result:
        reason for tp meter session stop
    :type result: u8

    :param test_time:
        total time ot the tp_meter session
    :type test_time: u32

    :param total_bytes:
        bytes acked to the receiver
    :type total_bytes: u64

    :param cookie:
        cookie of tp_meter session
    :type cookie: u32

.. _`batadv_netlink_tpmeter_notify.return`:

Return
------

0 on success, < 0 on error

.. _`batadv_netlink_tp_meter_start`:

batadv_netlink_tp_meter_start
=============================

.. c:function:: int batadv_netlink_tp_meter_start(struct sk_buff *skb, struct genl_info *info)

    Start a new tp_meter session

    :param skb:
        received netlink message
    :type skb: struct sk_buff \*

    :param info:
        receiver information
    :type info: struct genl_info \*

.. _`batadv_netlink_tp_meter_start.return`:

Return
------

0 on success, < 0 on error

.. _`batadv_netlink_tp_meter_cancel`:

batadv_netlink_tp_meter_cancel
==============================

.. c:function:: int batadv_netlink_tp_meter_cancel(struct sk_buff *skb, struct genl_info *info)

    Cancel a running tp_meter session

    :param skb:
        received netlink message
    :type skb: struct sk_buff \*

    :param info:
        receiver information
    :type info: struct genl_info \*

.. _`batadv_netlink_tp_meter_cancel.return`:

Return
------

0 on success, < 0 on error

.. _`batadv_netlink_dump_hardif_entry`:

batadv_netlink_dump_hardif_entry
================================

.. c:function:: int batadv_netlink_dump_hardif_entry(struct sk_buff *msg, u32 portid, u32 seq, struct batadv_hard_iface *hard_iface)

    Dump one hard interface into a message

    :param msg:
        Netlink message to dump into
    :type msg: struct sk_buff \*

    :param portid:
        Port making netlink request
    :type portid: u32

    :param seq:
        Sequence number of netlink message
    :type seq: u32

    :param hard_iface:
        Hard interface to dump
    :type hard_iface: struct batadv_hard_iface \*

.. _`batadv_netlink_dump_hardif_entry.return`:

Return
------

error code, or 0 on success

.. _`batadv_netlink_dump_hardifs`:

batadv_netlink_dump_hardifs
===========================

.. c:function:: int batadv_netlink_dump_hardifs(struct sk_buff *msg, struct netlink_callback *cb)

    Dump all hard interface into a messages

    :param msg:
        Netlink message to dump into
    :type msg: struct sk_buff \*

    :param cb:
        Parameters from query
    :type cb: struct netlink_callback \*

.. _`batadv_netlink_dump_hardifs.return`:

Return
------

error code, or length of reply message on success

.. _`batadv_netlink_register`:

batadv_netlink_register
=======================

.. c:function:: void batadv_netlink_register( void)

    register batadv genl netlink family

    :param void:
        no arguments
    :type void: 

.. _`batadv_netlink_unregister`:

batadv_netlink_unregister
=========================

.. c:function:: void batadv_netlink_unregister( void)

    unregister batadv genl netlink family

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

