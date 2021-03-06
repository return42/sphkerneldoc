.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/netlink/genetlink.c

.. _`genl_register_family`:

genl_register_family
====================

.. c:function:: int genl_register_family(struct genl_family *family)

    register a generic netlink family

    :param family:
        generic netlink family
    :type family: struct genl_family \*

.. _`genl_register_family.description`:

Description
-----------

Registers the specified family after validating it first. Only one
family may be registered with the same family name or identifier.

The family's ops, multicast groups and module pointer must already
be assigned.

Return 0 on success or a negative error code.

.. _`genl_unregister_family`:

genl_unregister_family
======================

.. c:function:: int genl_unregister_family(const struct genl_family *family)

    unregister generic netlink family

    :param family:
        generic netlink family
    :type family: const struct genl_family \*

.. _`genl_unregister_family.description`:

Description
-----------

Unregisters the specified family.

Returns 0 on success or a negative error code.

.. _`genlmsg_put`:

genlmsg_put
===========

.. c:function:: void *genlmsg_put(struct sk_buff *skb, u32 portid, u32 seq, const struct genl_family *family, int flags, u8 cmd)

    Add generic netlink header to netlink message

    :param skb:
        socket buffer holding the message
    :type skb: struct sk_buff \*

    :param portid:
        netlink portid the message is addressed to
    :type portid: u32

    :param seq:
        sequence number (usually the one of the sender)
    :type seq: u32

    :param family:
        generic netlink family
    :type family: const struct genl_family \*

    :param flags:
        netlink message flags
    :type flags: int

    :param cmd:
        generic netlink command
    :type cmd: u8

.. _`genlmsg_put.description`:

Description
-----------

Returns pointer to user specific header

.. _`genl_family_attrbuf`:

genl_family_attrbuf
===================

.. c:function:: struct nlattr **genl_family_attrbuf(const struct genl_family *family)

    return family's attrbuf

    :param family:
        the family
    :type family: const struct genl_family \*

.. _`genl_family_attrbuf.description`:

Description
-----------

Return the family's attrbuf, while validating that it's
actually valid to access it.

You cannot use this function with a family that has parallel_ops
and you can only use it within (pre/post) doit/dumpit callbacks.

.. This file was automatic generated / don't edit.

