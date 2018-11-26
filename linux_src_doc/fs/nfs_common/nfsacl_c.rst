.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs_common/nfsacl.c

.. _`nfsacl_encode`:

nfsacl_encode
=============

.. c:function:: int nfsacl_encode(struct xdr_buf *buf, unsigned int base, struct inode *inode, struct posix_acl *acl, int encode_entries, int typeflag)

    Encode an NFSv3 ACL

    :param buf:
        destination xdr_buf to contain XDR encoded ACL
    :type buf: struct xdr_buf \*

    :param base:
        byte offset in xdr_buf where XDR'd ACL begins
    :type base: unsigned int

    :param inode:
        inode of file whose ACL this is
    :type inode: struct inode \*

    :param acl:
        posix_acl to encode
    :type acl: struct posix_acl \*

    :param encode_entries:
        whether to encode ACEs as well
    :type encode_entries: int

    :param typeflag:
        ACL type: NFS_ACL_DEFAULT or zero
    :type typeflag: int

.. _`nfsacl_encode.description`:

Description
-----------

Returns size of encoded ACL in bytes or a negative errno value.

.. _`nfsacl_decode`:

nfsacl_decode
=============

.. c:function:: int nfsacl_decode(struct xdr_buf *buf, unsigned int base, unsigned int *aclcnt, struct posix_acl **pacl)

    Decode an NFSv3 ACL

    :param buf:
        xdr_buf containing XDR'd ACL data to decode
    :type buf: struct xdr_buf \*

    :param base:
        byte offset in xdr_buf where XDR'd ACL begins
    :type base: unsigned int

    :param aclcnt:
        count of ACEs in decoded posix_acl
    :type aclcnt: unsigned int \*

    :param pacl:
        buffer in which to place decoded posix_acl
    :type pacl: struct posix_acl \*\*

.. _`nfsacl_decode.description`:

Description
-----------

Returns the length of the decoded ACL in bytes, or a negative errno value.

.. This file was automatic generated / don't edit.

