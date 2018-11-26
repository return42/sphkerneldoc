.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv6/calipso.c

.. _`calipso_cache_entry_free`:

calipso_cache_entry_free
========================

.. c:function:: void calipso_cache_entry_free(struct calipso_map_cache_entry *entry)

    Frees a cache entry

    :param entry:
        the entry to free
    :type entry: struct calipso_map_cache_entry \*

.. _`calipso_cache_entry_free.description`:

Description
-----------

This function frees the memory associated with a cache entry including the
LSM cache data if there are no longer any users, i.e. reference count == 0.

.. _`calipso_map_cache_hash`:

calipso_map_cache_hash
======================

.. c:function:: u32 calipso_map_cache_hash(const unsigned char *key, u32 key_len)

    Hashing function for the CALIPSO cache

    :param key:
        the hash key
    :type key: const unsigned char \*

    :param key_len:
        the length of the key in bytes
    :type key_len: u32

.. _`calipso_map_cache_hash.description`:

Description
-----------

The CALIPSO tag hashing function.  Returns a 32-bit hash value.

.. _`calipso_cache_init`:

calipso_cache_init
==================

.. c:function:: int calipso_cache_init( void)

    Initialize the CALIPSO cache

    :param void:
        no arguments
    :type void: 

.. _`calipso_cache_init.description`:

Description
-----------

Initializes the CALIPSO label mapping cache, this function should be called
before any of the other functions defined in this file.  Returns zero on
success, negative values on error.

.. _`calipso_cache_invalidate`:

calipso_cache_invalidate
========================

.. c:function:: void calipso_cache_invalidate( void)

    Invalidates the current CALIPSO cache

    :param void:
        no arguments
    :type void: 

.. _`calipso_cache_invalidate.description`:

Description
-----------

Invalidates and frees any entries in the CALIPSO cache.  Returns zero on
success and negative values on failure.

.. _`calipso_cache_check`:

calipso_cache_check
===================

.. c:function:: int calipso_cache_check(const unsigned char *key, u32 key_len, struct netlbl_lsm_secattr *secattr)

    Check the CALIPSO cache for a label mapping

    :param key:
        the buffer to check
    :type key: const unsigned char \*

    :param key_len:
        buffer length in bytes
    :type key_len: u32

    :param secattr:
        the security attribute struct to use
    :type secattr: struct netlbl_lsm_secattr \*

.. _`calipso_cache_check.description`:

Description
-----------

This function checks the cache to see if a label mapping already exists for
the given key.  If there is a match then the cache is adjusted and the
\ ``secattr``\  struct is populated with the correct LSM security attributes.  The
cache is adjusted in the following manner if the entry is not already the

.. _`calipso_cache_check.first-in-the-cache-bucket`:

first in the cache bucket
-------------------------


1. The cache entry's activity counter is incremented
2. The previous (higher ranking) entry's activity counter is decremented
3. If the difference between the two activity counters is geater than
CALIPSO_CACHE_REORDERLIMIT the two entries are swapped

Returns zero on success, -ENOENT for a cache miss, and other negative values
on error.

.. _`calipso_cache_add`:

calipso_cache_add
=================

.. c:function:: int calipso_cache_add(const unsigned char *calipso_ptr, const struct netlbl_lsm_secattr *secattr)

    Add an entry to the CALIPSO cache

    :param calipso_ptr:
        the CALIPSO option
    :type calipso_ptr: const unsigned char \*

    :param secattr:
        the packet's security attributes
    :type secattr: const struct netlbl_lsm_secattr \*

.. _`calipso_cache_add.description`:

Description
-----------

Add a new entry into the CALIPSO label mapping cache.  Add the new entry to
head of the cache bucket's list, if the cache bucket is out of room remove
the last entry in the list first.  It is important to note that there is
currently no checking for duplicate keys.  Returns zero on success,
negative values on failure.  The key stored starts at calipso_ptr + 2,
i.e. the type and length bytes are not stored, this corresponds to
calipso_ptr[1] bytes of data.

.. _`calipso_doi_search`:

calipso_doi_search
==================

.. c:function:: struct calipso_doi *calipso_doi_search(u32 doi)

    Searches for a DOI definition

    :param doi:
        the DOI to search for
    :type doi: u32

.. _`calipso_doi_search.description`:

Description
-----------

Search the DOI definition list for a DOI definition with a DOI value that
matches \ ``doi``\ .  The caller is responsible for calling rcu_read_[un]lock().
Returns a pointer to the DOI definition on success and NULL on failure.

.. _`calipso_doi_add`:

calipso_doi_add
===============

.. c:function:: int calipso_doi_add(struct calipso_doi *doi_def, struct netlbl_audit *audit_info)

    Add a new DOI to the CALIPSO protocol engine

    :param doi_def:
        the DOI structure
    :type doi_def: struct calipso_doi \*

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`calipso_doi_add.description`:

Description
-----------

The caller defines a new DOI for use by the CALIPSO engine and calls this
function to add it to the list of acceptable domains.  The caller must
ensure that the mapping table specified in \ ``doi_def->map``\  meets all of the
requirements of the mapping type (see calipso.h for details).  Returns
zero on success and non-zero on failure.

.. _`calipso_doi_free`:

calipso_doi_free
================

.. c:function:: void calipso_doi_free(struct calipso_doi *doi_def)

    Frees a DOI definition

    :param doi_def:
        the DOI definition
    :type doi_def: struct calipso_doi \*

.. _`calipso_doi_free.description`:

Description
-----------

This function frees all of the memory associated with a DOI definition.

.. _`calipso_doi_free_rcu`:

calipso_doi_free_rcu
====================

.. c:function:: void calipso_doi_free_rcu(struct rcu_head *entry)

    Frees a DOI definition via the RCU pointer

    :param entry:
        the entry's RCU field
    :type entry: struct rcu_head \*

.. _`calipso_doi_free_rcu.description`:

Description
-----------

This function is designed to be used as a callback to the \ :c:func:`call_rcu`\ 
function so that the memory allocated to the DOI definition can be released
safely.

.. _`calipso_doi_remove`:

calipso_doi_remove
==================

.. c:function:: int calipso_doi_remove(u32 doi, struct netlbl_audit *audit_info)

    Remove an existing DOI from the CALIPSO protocol engine

    :param doi:
        the DOI value
    :type doi: u32

    :param audit_info:
        *undescribed*
    :type audit_info: struct netlbl_audit \*

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

    :param doi:
        the DOI value
    :type doi: u32

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

    :param doi_def:
        the DOI definition
    :type doi_def: struct calipso_doi \*

.. _`calipso_doi_putdef.description`:

Description
-----------

Releases a DOI definition reference obtained from \ :c:func:`calipso_doi_getdef`\ .

.. _`calipso_doi_walk`:

calipso_doi_walk
================

.. c:function:: int calipso_doi_walk(u32 *skip_cnt, int (*callback)(struct calipso_doi *doi_def, void *arg), void *cb_arg)

    Iterate through the DOI definitions

    :param skip_cnt:
        skip past this number of DOI definitions, updated
    :type skip_cnt: u32 \*

    :param int (\*callback)(struct calipso_doi \*doi_def, void \*arg):
        callback for each DOI definition

    :param cb_arg:
        argument for the callback function
    :type cb_arg: void \*

.. _`calipso_doi_walk.description`:

Description
-----------

Iterate over the DOI definition list, skipping the first \ ``skip_cnt``\  entries.
For each entry call \ ``callback``\ , if \ ``callback``\  returns a negative value stop
'walking' through the list and return.  Updates the value in \ ``skip_cnt``\  upon
return.  Returns zero on success, negative values on failure.

.. _`calipso_validate`:

calipso_validate
================

.. c:function:: bool calipso_validate(const struct sk_buff *skb, const unsigned char *option)

    Validate a CALIPSO option

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

    :param option:
        the start of the option
    :type option: const unsigned char \*

.. _`calipso_validate.description`:

Description
-----------

This routine is called to validate a CALIPSO option.
If the option is valid then \ ``true``\  is returned, otherwise
\ ``false``\  is returned.

The caller should have already checked that the length of the
option (including the TLV header) is >= 10 and that the catmap
length is consistent with the option length.

We leave checks on the level and categories to the socket layer.

.. _`calipso_map_cat_hton`:

calipso_map_cat_hton
====================

.. c:function:: int calipso_map_cat_hton(const struct calipso_doi *doi_def, const struct netlbl_lsm_secattr *secattr, unsigned char *net_cat, u32 net_cat_len)

    Perform a category mapping from host to network

    :param doi_def:
        the DOI definition
    :type doi_def: const struct calipso_doi \*

    :param secattr:
        the security attributes
    :type secattr: const struct netlbl_lsm_secattr \*

    :param net_cat:
        the zero'd out category bitmap in network/CALIPSO format
    :type net_cat: unsigned char \*

    :param net_cat_len:
        the length of the CALIPSO bitmap in bytes
    :type net_cat_len: u32

.. _`calipso_map_cat_hton.description`:

Description
-----------

Perform a label mapping to translate a local MLS category bitmap to the
correct CALIPSO bitmap using the given DOI definition.  Returns the minimum
size in bytes of the network bitmap on success, negative values otherwise.

.. _`calipso_map_cat_ntoh`:

calipso_map_cat_ntoh
====================

.. c:function:: int calipso_map_cat_ntoh(const struct calipso_doi *doi_def, const unsigned char *net_cat, u32 net_cat_len, struct netlbl_lsm_secattr *secattr)

    Perform a category mapping from network to host

    :param doi_def:
        the DOI definition
    :type doi_def: const struct calipso_doi \*

    :param net_cat:
        the category bitmap in network/CALIPSO format
    :type net_cat: const unsigned char \*

    :param net_cat_len:
        the length of the CALIPSO bitmap in bytes
    :type net_cat_len: u32

    :param secattr:
        the security attributes
    :type secattr: struct netlbl_lsm_secattr \*

.. _`calipso_map_cat_ntoh.description`:

Description
-----------

Perform a label mapping to translate a CALIPSO bitmap to the correct local
MLS category bitmap using the given DOI definition.  Returns zero on
success, negative values on failure.

.. _`calipso_pad_write`:

calipso_pad_write
=================

.. c:function:: int calipso_pad_write(unsigned char *buf, unsigned int offset, unsigned int count)

    Writes pad bytes in TLV format

    :param buf:
        the buffer
    :type buf: unsigned char \*

    :param offset:
        offset from start of buffer to write padding
    :type offset: unsigned int

    :param count:
        number of pad bytes to write
    :type count: unsigned int

.. _`calipso_pad_write.description`:

Description
-----------

Write \ ``count``\  bytes of TLV padding into \ ``buffer``\  starting at offset \ ``offset``\ .
\ ``count``\  should be less than 8 - see RFC 4942.

.. _`calipso_genopt`:

calipso_genopt
==============

.. c:function:: int calipso_genopt(unsigned char *buf, u32 start, u32 buf_len, const struct calipso_doi *doi_def, const struct netlbl_lsm_secattr *secattr)

    Generate a CALIPSO option

    :param buf:
        the option buffer
    :type buf: unsigned char \*

    :param start:
        offset from which to write
    :type start: u32

    :param buf_len:
        the size of opt_buf
    :type buf_len: u32

    :param doi_def:
        the CALIPSO DOI to use
    :type doi_def: const struct calipso_doi \*

    :param secattr:
        the security attributes
    :type secattr: const struct netlbl_lsm_secattr \*

.. _`calipso_genopt.description`:

Description
-----------

Generate a CALIPSO option using the DOI definition and security attributes
passed to the function. This also generates upto three bytes of leading
padding that ensures that the option is 4n + 2 aligned.  It returns the
number of bytes written (including any initial padding).

.. _`calipso_opt_update`:

calipso_opt_update
==================

.. c:function:: int calipso_opt_update(struct sock *sk, struct ipv6_opt_hdr *hop)

    Replaces socket's hop options with a new set

    :param sk:
        the socket
    :type sk: struct sock \*

    :param hop:
        new hop options
    :type hop: struct ipv6_opt_hdr \*

.. _`calipso_opt_update.description`:

Description
-----------

Replaces \ ``sk``\ 's hop options with \ ``hop``\ .  \ ``hop``\  may be NULL to leave
the socket with no hop options.

.. _`calipso_tlv_len`:

calipso_tlv_len
===============

.. c:function:: int calipso_tlv_len(struct ipv6_opt_hdr *opt, unsigned int offset)

    Returns the length of the TLV

    :param opt:
        the option header
    :type opt: struct ipv6_opt_hdr \*

    :param offset:
        offset of the TLV within the header
    :type offset: unsigned int

.. _`calipso_tlv_len.description`:

Description
-----------

Returns the length of the TLV option at offset \ ``offset``\  within
the option header \ ``opt``\ .  Checks that the entire TLV fits inside
the option header, returns a negative value if this is not the case.

.. _`calipso_opt_find`:

calipso_opt_find
================

.. c:function:: int calipso_opt_find(struct ipv6_opt_hdr *hop, unsigned int *start, unsigned int *end)

    Finds the CALIPSO option in an IPv6 hop options header

    :param hop:
        the hop options header
    :type hop: struct ipv6_opt_hdr \*

    :param start:
        on return holds the offset of any leading padding
    :type start: unsigned int \*

    :param end:
        on return holds the offset of the first non-pad TLV after CALIPSO
    :type end: unsigned int \*

.. _`calipso_opt_find.description`:

Description
-----------

Finds the space occupied by a CALIPSO option (including any leading and
trailing padding).

If a CALIPSO option exists set \ ``start``\  and \ ``end``\  to the
offsets within \ ``hop``\  of the start of padding before the first
CALIPSO option and the end of padding after the first CALIPSO
option.  In this case the function returns 0.

In the absence of a CALIPSO option, \ ``start``\  and \ ``end``\  will be
set to the start and end of any trailing padding in the header.
This is useful when appending a new option, as the caller may want
to overwrite some of this padding.  In this case the function will
return -ENOENT.

.. _`calipso_opt_insert`:

calipso_opt_insert
==================

.. c:function:: struct ipv6_opt_hdr *calipso_opt_insert(struct ipv6_opt_hdr *hop, const struct calipso_doi *doi_def, const struct netlbl_lsm_secattr *secattr)

    Inserts a CALIPSO option into an IPv6 hop opt hdr

    :param hop:
        the original hop options header
    :type hop: struct ipv6_opt_hdr \*

    :param doi_def:
        the CALIPSO DOI to use
    :type doi_def: const struct calipso_doi \*

    :param secattr:
        the specific security attributes of the socket
    :type secattr: const struct netlbl_lsm_secattr \*

.. _`calipso_opt_insert.description`:

Description
-----------

Creates a new hop options header based on \ ``hop``\  with a
CALIPSO option added to it.  If \ ``hop``\  already contains a CALIPSO
option this is overwritten, otherwise the new option is appended
after any existing options.  If \ ``hop``\  is NULL then the new header
will contain just the CALIPSO option and any needed padding.

.. _`calipso_opt_del`:

calipso_opt_del
===============

.. c:function:: int calipso_opt_del(struct ipv6_opt_hdr *hop, struct ipv6_opt_hdr **new)

    Removes the CALIPSO option from an option header

    :param hop:
        the original header
    :type hop: struct ipv6_opt_hdr \*

    :param new:
        the new header
    :type new: struct ipv6_opt_hdr \*\*

.. _`calipso_opt_del.description`:

Description
-----------

Creates a new header based on \ ``hop``\  without any CALIPSO option.  If \ ``hop``\ 
doesn't contain a CALIPSO option it returns -ENOENT.  If \ ``hop``\  contains
no other non-padding options, it returns zero with \ ``new``\  set to NULL.
Otherwise it returns zero, creates a new header without the CALIPSO
option (and removing as much padding as possible) and returns with
\ ``new``\  set to that header.

.. _`calipso_opt_getattr`:

calipso_opt_getattr
===================

.. c:function:: int calipso_opt_getattr(const unsigned char *calipso, struct netlbl_lsm_secattr *secattr)

    Get the security attributes from a memory block

    :param calipso:
        the CALIPSO option
    :type calipso: const unsigned char \*

    :param secattr:
        the security attributes
    :type secattr: struct netlbl_lsm_secattr \*

.. _`calipso_opt_getattr.description`:

Description
-----------

Inspect \ ``calipso``\  and return the security attributes in \ ``secattr``\ .
Returns zero on success and negative values on failure.

.. _`calipso_sock_getattr`:

calipso_sock_getattr
====================

.. c:function:: int calipso_sock_getattr(struct sock *sk, struct netlbl_lsm_secattr *secattr)

    Get the security attributes from a sock

    :param sk:
        the sock
    :type sk: struct sock \*

    :param secattr:
        the security attributes
    :type secattr: struct netlbl_lsm_secattr \*

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

    :param sk:
        the socket
    :type sk: struct sock \*

    :param doi_def:
        the CALIPSO DOI to use
    :type doi_def: const struct calipso_doi \*

    :param secattr:
        the specific security attributes of the socket
    :type secattr: const struct netlbl_lsm_secattr \*

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

    :param sk:
        the socket
    :type sk: struct sock \*

.. _`calipso_sock_delattr.description`:

Description
-----------

Removes the CALIPSO option from a socket, if present.

.. _`calipso_req_setattr`:

calipso_req_setattr
===================

.. c:function:: int calipso_req_setattr(struct request_sock *req, const struct calipso_doi *doi_def, const struct netlbl_lsm_secattr *secattr)

    Add a CALIPSO option to a connection request socket

    :param req:
        the connection request socket
    :type req: struct request_sock \*

    :param doi_def:
        the CALIPSO DOI to use
    :type doi_def: const struct calipso_doi \*

    :param secattr:
        the specific security attributes of the socket
    :type secattr: const struct netlbl_lsm_secattr \*

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

    :param req:
        *undescribed*
    :type req: struct request_sock \*

.. _`calipso_req_delattr.description`:

Description
-----------

Removes the CALIPSO option from a request socket, if present.

.. _`calipso_skbuff_optptr`:

calipso_skbuff_optptr
=====================

.. c:function:: unsigned char *calipso_skbuff_optptr(const struct sk_buff *skb)

    Find the CALIPSO option in the packet

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

.. _`calipso_skbuff_optptr.description`:

Description
-----------

Parse the packet's IP header looking for a CALIPSO option.  Returns a pointer
to the start of the CALIPSO option on success, NULL if one if not found.

.. _`calipso_skbuff_setattr`:

calipso_skbuff_setattr
======================

.. c:function:: int calipso_skbuff_setattr(struct sk_buff *skb, const struct calipso_doi *doi_def, const struct netlbl_lsm_secattr *secattr)

    Set the CALIPSO option on a packet

    :param skb:
        the packet
    :type skb: struct sk_buff \*

    :param doi_def:
        the CALIPSO DOI to use
    :type doi_def: const struct calipso_doi \*

    :param secattr:
        the security attributes
    :type secattr: const struct netlbl_lsm_secattr \*

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

    :param skb:
        the packet
    :type skb: struct sk_buff \*

.. _`calipso_skbuff_delattr.description`:

Description
-----------

Removes any and all CALIPSO options from the given packet.  Returns zero on
success, negative values on failure.

.. _`calipso_init`:

calipso_init
============

.. c:function:: int calipso_init( void)

    Initialize the CALIPSO module

    :param void:
        no arguments
    :type void: 

.. _`calipso_init.description`:

Description
-----------

Initialize the CALIPSO module and prepare it for use.  Returns zero on
success and negative values on failure.

.. This file was automatic generated / don't edit.

