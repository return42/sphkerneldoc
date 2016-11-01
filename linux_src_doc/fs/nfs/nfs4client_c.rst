.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/nfs4client.c

.. _`nfs4_find_ds_client`:

nfs4_find_ds_client
===================

.. c:function:: struct nfs4_ds_server *nfs4_find_ds_client(struct nfs_client *ds_clp, rpc_authflavor_t flavor)

    :param struct nfs_client \*ds_clp:
        *undescribed*

    :param rpc_authflavor_t flavor:
        *undescribed*

.. _`nfs4_find_or_create_ds_client`:

nfs4_find_or_create_ds_client
=============================

.. c:function:: struct rpc_clnt *nfs4_find_or_create_ds_client(struct nfs_client *ds_clp, struct inode *inode)

    in the nfs_client cl_ds_clients list.

    :param struct nfs_client \*ds_clp:
        *undescribed*

    :param struct inode \*inode:
        *undescribed*

.. _`nfs40_init_client`:

nfs40_init_client
=================

.. c:function:: int nfs40_init_client(struct nfs_client *clp)

    nfs_client initialization tasks for NFSv4.0 \ ``clp``\  - nfs_client to initialize

    :param struct nfs_client \*clp:
        *undescribed*

.. _`nfs40_init_client.description`:

Description
-----------

Returns zero on success, or a negative errno if some error occurred.

.. _`nfs41_init_client`:

nfs41_init_client
=================

.. c:function:: int nfs41_init_client(struct nfs_client *clp)

    nfs_client initialization tasks for NFSv4.1+ \ ``clp``\  - nfs_client to initialize

    :param struct nfs_client \*clp:
        *undescribed*

.. _`nfs41_init_client.description`:

Description
-----------

Returns zero on success, or a negative errno if some error occurred.

.. _`nfs4_init_client`:

nfs4_init_client
================

.. c:function:: struct nfs_client *nfs4_init_client(struct nfs_client *clp, const struct nfs_client_initdata *cl_init)

    Initialise an NFS4 client record

    :param struct nfs_client \*clp:
        nfs_client to initialise

    :param const struct nfs_client_initdata \*cl_init:
        *undescribed*

.. _`nfs4_init_client.description`:

Description
-----------

Returns pointer to an NFS client, or an ERR_PTR value.

.. _`nfs40_walk_client_list`:

nfs40_walk_client_list
======================

.. c:function:: int nfs40_walk_client_list(struct nfs_client *new, struct nfs_client **result, struct rpc_cred *cred)

    Find server that recognizes a client ID

    :param struct nfs_client \*new:
        nfs_client with client ID to test

    :param struct nfs_client \*\*result:
        OUT: found nfs_client, or new

    :param struct rpc_cred \*cred:
        credential to use for trunking test

.. _`nfs40_walk_client_list.description`:

Description
-----------

Returns zero, a negative errno, or a negative NFS4ERR status.
If zero is returned, an nfs_client pointer is planted in "result."

NB: \ :c:func:`nfs40_walk_client_list`\  relies on the new nfs_client being
the last nfs_client on the list.

.. _`nfs4_detect_session_trunking`:

nfs4_detect_session_trunking
============================

.. c:function:: int nfs4_detect_session_trunking(struct nfs_client *clp, struct nfs41_exchange_id_res *res, struct rpc_xprt *xprt)

    Checks for session trunking.

    :param struct nfs_client \*clp:
        original mount nfs_client

    :param struct nfs41_exchange_id_res \*res:
        result structure from an exchange_id using the original mount
        nfs_client with a new multi_addr transport

    :param struct rpc_xprt \*xprt:
        *undescribed*

.. _`nfs4_detect_session_trunking.description`:

Description
-----------

Called after a successful EXCHANGE_ID on a multi-addr connection.
Upon success, add the transport.

Returns zero on success, otherwise -EINVAL

.. _`nfs4_detect_session_trunking.note`:

Note
----

since the exchange_id for the new multi_addr transport uses the
same nfs_client from the original mount, the cl_owner_id is reused,
so eir_clientowner is the same.

.. _`nfs41_walk_client_list`:

nfs41_walk_client_list
======================

.. c:function:: int nfs41_walk_client_list(struct nfs_client *new, struct nfs_client **result, struct rpc_cred *cred)

    Find nfs_client that matches a client/server owner

    :param struct nfs_client \*new:
        nfs_client with client ID to test

    :param struct nfs_client \*\*result:
        OUT: found nfs_client, or new

    :param struct rpc_cred \*cred:
        credential to use for trunking test

.. _`nfs41_walk_client_list.description`:

Description
-----------

Returns zero, a negative errno, or a negative NFS4ERR status.
If zero is returned, an nfs_client pointer is planted in "result."

NB: \ :c:func:`nfs41_walk_client_list`\  relies on the new nfs_client being
the last nfs_client on the list.

.. _`nfs4_update_server`:

nfs4_update_server
==================

.. c:function:: int nfs4_update_server(struct nfs_server *server, const char *hostname, struct sockaddr *sap, size_t salen, struct net *net)

    Move an nfs_server to a different nfs_client

    :param struct nfs_server \*server:
        represents FSID to be moved

    :param const char \*hostname:
        new end-point's hostname

    :param struct sockaddr \*sap:
        new end-point's socket address

    :param size_t salen:
        size of "sap"

    :param struct net \*net:
        net namespace

.. _`nfs4_update_server.description`:

Description
-----------

The nfs_server must be quiescent before this function is invoked.
Either its session is drained (NFSv4.1+), or its transport is
plugged and drained (NFSv4.0).

Returns zero on success, or a negative errno value.

.. This file was automatic generated / don't edit.

