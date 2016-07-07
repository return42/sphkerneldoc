.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/selinux/netport.c

.. _`sel_netport_hashfn`:

sel_netport_hashfn
==================

.. c:function:: unsigned int sel_netport_hashfn(u16 pnum)

    Hashing function for the port table

    :param u16 pnum:
        port number

.. _`sel_netport_hashfn.description`:

Description
-----------

This is the hashing function for the port table, it returns the bucket
number for the given port.

.. _`sel_netport_find`:

sel_netport_find
================

.. c:function:: struct sel_netport *sel_netport_find(u8 protocol, u16 pnum)

    Search for a port record

    :param u8 protocol:
        protocol

    :param u16 pnum:
        *undescribed*

.. _`sel_netport_find.description`:

Description
-----------

Search the network port table and return the matching record.  If an entry
can not be found in the table return NULL.

.. _`sel_netport_insert`:

sel_netport_insert
==================

.. c:function:: void sel_netport_insert(struct sel_netport *port)

    Insert a new port into the table

    :param struct sel_netport \*port:
        the new port record

.. _`sel_netport_insert.description`:

Description
-----------

Add a new port record to the network address hash table.

.. _`sel_netport_sid_slow`:

sel_netport_sid_slow
====================

.. c:function:: int sel_netport_sid_slow(u8 protocol, u16 pnum, u32 *sid)

    Lookup the SID of a network address using the policy

    :param u8 protocol:
        protocol

    :param u16 pnum:
        port

    :param u32 \*sid:
        port SID

.. _`sel_netport_sid_slow.description`:

Description
-----------

This function determines the SID of a network port by quering the security
policy.  The result is added to the network port table to speedup future
queries.  Returns zero on success, negative values on failure.

.. _`sel_netport_sid`:

sel_netport_sid
===============

.. c:function:: int sel_netport_sid(u8 protocol, u16 pnum, u32 *sid)

    Lookup the SID of a network port

    :param u8 protocol:
        protocol

    :param u16 pnum:
        port

    :param u32 \*sid:
        port SID

.. _`sel_netport_sid.description`:

Description
-----------

This function determines the SID of a network port using the fastest method
possible.  First the port table is queried, but if an entry can't be found
then the policy is queried and the result is added to the table to speedup
future queries.  Returns zero on success, negative values on failure.

.. _`sel_netport_flush`:

sel_netport_flush
=================

.. c:function:: void sel_netport_flush( void)

    Flush the entire network port table

    :param  void:
        no arguments

.. _`sel_netport_flush.description`:

Description
-----------

Remove all entries from the network address table.

.. This file was automatic generated / don't edit.

