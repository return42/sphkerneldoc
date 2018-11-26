.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/client.c

.. _`nfs_init_client`:

nfs_init_client
===============

.. c:function:: struct nfs_client *nfs_init_client(struct nfs_client *clp, const struct nfs_client_initdata *cl_init)

    Initialise an NFS2 or NFS3 client

    :param clp:
        nfs_client to initialise
    :type clp: struct nfs_client \*

    :param cl_init:
        Initialisation parameters
    :type cl_init: const struct nfs_client_initdata \*

.. _`nfs_init_client.description`:

Description
-----------

Returns pointer to an NFS client, or an ERR_PTR value.

.. This file was automatic generated / don't edit.

