.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/netfilter/nf_tproxy.h

.. _`nf_tproxy_handle_time_wait4`:

nf_tproxy_handle_time_wait4
===========================

.. c:function:: struct sock *nf_tproxy_handle_time_wait4(struct net *net, struct sk_buff *skb, __be32 laddr, __be16 lport, struct sock *sk)

    handle IPv4 TCP TIME_WAIT reopen redirections

    :param net:
        *undescribed*
    :type net: struct net \*

    :param skb:
        The skb being processed.
    :type skb: struct sk_buff \*

    :param laddr:
        IPv4 address to redirect to or zero.
    :type laddr: __be32

    :param lport:
        TCP port to redirect to or zero.
    :type lport: __be16

    :param sk:
        The TIME_WAIT TCP socket found by the lookup.
    :type sk: struct sock \*

.. _`nf_tproxy_handle_time_wait4.description`:

Description
-----------

We have to handle SYN packets arriving to TIME_WAIT sockets

.. _`nf_tproxy_handle_time_wait4.differently`:

differently
-----------

instead of reopening the connection we should rather
redirect the new connection to the proxy if there's a listener
socket present.

\ :c:func:`nf_tproxy_handle_time_wait4`\  consumes the socket reference passed in.

Returns the listener socket if there's one, the TIME_WAIT socket if
no such listener is found, or NULL if the TCP header is incomplete.

.. _`nf_tproxy_handle_time_wait6`:

nf_tproxy_handle_time_wait6
===========================

.. c:function:: struct sock *nf_tproxy_handle_time_wait6(struct sk_buff *skb, int tproto, int thoff, struct net *net, const struct in6_addr *laddr, const __be16 lport, struct sock *sk)

    handle IPv6 TCP TIME_WAIT reopen redirections

    :param skb:
        The skb being processed.
    :type skb: struct sk_buff \*

    :param tproto:
        Transport protocol.
    :type tproto: int

    :param thoff:
        Transport protocol header offset.
    :type thoff: int

    :param net:
        Network namespace.
    :type net: struct net \*

    :param laddr:
        IPv6 address to redirect to.
    :type laddr: const struct in6_addr \*

    :param lport:
        TCP port to redirect to or zero.
    :type lport: const __be16

    :param sk:
        The TIME_WAIT TCP socket found by the lookup.
    :type sk: struct sock \*

.. _`nf_tproxy_handle_time_wait6.description`:

Description
-----------

We have to handle SYN packets arriving to TIME_WAIT sockets

.. _`nf_tproxy_handle_time_wait6.differently`:

differently
-----------

instead of reopening the connection we should rather
redirect the new connection to the proxy if there's a listener
socket present.

\ :c:func:`nf_tproxy_handle_time_wait6`\  consumes the socket reference passed in.

Returns the listener socket if there's one, the TIME_WAIT socket if
no such listener is found, or NULL if the TCP header is incomplete.

.. This file was automatic generated / don't edit.

