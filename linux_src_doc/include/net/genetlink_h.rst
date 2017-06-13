.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/genetlink.h

.. _`genl_multicast_group`:

struct genl_multicast_group
===========================

.. c:type:: struct genl_multicast_group

    generic netlink multicast group

.. _`genl_multicast_group.definition`:

Definition
----------

.. code-block:: c

    struct genl_multicast_group {
        char name;
    }

.. _`genl_multicast_group.members`:

Members
-------

name
    name of the multicast group, names are per-family

.. _`genl_family`:

struct genl_family
==================

.. c:type:: struct genl_family

    generic netlink family

.. _`genl_family.definition`:

Definition
----------

.. code-block:: c

    struct genl_family {
        int id;
        unsigned int hdrsize;
        char name;
        unsigned int version;
        unsigned int maxattr;
        bool netnsok;
        bool parallel_ops;
        int (*pre_doit)(const struct genl_ops *ops,struct sk_buff *skb, struct genl_info *info);
        void (*post_doit)(const struct genl_ops *ops,struct sk_buff *skb, struct genl_info *info);
        int (*mcast_bind)(struct net *net, int group);
        void (*mcast_unbind)(struct net *net, int group);
        struct nlattr **attrbuf;
        const struct genl_ops *ops;
        const struct genl_multicast_group *mcgrps;
        unsigned int n_ops;
        unsigned int n_mcgrps;
        unsigned int mcgrp_offset;
        struct module *module;
    }

.. _`genl_family.members`:

Members
-------

id
    protocol family identifier (private)

hdrsize
    length of user specific header in bytes

name
    name of family

version
    protocol version

maxattr
    maximum number of attributes supported

netnsok
    set to true if the family can handle network
    namespaces and should be presented in all of them

parallel_ops
    operations can be called in parallel and aren't
    synchronized by the core genetlink code

pre_doit
    called before an operation's doit callback, it may
    do additional, common, filtering and return an error

post_doit
    called after an operation's doit callback, it may
    undo operations done by pre_doit, for example release locks

mcast_bind
    a socket bound to the given multicast group (which
    is given as the offset into the groups array)

mcast_unbind
    a socket was unbound from the given multicast group.
    Note that \ :c:func:`unbind`\  will not be called symmetrically if the
    generic netlink family is removed while there are still open
    sockets.

attrbuf
    buffer to store parsed attributes (private)

ops
    the operations supported by this family

mcgrps
    multicast groups used by this family

n_ops
    number of operations supported by this family

n_mcgrps
    number of multicast groups

mcgrp_offset
    starting number of multicast group IDs in this family
    (private)

module
    *undescribed*

.. _`genl_info`:

struct genl_info
================

.. c:type:: struct genl_info

    receiving information

.. _`genl_info.definition`:

Definition
----------

.. code-block:: c

    struct genl_info {
        u32 snd_seq;
        u32 snd_portid;
        struct nlmsghdr *nlhdr;
        struct genlmsghdr *genlhdr;
        void *userhdr;
        struct nlattr **attrs;
        possible_net_t _net;
        void *user_ptr;
        struct netlink_ext_ack *extack;
    }

.. _`genl_info.members`:

Members
-------

snd_seq
    sending sequence number

snd_portid
    netlink portid of sender

nlhdr
    netlink message header

genlhdr
    generic netlink message header

userhdr
    user specific header

attrs
    netlink attributes

_net
    network namespace

user_ptr
    user pointers

extack
    extended ACK report struct

.. _`genl_ops`:

struct genl_ops
===============

.. c:type:: struct genl_ops

    generic netlink operations

.. _`genl_ops.definition`:

Definition
----------

.. code-block:: c

    struct genl_ops {
        const struct nla_policy *policy;
        int (*doit)(struct sk_buff *skb, struct genl_info *info);
        int (*start)(struct netlink_callback *cb);
        int (*dumpit)(struct sk_buff *skb, struct netlink_callback *cb);
        int (*done)(struct netlink_callback *cb);
        u8 cmd;
        u8 internal_flags;
        u8 flags;
    }

.. _`genl_ops.members`:

Members
-------

policy
    attribute validation policy

doit
    standard command callback

start
    start callback for dumps

dumpit
    callback for dumpers

done
    completion callback for dumps

cmd
    command identifier

internal_flags
    flags used by the family

flags
    flags

.. _`genlmsg_nlhdr`:

genlmsg_nlhdr
=============

.. c:function:: struct nlmsghdr *genlmsg_nlhdr(void *user_hdr, const struct genl_family *family)

    Obtain netlink header from user specified header

    :param void \*user_hdr:
        user header as returned from \ :c:func:`genlmsg_put`\ 

    :param const struct genl_family \*family:
        generic netlink family

.. _`genlmsg_nlhdr.description`:

Description
-----------

Returns pointer to netlink header.

.. _`genlmsg_parse`:

genlmsg_parse
=============

.. c:function:: int genlmsg_parse(const struct nlmsghdr *nlh, const struct genl_family *family, struct nlattr  *tb, int maxtype, const struct nla_policy *policy, struct netlink_ext_ack *extack)

    parse attributes of a genetlink message

    :param const struct nlmsghdr \*nlh:
        netlink message header

    :param const struct genl_family \*family:
        genetlink message family

    :param struct nlattr  \*tb:
        destination array with maxtype+1 elements

    :param int maxtype:
        maximum attribute type to be expected

    :param const struct nla_policy \*policy:
        validation policy

    :param struct netlink_ext_ack \*extack:
        extended ACK report struct

.. _`genl_dump_check_consistent`:

genl_dump_check_consistent
==========================

.. c:function:: void genl_dump_check_consistent(struct netlink_callback *cb, void *user_hdr, const struct genl_family *family)

    check if sequence is consistent and advertise if not

    :param struct netlink_callback \*cb:
        netlink callback structure that stores the sequence number

    :param void \*user_hdr:
        user header as returned from \ :c:func:`genlmsg_put`\ 

    :param const struct genl_family \*family:
        generic netlink family

.. _`genl_dump_check_consistent.description`:

Description
-----------

Cf. \ :c:func:`nl_dump_check_consistent`\ , this just provides a wrapper to make it
simpler to use with generic netlink.

.. _`genlmsg_put_reply`:

genlmsg_put_reply
=================

.. c:function:: void *genlmsg_put_reply(struct sk_buff *skb, struct genl_info *info, const struct genl_family *family, int flags, u8 cmd)

    Add generic netlink header to a reply message

    :param struct sk_buff \*skb:
        socket buffer holding the message

    :param struct genl_info \*info:
        receiver info

    :param const struct genl_family \*family:
        generic netlink family

    :param int flags:
        netlink message flags

    :param u8 cmd:
        generic netlink command

.. _`genlmsg_put_reply.description`:

Description
-----------

Returns pointer to user specific header

.. _`genlmsg_end`:

genlmsg_end
===========

.. c:function:: void genlmsg_end(struct sk_buff *skb, void *hdr)

    Finalize a generic netlink message

    :param struct sk_buff \*skb:
        socket buffer the message is stored in

    :param void \*hdr:
        user specific header

.. _`genlmsg_cancel`:

genlmsg_cancel
==============

.. c:function:: void genlmsg_cancel(struct sk_buff *skb, void *hdr)

    Cancel construction of a generic netlink message

    :param struct sk_buff \*skb:
        socket buffer the message is stored in

    :param void \*hdr:
        generic netlink message header

.. _`genlmsg_multicast_netns`:

genlmsg_multicast_netns
=======================

.. c:function:: int genlmsg_multicast_netns(const struct genl_family *family, struct net *net, struct sk_buff *skb, u32 portid, unsigned int group, gfp_t flags)

    multicast a netlink message to a specific netns

    :param const struct genl_family \*family:
        the generic netlink family

    :param struct net \*net:
        the net namespace

    :param struct sk_buff \*skb:
        netlink message as socket buffer

    :param u32 portid:
        own netlink portid to avoid sending to yourself

    :param unsigned int group:
        offset of multicast group in groups array

    :param gfp_t flags:
        allocation flags

.. _`genlmsg_multicast`:

genlmsg_multicast
=================

.. c:function:: int genlmsg_multicast(const struct genl_family *family, struct sk_buff *skb, u32 portid, unsigned int group, gfp_t flags)

    multicast a netlink message to the default netns

    :param const struct genl_family \*family:
        the generic netlink family

    :param struct sk_buff \*skb:
        netlink message as socket buffer

    :param u32 portid:
        own netlink portid to avoid sending to yourself

    :param unsigned int group:
        offset of multicast group in groups array

    :param gfp_t flags:
        allocation flags

.. _`genlmsg_multicast_allns`:

genlmsg_multicast_allns
=======================

.. c:function:: int genlmsg_multicast_allns(const struct genl_family *family, struct sk_buff *skb, u32 portid, unsigned int group, gfp_t flags)

    multicast a netlink message to all net namespaces

    :param const struct genl_family \*family:
        the generic netlink family

    :param struct sk_buff \*skb:
        netlink message as socket buffer

    :param u32 portid:
        own netlink portid to avoid sending to yourself

    :param unsigned int group:
        offset of multicast group in groups array

    :param gfp_t flags:
        allocation flags

.. _`genlmsg_multicast_allns.description`:

Description
-----------

This function must hold the RTNL or \ :c:func:`rcu_read_lock`\ .

.. _`genlmsg_unicast`:

genlmsg_unicast
===============

.. c:function:: int genlmsg_unicast(struct net *net, struct sk_buff *skb, u32 portid)

    unicast a netlink message

    :param struct net \*net:
        *undescribed*

    :param struct sk_buff \*skb:
        netlink message as socket buffer

    :param u32 portid:
        netlink portid of the destination socket

.. _`genlmsg_reply`:

genlmsg_reply
=============

.. c:function:: int genlmsg_reply(struct sk_buff *skb, struct genl_info *info)

    reply to a request

    :param struct sk_buff \*skb:
        netlink message to be sent back

    :param struct genl_info \*info:
        receiver information

.. _`genlmsg_data`:

genlmsg_data
============

.. c:function:: void *genlmsg_data(const struct genlmsghdr *gnlh)

    head of message payload

    :param const struct genlmsghdr \*gnlh:
        genetlink message header

.. _`genlmsg_len`:

genlmsg_len
===========

.. c:function:: int genlmsg_len(const struct genlmsghdr *gnlh)

    length of message payload

    :param const struct genlmsghdr \*gnlh:
        genetlink message header

.. _`genlmsg_msg_size`:

genlmsg_msg_size
================

.. c:function:: int genlmsg_msg_size(int payload)

    length of genetlink message not including padding

    :param int payload:
        length of message payload

.. _`genlmsg_total_size`:

genlmsg_total_size
==================

.. c:function:: int genlmsg_total_size(int payload)

    length of genetlink message including padding

    :param int payload:
        length of message payload

.. _`genlmsg_new`:

genlmsg_new
===========

.. c:function:: struct sk_buff *genlmsg_new(size_t payload, gfp_t flags)

    Allocate a new generic netlink message

    :param size_t payload:
        size of the message payload

    :param gfp_t flags:
        the type of memory to allocate.

.. _`genl_set_err`:

genl_set_err
============

.. c:function:: int genl_set_err(const struct genl_family *family, struct net *net, u32 portid, u32 group, int code)

    report error to genetlink broadcast listeners

    :param const struct genl_family \*family:
        the generic netlink family

    :param struct net \*net:
        the network namespace to report the error to

    :param u32 portid:
        the PORTID of a process that we want to skip (if any)

    :param u32 group:
        the broadcast group that will notice the error
        (this is the offset of the multicast group in the groups array)

    :param int code:
        error code, must be negative (as usual in kernelspace)

.. _`genl_set_err.description`:

Description
-----------

This function returns the number of broadcast listeners that have set the
NETLINK_RECV_NO_ENOBUFS socket option.

.. This file was automatic generated / don't edit.

