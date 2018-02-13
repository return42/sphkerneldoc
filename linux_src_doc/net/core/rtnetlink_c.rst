.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/rtnetlink.c

.. _`rtnl_register_module`:

rtnl_register_module
====================

.. c:function:: int rtnl_register_module(struct module *owner, int protocol, int msgtype, rtnl_doit_func doit, rtnl_dumpit_func dumpit, unsigned int flags)

    Register a rtnetlink message type

    :param struct module \*owner:
        module registering the hook (THIS_MODULE)

    :param int protocol:
        Protocol family or PF_UNSPEC

    :param int msgtype:
        rtnetlink message type

    :param rtnl_doit_func doit:
        Function pointer called for each request message

    :param rtnl_dumpit_func dumpit:
        Function pointer called for each dump request (NLM_F_DUMP) message

    :param unsigned int flags:
        rtnl_link_flags to modifiy behaviour of doit/dumpit functions

.. _`rtnl_register_module.description`:

Description
-----------

Like rtnl_register, but for use by removable modules.

.. _`rtnl_register`:

rtnl_register
=============

.. c:function:: void rtnl_register(int protocol, int msgtype, rtnl_doit_func doit, rtnl_dumpit_func dumpit, unsigned int flags)

    Register a rtnetlink message type

    :param int protocol:
        Protocol family or PF_UNSPEC

    :param int msgtype:
        rtnetlink message type

    :param rtnl_doit_func doit:
        Function pointer called for each request message

    :param rtnl_dumpit_func dumpit:
        Function pointer called for each dump request (NLM_F_DUMP) message

    :param unsigned int flags:
        rtnl_link_flags to modifiy behaviour of doit/dumpit functions

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

    :param int protocol:
        Protocol family or PF_UNSPEC

    :param int msgtype:
        rtnetlink message type

.. _`rtnl_unregister.description`:

Description
-----------

Returns 0 on success or a negative error code.

.. _`rtnl_unregister_all`:

rtnl_unregister_all
===================

.. c:function:: void rtnl_unregister_all(int protocol)

    Unregister all rtnetlink message type of a protocol

    :param int protocol:
        Protocol family or PF_UNSPEC

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

    :param struct rtnl_link_ops \*ops:
        struct rtnl_link_ops \* to register

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

    :param struct rtnl_link_ops \*ops:
        struct rtnl_link_ops \* to register

.. _`rtnl_link_register.description`:

Description
-----------

Returns 0 on success or a negative error code.

.. _`__rtnl_link_unregister`:

\__rtnl_link_unregister
=======================

.. c:function:: void __rtnl_link_unregister(struct rtnl_link_ops *ops)

    Unregister rtnl_link_ops from rtnetlink.

    :param struct rtnl_link_ops \*ops:
        struct rtnl_link_ops \* to unregister

.. _`__rtnl_link_unregister.description`:

Description
-----------

The caller must hold the rtnl_mutex.

.. _`rtnl_link_unregister`:

rtnl_link_unregister
====================

.. c:function:: void rtnl_link_unregister(struct rtnl_link_ops *ops)

    Unregister rtnl_link_ops from rtnetlink.

    :param struct rtnl_link_ops \*ops:
        struct rtnl_link_ops \* to unregister

.. _`rtnl_af_register`:

rtnl_af_register
================

.. c:function:: void rtnl_af_register(struct rtnl_af_ops *ops)

    Register rtnl_af_ops with rtnetlink.

    :param struct rtnl_af_ops \*ops:
        struct rtnl_af_ops \* to register

.. _`rtnl_af_register.description`:

Description
-----------

Returns 0 on success or a negative error code.

.. _`rtnl_af_unregister`:

rtnl_af_unregister
==================

.. c:function:: void rtnl_af_unregister(struct rtnl_af_ops *ops)

    Unregister rtnl_af_ops from rtnetlink.

    :param struct rtnl_af_ops \*ops:
        struct rtnl_af_ops \* to unregister

.. _`ndo_dflt_fdb_add`:

ndo_dflt_fdb_add
================

.. c:function:: int ndo_dflt_fdb_add(struct ndmsg *ndm, struct nlattr  *tb, struct net_device *dev, const unsigned char *addr, u16 vid, u16 flags)

    default netdevice operation to add an FDB entry

    :param struct ndmsg \*ndm:
        *undescribed*

    :param struct nlattr  \*tb:
        *undescribed*

    :param struct net_device \*dev:
        *undescribed*

    :param const unsigned char \*addr:
        *undescribed*

    :param u16 vid:
        *undescribed*

    :param u16 flags:
        *undescribed*

.. _`ndo_dflt_fdb_del`:

ndo_dflt_fdb_del
================

.. c:function:: int ndo_dflt_fdb_del(struct ndmsg *ndm, struct nlattr  *tb, struct net_device *dev, const unsigned char *addr, u16 vid)

    default netdevice operation to delete an FDB entry

    :param struct ndmsg \*ndm:
        *undescribed*

    :param struct nlattr  \*tb:
        *undescribed*

    :param struct net_device \*dev:
        *undescribed*

    :param const unsigned char \*addr:
        *undescribed*

    :param u16 vid:
        *undescribed*

.. _`ndo_dflt_fdb_dump`:

ndo_dflt_fdb_dump
=================

.. c:function:: int ndo_dflt_fdb_dump(struct sk_buff *skb, struct netlink_callback *cb, struct net_device *dev, struct net_device *filter_dev, int *idx)

    default netdevice operation to dump an FDB table.

    :param struct sk_buff \*skb:
        *undescribed*

    :param struct netlink_callback \*cb:
        *undescribed*

    :param struct net_device \*dev:
        netdevice

    :param struct net_device \*filter_dev:
        *undescribed*

    :param int \*idx:
        *undescribed*

.. _`ndo_dflt_fdb_dump.description`:

Description
-----------

Default netdevice operation to dump the existing unicast address list.
Returns number of addresses from list put in skb.

.. This file was automatic generated / don't edit.

