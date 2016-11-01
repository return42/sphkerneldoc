.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/netlabel/netlabel_calipso.c

.. _`netlbl_calipso_add_pass`:

netlbl_calipso_add_pass
=======================

.. c:function:: int netlbl_calipso_add_pass(struct genl_info *info, struct netlbl_audit *audit_info)

    Adds a CALIPSO pass DOI definition

    :param struct genl_info \*info:
        the Generic NETLINK info block

    :param struct netlbl_audit \*audit_info:
        NetLabel audit information

.. _`netlbl_calipso_add_pass.description`:

Description
-----------

Create a new CALIPSO_MAP_PASS DOI definition based on the given ADD message
and add it to the CALIPSO engine.  Return zero on success and non-zero on
error.

.. _`netlbl_calipso_add`:

netlbl_calipso_add
==================

.. c:function:: int netlbl_calipso_add(struct sk_buff *skb, struct genl_info *info)

    Handle an ADD message

    :param struct sk_buff \*skb:
        the NETLINK buffer

    :param struct genl_info \*info:
        the Generic NETLINK info block

.. _`netlbl_calipso_add.description`:

Description
-----------

Create a new DOI definition based on the given ADD message and add it to the
CALIPSO engine.  Returns zero on success, negative values on failure.

.. _`netlbl_calipso_list`:

netlbl_calipso_list
===================

.. c:function:: int netlbl_calipso_list(struct sk_buff *skb, struct genl_info *info)

    Handle a LIST message

    :param struct sk_buff \*skb:
        the NETLINK buffer

    :param struct genl_info \*info:
        the Generic NETLINK info block

.. _`netlbl_calipso_list.description`:

Description
-----------

Process a user generated LIST message and respond accordingly.
Returns zero on success and negative values on error.

.. _`netlbl_calipso_listall_cb`:

netlbl_calipso_listall_cb
=========================

.. c:function:: int netlbl_calipso_listall_cb(struct calipso_doi *doi_def, void *arg)

    calipso_doi_walk() callback for LISTALL

    :param struct calipso_doi \*doi_def:
        the CALIPSO DOI definition

    :param void \*arg:
        the netlbl_calipso_doiwalk_arg structure

.. _`netlbl_calipso_listall_cb.description`:

Description
-----------

This function is designed to be used as a callback to the
\ :c:func:`calipso_doi_walk`\  function for use in generating a response for a LISTALL
message.  Returns the size of the message on success, negative values on
failure.

.. _`netlbl_calipso_listall`:

netlbl_calipso_listall
======================

.. c:function:: int netlbl_calipso_listall(struct sk_buff *skb, struct netlink_callback *cb)

    Handle a LISTALL message

    :param struct sk_buff \*skb:
        the NETLINK buffer

    :param struct netlink_callback \*cb:
        the NETLINK callback

.. _`netlbl_calipso_listall.description`:

Description
-----------

Process a user generated LISTALL message and respond accordingly.  Returns
zero on success and negative values on error.

.. _`netlbl_calipso_remove_cb`:

netlbl_calipso_remove_cb
========================

.. c:function:: int netlbl_calipso_remove_cb(struct netlbl_dom_map *entry, void *arg)

    netlbl_calipso_remove() callback for REMOVE

    :param struct netlbl_dom_map \*entry:
        LSM domain mapping entry

    :param void \*arg:
        the netlbl_domhsh_walk_arg structure

.. _`netlbl_calipso_remove_cb.description`:

Description
-----------

This function is intended for use by \ :c:func:`netlbl_calipso_remove`\  as the callback
for the \ :c:func:`netlbl_domhsh_walk`\  function; it removes LSM domain map entries
which are associated with the CALIPSO DOI specified in \ ``arg``\ .  Returns zero on
success, negative values on failure.

.. _`netlbl_calipso_remove`:

netlbl_calipso_remove
=====================

.. c:function:: int netlbl_calipso_remove(struct sk_buff *skb, struct genl_info *info)

    Handle a REMOVE message

    :param struct sk_buff \*skb:
        the NETLINK buffer

    :param struct genl_info \*info:
        the Generic NETLINK info block

.. _`netlbl_calipso_remove.description`:

Description
-----------

Process a user generated REMOVE message and respond accordingly.  Returns
zero on success, negative values on failure.

.. _`netlbl_calipso_genl_init`:

netlbl_calipso_genl_init
========================

.. c:function:: int netlbl_calipso_genl_init( void)

    Register the CALIPSO NetLabel component

    :param  void:
        no arguments

.. _`netlbl_calipso_genl_init.description`:

Description
-----------

Register the CALIPSO packet NetLabel component with the Generic NETLINK
mechanism.  Returns zero on success, negative values on failure.

.. _`netlbl_calipso_ops_register`:

netlbl_calipso_ops_register
===========================

.. c:function:: const struct netlbl_calipso_ops *netlbl_calipso_ops_register(const struct netlbl_calipso_ops *ops)

    Register the CALIPSO operations

    :param const struct netlbl_calipso_ops \*ops:
        *undescribed*

.. _`netlbl_calipso_ops_register.description`:

Description
-----------

Register the CALIPSO packet engine operations.

.. _`calipso_doi_add`:

calipso_doi_add
===============

.. c:function:: int calipso_doi_add(struct calipso_doi *doi_def, struct netlbl_audit *audit_info)

    Add a new DOI to the CALIPSO protocol engine

    :param struct calipso_doi \*doi_def:
        the DOI structure

    :param struct netlbl_audit \*audit_info:
        NetLabel audit information

.. _`calipso_doi_add.description`:

Description
-----------

The caller defines a new DOI for use by the CALIPSO engine and calls this
function to add it to the list of acceptable domains.  The caller must
ensure that the mapping table specified in \ ``doi_def``\ ->map meets all of the
requirements of the mapping type (see calipso.h for details).  Returns
zero on success and non-zero on failure.

.. _`calipso_doi_free`:

calipso_doi_free
================

.. c:function:: void calipso_doi_free(struct calipso_doi *doi_def)

    Frees a DOI definition

    :param struct calipso_doi \*doi_def:
        the DOI definition

.. _`calipso_doi_free.description`:

Description
-----------

This function frees all of the memory associated with a DOI definition.

.. _`calipso_doi_remove`:

calipso_doi_remove
==================

.. c:function:: int calipso_doi_remove(u32 doi, struct netlbl_audit *audit_info)

    Remove an existing DOI from the CALIPSO protocol engine

    :param u32 doi:
        the DOI value

    :param struct netlbl_audit \*audit_info:
        *undescribed*

.. _`calipso_doi_remove.description`:

Description
-----------

Removes a DOI definition from the CALIPSO engine.  The NetLabel routines will
be called to release their own LSM domain mappings as well as our own
domain list.  Returns zero on success and negative values on failure.

.. _`calipso_doi_getdef`:

calipso_doi_getdef
==================

.. c:function:: struct calipso_doi *calipso_doi_getdef(u32 doi)

    Returns a reference to a valid DOI definition

    :param u32 doi:
        the DOI value

.. _`calipso_doi_getdef.description`:

Description
-----------

Searches for a valid DOI definition and if one is found it is returned to
the caller.  Otherwise NULL is returned.  The caller must ensure that
\ :c:func:`calipso_doi_putdef`\  is called when the caller is done.

.. _`calipso_doi_putdef`:

calipso_doi_putdef
==================

.. c:function:: void calipso_doi_putdef(struct calipso_doi *doi_def)

    Releases a reference for the given DOI definition

    :param struct calipso_doi \*doi_def:
        the DOI definition

.. _`calipso_doi_putdef.description`:

Description
-----------

Releases a DOI definition reference obtained from \ :c:func:`calipso_doi_getdef`\ .

.. _`calipso_doi_walk`:

calipso_doi_walk
================

.. c:function:: int calipso_doi_walk(u32 *skip_cnt, int (*callback)(struct calipso_doi *doi_def, void *arg), void *cb_arg)

    Iterate through the DOI definitions

    :param u32 \*skip_cnt:
        skip past this number of DOI definitions, updated

    :param int (\*callback)(struct calipso_doi \*doi_def, void \*arg):
        callback for each DOI definition

    :param void \*cb_arg:
        argument for the callback function

.. _`calipso_doi_walk.description`:

Description
-----------

Iterate over the DOI definition list, skipping the first \ ``skip_cnt``\  entries.
For each entry call \ ``callback``\ , if \ ``callback``\  returns a negative value stop
'walking' through the list and return.  Updates the value in \ ``skip_cnt``\  upon
return.  Returns zero on success, negative values on failure.

.. _`calipso_sock_getattr`:

calipso_sock_getattr
====================

.. c:function:: int calipso_sock_getattr(struct sock *sk, struct netlbl_lsm_secattr *secattr)

    Get the security attributes from a sock

    :param struct sock \*sk:
        the sock

    :param struct netlbl_lsm_secattr \*secattr:
        the security attributes

.. _`calipso_sock_getattr.description`:

Description
-----------

Query \ ``sk``\  to see if there is a CALIPSO option attached to the sock and if
there is return the CALIPSO security attributes in \ ``secattr``\ .  This function
requires that \ ``sk``\  be locked, or privately held, but it does not do any
locking itself.  Returns zero on success and negative values on failure.

.. _`calipso_sock_setattr`:

calipso_sock_setattr
====================

.. c:function:: int calipso_sock_setattr(struct sock *sk, const struct calipso_doi *doi_def, const struct netlbl_lsm_secattr *secattr)

    Add a CALIPSO option to a socket

    :param struct sock \*sk:
        the socket

    :param const struct calipso_doi \*doi_def:
        the CALIPSO DOI to use

    :param const struct netlbl_lsm_secattr \*secattr:
        the specific security attributes of the socket

.. _`calipso_sock_setattr.description`:

Description
-----------

Set the CALIPSO option on the given socket using the DOI definition and
security attributes passed to the function.  This function requires
exclusive access to \ ``sk``\ , which means it either needs to be in the
process of being created or locked.  Returns zero on success and negative
values on failure.

.. _`calipso_sock_delattr`:

calipso_sock_delattr
====================

.. c:function:: void calipso_sock_delattr(struct sock *sk)

    Delete the CALIPSO option from a socket

    :param struct sock \*sk:
        the socket

.. _`calipso_sock_delattr.description`:

Description
-----------

Removes the CALIPSO option from a socket, if present.

.. _`calipso_req_setattr`:

calipso_req_setattr
===================

.. c:function:: int calipso_req_setattr(struct request_sock *req, const struct calipso_doi *doi_def, const struct netlbl_lsm_secattr *secattr)

    Add a CALIPSO option to a connection request socket

    :param struct request_sock \*req:
        the connection request socket

    :param const struct calipso_doi \*doi_def:
        the CALIPSO DOI to use

    :param const struct netlbl_lsm_secattr \*secattr:
        the specific security attributes of the socket

.. _`calipso_req_setattr.description`:

Description
-----------

Set the CALIPSO option on the given socket using the DOI definition and
security attributes passed to the function.  Returns zero on success and
negative values on failure.

.. _`calipso_req_delattr`:

calipso_req_delattr
===================

.. c:function:: void calipso_req_delattr(struct request_sock *req)

    Delete the CALIPSO option from a request socket

    :param struct request_sock \*req:
        *undescribed*

.. _`calipso_req_delattr.description`:

Description
-----------

Removes the CALIPSO option from a request socket, if present.

.. _`calipso_optptr`:

calipso_optptr
==============

.. c:function:: unsigned char *calipso_optptr(const struct sk_buff *skb)

    Find the CALIPSO option in the packet

    :param const struct sk_buff \*skb:
        the packet

.. _`calipso_optptr.description`:

Description
-----------

Parse the packet's IP header looking for a CALIPSO option.  Returns a pointer
to the start of the CALIPSO option on success, NULL if one if not found.

.. _`calipso_getattr`:

calipso_getattr
===============

.. c:function:: int calipso_getattr(const unsigned char *calipso, struct netlbl_lsm_secattr *secattr)

    Get the security attributes from a memory block.

    :param const unsigned char \*calipso:
        the CALIPSO option

    :param struct netlbl_lsm_secattr \*secattr:
        the security attributes

.. _`calipso_getattr.description`:

Description
-----------

Inspect \ ``calipso``\  and return the security attributes in \ ``secattr``\ .
Returns zero on success and negative values on failure.

.. _`calipso_skbuff_setattr`:

calipso_skbuff_setattr
======================

.. c:function:: int calipso_skbuff_setattr(struct sk_buff *skb, const struct calipso_doi *doi_def, const struct netlbl_lsm_secattr *secattr)

    Set the CALIPSO option on a packet

    :param struct sk_buff \*skb:
        the packet

    :param const struct calipso_doi \*doi_def:
        the CALIPSO DOI to use

    :param const struct netlbl_lsm_secattr \*secattr:
        the security attributes

.. _`calipso_skbuff_setattr.description`:

Description
-----------

Set the CALIPSO option on the given packet based on the security attributes.
Returns a pointer to the IP header on success and NULL on failure.

.. _`calipso_skbuff_delattr`:

calipso_skbuff_delattr
======================

.. c:function:: int calipso_skbuff_delattr(struct sk_buff *skb)

    Delete any CALIPSO options from a packet

    :param struct sk_buff \*skb:
        the packet

.. _`calipso_skbuff_delattr.description`:

Description
-----------

Removes any and all CALIPSO options from the given packet.  Returns zero on
success, negative values on failure.

.. _`calipso_cache_invalidate`:

calipso_cache_invalidate
========================

.. c:function:: void calipso_cache_invalidate( void)

    Invalidates the current CALIPSO cache

    :param  void:
        no arguments

.. _`calipso_cache_invalidate.description`:

Description
-----------

Invalidates and frees any entries in the CALIPSO cache.  Returns zero on
success and negative values on failure.

.. _`calipso_cache_add`:

calipso_cache_add
=================

.. c:function:: int calipso_cache_add(const unsigned char *calipso_ptr, const struct netlbl_lsm_secattr *secattr)

    Add an entry to the CALIPSO cache

    :param const unsigned char \*calipso_ptr:
        the CALIPSO option

    :param const struct netlbl_lsm_secattr \*secattr:
        the packet's security attributes

.. _`calipso_cache_add.description`:

Description
-----------

Add a new entry into the CALIPSO label mapping cache.
Returns zero on success, negative values on failure.

.. This file was automatic generated / don't edit.

