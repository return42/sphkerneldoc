.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/flexfilelayout/flexfilelayoutdev.c

.. _`nfs4_ff_layout_prepare_ds`:

nfs4_ff_layout_prepare_ds
=========================

.. c:function:: struct nfs4_pnfs_ds *nfs4_ff_layout_prepare_ds(struct pnfs_layout_segment *lseg, u32 ds_idx, bool fail_return)

    prepare a DS connection for an RPC call

    :param lseg:
        the layout segment we're operating on
    :type lseg: struct pnfs_layout_segment \*

    :param ds_idx:
        index of the DS to use
    :type ds_idx: u32

    :param fail_return:
        return layout on connect failure?
    :type fail_return: bool

.. _`nfs4_ff_layout_prepare_ds.description`:

Description
-----------

Try to prepare a DS connection to accept an RPC call. This involves
selecting a mirror to use and connecting the client to it if it's not
already connected.

Since we only need a single functioning mirror to satisfy a read, we don't
want to return the layout if there is one. For writes though, any down
mirror should result in a LAYOUTRETURN. \ ``fail_return``\  is how we distinguish
between the two cases.

Returns a pointer to a connected DS object on success or NULL on failure.

.. _`nfs4_ff_find_or_create_ds_client`:

nfs4_ff_find_or_create_ds_client
================================

.. c:function:: struct rpc_clnt *nfs4_ff_find_or_create_ds_client(struct pnfs_layout_segment *lseg, u32 ds_idx, struct nfs_client *ds_clp, struct inode *inode)

    in the nfs_client cl_ds_clients list.

    :param lseg:
        *undescribed*
    :type lseg: struct pnfs_layout_segment \*

    :param ds_idx:
        *undescribed*
    :type ds_idx: u32

    :param ds_clp:
        *undescribed*
    :type ds_clp: struct nfs_client \*

    :param inode:
        *undescribed*
    :type inode: struct inode \*

.. This file was automatic generated / don't edit.

