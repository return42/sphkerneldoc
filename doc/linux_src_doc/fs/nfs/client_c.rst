.. -*- coding: utf-8; mode: rst -*-

========
client.c
========


.. _`nfs_init_client`:

nfs_init_client
===============

.. c:function:: struct nfs_client *nfs_init_client (struct nfs_client *clp, const struct rpc_timeout *timeparms, const char *ip_addr)

    Initialise an NFS2 or NFS3 client

    :param struct nfs_client \*clp:
        nfs_client to initialise

    :param const struct rpc_timeout \*timeparms:
        timeout parameters for underlying RPC transport

    :param const char \*ip_addr:
        IP presentation address (not used)



.. _`nfs_init_client.description`:

Description
-----------

Returns pointer to an NFS client, or an ERR_PTR value.

