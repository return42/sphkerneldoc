.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv6/ip6_output.c

.. _`ip6_dst_lookup`:

ip6_dst_lookup
==============

.. c:function:: int ip6_dst_lookup(struct net *net, struct sock *sk, struct dst_entry **dst, struct flowi6 *fl6)

    perform route lookup on flow

    :param net:
        *undescribed*
    :type net: struct net \*

    :param sk:
        socket which provides route info
    :type sk: struct sock \*

    :param dst:
        pointer to dst_entry \* for result
    :type dst: struct dst_entry \*\*

    :param fl6:
        flow to lookup
    :type fl6: struct flowi6 \*

.. _`ip6_dst_lookup.description`:

Description
-----------

This function performs a route lookup on the given flow.

It returns zero on success, or a standard errno code on error.

.. _`ip6_dst_lookup_flow`:

ip6_dst_lookup_flow
===================

.. c:function:: struct dst_entry *ip6_dst_lookup_flow(const struct sock *sk, struct flowi6 *fl6, const struct in6_addr *final_dst)

    perform route lookup on flow with ipsec

    :param sk:
        socket which provides route info
    :type sk: const struct sock \*

    :param fl6:
        flow to lookup
    :type fl6: struct flowi6 \*

    :param final_dst:
        final destination address for ipsec lookup
    :type final_dst: const struct in6_addr \*

.. _`ip6_dst_lookup_flow.description`:

Description
-----------

This function performs a route lookup on the given flow.

It returns a valid dst pointer on success, or a pointer encoded
error code.

.. _`ip6_sk_dst_lookup_flow`:

ip6_sk_dst_lookup_flow
======================

.. c:function:: struct dst_entry *ip6_sk_dst_lookup_flow(struct sock *sk, struct flowi6 *fl6, const struct in6_addr *final_dst, bool connected)

    perform socket cached route lookup on flow

    :param sk:
        socket which provides the dst cache and route info
    :type sk: struct sock \*

    :param fl6:
        flow to lookup
    :type fl6: struct flowi6 \*

    :param final_dst:
        final destination address for ipsec lookup
    :type final_dst: const struct in6_addr \*

    :param connected:
        whether \ ``sk``\  is connected or not
    :type connected: bool

.. _`ip6_sk_dst_lookup_flow.description`:

Description
-----------

This function performs a route lookup on the given flow with the
possibility of using the cached route in the socket if it is valid.
It will take the socket dst lock when operating on the dst cache.
As a result, this function can only be used in process context.

In addition, for a connected socket, cache the dst in the socket
if the current cache is not valid.

It returns a valid dst pointer on success, or a pointer encoded
error code.

.. This file was automatic generated / don't edit.

