.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/nfs4renewd.c

.. _`nfs4_set_lease_period`:

nfs4_set_lease_period
=====================

.. c:function:: void nfs4_set_lease_period(struct nfs_client *clp, unsigned long lease, unsigned long lastrenewed)

    Sets the lease period on a nfs_client

    :param struct nfs_client \*clp:
        pointer to nfs_client

    :param unsigned long lease:
        new value for lease period

    :param unsigned long lastrenewed:
        time at which lease was last renewed

.. This file was automatic generated / don't edit.

