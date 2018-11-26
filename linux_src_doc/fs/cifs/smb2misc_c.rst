.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/cifs/smb2misc.c

.. _`smb311_update_preauth_hash`:

smb311_update_preauth_hash
==========================

.. c:function:: int smb311_update_preauth_hash(struct cifs_ses *ses, struct kvec *iov, int nvec)

    update \ ``ses``\  hash with the packet data in \ ``iov``\ 

    :param ses:
        *undescribed*
    :type ses: struct cifs_ses \*

    :param iov:
        *undescribed*
    :type iov: struct kvec \*

    :param nvec:
        *undescribed*
    :type nvec: int

.. _`smb311_update_preauth_hash.description`:

Description
-----------

Assumes \ ``iov``\  does not contain the rfc1002 length and iov[0] has the
SMB2 header.

.. This file was automatic generated / don't edit.

