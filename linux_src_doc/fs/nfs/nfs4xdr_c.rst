.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/nfs4xdr.c

.. _`nfs4_decode_dirent`:

nfs4_decode_dirent
==================

.. c:function:: int nfs4_decode_dirent(struct xdr_stream *xdr, struct nfs_entry *entry, bool plus)

    Decode a single NFSv4 directory entry stored in the local page cache.

    :param xdr:
        XDR stream where entry resides
    :type xdr: struct xdr_stream \*

    :param entry:
        buffer to fill in with entry data
    :type entry: struct nfs_entry \*

    :param plus:
        boolean indicating whether this should be a readdirplus entry
    :type plus: bool

.. _`nfs4_decode_dirent.description`:

Description
-----------

Returns zero if successful, otherwise a negative errno value is
returned.

This function is not invoked during READDIR reply decoding, but
rather whenever an application invokes the getdents(2) system call
on a directory already in our cache.

.. This file was automatic generated / don't edit.

