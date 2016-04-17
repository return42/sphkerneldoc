.. -*- coding: utf-8; mode: rst -*-

============
af_netlink.c
============


.. _`__netlink_ns_capable`:

__netlink_ns_capable
====================

.. c:function:: bool __netlink_ns_capable (const struct netlink_skb_parms *nsp, struct user_namespace *user_ns, int cap)

    General netlink message capability test

    :param const struct netlink_skb_parms \*nsp:
        NETLINK_CB of the socket buffer holding a netlink command from userspace.

    :param struct user_namespace \*user_ns:
        The user namespace of the capability to use

    :param int cap:
        The capability to use



.. _`__netlink_ns_capable.description`:

Description
-----------

Test to see if the opener of the socket we received the message
from had when the netlink socket was created and the sender of the
message has has the capability ``cap`` in the user namespace ``user_ns``\ .



.. _`netlink_ns_capable`:

netlink_ns_capable
==================

.. c:function:: bool netlink_ns_capable (const struct sk_buff *skb, struct user_namespace *user_ns, int cap)

    General netlink message capability test

    :param const struct sk_buff \*skb:
        socket buffer holding a netlink command from userspace

    :param struct user_namespace \*user_ns:
        The user namespace of the capability to use

    :param int cap:
        The capability to use



.. _`netlink_ns_capable.description`:

Description
-----------

Test to see if the opener of the socket we received the message
from had when the netlink socket was created and the sender of the
message has has the capability ``cap`` in the user namespace ``user_ns``\ .



.. _`netlink_capable`:

netlink_capable
===============

.. c:function:: bool netlink_capable (const struct sk_buff *skb, int cap)

    Netlink global message capability test

    :param const struct sk_buff \*skb:
        socket buffer holding a netlink command from userspace

    :param int cap:
        The capability to use



.. _`netlink_capable.description`:

Description
-----------

Test to see if the opener of the socket we received the message
from had when the netlink socket was created and the sender of the
message has has the capability ``cap`` in all user namespaces.



.. _`netlink_net_capable`:

netlink_net_capable
===================

.. c:function:: bool netlink_net_capable (const struct sk_buff *skb, int cap)

    Netlink network namespace message capability test

    :param const struct sk_buff \*skb:
        socket buffer holding a netlink command from userspace

    :param int cap:
        The capability to use



.. _`netlink_net_capable.description`:

Description
-----------

Test to see if the opener of the socket we received the message
from had when the netlink socket was created and the sender of the
message has has the capability ``cap`` over the network namespace of
the socket we received the message from.



.. _`netlink_set_err`:

netlink_set_err
===============

.. c:function:: int netlink_set_err (struct sock *ssk, u32 portid, u32 group, int code)

    report error to broadcast listeners

    :param struct sock \*ssk:
        the kernel netlink socket, as returned by :c:func:`netlink_kernel_create`

    :param u32 portid:
        the PORTID of a process that we want to skip (if any)

    :param u32 group:
        the broadcast group that will notice the error

    :param int code:
        error code, must be negative (as usual in kernelspace)



.. _`netlink_set_err.description`:

Description
-----------

This function returns the number of broadcast listeners that have set the
NETLINK_NO_ENOBUFS socket option.



.. _`netlink_change_ngroups`:

netlink_change_ngroups
======================

.. c:function:: int netlink_change_ngroups (struct sock *sk, unsigned int groups)

    change number of multicast groups

    :param struct sock \*sk:
        The kernel netlink socket, as returned by :c:func:`netlink_kernel_create`.

    :param unsigned int groups:
        The new number of groups.



.. _`netlink_change_ngroups.description`:

Description
-----------


This changes the number of multicast groups that are available
on a certain netlink family. Note that it is not possible to
change the number of groups to below 32. Also note that it does
not implicitly call :c:func:`netlink_clear_multicast_users` when the
number of groups is reduced.



.. _`nlmsg_notify`:

nlmsg_notify
============

.. c:function:: int nlmsg_notify (struct sock *sk, struct sk_buff *skb, u32 portid, unsigned int group, int report, gfp_t flags)

    send a notification netlink message

    :param struct sock \*sk:
        netlink socket to use

    :param struct sk_buff \*skb:
        notification message

    :param u32 portid:
        destination netlink portid for reports or 0

    :param unsigned int group:
        destination multicast group or 0

    :param int report:
        1 to report back, 0 to disable

    :param gfp_t flags:
        allocation flags

