.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/netlabel/netlabel_domainhash.c

.. _`netlbl_domhsh_free_entry`:

netlbl_domhsh_free_entry
========================

.. c:function:: void netlbl_domhsh_free_entry(struct rcu_head *entry)

    Frees a domain hash table entry

    :param struct rcu_head \*entry:
        the entry's RCU field

.. _`netlbl_domhsh_free_entry.description`:

Description
-----------

This function is designed to be used as a callback to the \ :c:func:`call_rcu`\ 
function so that the memory allocated to a hash table entry can be released
safely.

.. _`netlbl_domhsh_hash`:

netlbl_domhsh_hash
==================

.. c:function:: u32 netlbl_domhsh_hash(const char *key)

    Hashing function for the domain hash table

    :param const char \*key:
        *undescribed*

.. _`netlbl_domhsh_hash.description`:

Description
-----------

This is the hashing function for the domain hash table, it returns the
correct bucket number for the domain.  The caller is responsible for
ensuring that the hash table is protected with either a RCU read lock or the
hash table lock.

.. _`netlbl_domhsh_search`:

netlbl_domhsh_search
====================

.. c:function:: struct netlbl_dom_map *netlbl_domhsh_search(const char *domain)

    Search for a domain entry

    :param const char \*domain:
        the domain

.. _`netlbl_domhsh_search.description`:

Description
-----------

Searches the domain hash table and returns a pointer to the hash table
entry if found, otherwise NULL is returned.  The caller is responsible for
ensuring that the hash table is protected with either a RCU read lock or the
hash table lock.

.. _`netlbl_domhsh_search_def`:

netlbl_domhsh_search_def
========================

.. c:function:: struct netlbl_dom_map *netlbl_domhsh_search_def(const char *domain)

    Search for a domain entry

    :param const char \*domain:
        the domain

.. _`netlbl_domhsh_search_def.description`:

Description
-----------

Searches the domain hash table and returns a pointer to the hash table
entry if an exact match is found, if an exact match is not present in the
hash table then the default entry is returned if valid otherwise NULL is
returned.  The caller is responsible ensuring that the hash table is
protected with either a RCU read lock or the hash table lock.

.. _`netlbl_domhsh_audit_add`:

netlbl_domhsh_audit_add
=======================

.. c:function:: void netlbl_domhsh_audit_add(struct netlbl_dom_map *entry, struct netlbl_af4list *addr4, struct netlbl_af6list *addr6, int result, struct netlbl_audit *audit_info)

    Generate an audit entry for an add event

    :param struct netlbl_dom_map \*entry:
        the entry being added

    :param struct netlbl_af4list \*addr4:
        the IPv4 address information

    :param struct netlbl_af6list \*addr6:
        the IPv6 address information

    :param int result:
        the result code

    :param struct netlbl_audit \*audit_info:
        NetLabel audit information

.. _`netlbl_domhsh_audit_add.description`:

Description
-----------

Generate an audit record for adding a new NetLabel/LSM mapping entry with
the given information.  Caller is responsible for holding the necessary
locks.

.. _`netlbl_domhsh_validate`:

netlbl_domhsh_validate
======================

.. c:function:: int netlbl_domhsh_validate(const struct netlbl_dom_map *entry)

    Validate a new domain mapping entry

    :param const struct netlbl_dom_map \*entry:
        the entry to validate

.. _`netlbl_domhsh_validate.description`:

Description
-----------

This function validates the new domain mapping entry to ensure that it is
a valid entry.  Returns zero on success, negative values on failure.

.. _`netlbl_domhsh_init`:

netlbl_domhsh_init
==================

.. c:function:: int netlbl_domhsh_init(u32 size)

    Init for the domain hash

    :param u32 size:
        the number of bits to use for the hash buckets

.. _`netlbl_domhsh_init.description`:

Description
-----------

Initializes the domain hash table, should be called only by
\ :c:func:`netlbl_user_init`\  during initialization.  Returns zero on success, non-zero
values on error.

.. _`netlbl_domhsh_add`:

netlbl_domhsh_add
=================

.. c:function:: int netlbl_domhsh_add(struct netlbl_dom_map *entry, struct netlbl_audit *audit_info)

    Adds a entry to the domain hash table

    :param struct netlbl_dom_map \*entry:
        the entry to add

    :param struct netlbl_audit \*audit_info:
        NetLabel audit information

.. _`netlbl_domhsh_add.description`:

Description
-----------

Adds a new entry to the domain hash table and handles any updates to the
lower level protocol handler (i.e. CIPSO).  Returns zero on success,
negative on failure.

.. _`netlbl_domhsh_add_default`:

netlbl_domhsh_add_default
=========================

.. c:function:: int netlbl_domhsh_add_default(struct netlbl_dom_map *entry, struct netlbl_audit *audit_info)

    Adds the default entry to the domain hash table

    :param struct netlbl_dom_map \*entry:
        the entry to add

    :param struct netlbl_audit \*audit_info:
        NetLabel audit information

.. _`netlbl_domhsh_add_default.description`:

Description
-----------

Adds a new default entry to the domain hash table and handles any updates
to the lower level protocol handler (i.e. CIPSO).  Returns zero on success,
negative on failure.

.. _`netlbl_domhsh_remove_entry`:

netlbl_domhsh_remove_entry
==========================

.. c:function:: int netlbl_domhsh_remove_entry(struct netlbl_dom_map *entry, struct netlbl_audit *audit_info)

    Removes a given entry from the domain table

    :param struct netlbl_dom_map \*entry:
        the entry to remove

    :param struct netlbl_audit \*audit_info:
        NetLabel audit information

.. _`netlbl_domhsh_remove_entry.description`:

Description
-----------

Removes an entry from the domain hash table and handles any updates to the
lower level protocol handler (i.e. CIPSO).  Caller is responsible for
ensuring that the RCU read lock is held.  Returns zero on success, negative
on failure.

.. _`netlbl_domhsh_remove_af4`:

netlbl_domhsh_remove_af4
========================

.. c:function:: int netlbl_domhsh_remove_af4(const char *domain, const struct in_addr *addr, const struct in_addr *mask, struct netlbl_audit *audit_info)

    Removes an address selector entry

    :param const char \*domain:
        the domain

    :param const struct in_addr \*addr:
        IPv4 address

    :param const struct in_addr \*mask:
        IPv4 address mask

    :param struct netlbl_audit \*audit_info:
        NetLabel audit information

.. _`netlbl_domhsh_remove_af4.description`:

Description
-----------

Removes an individual address selector from a domain mapping and potentially
the entire mapping if it is empty.  Returns zero on success, negative values
on failure.

.. _`netlbl_domhsh_remove`:

netlbl_domhsh_remove
====================

.. c:function:: int netlbl_domhsh_remove(const char *domain, struct netlbl_audit *audit_info)

    Removes an entry from the domain hash table

    :param const char \*domain:
        the domain to remove

    :param struct netlbl_audit \*audit_info:
        NetLabel audit information

.. _`netlbl_domhsh_remove.description`:

Description
-----------

Removes an entry from the domain hash table and handles any updates to the
lower level protocol handler (i.e. CIPSO).  Returns zero on success,
negative on failure.

.. _`netlbl_domhsh_remove_default`:

netlbl_domhsh_remove_default
============================

.. c:function:: int netlbl_domhsh_remove_default(struct netlbl_audit *audit_info)

    Removes the default entry from the table

    :param struct netlbl_audit \*audit_info:
        NetLabel audit information

.. _`netlbl_domhsh_remove_default.description`:

Description
-----------

Removes/resets the default entry for the domain hash table and handles any
updates to the lower level protocol handler (i.e. CIPSO).  Returns zero on
success, non-zero on failure.

.. _`netlbl_domhsh_getentry`:

netlbl_domhsh_getentry
======================

.. c:function:: struct netlbl_dom_map *netlbl_domhsh_getentry(const char *domain)

    Get an entry from the domain hash table

    :param const char \*domain:
        the domain name to search for

.. _`netlbl_domhsh_getentry.description`:

Description
-----------

Look through the domain hash table searching for an entry to match \ ``domain``\ ,
return a pointer to a copy of the entry or NULL.  The caller is responsible
for ensuring that rcu_read_[un]\ :c:func:`lock`\  is called.

.. _`netlbl_domhsh_getentry_af4`:

netlbl_domhsh_getentry_af4
==========================

.. c:function:: struct netlbl_dommap_def *netlbl_domhsh_getentry_af4(const char *domain, __be32 addr)

    Get an entry from the domain hash table

    :param const char \*domain:
        the domain name to search for

    :param __be32 addr:
        the IP address to search for

.. _`netlbl_domhsh_getentry_af4.description`:

Description
-----------

Look through the domain hash table searching for an entry to match \ ``domain``\ 
and \ ``addr``\ , return a pointer to a copy of the entry or NULL.  The caller is
responsible for ensuring that rcu_read_[un]\ :c:func:`lock`\  is called.

.. _`netlbl_domhsh_getentry_af6`:

netlbl_domhsh_getentry_af6
==========================

.. c:function:: struct netlbl_dommap_def *netlbl_domhsh_getentry_af6(const char *domain, const struct in6_addr *addr)

    Get an entry from the domain hash table

    :param const char \*domain:
        the domain name to search for

    :param const struct in6_addr \*addr:
        the IP address to search for

.. _`netlbl_domhsh_getentry_af6.description`:

Description
-----------

Look through the domain hash table searching for an entry to match \ ``domain``\ 
and \ ``addr``\ , return a pointer to a copy of the entry or NULL.  The caller is
responsible for ensuring that rcu_read_[un]\ :c:func:`lock`\  is called.

.. _`netlbl_domhsh_walk`:

netlbl_domhsh_walk
==================

.. c:function:: int netlbl_domhsh_walk(u32 *skip_bkt, u32 *skip_chain, int (*callback)(struct netlbl_dom_map *entry, void *arg), void *cb_arg)

    Iterate through the domain mapping hash table

    :param u32 \*skip_bkt:
        the number of buckets to skip at the start

    :param u32 \*skip_chain:
        the number of entries to skip in the first iterated bucket

    :param int (\*callback)(struct netlbl_dom_map \*entry, void \*arg):
        callback for each entry

    :param void \*cb_arg:
        argument for the callback function

.. _`netlbl_domhsh_walk.description`:

Description
-----------

Interate over the domain mapping hash table, skipping the first \ ``skip_bkt``\ 
buckets and \ ``skip_chain``\  entries.  For each entry in the table call
\ ``callback``\ , if \ ``callback``\  returns a negative value stop 'walking' through the
table and return.  Updates the values in \ ``skip_bkt``\  and \ ``skip_chain``\  on
return.  Returns zero on success, negative values on failure.

.. This file was automatic generated / don't edit.

