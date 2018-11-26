.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/netlabel/netlabel_mgmt.c

.. _`netlbl_mgmt_add_common`:

netlbl_mgmt_add_common
======================

.. c:function:: int netlbl_mgmt_add_common(struct genl_info *info, struct netlbl_audit *audit_info)

    Handle an ADD message

    :param info:
        the Generic NETLINK info block
    :type info: struct genl_info \*

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`netlbl_mgmt_add_common.description`:

Description
-----------

Helper function for the ADD and ADDDEF messages to add the domain mappings
from the message to the hash table.  See netlabel.h for a description of the
message format.  Returns zero on success, negative values on failure.

.. _`netlbl_mgmt_listentry`:

netlbl_mgmt_listentry
=====================

.. c:function:: int netlbl_mgmt_listentry(struct sk_buff *skb, struct netlbl_dom_map *entry)

    List a NetLabel/LSM domain map entry

    :param skb:
        the NETLINK buffer
    :type skb: struct sk_buff \*

    :param entry:
        the map entry
    :type entry: struct netlbl_dom_map \*

.. _`netlbl_mgmt_listentry.description`:

Description
-----------

This function is a helper function used by the LISTALL and LISTDEF command
handlers.  The caller is responsible for ensuring that the RCU read lock
is held.  Returns zero on success, negative values on failure.

.. _`netlbl_mgmt_add`:

netlbl_mgmt_add
===============

.. c:function:: int netlbl_mgmt_add(struct sk_buff *skb, struct genl_info *info)

    Handle an ADD message

    :param skb:
        the NETLINK buffer
    :type skb: struct sk_buff \*

    :param info:
        the Generic NETLINK info block
    :type info: struct genl_info \*

.. _`netlbl_mgmt_add.description`:

Description
-----------

Process a user generated ADD message and add the domains from the message
to the hash table.  See netlabel.h for a description of the message format.
Returns zero on success, negative values on failure.

.. _`netlbl_mgmt_remove`:

netlbl_mgmt_remove
==================

.. c:function:: int netlbl_mgmt_remove(struct sk_buff *skb, struct genl_info *info)

    Handle a REMOVE message

    :param skb:
        the NETLINK buffer
    :type skb: struct sk_buff \*

    :param info:
        the Generic NETLINK info block
    :type info: struct genl_info \*

.. _`netlbl_mgmt_remove.description`:

Description
-----------

Process a user generated REMOVE message and remove the specified domain
mappings.  Returns zero on success, negative values on failure.

.. _`netlbl_mgmt_listall_cb`:

netlbl_mgmt_listall_cb
======================

.. c:function:: int netlbl_mgmt_listall_cb(struct netlbl_dom_map *entry, void *arg)

    \ :c:func:`netlbl_domhsh_walk`\  callback for LISTALL

    :param entry:
        the domain mapping hash table entry
    :type entry: struct netlbl_dom_map \*

    :param arg:
        the netlbl_domhsh_walk_arg structure
    :type arg: void \*

.. _`netlbl_mgmt_listall_cb.description`:

Description
-----------

This function is designed to be used as a callback to the
\ :c:func:`netlbl_domhsh_walk`\  function for use in generating a response for a LISTALL
message.  Returns the size of the message on success, negative values on
failure.

.. _`netlbl_mgmt_listall`:

netlbl_mgmt_listall
===================

.. c:function:: int netlbl_mgmt_listall(struct sk_buff *skb, struct netlink_callback *cb)

    Handle a LISTALL message

    :param skb:
        the NETLINK buffer
    :type skb: struct sk_buff \*

    :param cb:
        the NETLINK callback
    :type cb: struct netlink_callback \*

.. _`netlbl_mgmt_listall.description`:

Description
-----------

Process a user generated LISTALL message and dumps the domain hash table in
a form suitable for use in a kernel generated LISTALL message.  Returns zero
on success, negative values on failure.

.. _`netlbl_mgmt_adddef`:

netlbl_mgmt_adddef
==================

.. c:function:: int netlbl_mgmt_adddef(struct sk_buff *skb, struct genl_info *info)

    Handle an ADDDEF message

    :param skb:
        the NETLINK buffer
    :type skb: struct sk_buff \*

    :param info:
        the Generic NETLINK info block
    :type info: struct genl_info \*

.. _`netlbl_mgmt_adddef.description`:

Description
-----------

Process a user generated ADDDEF message and respond accordingly.  Returns
zero on success, negative values on failure.

.. _`netlbl_mgmt_removedef`:

netlbl_mgmt_removedef
=====================

.. c:function:: int netlbl_mgmt_removedef(struct sk_buff *skb, struct genl_info *info)

    Handle a REMOVEDEF message

    :param skb:
        the NETLINK buffer
    :type skb: struct sk_buff \*

    :param info:
        the Generic NETLINK info block
    :type info: struct genl_info \*

.. _`netlbl_mgmt_removedef.description`:

Description
-----------

Process a user generated REMOVEDEF message and remove the default domain
mapping.  Returns zero on success, negative values on failure.

.. _`netlbl_mgmt_listdef`:

netlbl_mgmt_listdef
===================

.. c:function:: int netlbl_mgmt_listdef(struct sk_buff *skb, struct genl_info *info)

    Handle a LISTDEF message

    :param skb:
        the NETLINK buffer
    :type skb: struct sk_buff \*

    :param info:
        the Generic NETLINK info block
    :type info: struct genl_info \*

.. _`netlbl_mgmt_listdef.description`:

Description
-----------

Process a user generated LISTDEF message and dumps the default domain
mapping in a form suitable for use in a kernel generated LISTDEF message.
Returns zero on success, negative values on failure.

.. _`netlbl_mgmt_protocols_cb`:

netlbl_mgmt_protocols_cb
========================

.. c:function:: int netlbl_mgmt_protocols_cb(struct sk_buff *skb, struct netlink_callback *cb, u32 protocol)

    Write an individual PROTOCOL message response

    :param skb:
        the skb to write to
    :type skb: struct sk_buff \*

    :param cb:
        the NETLINK callback
    :type cb: struct netlink_callback \*

    :param protocol:
        the NetLabel protocol to use in the message
    :type protocol: u32

.. _`netlbl_mgmt_protocols_cb.description`:

Description
-----------

This function is to be used in conjunction with \ :c:func:`netlbl_mgmt_protocols`\  to
answer a application's PROTOCOLS message.  Returns the size of the message
on success, negative values on failure.

.. _`netlbl_mgmt_protocols`:

netlbl_mgmt_protocols
=====================

.. c:function:: int netlbl_mgmt_protocols(struct sk_buff *skb, struct netlink_callback *cb)

    Handle a PROTOCOLS message

    :param skb:
        the NETLINK buffer
    :type skb: struct sk_buff \*

    :param cb:
        the NETLINK callback
    :type cb: struct netlink_callback \*

.. _`netlbl_mgmt_protocols.description`:

Description
-----------

Process a user generated PROTOCOLS message and respond accordingly.

.. _`netlbl_mgmt_version`:

netlbl_mgmt_version
===================

.. c:function:: int netlbl_mgmt_version(struct sk_buff *skb, struct genl_info *info)

    Handle a VERSION message

    :param skb:
        the NETLINK buffer
    :type skb: struct sk_buff \*

    :param info:
        the Generic NETLINK info block
    :type info: struct genl_info \*

.. _`netlbl_mgmt_version.description`:

Description
-----------

Process a user generated VERSION message and respond accordingly.  Returns
zero on success, negative values on failure.

.. _`netlbl_mgmt_genl_init`:

netlbl_mgmt_genl_init
=====================

.. c:function:: int netlbl_mgmt_genl_init( void)

    Register the NetLabel management component

    :param void:
        no arguments
    :type void: 

.. _`netlbl_mgmt_genl_init.description`:

Description
-----------

Register the NetLabel management component with the Generic NETLINK
mechanism.  Returns zero on success, negative values on failure.

.. This file was automatic generated / don't edit.

