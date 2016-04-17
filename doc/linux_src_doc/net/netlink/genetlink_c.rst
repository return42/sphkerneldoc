.. -*- coding: utf-8; mode: rst -*-

===========
genetlink.c
===========


.. _`__genl_register_family`:

__genl_register_family
======================

.. c:function:: int __genl_register_family (struct genl_family *family)

    register a generic netlink family

    :param struct genl_family \*family:
        generic netlink family



.. _`__genl_register_family.description`:

Description
-----------

Registers the specified family after validating it first. Only one
family may be registered with the same family name or identifier.
The family id may equal GENL_ID_GENERATE causing an unique id to
be automatically generated and assigned.

The family's ops array must already be assigned, you can use the
:c:func:`genl_register_family_with_ops` helper function.

Return 0 on success or a negative error code.



.. _`genl_unregister_family`:

genl_unregister_family
======================

.. c:function:: int genl_unregister_family (struct genl_family *family)

    unregister generic netlink family

    :param struct genl_family \*family:
        generic netlink family



.. _`genl_unregister_family.description`:

Description
-----------

Unregisters the specified family.

Returns 0 on success or a negative error code.



.. _`genlmsg_put`:

genlmsg_put
===========

.. c:function:: void *genlmsg_put (struct sk_buff *skb, u32 portid, u32 seq, struct genl_family *family, int flags, u8 cmd)

    Add generic netlink header to netlink message

    :param struct sk_buff \*skb:
        socket buffer holding the message

    :param u32 portid:
        netlink portid the message is addressed to

    :param u32 seq:
        sequence number (usually the one of the sender)

    :param struct genl_family \*family:
        generic netlink family

    :param int flags:
        netlink message flags

    :param u8 cmd:
        generic netlink command



.. _`genlmsg_put.description`:

Description
-----------

Returns pointer to user specific header

