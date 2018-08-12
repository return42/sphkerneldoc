.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/netfilter/nf_tproxy.h

.. _`nf_tproxy_handle_time_wait4`:

nf_tproxy_handle_time_wait4
===========================

.. c:function:: struct sock *nf_tproxy_handle_time_wait4(struct net *net, struct sk_buff *skb, __be32 laddr, __be16 lport, struct sock *sk)

    handle IPv4 TCP TIME_WAIT reopen redirections

    :param struct net \*net:
        *undescribed*

    :param struct sk_buff \*skb:
        The skb being processed.

    :param __be32 laddr:
        IPv4 address to redirect to or zero.

    :param __be16 lport:
        TCP port to redirect to or zero.

    :param struct sock \*sk:
        The TIME_WAIT TCP socket found by the lookup.

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

    :param struct sk_buff \*skb:
        The skb being processed.

    :param int tproto:
        Transport protocol.

    :param int thoff:
        Transport protocol header offset.

    :param struct net \*net:
        Network namespace.

    :param const struct in6_addr \*laddr:
        IPv6 address to redirect to.

    :param const __be16 lport:
        TCP port to redirect to or zero.

    :param struct sock \*sk:
        The TIME_WAIT TCP socket found by the lookup.

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

