.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfsd/nfs4state.c

.. _`nfs4_delegation_exists`:

nfs4_delegation_exists
======================

.. c:function:: bool nfs4_delegation_exists(struct nfs4_client *clp, struct nfs4_file *fp)

    Discover if this delegation already exists

    :param clp:
        a pointer to the nfs4_client we're granting a delegation to
    :type clp: struct nfs4_client \*

    :param fp:
        a pointer to the nfs4_file we're granting a delegation on
    :type fp: struct nfs4_file \*

.. _`nfs4_delegation_exists.on-success`:

On success
----------

true iff an existing delegation is found

.. _`hash_delegation_locked`:

hash_delegation_locked
======================

.. c:function:: int hash_delegation_locked(struct nfs4_delegation *dp, struct nfs4_file *fp)

    Add a delegation to the appropriate lists

    :param dp:
        a pointer to the nfs4_delegation we are adding.
    :type dp: struct nfs4_delegation \*

    :param fp:
        a pointer to the nfs4_file we're granting a delegation on
    :type fp: struct nfs4_file \*

.. _`hash_delegation_locked.on-success`:

On success
----------

NULL if the delegation was successfully hashed.

.. _`hash_delegation_locked.on-error`:

On error
--------

-EAGAIN if one was previously granted to this
nfs4_client for this nfs4_file. Delegation is not hashed.

.. This file was automatic generated / don't edit.

