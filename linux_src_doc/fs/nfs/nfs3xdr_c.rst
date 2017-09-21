.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/nfs3xdr.c

.. _`nfs3_decode_dirent`:

nfs3_decode_dirent
==================

.. c:function:: int nfs3_decode_dirent(struct xdr_stream *xdr, struct nfs_entry *entry, bool plus)

    Decode a single NFSv3 directory entry stored in the local page cache

    :param struct xdr_stream \*xdr:
        XDR stream where entry resides

    :param struct nfs_entry \*entry:
        buffer to fill in with entry data

    :param bool plus:
        boolean indicating whether this should be a readdirplus entry

.. _`nfs3_decode_dirent.description`:

Description
-----------

Returns zero if successful, otherwise a negative errno value is
returned.

This function is not invoked during READDIR reply decoding, but
rather whenever an application invokes the getdents(2) system call
on a directory already in our cache.

3.3.16  entry3

struct entry3 {
fileid3         fileid;
filename3       name;
cookie3         cookie;
fhandle3        filehandle;
post_op_attr3   attributes;
entry3          \*nextentry;
};

3.3.17  entryplus3
struct entryplus3 {
fileid3         fileid;
filename3       name;
cookie3         cookie;
post_op_attr    name_attributes;
post_op_fh3     name_handle;
entryplus3      \*nextentry;
};

.. _`nfs3_stat_to_errno`:

nfs3_stat_to_errno
==================

.. c:function:: int nfs3_stat_to_errno(enum nfs_stat status)

    convert an NFS status code to a local errno

    :param enum nfs_stat status:
        NFS status code to convert

.. _`nfs3_stat_to_errno.description`:

Description
-----------

Returns a local errno value, or -EIO if the NFS status code is
not recognized.  This function is used jointly by NFSv2 and NFSv3.

.. This file was automatic generated / don't edit.

