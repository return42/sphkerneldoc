.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/netlabel/netlabel_addrlist.c

.. _`netlbl_af4list_search`:

netlbl_af4list_search
=====================

.. c:function:: struct netlbl_af4list *netlbl_af4list_search(__be32 addr, struct list_head *head)

    Search for a matching IPv4 address entry

    :param __be32 addr:
        IPv4 address

    :param struct list_head \*head:
        the list head

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

    :param __be32 addr:
        IPv4 address

    :param __be32 mask:
        IPv4 address mask

    :param struct list_head \*head:
        the list head

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

    :param const struct in6_addr \*addr:
        IPv6 address

    :param struct list_head \*head:
        the list head

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

    :param const struct in6_addr \*addr:
        IPv6 address

    :param const struct in6_addr \*mask:
        IPv6 address mask

    :param struct list_head \*head:
        the list head

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

    :param struct netlbl_af4list \*entry:
        address entry

    :param struct list_head \*head:
        the list head

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

    :param struct netlbl_af6list \*entry:
        address entry

    :param struct list_head \*head:
        the list head

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

    :param struct netlbl_af4list \*entry:
        address entry

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

    :param __be32 addr:
        IP address

    :param __be32 mask:
        IP address mask

    :param struct list_head \*head:
        the list head

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

    :param struct netlbl_af6list \*entry:
        address entry

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

    :param const struct in6_addr \*addr:
        IP address

    :param const struct in6_addr \*mask:
        IP address mask

    :param struct list_head \*head:
        the list head

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

    :param struct audit_buffer \*audit_buf:
        audit buffer

    :param int src:
        true if source address, false if destination

    :param const char \*dev:
        network interface

    :param __be32 addr:
        IP address

    :param __be32 mask:
        IP address mask

.. _`netlbl_af4list_audit_addr.description`:

Description
-----------

Write the IPv4 address and address mask, if necessary, to \ ``audit_buf``\ .

.. _`netlbl_af6list_audit_addr`:

netlbl_af6list_audit_addr
=========================

.. c:function:: void netlbl_af6list_audit_addr(struct audit_buffer *audit_buf, int src, const char *dev, const struct in6_addr *addr, const struct in6_addr *mask)

    Audit an IPv6 address

    :param struct audit_buffer \*audit_buf:
        audit buffer

    :param int src:
        true if source address, false if destination

    :param const char \*dev:
        network interface

    :param const struct in6_addr \*addr:
        IP address

    :param const struct in6_addr \*mask:
        IP address mask

.. _`netlbl_af6list_audit_addr.description`:

Description
-----------

Write the IPv6 address and address mask, if necessary, to \ ``audit_buf``\ .

.. This file was automatic generated / don't edit.

