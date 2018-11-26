.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/nfs4state.c

.. _`nfs40_discover_server_trunking`:

nfs40_discover_server_trunking
==============================

.. c:function:: int nfs40_discover_server_trunking(struct nfs_client *clp, struct nfs_client **result, struct rpc_cred *cred)

    Detect server IP address trunking (mv0)

    :param clp:
        nfs_client under test
    :type clp: struct nfs_client \*

    :param result:
        OUT: found nfs_client, or clp
    :type result: struct nfs_client \*\*

    :param cred:
        credential to use for trunking test
    :type cred: struct rpc_cred \*

.. _`nfs40_discover_server_trunking.description`:

Description
-----------

Returns zero, a negative errno, or a negative NFS4ERR status.
If zero is returned, an nfs_client pointer is planted in
"result".

.. _`nfs40_discover_server_trunking.note`:

Note
----

The returned client may not yet be marked ready.

.. _`nfs4_get_renew_cred_locked`:

nfs4_get_renew_cred_locked
==========================

.. c:function:: struct rpc_cred *nfs4_get_renew_cred_locked(struct nfs_client *clp)

    Acquire credential for a renew operation

    :param clp:
        client state handle
    :type clp: struct nfs_client \*

.. _`nfs4_get_renew_cred_locked.description`:

Description
-----------

Returns an rpc_cred with reference count bumped, or NULL.
Caller must hold clp->cl_lock.

.. _`nfs41_discover_server_trunking`:

nfs41_discover_server_trunking
==============================

.. c:function:: int nfs41_discover_server_trunking(struct nfs_client *clp, struct nfs_client **result, struct rpc_cred *cred)

    Detect server IP address trunking (mv1)

    :param clp:
        nfs_client under test
    :type clp: struct nfs_client \*

    :param result:
        OUT: found nfs_client, or clp
    :type result: struct nfs_client \*\*

    :param cred:
        credential to use for trunking test
    :type cred: struct rpc_cred \*

.. _`nfs41_discover_server_trunking.description`:

Description
-----------

Returns NFS4_OK, a negative errno, or a negative NFS4ERR status.
If NFS4_OK is returned, an nfs_client pointer is planted in
"result".

.. _`nfs41_discover_server_trunking.note`:

Note
----

The returned client may not yet be marked ready.

.. _`nfs4_get_clid_cred`:

nfs4_get_clid_cred
==================

.. c:function:: struct rpc_cred *nfs4_get_clid_cred(struct nfs_client *clp)

    Acquire credential for a setclientid operation

    :param clp:
        client state handle
    :type clp: struct nfs_client \*

.. _`nfs4_get_clid_cred.description`:

Description
-----------

Returns an rpc_cred with reference count bumped, or NULL.

.. _`nfs4_get_state_owner`:

nfs4_get_state_owner
====================

.. c:function:: struct nfs4_state_owner *nfs4_get_state_owner(struct nfs_server *server, struct rpc_cred *cred, gfp_t gfp_flags)

    Look up a state owner given a credential

    :param server:
        nfs_server to search
    :type server: struct nfs_server \*

    :param cred:
        RPC credential to match
    :type cred: struct rpc_cred \*

    :param gfp_flags:
        *undescribed*
    :type gfp_flags: gfp_t

.. _`nfs4_get_state_owner.description`:

Description
-----------

Returns a pointer to an instantiated nfs4_state_owner struct, or NULL.

.. _`nfs4_put_state_owner`:

nfs4_put_state_owner
====================

.. c:function:: void nfs4_put_state_owner(struct nfs4_state_owner *sp)

    Release a nfs4_state_owner

    :param sp:
        state owner data to release
    :type sp: struct nfs4_state_owner \*

.. _`nfs4_put_state_owner.description`:

Description
-----------

Note that we keep released state owners on an LRU
list.
This caches valid state owners so that they can be
reused, to avoid the OPEN_CONFIRM on minor version 0.
It also pins the uniquifier of dropped state owners for
a while, to ensure that those state owner names are
never reused.

.. _`nfs4_purge_state_owners`:

nfs4_purge_state_owners
=======================

.. c:function:: void nfs4_purge_state_owners(struct nfs_server *server)

    Release all cached state owners

    :param server:
        nfs_server with cached state owners to release
    :type server: struct nfs_server \*

.. _`nfs4_purge_state_owners.description`:

Description
-----------

Called at umount time.  Remaining state owners will be on
the LRU with ref count of zero.

.. _`nfs4_schedule_migration_recovery`:

nfs4_schedule_migration_recovery
================================

.. c:function:: int nfs4_schedule_migration_recovery(const struct nfs_server *server)

    trigger migration recovery

    :param server:
        FSID that is migrating
    :type server: const struct nfs_server \*

.. _`nfs4_schedule_migration_recovery.description`:

Description
-----------

Returns zero if recovery has started, otherwise a negative NFS4ERR
value is returned.

.. _`nfs4_schedule_lease_moved_recovery`:

nfs4_schedule_lease_moved_recovery
==================================

.. c:function:: void nfs4_schedule_lease_moved_recovery(struct nfs_client *clp)

    start lease-moved recovery

    :param clp:
        server to check for moved leases
    :type clp: struct nfs_client \*

.. _`nfs4_discover_server_trunking`:

nfs4_discover_server_trunking
=============================

.. c:function:: int nfs4_discover_server_trunking(struct nfs_client *clp, struct nfs_client **result)

    Detect server IP address trunking

    :param clp:
        nfs_client under test
    :type clp: struct nfs_client \*

    :param result:
        OUT: found nfs_client, or clp
    :type result: struct nfs_client \*\*

.. _`nfs4_discover_server_trunking.description`:

Description
-----------

Returns zero or a negative errno.  If zero is returned,
an nfs_client pointer is planted in "result".

.. _`nfs4_discover_server_trunking.note`:

Note
----

since we are invoked in process context, and
not from inside the state manager, we cannot use
\ :c:func:`nfs4_handle_reclaim_lease_error`\ .

.. This file was automatic generated / don't edit.

