.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/nfs2xdr.c

.. _`nfs2_decode_dirent`:

nfs2_decode_dirent
==================

.. c:function:: int nfs2_decode_dirent(struct xdr_stream *xdr, struct nfs_entry *entry, bool plus)

    Decode a single NFSv2 directory entry stored in the local page cache.

    :param xdr:
        XDR stream where entry resides
    :type xdr: struct xdr_stream \*

    :param entry:
        buffer to fill in with entry data
    :type entry: struct nfs_entry \*

    :param plus:
        boolean indicating whether this should be a readdirplus entry
    :type plus: bool

.. _`nfs2_decode_dirent.description`:

Description
-----------

Returns zero if successful, otherwise a negative errno value is
returned.

This function is not invoked during READDIR reply decoding, but
rather whenever an application invokes the getdents(2) system call
on a directory already in our cache.

2.2.17.  entry

struct entry {
unsigned        fileid;
filename        name;
nfscookie       cookie;
entry           \*nextentry;
};

.. _`nfs_stat_to_errno`:

nfs_stat_to_errno
=================

.. c:function:: int nfs_stat_to_errno(enum nfs_stat status)

    convert an NFS status code to a local errno

    :param status:
        NFS status code to convert
    :type status: enum nfs_stat

.. _`nfs_stat_to_errno.description`:

Description
-----------

Returns a local errno value, or -EIO if the NFS status code is
not recognized.  This function is used jointly by NFSv2 and NFSv3.

.. This file was automatic generated / don't edit.

