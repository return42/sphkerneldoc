.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/selinux/ibpkey.c

.. _`sel_ib_pkey_hashfn`:

sel_ib_pkey_hashfn
==================

.. c:function:: unsigned int sel_ib_pkey_hashfn(u16 pkey)

    Hashing function for the pkey table

    :param pkey:
        pkey number
    :type pkey: u16

.. _`sel_ib_pkey_hashfn.description`:

Description
-----------

This is the hashing function for the pkey table, it returns the bucket
number for the given pkey.

.. _`sel_ib_pkey_find`:

sel_ib_pkey_find
================

.. c:function:: struct sel_ib_pkey *sel_ib_pkey_find(u64 subnet_prefix, u16 pkey_num)

    Search for a pkey record

    :param subnet_prefix:
        subnet_prefix
    :type subnet_prefix: u64

    :param pkey_num:
        pkey_num
    :type pkey_num: u16

.. _`sel_ib_pkey_find.description`:

Description
-----------

Search the pkey table and return the matching record.  If an entry
can not be found in the table return NULL.

.. _`sel_ib_pkey_insert`:

sel_ib_pkey_insert
==================

.. c:function:: void sel_ib_pkey_insert(struct sel_ib_pkey *pkey)

    Insert a new pkey into the table

    :param pkey:
        the new pkey record
    :type pkey: struct sel_ib_pkey \*

.. _`sel_ib_pkey_insert.description`:

Description
-----------

Add a new pkey record to the hash table.

.. _`sel_ib_pkey_sid_slow`:

sel_ib_pkey_sid_slow
====================

.. c:function:: int sel_ib_pkey_sid_slow(u64 subnet_prefix, u16 pkey_num, u32 *sid)

    Lookup the SID of a pkey using the policy

    :param subnet_prefix:
        subnet prefix
    :type subnet_prefix: u64

    :param pkey_num:
        pkey number
    :type pkey_num: u16

    :param sid:
        pkey SID
    :type sid: u32 \*

.. _`sel_ib_pkey_sid_slow.description`:

Description
-----------

This function determines the SID of a pkey by querying the security
policy.  The result is added to the pkey table to speedup future
queries.  Returns zero on success, negative values on failure.

.. _`sel_ib_pkey_sid`:

sel_ib_pkey_sid
===============

.. c:function:: int sel_ib_pkey_sid(u64 subnet_prefix, u16 pkey_num, u32 *sid)

    Lookup the SID of a PKEY

    :param subnet_prefix:
        subnet_prefix
    :type subnet_prefix: u64

    :param pkey_num:
        pkey number
    :type pkey_num: u16

    :param sid:
        pkey SID
    :type sid: u32 \*

.. _`sel_ib_pkey_sid.description`:

Description
-----------

This function determines the SID of a PKEY using the fastest method
possible.  First the pkey table is queried, but if an entry can't be found
then the policy is queried and the result is added to the table to speedup
future queries.  Returns zero on success, negative values on failure.

.. _`sel_ib_pkey_flush`:

sel_ib_pkey_flush
=================

.. c:function:: void sel_ib_pkey_flush( void)

    Flush the entire pkey table

    :param void:
        no arguments
    :type void: 

.. _`sel_ib_pkey_flush.description`:

Description
-----------

Remove all entries from the pkey table

.. This file was automatic generated / don't edit.

