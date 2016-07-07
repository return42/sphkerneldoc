.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/netfilter/xt_TPROXY.c

.. _`tproxy_handle_time_wait4`:

tproxy_handle_time_wait4
========================

.. c:function:: struct sock *tproxy_handle_time_wait4(struct net *net, struct sk_buff *skb, __be32 laddr, __be16 lport, struct sock *sk)

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

.. _`tproxy_handle_time_wait4.description`:

Description
-----------

We have to handle SYN packets arriving to TIME_WAIT sockets

.. _`tproxy_handle_time_wait4.differently`:

differently
-----------

instead of reopening the connection we should rather
redirect the new connection to the proxy if there's a listener
socket present.

\ :c:func:`tproxy_handle_time_wait4`\  consumes the socket reference passed in.

Returns the listener socket if there's one, the TIME_WAIT socket if
no such listener is found, or NULL if the TCP header is incomplete.

.. _`tproxy_handle_time_wait6`:

tproxy_handle_time_wait6
========================

.. c:function:: struct sock *tproxy_handle_time_wait6(struct sk_buff *skb, int tproto, int thoff, const struct xt_action_param *par, struct sock *sk)

    handle IPv6 TCP TIME_WAIT reopen redirections

    :param struct sk_buff \*skb:
        The skb being processed.

    :param int tproto:
        Transport protocol.

    :param int thoff:
        Transport protocol header offset.

    :param const struct xt_action_param \*par:
        Iptables target parameters.

    :param struct sock \*sk:
        The TIME_WAIT TCP socket found by the lookup.

.. _`tproxy_handle_time_wait6.description`:

Description
-----------

We have to handle SYN packets arriving to TIME_WAIT sockets

.. _`tproxy_handle_time_wait6.differently`:

differently
-----------

instead of reopening the connection we should rather
redirect the new connection to the proxy if there's a listener
socket present.

\ :c:func:`tproxy_handle_time_wait6`\  consumes the socket reference passed in.

Returns the listener socket if there's one, the TIME_WAIT socket if
no such listener is found, or NULL if the TCP header is incomplete.

.. This file was automatic generated / don't edit.

