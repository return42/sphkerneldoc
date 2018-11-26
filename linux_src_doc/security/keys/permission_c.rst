.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/keys/permission.c

.. _`key_task_permission`:

key_task_permission
===================

.. c:function:: int key_task_permission(const key_ref_t key_ref, const struct cred *cred, unsigned perm)

    Check a key can be used

    :param key_ref:
        The key to check.
    :type key_ref: const key_ref_t

    :param cred:
        The credentials to use.
    :type cred: const struct cred \*

    :param perm:
        The permissions to check for.
    :type perm: unsigned

.. _`key_task_permission.description`:

Description
-----------

Check to see whether permission is granted to use a key in the desired way,
but permit the security modules to override.

The caller must hold either a ref on cred or must hold the RCU readlock.

Returns 0 if successful, -EACCES if access is denied based on the
permissions bits or the LSM check.

.. _`key_validate`:

key_validate
============

.. c:function:: int key_validate(const struct key *key)

    Validate a key.

    :param key:
        The key to be validated.
    :type key: const struct key \*

.. _`key_validate.description`:

Description
-----------

Check that a key is valid, returning 0 if the key is okay, -ENOKEY if the
key is invalidated, -EKEYREVOKED if the key's type has been removed or if
the key has been revoked or -EKEYEXPIRED if the key has expired.

.. This file was automatic generated / don't edit.

