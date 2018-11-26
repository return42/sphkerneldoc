.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/rtnetlink.c

.. _`rtnl_register_module`:

rtnl_register_module
====================

.. c:function:: int rtnl_register_module(struct module *owner, int protocol, int msgtype, rtnl_doit_func doit, rtnl_dumpit_func dumpit, unsigned int flags)

    Register a rtnetlink message type

    :param owner:
        module registering the hook (THIS_MODULE)
    :type owner: struct module \*

    :param protocol:
        Protocol family or PF_UNSPEC
    :type protocol: int

    :param msgtype:
        rtnetlink message type
    :type msgtype: int

    :param doit:
        Function pointer called for each request message
    :type doit: rtnl_doit_func

    :param dumpit:
        Function pointer called for each dump request (NLM_F_DUMP) message
    :type dumpit: rtnl_dumpit_func

    :param flags:
        rtnl_link_flags to modifiy behaviour of doit/dumpit functions
    :type flags: unsigned int

.. _`rtnl_register_module.description`:

Description
-----------

Like rtnl_register, but for use by removable modules.

.. _`rtnl_register`:

rtnl_register
=============

.. c:function:: void rtnl_register(int protocol, int msgtype, rtnl_doit_func doit, rtnl_dumpit_func dumpit, unsigned int flags)

    Register a rtnetlink message type

    :param protocol:
        Protocol family or PF_UNSPEC
    :type protocol: int

    :param msgtype:
        rtnetlink message type
    :type msgtype: int

    :param doit:
        Function pointer called for each request message
    :type doit: rtnl_doit_func

    :param dumpit:
        Function pointer called for each dump request (NLM_F_DUMP) message
    :type dumpit: rtnl_dumpit_func

    :param flags:
        rtnl_link_flags to modifiy behaviour of doit/dumpit functions
    :type flags: unsigned int

.. _`rtnl_register.description`:

Description
-----------

Registers the specified function pointers (at least one of them has
to be non-NULL) to be called whenever a request message for the
specified protocol family and message type is received.

The special protocol family PF_UNSPEC may be used to define fallback
function pointers for the case when no entry for the specific protocol
family exists.

.. _`rtnl_unregister`:

rtnl_unregister
===============

.. c:function:: int rtnl_unregister(int protocol, int msgtype)

    Unregister a rtnetlink message type

    :param protocol:
        Protocol family or PF_UNSPEC
    :type protocol: int

    :param msgtype:
        rtnetlink message type
    :type msgtype: int

.. _`rtnl_unregister.description`:

Description
-----------

Returns 0 on success or a negative error code.

.. _`rtnl_unregister_all`:

rtnl_unregister_all
===================

.. c:function:: void rtnl_unregister_all(int protocol)

    Unregister all rtnetlink message type of a protocol

    :param protocol:
        Protocol family or PF_UNSPEC
    :type protocol: int

.. _`rtnl_unregister_all.description`:

Description
-----------

Identical to calling \ :c:func:`rtnl_unregster`\  for all registered message types
of a certain protocol family.

.. _`__rtnl_link_register`:

\__rtnl_link_register
=====================

.. c:function:: int __rtnl_link_register(struct rtnl_link_ops *ops)

    Register rtnl_link_ops with rtnetlink.

    :param ops:
        struct rtnl_link_ops \* to register
    :type ops: struct rtnl_link_ops \*

.. _`__rtnl_link_register.description`:

Description
-----------

The caller must hold the rtnl_mutex. This function should be used
by drivers that create devices during module initialization. It
must be called before registering the devices.

Returns 0 on success or a negative error code.

.. _`rtnl_link_register`:

rtnl_link_register
==================

.. c:function:: int rtnl_link_register(struct rtnl_link_ops *ops)

    Register rtnl_link_ops with rtnetlink.

    :param ops:
        struct rtnl_link_ops \* to register
    :type ops: struct rtnl_link_ops \*

.. _`rtnl_link_register.description`:

Description
-----------

Returns 0 on success or a negative error code.

.. _`__rtnl_link_unregister`:

\__rtnl_link_unregister
=======================

.. c:function:: void __rtnl_link_unregister(struct rtnl_link_ops *ops)

    Unregister rtnl_link_ops from rtnetlink.

    :param ops:
        struct rtnl_link_ops \* to unregister
    :type ops: struct rtnl_link_ops \*

.. _`__rtnl_link_unregister.description`:

Description
-----------

The caller must hold the rtnl_mutex and guarantee net_namespace_list
integrity (hold pernet_ops_rwsem for writing to close the race
with \ :c:func:`setup_net`\  and \ :c:func:`cleanup_net`\ ).

.. _`rtnl_link_unregister`:

rtnl_link_unregister
====================

.. c:function:: void rtnl_link_unregister(struct rtnl_link_ops *ops)

    Unregister rtnl_link_ops from rtnetlink.

    :param ops:
        struct rtnl_link_ops \* to unregister
    :type ops: struct rtnl_link_ops \*

.. _`rtnl_af_register`:

rtnl_af_register
================

.. c:function:: void rtnl_af_register(struct rtnl_af_ops *ops)

    Register rtnl_af_ops with rtnetlink.

    :param ops:
        struct rtnl_af_ops \* to register
    :type ops: struct rtnl_af_ops \*

.. _`rtnl_af_register.description`:

Description
-----------

Returns 0 on success or a negative error code.

.. _`rtnl_af_unregister`:

rtnl_af_unregister
==================

.. c:function:: void rtnl_af_unregister(struct rtnl_af_ops *ops)

    Unregister rtnl_af_ops from rtnetlink.

    :param ops:
        struct rtnl_af_ops \* to unregister
    :type ops: struct rtnl_af_ops \*

.. _`rtnl_get_net_ns_capable`:

rtnl_get_net_ns_capable
=======================

.. c:function:: struct net *rtnl_get_net_ns_capable(struct sock *sk, int netnsid)

    Get netns if sufficiently privileged.

    :param sk:
        netlink socket
    :type sk: struct sock \*

    :param netnsid:
        network namespace identifier
    :type netnsid: int

.. _`rtnl_get_net_ns_capable.description`:

Description
-----------

Returns the network namespace identified by netnsid on success or an error
pointer on failure.

.. _`ndo_dflt_fdb_add`:

ndo_dflt_fdb_add
================

.. c:function:: int ndo_dflt_fdb_add(struct ndmsg *ndm, struct nlattr  *tb, struct net_device *dev, const unsigned char *addr, u16 vid, u16 flags)

    default netdevice operation to add an FDB entry

    :param ndm:
        *undescribed*
    :type ndm: struct ndmsg \*

    :param tb:
        *undescribed*
    :type tb: struct nlattr  \*

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

    :param addr:
        *undescribed*
    :type addr: const unsigned char \*

    :param vid:
        *undescribed*
    :type vid: u16

    :param flags:
        *undescribed*
    :type flags: u16

.. _`ndo_dflt_fdb_del`:

ndo_dflt_fdb_del
================

.. c:function:: int ndo_dflt_fdb_del(struct ndmsg *ndm, struct nlattr  *tb, struct net_device *dev, const unsigned char *addr, u16 vid)

    default netdevice operation to delete an FDB entry

    :param ndm:
        *undescribed*
    :type ndm: struct ndmsg \*

    :param tb:
        *undescribed*
    :type tb: struct nlattr  \*

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

    :param addr:
        *undescribed*
    :type addr: const unsigned char \*

    :param vid:
        *undescribed*
    :type vid: u16

.. _`ndo_dflt_fdb_dump`:

ndo_dflt_fdb_dump
=================

.. c:function:: int ndo_dflt_fdb_dump(struct sk_buff *skb, struct netlink_callback *cb, struct net_device *dev, struct net_device *filter_dev, int *idx)

    default netdevice operation to dump an FDB table.

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param cb:
        *undescribed*
    :type cb: struct netlink_callback \*

    :param dev:
        netdevice
    :type dev: struct net_device \*

    :param filter_dev:
        *undescribed*
    :type filter_dev: struct net_device \*

    :param idx:
        *undescribed*
    :type idx: int \*

.. _`ndo_dflt_fdb_dump.description`:

Description
-----------

Default netdevice operation to dump the existing unicast address list.
Returns number of addresses from list put in skb.

.. This file was automatic generated / don't edit.

