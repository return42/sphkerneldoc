.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/rdma_netlink.h

.. _`rdma_nl_register`:

rdma_nl_register
================

.. c:function:: void rdma_nl_register(unsigned int index, const struct rdma_nl_cbs cb_table)

    :param unsigned int index:
        Index of the added client

    :param const struct rdma_nl_cbs cb_table:
        A table for op->callback

.. _`rdma_nl_unregister`:

rdma_nl_unregister
==================

.. c:function:: void rdma_nl_unregister(unsigned int index)

    :param unsigned int index:
        Index of the removed IB client.

.. _`ibnl_put_msg`:

ibnl_put_msg
============

.. c:function:: void *ibnl_put_msg(struct sk_buff *skb, struct nlmsghdr **nlh, int seq, int len, int client, int op, int flags)

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

.. c:function:: int ibnl_put_attr(struct sk_buff *skb, struct nlmsghdr *nlh, int len, void *data, int type)

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

.. _`rdma_nl_unicast`:

rdma_nl_unicast
===============

.. c:function:: int rdma_nl_unicast(struct sk_buff *skb, u32 pid)

    :param struct sk_buff \*skb:
        The netlink skb

    :param u32 pid:
        Userspace netlink process ID
        Returns 0 on success or a negative error code.

.. _`rdma_nl_unicast_wait`:

rdma_nl_unicast_wait
====================

.. c:function:: int rdma_nl_unicast_wait(struct sk_buff *skb, __u32 pid)

    :param struct sk_buff \*skb:
        The netlink skb

    :param __u32 pid:
        Userspace netlink process ID
        Returns 0 on success or a negative error code.

.. _`rdma_nl_multicast`:

rdma_nl_multicast
=================

.. c:function:: int rdma_nl_multicast(struct sk_buff *skb, unsigned int group, gfp_t flags)

    :param struct sk_buff \*skb:
        The netlink skb

    :param unsigned int group:
        Netlink group ID

    :param gfp_t flags:
        allocation flags
        Returns 0 on success or a negative error code.

.. _`rdma_nl_chk_listeners`:

rdma_nl_chk_listeners
=====================

.. c:function:: int rdma_nl_chk_listeners(unsigned int group)

    :param unsigned int group:
        the netlink group ID
        Returns 0 on success or a negative for no listeners.

.. This file was automatic generated / don't edit.

