.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfsd/nfs4state.c

.. _`nfs4_get_existing_delegation`:

nfs4_get_existing_delegation
============================

.. c:function:: int nfs4_get_existing_delegation(struct nfs4_client *clp, struct nfs4_file *fp)

    Discover if this delegation already exists

    :param struct nfs4_client \*clp:
        a pointer to the nfs4_client we're granting a delegation to

    :param struct nfs4_file \*fp:
        a pointer to the nfs4_file we're granting a delegation on

.. _`nfs4_get_existing_delegation.on-success`:

On success
----------

NULL if an existing delegation was not found.

.. _`nfs4_get_existing_delegation.on-error`:

On error
--------

-EAGAIN if one was previously granted to this nfs4_client
for this nfs4_file.

.. _`hash_delegation_locked`:

hash_delegation_locked
======================

.. c:function:: int hash_delegation_locked(struct nfs4_delegation *dp, struct nfs4_file *fp)

    Add a delegation to the appropriate lists

    :param struct nfs4_delegation \*dp:
        a pointer to the nfs4_delegation we are adding.

    :param struct nfs4_file \*fp:
        a pointer to the nfs4_file we're granting a delegation on

.. _`hash_delegation_locked.on-success`:

On success
----------

NULL if the delegation was successfully hashed.

.. _`hash_delegation_locked.on-error`:

On error
--------

-EAGAIN if one was previously granted to this
nfs4_client for this nfs4_file. Delegation is not hashed.

.. _`nfs4_setlease`:

nfs4_setlease
=============

.. c:function:: int nfs4_setlease(struct nfs4_delegation *dp)

    Obtain a delegation by requesting lease from vfs layer

    :param struct nfs4_delegation \*dp:
        a pointer to the nfs4_delegation we're adding.

.. _`nfs4_setlease.on-success`:

On success
----------

Return code will be 0 on success.

.. _`nfs4_setlease.on-error`:

On error
--------

-EAGAIN if there was an existing delegation.
nonzero if there is an error in other cases.

.. This file was automatic generated / don't edit.

