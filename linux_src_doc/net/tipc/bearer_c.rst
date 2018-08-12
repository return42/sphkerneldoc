.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/bearer.c

.. _`tipc_media_find`:

tipc_media_find
===============

.. c:function:: struct tipc_media *tipc_media_find(const char *name)

    locates specified media object by name

    :param const char \*name:
        *undescribed*

.. _`media_find_id`:

media_find_id
=============

.. c:function:: struct tipc_media *media_find_id(u8 type)

    locates specified media object by type identifier

    :param u8 type:
        *undescribed*

.. _`tipc_media_addr_printf`:

tipc_media_addr_printf
======================

.. c:function:: void tipc_media_addr_printf(char *buf, int len, struct tipc_media_addr *a)

    record media address in print buffer

    :param char \*buf:
        *undescribed*

    :param int len:
        *undescribed*

    :param struct tipc_media_addr \*a:
        *undescribed*

.. _`bearer_name_validate`:

bearer_name_validate
====================

.. c:function:: int bearer_name_validate(const char *name, struct tipc_bearer_names *name_parts)

    validate & (optionally) deconstruct bearer name

    :param const char \*name:
        ptr to bearer name string

    :param struct tipc_bearer_names \*name_parts:
        ptr to area for bearer name components (or NULL if not needed)

.. _`bearer_name_validate.description`:

Description
-----------

Returns 1 if bearer name is valid, otherwise 0.

.. _`tipc_bearer_find`:

tipc_bearer_find
================

.. c:function:: struct tipc_bearer *tipc_bearer_find(struct net *net, const char *name)

    locates bearer object with matching bearer name

    :param struct net \*net:
        *undescribed*

    :param const char \*name:
        *undescribed*

.. _`tipc_enable_bearer`:

tipc_enable_bearer
==================

.. c:function:: int tipc_enable_bearer(struct net *net, const char *name, u32 disc_domain, u32 prio, struct nlattr  *attr)

    enable bearer with the given name

    :param struct net \*net:
        *undescribed*

    :param const char \*name:
        *undescribed*

    :param u32 disc_domain:
        *undescribed*

    :param u32 prio:
        *undescribed*

    :param struct nlattr  \*attr:
        *undescribed*

.. _`tipc_reset_bearer`:

tipc_reset_bearer
=================

.. c:function:: int tipc_reset_bearer(struct net *net, struct tipc_bearer *b)

    Reset all links established over this bearer

    :param struct net \*net:
        *undescribed*

    :param struct tipc_bearer \*b:
        *undescribed*

.. _`bearer_disable`:

bearer_disable
==============

.. c:function:: void bearer_disable(struct net *net, struct tipc_bearer *b)

    :param struct net \*net:
        *undescribed*

    :param struct tipc_bearer \*b:
        *undescribed*

.. _`bearer_disable.note`:

Note
----

This routine assumes caller holds RTNL lock.

.. _`tipc_l2_send_msg`:

tipc_l2_send_msg
================

.. c:function:: int tipc_l2_send_msg(struct net *net, struct sk_buff *skb, struct tipc_bearer *b, struct tipc_media_addr *dest)

    send a TIPC packet out over an L2 interface

    :param struct net \*net:
        *undescribed*

    :param struct sk_buff \*skb:
        the packet to be sent

    :param struct tipc_bearer \*b:
        the bearer through which the packet is to be sent

    :param struct tipc_media_addr \*dest:
        peer destination address

.. _`tipc_l2_rcv_msg`:

tipc_l2_rcv_msg
===============

.. c:function:: int tipc_l2_rcv_msg(struct sk_buff *skb, struct net_device *dev, struct packet_type *pt, struct net_device *orig_dev)

    handle incoming TIPC message from an interface

    :param struct sk_buff \*skb:
        *undescribed*

    :param struct net_device \*dev:
        the net device that the packet was received on

    :param struct packet_type \*pt:
        the packet_type structure which was used to register this handler

    :param struct net_device \*orig_dev:
        the original receive net device in case the device is a bond

.. _`tipc_l2_rcv_msg.description`:

Description
-----------

Accept only packets explicitly sent to this node, or broadcast packets;
ignores packets sent using interface multicast, and traffic sent to other
nodes (which can happen if interface is running in promiscuous mode).

.. _`tipc_l2_device_event`:

tipc_l2_device_event
====================

.. c:function:: int tipc_l2_device_event(struct notifier_block *nb, unsigned long evt, void *ptr)

    handle device events from network device

    :param struct notifier_block \*nb:
        the context of the notification

    :param unsigned long evt:
        the type of event

    :param void \*ptr:
        the net device that the event was on

.. _`tipc_l2_device_event.description`:

Description
-----------

This function is called by the Ethernet driver in case of link
change event.

.. This file was automatic generated / don't edit.

