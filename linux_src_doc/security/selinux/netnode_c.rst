.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/selinux/netnode.c

.. _`sel_netnode_hashfn_ipv4`:

sel_netnode_hashfn_ipv4
=======================

.. c:function:: unsigned int sel_netnode_hashfn_ipv4(__be32 addr)

    IPv4 hashing function for the node table

    :param addr:
        IPv4 address
    :type addr: __be32

.. _`sel_netnode_hashfn_ipv4.description`:

Description
-----------

This is the IPv4 hashing function for the node interface table, it returns
the bucket number for the given IP address.

.. _`sel_netnode_hashfn_ipv6`:

sel_netnode_hashfn_ipv6
=======================

.. c:function:: unsigned int sel_netnode_hashfn_ipv6(const struct in6_addr *addr)

    IPv6 hashing function for the node table

    :param addr:
        IPv6 address
    :type addr: const struct in6_addr \*

.. _`sel_netnode_hashfn_ipv6.description`:

Description
-----------

This is the IPv6 hashing function for the node interface table, it returns
the bucket number for the given IP address.

.. _`sel_netnode_find`:

sel_netnode_find
================

.. c:function:: struct sel_netnode *sel_netnode_find(const void *addr, u16 family)

    Search for a node record

    :param addr:
        IP address
    :type addr: const void \*

    :param family:
        address family
    :type family: u16

.. _`sel_netnode_find.description`:

Description
-----------

Search the network node table and return the record matching \ ``addr``\ .  If an
entry can not be found in the table return NULL.

.. _`sel_netnode_insert`:

sel_netnode_insert
==================

.. c:function:: void sel_netnode_insert(struct sel_netnode *node)

    Insert a new node into the table

    :param node:
        the new node record
    :type node: struct sel_netnode \*

.. _`sel_netnode_insert.description`:

Description
-----------

Add a new node record to the network address hash table.

.. _`sel_netnode_sid_slow`:

sel_netnode_sid_slow
====================

.. c:function:: int sel_netnode_sid_slow(void *addr, u16 family, u32 *sid)

    Lookup the SID of a network address using the policy

    :param addr:
        the IP address
    :type addr: void \*

    :param family:
        the address family
    :type family: u16

    :param sid:
        node SID
    :type sid: u32 \*

.. _`sel_netnode_sid_slow.description`:

Description
-----------

This function determines the SID of a network address by quering the
security policy.  The result is added to the network address table to
speedup future queries.  Returns zero on success, negative values on
failure.

.. _`sel_netnode_sid`:

sel_netnode_sid
===============

.. c:function:: int sel_netnode_sid(void *addr, u16 family, u32 *sid)

    Lookup the SID of a network address

    :param addr:
        the IP address
    :type addr: void \*

    :param family:
        the address family
    :type family: u16

    :param sid:
        node SID
    :type sid: u32 \*

.. _`sel_netnode_sid.description`:

Description
-----------

This function determines the SID of a network address using the fastest
method possible.  First the address table is queried, but if an entry
can't be found then the policy is queried and the result is added to the
table to speedup future queries.  Returns zero on success, negative values
on failure.

.. _`sel_netnode_flush`:

sel_netnode_flush
=================

.. c:function:: void sel_netnode_flush( void)

    Flush the entire network address table

    :param void:
        no arguments
    :type void: 

.. _`sel_netnode_flush.description`:

Description
-----------

Remove all entries from the network address table.

.. This file was automatic generated / don't edit.

