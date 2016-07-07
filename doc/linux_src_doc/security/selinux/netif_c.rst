.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/selinux/netif.c

.. _`sel_netif_hashfn`:

sel_netif_hashfn
================

.. c:function:: u32 sel_netif_hashfn(const struct net *ns, int ifindex)

    Hashing function for the interface table

    :param const struct net \*ns:
        the network namespace

    :param int ifindex:
        the network interface

.. _`sel_netif_hashfn.description`:

Description
-----------

This is the hashing function for the network interface table, it returns the
bucket number for the given interface.

.. _`sel_netif_find`:

sel_netif_find
==============

.. c:function:: struct sel_netif *sel_netif_find(const struct net *ns, int ifindex)

    Search for an interface record

    :param const struct net \*ns:
        the network namespace

    :param int ifindex:
        the network interface

.. _`sel_netif_find.description`:

Description
-----------

Search the network interface table and return the record matching \ ``ifindex``\ .
If an entry can not be found in the table return NULL.

.. _`sel_netif_insert`:

sel_netif_insert
================

.. c:function:: int sel_netif_insert(struct sel_netif *netif)

    Insert a new interface into the table

    :param struct sel_netif \*netif:
        the new interface record

.. _`sel_netif_insert.description`:

Description
-----------

Add a new interface record to the network interface hash table.  Returns
zero on success, negative values on failure.

.. _`sel_netif_destroy`:

sel_netif_destroy
=================

.. c:function:: void sel_netif_destroy(struct sel_netif *netif)

    Remove an interface record from the table

    :param struct sel_netif \*netif:
        the existing interface record

.. _`sel_netif_destroy.description`:

Description
-----------

Remove an existing interface record from the network interface table.

.. _`sel_netif_sid_slow`:

sel_netif_sid_slow
==================

.. c:function:: int sel_netif_sid_slow(struct net *ns, int ifindex, u32 *sid)

    Lookup the SID of a network interface using the policy

    :param struct net \*ns:
        the network namespace

    :param int ifindex:
        the network interface

    :param u32 \*sid:
        interface SID

.. _`sel_netif_sid_slow.description`:

Description
-----------

This function determines the SID of a network interface by quering the
security policy.  The result is added to the network interface table to
speedup future queries.  Returns zero on success, negative values on
failure.

.. _`sel_netif_sid`:

sel_netif_sid
=============

.. c:function:: int sel_netif_sid(struct net *ns, int ifindex, u32 *sid)

    Lookup the SID of a network interface

    :param struct net \*ns:
        the network namespace

    :param int ifindex:
        the network interface

    :param u32 \*sid:
        interface SID

.. _`sel_netif_sid.description`:

Description
-----------

This function determines the SID of a network interface using the fastest
method possible.  First the interface table is queried, but if an entry
can't be found then the policy is queried and the result is added to the
table to speedup future queries.  Returns zero on success, negative values
on failure.

.. _`sel_netif_kill`:

sel_netif_kill
==============

.. c:function:: void sel_netif_kill(const struct net *ns, int ifindex)

    Remove an entry from the network interface table

    :param const struct net \*ns:
        the network namespace

    :param int ifindex:
        the network interface

.. _`sel_netif_kill.description`:

Description
-----------

This function removes the entry matching \ ``ifindex``\  from the network interface
table if it exists.

.. _`sel_netif_flush`:

sel_netif_flush
===============

.. c:function:: void sel_netif_flush( void)

    Flush the entire network interface table

    :param  void:
        no arguments

.. _`sel_netif_flush.description`:

Description
-----------

Remove all entries from the network interface table.

.. This file was automatic generated / don't edit.

