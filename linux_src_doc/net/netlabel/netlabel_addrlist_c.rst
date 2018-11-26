.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/netlabel/netlabel_addrlist.c

.. _`netlbl_af4list_search`:

netlbl_af4list_search
=====================

.. c:function:: struct netlbl_af4list *netlbl_af4list_search(__be32 addr, struct list_head *head)

    Search for a matching IPv4 address entry

    :param addr:
        IPv4 address
    :type addr: __be32

    :param head:
        the list head
    :type head: struct list_head \*

.. _`netlbl_af4list_search.description`:

Description
-----------

Searches the IPv4 address list given by \ ``head``\ .  If a matching address entry
is found it is returned, otherwise NULL is returned.  The caller is
responsible for calling the rcu_read_[un]lock() functions.

.. _`netlbl_af4list_search_exact`:

netlbl_af4list_search_exact
===========================

.. c:function:: struct netlbl_af4list *netlbl_af4list_search_exact(__be32 addr, __be32 mask, struct list_head *head)

    Search for an exact IPv4 address entry

    :param addr:
        IPv4 address
    :type addr: __be32

    :param mask:
        IPv4 address mask
    :type mask: __be32

    :param head:
        the list head
    :type head: struct list_head \*

.. _`netlbl_af4list_search_exact.description`:

Description
-----------

Searches the IPv4 address list given by \ ``head``\ .  If an exact match if found
it is returned, otherwise NULL is returned.  The caller is responsible for
calling the rcu_read_[un]lock() functions.

.. _`netlbl_af6list_search`:

netlbl_af6list_search
=====================

.. c:function:: struct netlbl_af6list *netlbl_af6list_search(const struct in6_addr *addr, struct list_head *head)

    Search for a matching IPv6 address entry

    :param addr:
        IPv6 address
    :type addr: const struct in6_addr \*

    :param head:
        the list head
    :type head: struct list_head \*

.. _`netlbl_af6list_search.description`:

Description
-----------

Searches the IPv6 address list given by \ ``head``\ .  If a matching address entry
is found it is returned, otherwise NULL is returned.  The caller is
responsible for calling the rcu_read_[un]lock() functions.

.. _`netlbl_af6list_search_exact`:

netlbl_af6list_search_exact
===========================

.. c:function:: struct netlbl_af6list *netlbl_af6list_search_exact(const struct in6_addr *addr, const struct in6_addr *mask, struct list_head *head)

    Search for an exact IPv6 address entry

    :param addr:
        IPv6 address
    :type addr: const struct in6_addr \*

    :param mask:
        IPv6 address mask
    :type mask: const struct in6_addr \*

    :param head:
        the list head
    :type head: struct list_head \*

.. _`netlbl_af6list_search_exact.description`:

Description
-----------

Searches the IPv6 address list given by \ ``head``\ .  If an exact match if found
it is returned, otherwise NULL is returned.  The caller is responsible for
calling the rcu_read_[un]lock() functions.

.. _`netlbl_af4list_add`:

netlbl_af4list_add
==================

.. c:function:: int netlbl_af4list_add(struct netlbl_af4list *entry, struct list_head *head)

    Add a new IPv4 address entry to a list

    :param entry:
        address entry
    :type entry: struct netlbl_af4list \*

    :param head:
        the list head
    :type head: struct list_head \*

.. _`netlbl_af4list_add.description`:

Description
-----------

Add a new address entry to the list pointed to by \ ``head``\ .  On success zero is
returned, otherwise a negative value is returned.  The caller is responsible
for calling the necessary locking functions.

.. _`netlbl_af6list_add`:

netlbl_af6list_add
==================

.. c:function:: int netlbl_af6list_add(struct netlbl_af6list *entry, struct list_head *head)

    Add a new IPv6 address entry to a list

    :param entry:
        address entry
    :type entry: struct netlbl_af6list \*

    :param head:
        the list head
    :type head: struct list_head \*

.. _`netlbl_af6list_add.description`:

Description
-----------

Add a new address entry to the list pointed to by \ ``head``\ .  On success zero is
returned, otherwise a negative value is returned.  The caller is responsible
for calling the necessary locking functions.

.. _`netlbl_af4list_remove_entry`:

netlbl_af4list_remove_entry
===========================

.. c:function:: void netlbl_af4list_remove_entry(struct netlbl_af4list *entry)

    Remove an IPv4 address entry

    :param entry:
        address entry
    :type entry: struct netlbl_af4list \*

.. _`netlbl_af4list_remove_entry.description`:

Description
-----------

Remove the specified IP address entry.  The caller is responsible for
calling the necessary locking functions.

.. _`netlbl_af4list_remove`:

netlbl_af4list_remove
=====================

.. c:function:: struct netlbl_af4list *netlbl_af4list_remove(__be32 addr, __be32 mask, struct list_head *head)

    Remove an IPv4 address entry

    :param addr:
        IP address
    :type addr: __be32

    :param mask:
        IP address mask
    :type mask: __be32

    :param head:
        the list head
    :type head: struct list_head \*

.. _`netlbl_af4list_remove.description`:

Description
-----------

Remove an IP address entry from the list pointed to by \ ``head``\ .  Returns the
entry on success, NULL on failure.  The caller is responsible for calling
the necessary locking functions.

.. _`netlbl_af6list_remove_entry`:

netlbl_af6list_remove_entry
===========================

.. c:function:: void netlbl_af6list_remove_entry(struct netlbl_af6list *entry)

    Remove an IPv6 address entry

    :param entry:
        address entry
    :type entry: struct netlbl_af6list \*

.. _`netlbl_af6list_remove_entry.description`:

Description
-----------

Remove the specified IP address entry.  The caller is responsible for
calling the necessary locking functions.

.. _`netlbl_af6list_remove`:

netlbl_af6list_remove
=====================

.. c:function:: struct netlbl_af6list *netlbl_af6list_remove(const struct in6_addr *addr, const struct in6_addr *mask, struct list_head *head)

    Remove an IPv6 address entry

    :param addr:
        IP address
    :type addr: const struct in6_addr \*

    :param mask:
        IP address mask
    :type mask: const struct in6_addr \*

    :param head:
        the list head
    :type head: struct list_head \*

.. _`netlbl_af6list_remove.description`:

Description
-----------

Remove an IP address entry from the list pointed to by \ ``head``\ .  Returns the
entry on success, NULL on failure.  The caller is responsible for calling
the necessary locking functions.

.. _`netlbl_af4list_audit_addr`:

netlbl_af4list_audit_addr
=========================

.. c:function:: void netlbl_af4list_audit_addr(struct audit_buffer *audit_buf, int src, const char *dev, __be32 addr, __be32 mask)

    Audit an IPv4 address

    :param audit_buf:
        audit buffer
    :type audit_buf: struct audit_buffer \*

    :param src:
        true if source address, false if destination
    :type src: int

    :param dev:
        network interface
    :type dev: const char \*

    :param addr:
        IP address
    :type addr: __be32

    :param mask:
        IP address mask
    :type mask: __be32

.. _`netlbl_af4list_audit_addr.description`:

Description
-----------

Write the IPv4 address and address mask, if necessary, to \ ``audit_buf``\ .

.. _`netlbl_af6list_audit_addr`:

netlbl_af6list_audit_addr
=========================

.. c:function:: void netlbl_af6list_audit_addr(struct audit_buffer *audit_buf, int src, const char *dev, const struct in6_addr *addr, const struct in6_addr *mask)

    Audit an IPv6 address

    :param audit_buf:
        audit buffer
    :type audit_buf: struct audit_buffer \*

    :param src:
        true if source address, false if destination
    :type src: int

    :param dev:
        network interface
    :type dev: const char \*

    :param addr:
        IP address
    :type addr: const struct in6_addr \*

    :param mask:
        IP address mask
    :type mask: const struct in6_addr \*

.. _`netlbl_af6list_audit_addr.description`:

Description
-----------

Write the IPv6 address and address mask, if necessary, to \ ``audit_buf``\ .

.. This file was automatic generated / don't edit.

