.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/integrity/evm/evm_main.c

.. _`evm_verifyxattr`:

evm_verifyxattr
===============

.. c:function:: enum integrity_status evm_verifyxattr(struct dentry *dentry, const char *xattr_name, void *xattr_value, size_t xattr_value_len, struct integrity_iint_cache *iint)

    verify the integrity of the requested xattr

    :param dentry:
        object of the verify xattr
    :type dentry: struct dentry \*

    :param xattr_name:
        requested xattr
    :type xattr_name: const char \*

    :param xattr_value:
        requested xattr value
    :type xattr_value: void \*

    :param xattr_value_len:
        requested xattr value length
    :type xattr_value_len: size_t

    :param iint:
        *undescribed*
    :type iint: struct integrity_iint_cache \*

.. _`evm_verifyxattr.description`:

Description
-----------

Calculate the HMAC for the given dentry and verify it against the stored
security.evm xattr. For performance, use the xattr value and length
previously retrieved to calculate the HMAC.

Returns the xattr integrity status.

This function requires the caller to lock the inode's i_mutex before it
is executed.

.. _`evm_inode_setxattr`:

evm_inode_setxattr
==================

.. c:function:: int evm_inode_setxattr(struct dentry *dentry, const char *xattr_name, const void *xattr_value, size_t xattr_value_len)

    protect the EVM extended attribute

    :param dentry:
        pointer to the affected dentry
    :type dentry: struct dentry \*

    :param xattr_name:
        pointer to the affected extended attribute name
    :type xattr_name: const char \*

    :param xattr_value:
        pointer to the new extended attribute value
    :type xattr_value: const void \*

    :param xattr_value_len:
        pointer to the new extended attribute value length
    :type xattr_value_len: size_t

.. _`evm_inode_setxattr.description`:

Description
-----------

Before allowing the 'security.evm' protected xattr to be updated,
verify the existing value is valid.  As only the kernel should have
access to the EVM encrypted key needed to calculate the HMAC, prevent
userspace from writing HMAC value.  Writing 'security.evm' requires
requires CAP_SYS_ADMIN privileges.

.. _`evm_inode_removexattr`:

evm_inode_removexattr
=====================

.. c:function:: int evm_inode_removexattr(struct dentry *dentry, const char *xattr_name)

    protect the EVM extended attribute

    :param dentry:
        pointer to the affected dentry
    :type dentry: struct dentry \*

    :param xattr_name:
        pointer to the affected extended attribute name
    :type xattr_name: const char \*

.. _`evm_inode_removexattr.description`:

Description
-----------

Removing 'security.evm' requires CAP_SYS_ADMIN privileges and that
the current value is valid.

.. _`evm_inode_post_setxattr`:

evm_inode_post_setxattr
=======================

.. c:function:: void evm_inode_post_setxattr(struct dentry *dentry, const char *xattr_name, const void *xattr_value, size_t xattr_value_len)

    update 'security.evm' to reflect the changes

    :param dentry:
        pointer to the affected dentry
    :type dentry: struct dentry \*

    :param xattr_name:
        pointer to the affected extended attribute name
    :type xattr_name: const char \*

    :param xattr_value:
        pointer to the new extended attribute value
    :type xattr_value: const void \*

    :param xattr_value_len:
        pointer to the new extended attribute value length
    :type xattr_value_len: size_t

.. _`evm_inode_post_setxattr.description`:

Description
-----------

Update the HMAC stored in 'security.evm' to reflect the change.

No need to take the i_mutex lock here, as this function is called from
\__vfs_setxattr_noperm().  The caller of which has taken the inode's
i_mutex lock.

.. _`evm_inode_post_removexattr`:

evm_inode_post_removexattr
==========================

.. c:function:: void evm_inode_post_removexattr(struct dentry *dentry, const char *xattr_name)

    update 'security.evm' after removing the xattr

    :param dentry:
        pointer to the affected dentry
    :type dentry: struct dentry \*

    :param xattr_name:
        pointer to the affected extended attribute name
    :type xattr_name: const char \*

.. _`evm_inode_post_removexattr.description`:

Description
-----------

Update the HMAC stored in 'security.evm' to reflect removal of the xattr.

No need to take the i_mutex lock here, as this function is called from
\ :c:func:`vfs_removexattr`\  which takes the i_mutex.

.. _`evm_inode_setattr`:

evm_inode_setattr
=================

.. c:function:: int evm_inode_setattr(struct dentry *dentry, struct iattr *attr)

    prevent updating an invalid EVM extended attribute

    :param dentry:
        pointer to the affected dentry
    :type dentry: struct dentry \*

    :param attr:
        *undescribed*
    :type attr: struct iattr \*

.. _`evm_inode_setattr.description`:

Description
-----------

Permit update of file attributes when files have a valid EVM signature,
except in the case of them having an immutable portable signature.

.. _`evm_inode_post_setattr`:

evm_inode_post_setattr
======================

.. c:function:: void evm_inode_post_setattr(struct dentry *dentry, int ia_valid)

    update 'security.evm' after modifying metadata

    :param dentry:
        pointer to the affected dentry
    :type dentry: struct dentry \*

    :param ia_valid:
        for the UID and GID status
    :type ia_valid: int

.. _`evm_inode_post_setattr.description`:

Description
-----------

For now, update the HMAC stored in 'security.evm' to reflect UID/GID
changes.

This function is called from \ :c:func:`notify_change`\ , which expects the caller
to lock the inode's i_mutex.

.. This file was automatic generated / don't edit.

