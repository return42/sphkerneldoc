.. -*- coding: utf-8; mode: rst -*-

==============
rdma_netlink.h
==============


.. _`ibnl_add_client`:

ibnl_add_client
===============

.. c:function:: int ibnl_add_client (int index, int nops, const struct ibnl_client_cbs cb_table[])

    :param int index:
        Index of the added client

    :param int nops:
        Number of supported ops by the added client.

    :param const struct ibnl_client_cbs cb_table:
        A table for op->callback



.. _`ibnl_add_client.description`:

Description
-----------

Returns 0 on success or a negative error code.



.. _`ibnl_remove_client`:

ibnl_remove_client
==================

.. c:function:: int ibnl_remove_client (int index)

    :param int index:
        Index of the removed IB client.



.. _`ibnl_remove_client.description`:

Description
-----------

Returns 0 on success or a negative error code.



.. _`ibnl_put_msg`:

ibnl_put_msg
============

.. c:function:: void *ibnl_put_msg (struct sk_buff *skb, struct nlmsghdr **nlh, int seq, int len, int client, int op, int flags)

    :param struct sk_buff \*skb:
        The netlink skb.

    :param struct nlmsghdr \*\*nlh:
        Pointer to put the header of the new netlink message.

    :param int seq:
        The message sequence number.

    :param int len:
        The requested message length to allocate.

    :param int client:
        Calling IB netlink client.

    :param int op:
        message content op.
        Returns the allocated buffer on success and NULL on failure.

    :param int flags:

        *undescribed*



.. _`ibnl_put_attr`:

ibnl_put_attr
=============

.. c:function:: int ibnl_put_attr (struct sk_buff *skb, struct nlmsghdr *nlh, int len, void *data, int type)

    :param struct sk_buff \*skb:
        The netlink skb.

    :param struct nlmsghdr \*nlh:
        Header of the netlink message to append the attribute to.

    :param int len:
        The length of the attribute data.

    :param void \*data:
        The attribute data to put.

    :param int type:
        The attribute type.
        Returns the 0 and a negative error code on failure.



.. _`ibnl_unicast`:

ibnl_unicast
============

.. c:function:: int ibnl_unicast (struct sk_buff *skb, struct nlmsghdr *nlh, __u32 pid)

    :param struct sk_buff \*skb:
        The netlink skb

    :param struct nlmsghdr \*nlh:
        Header of the netlink message to send

    :param __u32 pid:
        Userspace netlink process ID
        Returns 0 on success or a negative error code.



.. _`ibnl_multicast`:

ibnl_multicast
==============

.. c:function:: int ibnl_multicast (struct sk_buff *skb, struct nlmsghdr *nlh, unsigned int group, gfp_t flags)

    :param struct sk_buff \*skb:
        The netlink skb

    :param struct nlmsghdr \*nlh:
        Header of the netlink message to send

    :param unsigned int group:
        Netlink group ID

    :param gfp_t flags:
        allocation flags
        Returns 0 on success or a negative error code.



.. _`ibnl_chk_listeners`:

ibnl_chk_listeners
==================

.. c:function:: int ibnl_chk_listeners (unsigned int group)

    :param unsigned int group:
        the netlink group ID
        Returns 0 on success or a negative for no listeners.

