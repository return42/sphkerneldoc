.. -*- coding: utf-8; mode: rst -*-

========
nfsacl.c
========


.. _`nfsacl_encode`:

nfsacl_encode
=============

.. c:function:: int nfsacl_encode (struct xdr_buf *buf, unsigned int base, struct inode *inode, struct posix_acl *acl, int encode_entries, int typeflag)

    Encode an NFSv3 ACL

    :param struct xdr_buf \*buf:
        destination xdr_buf to contain XDR encoded ACL

    :param unsigned int base:
        byte offset in xdr_buf where XDR'd ACL begins

    :param struct inode \*inode:
        inode of file whose ACL this is

    :param struct posix_acl \*acl:
        posix_acl to encode

    :param int encode_entries:
        whether to encode ACEs as well

    :param int typeflag:
        ACL type: NFS_ACL_DEFAULT or zero



.. _`nfsacl_encode.description`:

Description
-----------

Returns size of encoded ACL in bytes or a negative errno value.



.. _`nfsacl_decode`:

nfsacl_decode
=============

.. c:function:: int nfsacl_decode (struct xdr_buf *buf, unsigned int base, unsigned int *aclcnt, struct posix_acl **pacl)

    Decode an NFSv3 ACL

    :param struct xdr_buf \*buf:
        xdr_buf containing XDR'd ACL data to decode

    :param unsigned int base:
        byte offset in xdr_buf where XDR'd ACL begins

    :param unsigned int \*aclcnt:
        count of ACEs in decoded posix_acl

    :param struct posix_acl \*\*pacl:
        buffer in which to place decoded posix_acl



.. _`nfsacl_decode.description`:

Description
-----------

Returns the length of the decoded ACL in bytes, or a negative errno value.

