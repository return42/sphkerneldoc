.. -*- coding: utf-8; mode: rst -*-

=============
nfs4session.c
=============


.. _`nfs4_slot_tbl_drain_complete`:

nfs4_slot_tbl_drain_complete
============================

.. c:function:: void nfs4_slot_tbl_drain_complete (struct nfs4_slot_table *tbl)

    wake waiters when drain is complete @tbl - controlling slot table

    :param struct nfs4_slot_table \*tbl:

        *undescribed*



.. _`nfs4_shutdown_slot_table`:

nfs4_shutdown_slot_table
========================

.. c:function:: void nfs4_shutdown_slot_table (struct nfs4_slot_table *tbl)

    release resources attached to a slot table

    :param struct nfs4_slot_table \*tbl:
        slot table to shut down



.. _`nfs4_setup_slot_table`:

nfs4_setup_slot_table
=====================

.. c:function:: int nfs4_setup_slot_table (struct nfs4_slot_table *tbl, unsigned int max_reqs, const char *queue)

    prepare a stand-alone slot table for use

    :param struct nfs4_slot_table \*tbl:
        slot table to set up

    :param unsigned int max_reqs:
        maximum number of requests allowed

    :param const char \*queue:
        name to give RPC wait queue



.. _`nfs4_setup_slot_table.description`:

Description
-----------

Returns zero on success, or a negative errno.

