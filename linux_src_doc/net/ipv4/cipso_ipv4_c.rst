.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv4/cipso_ipv4.c

.. _`cipso_v4_cache_entry_free`:

cipso_v4_cache_entry_free
=========================

.. c:function:: void cipso_v4_cache_entry_free(struct cipso_v4_map_cache_entry *entry)

    Frees a cache entry

    :param struct cipso_v4_map_cache_entry \*entry:
        the entry to free

.. _`cipso_v4_cache_entry_free.description`:

Description
-----------

This function frees the memory associated with a cache entry including the
LSM cache data if there are no longer any users, i.e. reference count == 0.

.. _`cipso_v4_map_cache_hash`:

cipso_v4_map_cache_hash
=======================

.. c:function:: u32 cipso_v4_map_cache_hash(const unsigned char *key, u32 key_len)

    Hashing function for the CIPSO cache

    :param const unsigned char \*key:
        the hash key

    :param u32 key_len:
        the length of the key in bytes

.. _`cipso_v4_map_cache_hash.description`:

Description
-----------

The CIPSO tag hashing function.  Returns a 32-bit hash value.

.. _`cipso_v4_cache_init`:

cipso_v4_cache_init
===================

.. c:function:: int cipso_v4_cache_init( void)

    Initialize the CIPSO cache

    :param  void:
        no arguments

.. _`cipso_v4_cache_init.description`:

Description
-----------

Initializes the CIPSO label mapping cache, this function should be called
before any of the other functions defined in this file.  Returns zero on
success, negative values on error.

.. _`cipso_v4_cache_invalidate`:

cipso_v4_cache_invalidate
=========================

.. c:function:: void cipso_v4_cache_invalidate( void)

    Invalidates the current CIPSO cache

    :param  void:
        no arguments

.. _`cipso_v4_cache_invalidate.description`:

Description
-----------

Invalidates and frees any entries in the CIPSO cache.  Returns zero on
success and negative values on failure.

.. _`cipso_v4_cache_check`:

cipso_v4_cache_check
====================

.. c:function:: int cipso_v4_cache_check(const unsigned char *key, u32 key_len, struct netlbl_lsm_secattr *secattr)

    Check the CIPSO cache for a label mapping

    :param const unsigned char \*key:
        the buffer to check

    :param u32 key_len:
        buffer length in bytes

    :param struct netlbl_lsm_secattr \*secattr:
        the security attribute struct to use

.. _`cipso_v4_cache_check.description`:

Description
-----------

This function checks the cache to see if a label mapping already exists for
the given key.  If there is a match then the cache is adjusted and the
\ ``secattr``\  struct is populated with the correct LSM security attributes.  The
cache is adjusted in the following manner if the entry is not already the

.. _`cipso_v4_cache_check.first-in-the-cache-bucket`:

first in the cache bucket
-------------------------


1. The cache entry's activity counter is incremented
2. The previous (higher ranking) entry's activity counter is decremented
3. If the difference between the two activity counters is geater than
CIPSO_V4_CACHE_REORDERLIMIT the two entries are swapped

Returns zero on success, -ENOENT for a cache miss, and other negative values
on error.

.. _`cipso_v4_cache_add`:

cipso_v4_cache_add
==================

.. c:function:: int cipso_v4_cache_add(const unsigned char *cipso_ptr, const struct netlbl_lsm_secattr *secattr)

    Add an entry to the CIPSO cache

    :param const unsigned char \*cipso_ptr:
        *undescribed*

    :param const struct netlbl_lsm_secattr \*secattr:
        the packet's security attributes

.. _`cipso_v4_cache_add.description`:

Description
-----------

Add a new entry into the CIPSO label mapping cache.  Add the new entry to
head of the cache bucket's list, if the cache bucket is out of room remove
the last entry in the list first.  It is important to note that there is
currently no checking for duplicate keys.  Returns zero on success,
negative values on failure.

.. _`cipso_v4_doi_search`:

cipso_v4_doi_search
===================

.. c:function:: struct cipso_v4_doi *cipso_v4_doi_search(u32 doi)

    Searches for a DOI definition

    :param u32 doi:
        the DOI to search for

.. _`cipso_v4_doi_search.description`:

Description
-----------

Search the DOI definition list for a DOI definition with a DOI value that
matches \ ``doi``\ .  The caller is responsible for calling rcu_read_[un]lock().
Returns a pointer to the DOI definition on success and NULL on failure.

.. _`cipso_v4_doi_add`:

cipso_v4_doi_add
================

.. c:function:: int cipso_v4_doi_add(struct cipso_v4_doi *doi_def, struct netlbl_audit *audit_info)

    Add a new DOI to the CIPSO protocol engine

    :param struct cipso_v4_doi \*doi_def:
        the DOI structure

    :param struct netlbl_audit \*audit_info:
        NetLabel audit information

.. _`cipso_v4_doi_add.description`:

Description
-----------

The caller defines a new DOI for use by the CIPSO engine and calls this
function to add it to the list of acceptable domains.  The caller must
ensure that the mapping table specified in \ ``doi_def``\ ->map meets all of the
requirements of the mapping type (see cipso_ipv4.h for details).  Returns
zero on success and non-zero on failure.

.. _`cipso_v4_doi_free`:

cipso_v4_doi_free
=================

.. c:function:: void cipso_v4_doi_free(struct cipso_v4_doi *doi_def)

    Frees a DOI definition

    :param struct cipso_v4_doi \*doi_def:
        the DOI definition

.. _`cipso_v4_doi_free.description`:

Description
-----------

This function frees all of the memory associated with a DOI definition.

.. _`cipso_v4_doi_free_rcu`:

cipso_v4_doi_free_rcu
=====================

.. c:function:: void cipso_v4_doi_free_rcu(struct rcu_head *entry)

    Frees a DOI definition via the RCU pointer

    :param struct rcu_head \*entry:
        the entry's RCU field

.. _`cipso_v4_doi_free_rcu.description`:

Description
-----------

This function is designed to be used as a callback to the \ :c:func:`call_rcu`\ 
function so that the memory allocated to the DOI definition can be released
safely.

.. _`cipso_v4_doi_remove`:

cipso_v4_doi_remove
===================

.. c:function:: int cipso_v4_doi_remove(u32 doi, struct netlbl_audit *audit_info)

    Remove an existing DOI from the CIPSO protocol engine

    :param u32 doi:
        the DOI value

    :param struct netlbl_audit \*audit_info:
        *undescribed*

.. _`cipso_v4_doi_remove.description`:

Description
-----------

Removes a DOI definition from the CIPSO engine.  The NetLabel routines will
be called to release their own LSM domain mappings as well as our own
domain list.  Returns zero on success and negative values on failure.

.. _`cipso_v4_doi_getdef`:

cipso_v4_doi_getdef
===================

.. c:function:: struct cipso_v4_doi *cipso_v4_doi_getdef(u32 doi)

    Returns a reference to a valid DOI definition

    :param u32 doi:
        the DOI value

.. _`cipso_v4_doi_getdef.description`:

Description
-----------

Searches for a valid DOI definition and if one is found it is returned to
the caller.  Otherwise NULL is returned.  The caller must ensure that
\ :c:func:`rcu_read_lock`\  is held while accessing the returned definition and the DOI
definition reference count is decremented when the caller is done.

.. _`cipso_v4_doi_putdef`:

cipso_v4_doi_putdef
===================

.. c:function:: void cipso_v4_doi_putdef(struct cipso_v4_doi *doi_def)

    Releases a reference for the given DOI definition

    :param struct cipso_v4_doi \*doi_def:
        the DOI definition

.. _`cipso_v4_doi_putdef.description`:

Description
-----------

Releases a DOI definition reference obtained from \ :c:func:`cipso_v4_doi_getdef`\ .

.. _`cipso_v4_doi_walk`:

cipso_v4_doi_walk
=================

.. c:function:: int cipso_v4_doi_walk(u32 *skip_cnt, int (*callback)(struct cipso_v4_doi *doi_def, void *arg), void *cb_arg)

    Iterate through the DOI definitions

    :param u32 \*skip_cnt:
        skip past this number of DOI definitions, updated

    :param int (\*callback)(struct cipso_v4_doi \*doi_def, void \*arg):
        callback for each DOI definition

    :param void \*cb_arg:
        argument for the callback function

.. _`cipso_v4_doi_walk.description`:

Description
-----------

Iterate over the DOI definition list, skipping the first \ ``skip_cnt``\  entries.
For each entry call \ ``callback``\ , if \ ``callback``\  returns a negative value stop
'walking' through the list and return.  Updates the value in \ ``skip_cnt``\  upon
return.  Returns zero on success, negative values on failure.

.. _`cipso_v4_map_lvl_valid`:

cipso_v4_map_lvl_valid
======================

.. c:function:: int cipso_v4_map_lvl_valid(const struct cipso_v4_doi *doi_def, u8 level)

    Checks to see if the given level is understood

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param u8 level:
        the level to check

.. _`cipso_v4_map_lvl_valid.description`:

Description
-----------

Checks the given level against the given DOI definition and returns a
negative value if the level does not have a valid mapping and a zero value
if the level is defined by the DOI.

.. _`cipso_v4_map_lvl_hton`:

cipso_v4_map_lvl_hton
=====================

.. c:function:: int cipso_v4_map_lvl_hton(const struct cipso_v4_doi *doi_def, u32 host_lvl, u32 *net_lvl)

    Perform a level mapping from the host to the network

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param u32 host_lvl:
        the host MLS level

    :param u32 \*net_lvl:
        the network/CIPSO MLS level

.. _`cipso_v4_map_lvl_hton.description`:

Description
-----------

Perform a label mapping to translate a local MLS level to the correct
CIPSO level using the given DOI definition.  Returns zero on success,
negative values otherwise.

.. _`cipso_v4_map_lvl_ntoh`:

cipso_v4_map_lvl_ntoh
=====================

.. c:function:: int cipso_v4_map_lvl_ntoh(const struct cipso_v4_doi *doi_def, u32 net_lvl, u32 *host_lvl)

    Perform a level mapping from the network to the host

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param u32 net_lvl:
        the network/CIPSO MLS level

    :param u32 \*host_lvl:
        the host MLS level

.. _`cipso_v4_map_lvl_ntoh.description`:

Description
-----------

Perform a label mapping to translate a CIPSO level to the correct local MLS
level using the given DOI definition.  Returns zero on success, negative
values otherwise.

.. _`cipso_v4_map_cat_rbm_valid`:

cipso_v4_map_cat_rbm_valid
==========================

.. c:function:: int cipso_v4_map_cat_rbm_valid(const struct cipso_v4_doi *doi_def, const unsigned char *bitmap, u32 bitmap_len)

    Checks to see if the category bitmap is valid

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param const unsigned char \*bitmap:
        category bitmap

    :param u32 bitmap_len:
        bitmap length in bytes

.. _`cipso_v4_map_cat_rbm_valid.description`:

Description
-----------

Checks the given category bitmap against the given DOI definition and
returns a negative value if any of the categories in the bitmap do not have
a valid mapping and a zero value if all of the categories are valid.

.. _`cipso_v4_map_cat_rbm_hton`:

cipso_v4_map_cat_rbm_hton
=========================

.. c:function:: int cipso_v4_map_cat_rbm_hton(const struct cipso_v4_doi *doi_def, const struct netlbl_lsm_secattr *secattr, unsigned char *net_cat, u32 net_cat_len)

    Perform a category mapping from host to network

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param const struct netlbl_lsm_secattr \*secattr:
        the security attributes

    :param unsigned char \*net_cat:
        the zero'd out category bitmap in network/CIPSO format

    :param u32 net_cat_len:
        the length of the CIPSO bitmap in bytes

.. _`cipso_v4_map_cat_rbm_hton.description`:

Description
-----------

Perform a label mapping to translate a local MLS category bitmap to the
correct CIPSO bitmap using the given DOI definition.  Returns the minimum
size in bytes of the network bitmap on success, negative values otherwise.

.. _`cipso_v4_map_cat_rbm_ntoh`:

cipso_v4_map_cat_rbm_ntoh
=========================

.. c:function:: int cipso_v4_map_cat_rbm_ntoh(const struct cipso_v4_doi *doi_def, const unsigned char *net_cat, u32 net_cat_len, struct netlbl_lsm_secattr *secattr)

    Perform a category mapping from network to host

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param const unsigned char \*net_cat:
        the category bitmap in network/CIPSO format

    :param u32 net_cat_len:
        the length of the CIPSO bitmap in bytes

    :param struct netlbl_lsm_secattr \*secattr:
        the security attributes

.. _`cipso_v4_map_cat_rbm_ntoh.description`:

Description
-----------

Perform a label mapping to translate a CIPSO bitmap to the correct local
MLS category bitmap using the given DOI definition.  Returns zero on
success, negative values on failure.

.. _`cipso_v4_map_cat_enum_valid`:

cipso_v4_map_cat_enum_valid
===========================

.. c:function:: int cipso_v4_map_cat_enum_valid(const struct cipso_v4_doi *doi_def, const unsigned char *enumcat, u32 enumcat_len)

    Checks to see if the categories are valid

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param const unsigned char \*enumcat:
        category list

    :param u32 enumcat_len:
        length of the category list in bytes

.. _`cipso_v4_map_cat_enum_valid.description`:

Description
-----------

Checks the given categories against the given DOI definition and returns a
negative value if any of the categories do not have a valid mapping and a
zero value if all of the categories are valid.

.. _`cipso_v4_map_cat_enum_hton`:

cipso_v4_map_cat_enum_hton
==========================

.. c:function:: int cipso_v4_map_cat_enum_hton(const struct cipso_v4_doi *doi_def, const struct netlbl_lsm_secattr *secattr, unsigned char *net_cat, u32 net_cat_len)

    Perform a category mapping from host to network

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param const struct netlbl_lsm_secattr \*secattr:
        the security attributes

    :param unsigned char \*net_cat:
        the zero'd out category list in network/CIPSO format

    :param u32 net_cat_len:
        the length of the CIPSO category list in bytes

.. _`cipso_v4_map_cat_enum_hton.description`:

Description
-----------

Perform a label mapping to translate a local MLS category bitmap to the
correct CIPSO category list using the given DOI definition.   Returns the
size in bytes of the network category bitmap on success, negative values
otherwise.

.. _`cipso_v4_map_cat_enum_ntoh`:

cipso_v4_map_cat_enum_ntoh
==========================

.. c:function:: int cipso_v4_map_cat_enum_ntoh(const struct cipso_v4_doi *doi_def, const unsigned char *net_cat, u32 net_cat_len, struct netlbl_lsm_secattr *secattr)

    Perform a category mapping from network to host

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param const unsigned char \*net_cat:
        the category list in network/CIPSO format

    :param u32 net_cat_len:
        the length of the CIPSO bitmap in bytes

    :param struct netlbl_lsm_secattr \*secattr:
        the security attributes

.. _`cipso_v4_map_cat_enum_ntoh.description`:

Description
-----------

Perform a label mapping to translate a CIPSO category list to the correct
local MLS category bitmap using the given DOI definition.  Returns zero on
success, negative values on failure.

.. _`cipso_v4_map_cat_rng_valid`:

cipso_v4_map_cat_rng_valid
==========================

.. c:function:: int cipso_v4_map_cat_rng_valid(const struct cipso_v4_doi *doi_def, const unsigned char *rngcat, u32 rngcat_len)

    Checks to see if the categories are valid

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param const unsigned char \*rngcat:
        category list

    :param u32 rngcat_len:
        length of the category list in bytes

.. _`cipso_v4_map_cat_rng_valid.description`:

Description
-----------

Checks the given categories against the given DOI definition and returns a
negative value if any of the categories do not have a valid mapping and a
zero value if all of the categories are valid.

.. _`cipso_v4_map_cat_rng_hton`:

cipso_v4_map_cat_rng_hton
=========================

.. c:function:: int cipso_v4_map_cat_rng_hton(const struct cipso_v4_doi *doi_def, const struct netlbl_lsm_secattr *secattr, unsigned char *net_cat, u32 net_cat_len)

    Perform a category mapping from host to network

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param const struct netlbl_lsm_secattr \*secattr:
        the security attributes

    :param unsigned char \*net_cat:
        the zero'd out category list in network/CIPSO format

    :param u32 net_cat_len:
        the length of the CIPSO category list in bytes

.. _`cipso_v4_map_cat_rng_hton.description`:

Description
-----------

Perform a label mapping to translate a local MLS category bitmap to the
correct CIPSO category list using the given DOI definition.   Returns the
size in bytes of the network category bitmap on success, negative values
otherwise.

.. _`cipso_v4_map_cat_rng_ntoh`:

cipso_v4_map_cat_rng_ntoh
=========================

.. c:function:: int cipso_v4_map_cat_rng_ntoh(const struct cipso_v4_doi *doi_def, const unsigned char *net_cat, u32 net_cat_len, struct netlbl_lsm_secattr *secattr)

    Perform a category mapping from network to host

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param const unsigned char \*net_cat:
        the category list in network/CIPSO format

    :param u32 net_cat_len:
        the length of the CIPSO bitmap in bytes

    :param struct netlbl_lsm_secattr \*secattr:
        the security attributes

.. _`cipso_v4_map_cat_rng_ntoh.description`:

Description
-----------

Perform a label mapping to translate a CIPSO category list to the correct
local MLS category bitmap using the given DOI definition.  Returns zero on
success, negative values on failure.

.. _`cipso_v4_gentag_hdr`:

cipso_v4_gentag_hdr
===================

.. c:function:: void cipso_v4_gentag_hdr(const struct cipso_v4_doi *doi_def, unsigned char *buf, u32 len)

    Generate a CIPSO option header

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param unsigned char \*buf:
        the CIPSO option buffer

    :param u32 len:
        the total tag length in bytes, not including this header

.. _`cipso_v4_gentag_hdr.description`:

Description
-----------

Write a CIPSO header into the beginning of \ ``buffer``\ .

.. _`cipso_v4_gentag_rbm`:

cipso_v4_gentag_rbm
===================

.. c:function:: int cipso_v4_gentag_rbm(const struct cipso_v4_doi *doi_def, const struct netlbl_lsm_secattr *secattr, unsigned char *buffer, u32 buffer_len)

    Generate a CIPSO restricted bitmap tag (type #1)

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param const struct netlbl_lsm_secattr \*secattr:
        the security attributes

    :param unsigned char \*buffer:
        the option buffer

    :param u32 buffer_len:
        length of buffer in bytes

.. _`cipso_v4_gentag_rbm.description`:

Description
-----------

Generate a CIPSO option using the restricted bitmap tag, tag type #1.  The
actual buffer length may be larger than the indicated size due to
translation between host and network category bitmaps.  Returns the size of
the tag on success, negative values on failure.

.. _`cipso_v4_parsetag_rbm`:

cipso_v4_parsetag_rbm
=====================

.. c:function:: int cipso_v4_parsetag_rbm(const struct cipso_v4_doi *doi_def, const unsigned char *tag, struct netlbl_lsm_secattr *secattr)

    Parse a CIPSO restricted bitmap tag

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param const unsigned char \*tag:
        the CIPSO tag

    :param struct netlbl_lsm_secattr \*secattr:
        the security attributes

.. _`cipso_v4_parsetag_rbm.description`:

Description
-----------

Parse a CIPSO restricted bitmap tag (tag type #1) and return the security
attributes in \ ``secattr``\ .  Return zero on success, negatives values on
failure.

.. _`cipso_v4_gentag_enum`:

cipso_v4_gentag_enum
====================

.. c:function:: int cipso_v4_gentag_enum(const struct cipso_v4_doi *doi_def, const struct netlbl_lsm_secattr *secattr, unsigned char *buffer, u32 buffer_len)

    Generate a CIPSO enumerated tag (type #2)

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param const struct netlbl_lsm_secattr \*secattr:
        the security attributes

    :param unsigned char \*buffer:
        the option buffer

    :param u32 buffer_len:
        length of buffer in bytes

.. _`cipso_v4_gentag_enum.description`:

Description
-----------

Generate a CIPSO option using the enumerated tag, tag type #2.  Returns the
size of the tag on success, negative values on failure.

.. _`cipso_v4_parsetag_enum`:

cipso_v4_parsetag_enum
======================

.. c:function:: int cipso_v4_parsetag_enum(const struct cipso_v4_doi *doi_def, const unsigned char *tag, struct netlbl_lsm_secattr *secattr)

    Parse a CIPSO enumerated tag

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param const unsigned char \*tag:
        the CIPSO tag

    :param struct netlbl_lsm_secattr \*secattr:
        the security attributes

.. _`cipso_v4_parsetag_enum.description`:

Description
-----------

Parse a CIPSO enumerated tag (tag type #2) and return the security
attributes in \ ``secattr``\ .  Return zero on success, negatives values on
failure.

.. _`cipso_v4_gentag_rng`:

cipso_v4_gentag_rng
===================

.. c:function:: int cipso_v4_gentag_rng(const struct cipso_v4_doi *doi_def, const struct netlbl_lsm_secattr *secattr, unsigned char *buffer, u32 buffer_len)

    Generate a CIPSO ranged tag (type #5)

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param const struct netlbl_lsm_secattr \*secattr:
        the security attributes

    :param unsigned char \*buffer:
        the option buffer

    :param u32 buffer_len:
        length of buffer in bytes

.. _`cipso_v4_gentag_rng.description`:

Description
-----------

Generate a CIPSO option using the ranged tag, tag type #5.  Returns the
size of the tag on success, negative values on failure.

.. _`cipso_v4_parsetag_rng`:

cipso_v4_parsetag_rng
=====================

.. c:function:: int cipso_v4_parsetag_rng(const struct cipso_v4_doi *doi_def, const unsigned char *tag, struct netlbl_lsm_secattr *secattr)

    Parse a CIPSO ranged tag

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param const unsigned char \*tag:
        the CIPSO tag

    :param struct netlbl_lsm_secattr \*secattr:
        the security attributes

.. _`cipso_v4_parsetag_rng.description`:

Description
-----------

Parse a CIPSO ranged tag (tag type #5) and return the security attributes
in \ ``secattr``\ .  Return zero on success, negatives values on failure.

.. _`cipso_v4_gentag_loc`:

cipso_v4_gentag_loc
===================

.. c:function:: int cipso_v4_gentag_loc(const struct cipso_v4_doi *doi_def, const struct netlbl_lsm_secattr *secattr, unsigned char *buffer, u32 buffer_len)

    Generate a CIPSO local tag (non-standard)

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param const struct netlbl_lsm_secattr \*secattr:
        the security attributes

    :param unsigned char \*buffer:
        the option buffer

    :param u32 buffer_len:
        length of buffer in bytes

.. _`cipso_v4_gentag_loc.description`:

Description
-----------

Generate a CIPSO option using the local tag.  Returns the size of the tag
on success, negative values on failure.

.. _`cipso_v4_parsetag_loc`:

cipso_v4_parsetag_loc
=====================

.. c:function:: int cipso_v4_parsetag_loc(const struct cipso_v4_doi *doi_def, const unsigned char *tag, struct netlbl_lsm_secattr *secattr)

    Parse a CIPSO local tag

    :param const struct cipso_v4_doi \*doi_def:
        the DOI definition

    :param const unsigned char \*tag:
        the CIPSO tag

    :param struct netlbl_lsm_secattr \*secattr:
        the security attributes

.. _`cipso_v4_parsetag_loc.description`:

Description
-----------

Parse a CIPSO local tag and return the security attributes in \ ``secattr``\ .
Return zero on success, negatives values on failure.

.. _`cipso_v4_optptr`:

cipso_v4_optptr
===============

.. c:function:: unsigned char *cipso_v4_optptr(const struct sk_buff *skb)

    Find the CIPSO option in the packet

    :param const struct sk_buff \*skb:
        the packet

.. _`cipso_v4_optptr.description`:

Description
-----------

Parse the packet's IP header looking for a CIPSO option.  Returns a pointer
to the start of the CIPSO option on success, NULL if one if not found.

.. _`cipso_v4_validate`:

cipso_v4_validate
=================

.. c:function:: int cipso_v4_validate(const struct sk_buff *skb, unsigned char **option)

    Validate a CIPSO option

    :param const struct sk_buff \*skb:
        *undescribed*

    :param unsigned char \*\*option:
        the start of the option, on error it is set to point to the error

.. _`cipso_v4_validate.description`:

Description
-----------

This routine is called to validate a CIPSO option, it checks all of the
fields to ensure that they are at least valid, see the draft snippet below
for details.  If the option is valid then a zero value is returned and
the value of \ ``option``\  is unchanged.  If the option is invalid then a
non-zero value is returned and \ ``option``\  is adjusted to point to the
offending portion of the option.  From the IETF draft ...

"If any field within the CIPSO options, such as the DOI identifier, is not
recognized the IP datagram is discarded and an ICMP 'parameter problem'
(type 12) is generated and returned.  The ICMP code field is set to 'bad
parameter' (code 0) and the pointer is set to the start of the CIPSO field
that is unrecognized."

.. _`cipso_v4_error`:

cipso_v4_error
==============

.. c:function:: void cipso_v4_error(struct sk_buff *skb, int error, u32 gateway)

    Send the correct response for a bad packet

    :param struct sk_buff \*skb:
        the packet

    :param int error:
        the error code

    :param u32 gateway:
        CIPSO gateway flag

.. _`cipso_v4_error.description`:

Description
-----------

Based on the error code given in \ ``error``\ , send an ICMP error message back to
the originating host.  From the IETF draft ...

"If the contents of the CIPSO [option] are valid but the security label is
outside of the configured host or port label range, the datagram is
discarded and an ICMP 'destination unreachable' (type 3) is generated and
returned.  The code field of the ICMP is set to 'communication with
destination network administratively prohibited' (code 9) or to
'communication with destination host administratively prohibited'
(code 10).  The value of the code is dependent on whether the originator
of the ICMP message is acting as a CIPSO host or a CIPSO gateway.  The
recipient of the ICMP message MUST be able to handle either value.  The
same procedure is performed if a CIPSO [option] can not be added to an
IP packet because it is too large to fit in the IP options area."

"If the error is triggered by receipt of an ICMP message, the message is
discarded and no response is permitted (consistent with general ICMP
processing rules)."

.. _`cipso_v4_genopt`:

cipso_v4_genopt
===============

.. c:function:: int cipso_v4_genopt(unsigned char *buf, u32 buf_len, const struct cipso_v4_doi *doi_def, const struct netlbl_lsm_secattr *secattr)

    Generate a CIPSO option

    :param unsigned char \*buf:
        the option buffer

    :param u32 buf_len:
        the size of opt_buf

    :param const struct cipso_v4_doi \*doi_def:
        the CIPSO DOI to use

    :param const struct netlbl_lsm_secattr \*secattr:
        the security attributes

.. _`cipso_v4_genopt.description`:

Description
-----------

Generate a CIPSO option using the DOI definition and security attributes
passed to the function.  Returns the length of the option on success and
negative values on failure.

.. _`cipso_v4_sock_setattr`:

cipso_v4_sock_setattr
=====================

.. c:function:: int cipso_v4_sock_setattr(struct sock *sk, const struct cipso_v4_doi *doi_def, const struct netlbl_lsm_secattr *secattr)

    Add a CIPSO option to a socket

    :param struct sock \*sk:
        the socket

    :param const struct cipso_v4_doi \*doi_def:
        the CIPSO DOI to use

    :param const struct netlbl_lsm_secattr \*secattr:
        the specific security attributes of the socket

.. _`cipso_v4_sock_setattr.description`:

Description
-----------

Set the CIPSO option on the given socket using the DOI definition and
security attributes passed to the function.  This function requires
exclusive access to \ ``sk``\ , which means it either needs to be in the
process of being created or locked.  Returns zero on success and negative
values on failure.

.. _`cipso_v4_req_setattr`:

cipso_v4_req_setattr
====================

.. c:function:: int cipso_v4_req_setattr(struct request_sock *req, const struct cipso_v4_doi *doi_def, const struct netlbl_lsm_secattr *secattr)

    Add a CIPSO option to a connection request socket

    :param struct request_sock \*req:
        the connection request socket

    :param const struct cipso_v4_doi \*doi_def:
        the CIPSO DOI to use

    :param const struct netlbl_lsm_secattr \*secattr:
        the specific security attributes of the socket

.. _`cipso_v4_req_setattr.description`:

Description
-----------

Set the CIPSO option on the given socket using the DOI definition and
security attributes passed to the function.  Returns zero on success and
negative values on failure.

.. _`cipso_v4_delopt`:

cipso_v4_delopt
===============

.. c:function:: int cipso_v4_delopt(struct ip_options_rcu **opt_ptr)

    Delete the CIPSO option from a set of IP options

    :param struct ip_options_rcu \*\*opt_ptr:
        IP option pointer

.. _`cipso_v4_delopt.description`:

Description
-----------

Deletes the CIPSO IP option from a set of IP options and makes the necessary
adjustments to the IP option structure.  Returns zero on success, negative
values on failure.

.. _`cipso_v4_sock_delattr`:

cipso_v4_sock_delattr
=====================

.. c:function:: void cipso_v4_sock_delattr(struct sock *sk)

    Delete the CIPSO option from a socket

    :param struct sock \*sk:
        the socket

.. _`cipso_v4_sock_delattr.description`:

Description
-----------

Removes the CIPSO option from a socket, if present.

.. _`cipso_v4_req_delattr`:

cipso_v4_req_delattr
====================

.. c:function:: void cipso_v4_req_delattr(struct request_sock *req)

    Delete the CIPSO option from a request socket

    :param struct request_sock \*req:
        *undescribed*

.. _`cipso_v4_req_delattr.description`:

Description
-----------

Removes the CIPSO option from a request socket, if present.

.. _`cipso_v4_getattr`:

cipso_v4_getattr
================

.. c:function:: int cipso_v4_getattr(const unsigned char *cipso, struct netlbl_lsm_secattr *secattr)

    Helper function for the cipso_v4\_\*\_getattr functions

    :param const unsigned char \*cipso:
        the CIPSO v4 option

    :param struct netlbl_lsm_secattr \*secattr:
        the security attributes

.. _`cipso_v4_getattr.description`:

Description
-----------

Inspect \ ``cipso``\  and return the security attributes in \ ``secattr``\ .  Returns zero
on success and negative values on failure.

.. _`cipso_v4_sock_getattr`:

cipso_v4_sock_getattr
=====================

.. c:function:: int cipso_v4_sock_getattr(struct sock *sk, struct netlbl_lsm_secattr *secattr)

    Get the security attributes from a sock

    :param struct sock \*sk:
        the sock

    :param struct netlbl_lsm_secattr \*secattr:
        the security attributes

.. _`cipso_v4_sock_getattr.description`:

Description
-----------

Query \ ``sk``\  to see if there is a CIPSO option attached to the sock and if
there is return the CIPSO security attributes in \ ``secattr``\ .  This function
requires that \ ``sk``\  be locked, or privately held, but it does not do any
locking itself.  Returns zero on success and negative values on failure.

.. _`cipso_v4_skbuff_setattr`:

cipso_v4_skbuff_setattr
=======================

.. c:function:: int cipso_v4_skbuff_setattr(struct sk_buff *skb, const struct cipso_v4_doi *doi_def, const struct netlbl_lsm_secattr *secattr)

    Set the CIPSO option on a packet

    :param struct sk_buff \*skb:
        the packet

    :param const struct cipso_v4_doi \*doi_def:
        *undescribed*

    :param const struct netlbl_lsm_secattr \*secattr:
        the security attributes

.. _`cipso_v4_skbuff_setattr.description`:

Description
-----------

Set the CIPSO option on the given packet based on the security attributes.
Returns a pointer to the IP header on success and NULL on failure.

.. _`cipso_v4_skbuff_delattr`:

cipso_v4_skbuff_delattr
=======================

.. c:function:: int cipso_v4_skbuff_delattr(struct sk_buff *skb)

    Delete any CIPSO options from a packet

    :param struct sk_buff \*skb:
        the packet

.. _`cipso_v4_skbuff_delattr.description`:

Description
-----------

Removes any and all CIPSO options from the given packet.  Returns zero on
success, negative values on failure.

.. _`cipso_v4_init`:

cipso_v4_init
=============

.. c:function:: int cipso_v4_init( void)

    Initialize the CIPSO module

    :param  void:
        no arguments

.. _`cipso_v4_init.description`:

Description
-----------

Initialize the CIPSO module and prepare it for use.  Returns zero on success
and negative values on failure.

.. This file was automatic generated / don't edit.

