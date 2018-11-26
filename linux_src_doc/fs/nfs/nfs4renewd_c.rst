.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/nfs4renewd.c

.. _`nfs4_set_lease_period`:

nfs4_set_lease_period
=====================

.. c:function:: void nfs4_set_lease_period(struct nfs_client *clp, unsigned long lease, unsigned long lastrenewed)

    Sets the lease period on a nfs_client

    :param clp:
        pointer to nfs_client
    :type clp: struct nfs_client \*

    :param lease:
        new value for lease period
    :type lease: unsigned long

    :param lastrenewed:
        time at which lease was last renewed
    :type lastrenewed: unsigned long

.. This file was automatic generated / don't edit.

