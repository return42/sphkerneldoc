.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/ib_addr.h

.. _`rdma_addr_register_client`:

rdma_addr_register_client
=========================

.. c:function:: void rdma_addr_register_client(struct rdma_addr_client *client)

    Register an address client.

    :param struct rdma_addr_client \*client:
        *undescribed*

.. _`rdma_addr_unregister_client`:

rdma_addr_unregister_client
===========================

.. c:function:: void rdma_addr_unregister_client(struct rdma_addr_client *client)

    Deregister an address client.

    :param struct rdma_addr_client \*client:
        Client object to deregister.

.. _`rdma_dev_addr`:

struct rdma_dev_addr
====================

.. c:type:: struct rdma_dev_addr

    Contains resolved RDMA hardware addresses

.. _`rdma_dev_addr.definition`:

Definition
----------

.. code-block:: c

    struct rdma_dev_addr {
        unsigned char src_dev_addr[MAX_ADDR_LEN];
        unsigned char dst_dev_addr[MAX_ADDR_LEN];
        unsigned char broadcast[MAX_ADDR_LEN];
        unsigned short dev_type;
        int bound_dev_if;
        enum rdma_transport_type transport;
        struct net *net;
        enum rdma_network_type network;
        int hoplimit;
    }

.. _`rdma_dev_addr.members`:

Members
-------

src_dev_addr
    Source MAC address.

dst_dev_addr
    Destination MAC address.

broadcast
    Broadcast address of the device.

dev_type
    The interface hardware type of the device.

bound_dev_if
    An optional device interface index.

transport
    The transport type used.

net
    Network namespace containing the bound_dev_if net_dev.

network
    *undescribed*

hoplimit
    *undescribed*

.. _`rdma_translate_ip`:

rdma_translate_ip
=================

.. c:function:: int rdma_translate_ip(const struct sockaddr *addr, struct rdma_dev_addr *dev_addr)

    Translate a local IP address to an RDMA hardware address.

    :param const struct sockaddr \*addr:
        *undescribed*

    :param struct rdma_dev_addr \*dev_addr:
        *undescribed*

.. _`rdma_translate_ip.description`:

Description
-----------

The dev_addr->net field must be initialized.

.. _`rdma_resolve_ip`:

rdma_resolve_ip
===============

.. c:function:: int rdma_resolve_ip(struct rdma_addr_client *client, struct sockaddr *src_addr, struct sockaddr *dst_addr, struct rdma_dev_addr *addr, int timeout_ms, void (*callback)(int status, struct sockaddr *src_addr, struct rdma_dev_addr *addr, void *context), void *context)

    Resolve source and destination IP addresses to RDMA hardware addresses.

    :param struct rdma_addr_client \*client:
        Address client associated with request.

    :param struct sockaddr \*src_addr:
        An optional source address to use in the resolution.  If a
        source address is not provided, a usable address will be returned via
        the callback.

    :param struct sockaddr \*dst_addr:
        The destination address to resolve.

    :param struct rdma_dev_addr \*addr:
        A reference to a data location that will receive the resolved
        addresses.  The data location must remain valid until the callback has
        been invoked. The net field of the addr struct must be valid.

    :param int timeout_ms:
        Amount of time to wait for the address resolution to complete.

    :param void (\*callback)(int status, struct sockaddr \*src_addr, struct rdma_dev_addr \*addr, void \*context):
        Call invoked once address resolution has completed, timed out,
        or been canceled.  A status of 0 indicates success.

    :param void \*context:
        User-specified context associated with the call.

.. This file was automatic generated / don't edit.

