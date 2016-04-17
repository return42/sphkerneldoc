.. -*- coding: utf-8; mode: rst -*-

============
nfs4client.c
============


.. _`nfs4_find_ds_client`:

nfs4_find_ds_client
===================

.. c:function:: struct nfs4_ds_server *nfs4_find_ds_client (struct nfs_client *ds_clp, rpc_authflavor_t flavor)

    :param struct nfs_client \*ds_clp:

        *undescribed*

    :param rpc_authflavor_t flavor:

        *undescribed*



.. _`nfs4_find_or_create_ds_client`:

nfs4_find_or_create_ds_client
=============================

.. c:function:: struct rpc_clnt *nfs4_find_or_create_ds_client (struct nfs_client *ds_clp, struct inode *inode)

    :param struct nfs_client \*ds_clp:

        *undescribed*

    :param struct inode \*inode:

        *undescribed*



.. _`nfs4_find_or_create_ds_client.description`:

Description
-----------

in the nfs_client cl_ds_clients list.



.. _`nfs40_init_client`:

nfs40_init_client
=================

.. c:function:: int nfs40_init_client (struct nfs_client *clp)

    nfs_client initialization tasks for NFSv4.0 @clp - nfs_client to initialize

    :param struct nfs_client \*clp:

        *undescribed*



.. _`nfs40_init_client.description`:

Description
-----------


Returns zero on success, or a negative errno if some error occurred.



.. _`nfs41_init_client`:

nfs41_init_client
=================

.. c:function:: int nfs41_init_client (struct nfs_client *clp)

    nfs_client initialization tasks for NFSv4.1+ @clp - nfs_client to initialize

    :param struct nfs_client \*clp:

        *undescribed*



.. _`nfs41_init_client.description`:

Description
-----------


Returns zero on success, or a negative errno if some error occurred.



.. _`nfs4_init_client`:

nfs4_init_client
================

.. c:function:: struct nfs_client *nfs4_init_client (struct nfs_client *clp, const struct rpc_timeout *timeparms, const char *ip_addr)

    Initialise an NFS4 client record

    :param struct nfs_client \*clp:
        nfs_client to initialise

    :param const struct rpc_timeout \*timeparms:
        timeout parameters for underlying RPC transport

    :param const char \*ip_addr:
        callback IP address in presentation format



.. _`nfs4_init_client.description`:

Description
-----------

Returns pointer to an NFS client, or an ERR_PTR value.



.. _`nfs40_walk_client_list`:

nfs40_walk_client_list
======================

.. c:function:: int nfs40_walk_client_list (struct nfs_client *new, struct nfs_client **result, struct rpc_cred *cred)

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



.. _`nfs40_walk_client_list.nb`:

NB
--

:c:func:`nfs40_walk_client_list` relies on the new nfs_client being
the last nfs_client on the list.



.. _`nfs41_walk_client_list`:

nfs41_walk_client_list
======================

.. c:function:: int nfs41_walk_client_list (struct nfs_client *new, struct nfs_client **result, struct rpc_cred *cred)

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



.. _`nfs41_walk_client_list.nb`:

NB
--

:c:func:`nfs41_walk_client_list` relies on the new nfs_client being
the last nfs_client on the list.



.. _`nfs4_update_server`:

nfs4_update_server
==================

.. c:function:: int nfs4_update_server (struct nfs_server *server, const char *hostname, struct sockaddr *sap, size_t salen, struct net *net)

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

