.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/rdma_netlink.h

.. _`rdma_nl_register`:

rdma_nl_register
================

.. c:function:: void rdma_nl_register(unsigned int index, const struct rdma_nl_cbs cb_table)

    :param index:
        Index of the added client
    :type index: unsigned int

    :param cb_table:
        A table for op->callback
    :type cb_table: const struct rdma_nl_cbs

.. _`rdma_nl_unregister`:

rdma_nl_unregister
==================

.. c:function:: void rdma_nl_unregister(unsigned int index)

    :param index:
        Index of the removed IB client.
    :type index: unsigned int

.. _`ibnl_put_msg`:

ibnl_put_msg
============

.. c:function:: void *ibnl_put_msg(struct sk_buff *skb, struct nlmsghdr **nlh, int seq, int len, int client, int op, int flags)

    :param skb:
        The netlink skb.
    :type skb: struct sk_buff \*

    :param nlh:
        Pointer to put the header of the new netlink message.
    :type nlh: struct nlmsghdr \*\*

    :param seq:
        The message sequence number.
    :type seq: int

    :param len:
        The requested message length to allocate.
    :type len: int

    :param client:
        Calling IB netlink client.
    :type client: int

    :param op:
        message content op.
        Returns the allocated buffer on success and NULL on failure.
    :type op: int

    :param flags:
        *undescribed*
    :type flags: int

.. _`ibnl_put_attr`:

ibnl_put_attr
=============

.. c:function:: int ibnl_put_attr(struct sk_buff *skb, struct nlmsghdr *nlh, int len, void *data, int type)

    :param skb:
        The netlink skb.
    :type skb: struct sk_buff \*

    :param nlh:
        Header of the netlink message to append the attribute to.
    :type nlh: struct nlmsghdr \*

    :param len:
        The length of the attribute data.
    :type len: int

    :param data:
        The attribute data to put.
    :type data: void \*

    :param type:
        The attribute type.
        Returns the 0 and a negative error code on failure.
    :type type: int

.. _`rdma_nl_unicast`:

rdma_nl_unicast
===============

.. c:function:: int rdma_nl_unicast(struct sk_buff *skb, u32 pid)

    :param skb:
        The netlink skb
    :type skb: struct sk_buff \*

    :param pid:
        Userspace netlink process ID
        Returns 0 on success or a negative error code.
    :type pid: u32

.. _`rdma_nl_unicast_wait`:

rdma_nl_unicast_wait
====================

.. c:function:: int rdma_nl_unicast_wait(struct sk_buff *skb, __u32 pid)

    :param skb:
        The netlink skb
    :type skb: struct sk_buff \*

    :param pid:
        Userspace netlink process ID
        Returns 0 on success or a negative error code.
    :type pid: __u32

.. _`rdma_nl_multicast`:

rdma_nl_multicast
=================

.. c:function:: int rdma_nl_multicast(struct sk_buff *skb, unsigned int group, gfp_t flags)

    :param skb:
        The netlink skb
    :type skb: struct sk_buff \*

    :param group:
        Netlink group ID
    :type group: unsigned int

    :param flags:
        allocation flags
        Returns 0 on success or a negative error code.
    :type flags: gfp_t

.. _`rdma_nl_chk_listeners`:

rdma_nl_chk_listeners
=====================

.. c:function:: bool rdma_nl_chk_listeners(unsigned int group)

    :param group:
        the netlink group ID
        Returns true on success or false if no listeners.
    :type group: unsigned int

.. This file was automatic generated / don't edit.

