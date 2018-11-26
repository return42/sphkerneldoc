.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/addr.c

.. _`rdma_copy_src_l2_addr`:

rdma_copy_src_l2_addr
=====================

.. c:function:: void rdma_copy_src_l2_addr(struct rdma_dev_addr *dev_addr, const struct net_device *dev)

    Copy netdevice source addresses

    :param dev_addr:
        Destination address pointer where to copy the addresses
    :type dev_addr: struct rdma_dev_addr \*

    :param dev:
        Netdevice whose source addresses to copy
    :type dev: const struct net_device \*

.. _`rdma_copy_src_l2_addr.description`:

Description
-----------

\ :c:func:`rdma_copy_src_l2_addr`\  copies source addresses from the specified netdevice.
This includes unicast address, broadcast address, device type and
interface index.

.. _`rdma_addr_cancel`:

rdma_addr_cancel
================

.. c:function:: void rdma_addr_cancel(struct rdma_dev_addr *addr)

    Cancel resolve ip request

    :param addr:
        Pointer to address structure given previously
        during \ :c:func:`rdma_resolve_ip`\ .
        \ :c:func:`rdma_addr_cancel`\  is synchronous function which cancels any pending
        request if there is any.
    :type addr: struct rdma_dev_addr \*

.. This file was automatic generated / don't edit.

