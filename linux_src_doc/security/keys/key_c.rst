.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/keys/key.c

.. _`key_alloc`:

key_alloc
=========

.. c:function:: struct key *key_alloc(struct key_type *type, const char *desc, kuid_t uid, kgid_t gid, const struct cred *cred, key_perm_t perm, unsigned long flags, struct key_restriction *restrict_link)

    Allocate a key of the specified type.

    :param type:
        The type of key to allocate.
    :type type: struct key_type \*

    :param desc:
        The key description to allow the key to be searched out.
    :type desc: const char \*

    :param uid:
        The owner of the new key.
    :type uid: kuid_t

    :param gid:
        The group ID for the new key's group permissions.
    :type gid: kgid_t

    :param cred:
        The credentials specifying UID namespace.
    :type cred: const struct cred \*

    :param perm:
        The permissions mask of the new key.
    :type perm: key_perm_t

    :param flags:
        Flags specifying quota properties.
    :type flags: unsigned long

    :param restrict_link:
        Optional link restriction for new keyrings.
    :type restrict_link: struct key_restriction \*

.. _`key_alloc.description`:

Description
-----------

Allocate a key of the specified type with the attributes given.  The key is
returned in an uninstantiated state and the caller needs to instantiate the
key before returning.

The restrict_link structure (if not NULL) will be freed when the
keyring is destroyed, so it must be dynamically allocated.

The user's key count quota is updated to reflect the creation of the key and
the user's key data quota has the default for the key type reserved.  The
instantiation function should amend this as necessary.  If insufficient
quota is available, -EDQUOT will be returned.

The LSM security modules can prevent a key being created, in which case
-EACCES will be returned.

Returns a pointer to the new key if successful and an error code otherwise.

Note that the caller needs to ensure the key type isn't uninstantiated.
Internally this can be done by locking key_types_sem.  Externally, this can
be done by either never unregistering the key type, or making sure
\ :c:func:`key_alloc`\  calls don't race with module unloading.

.. _`key_payload_reserve`:

key_payload_reserve
===================

.. c:function:: int key_payload_reserve(struct key *key, size_t datalen)

    Adjust data quota reservation for the key's payload

    :param key:
        The key to make the reservation for.
    :type key: struct key \*

    :param datalen:
        The amount of data payload the caller now wants.
    :type datalen: size_t

.. _`key_payload_reserve.description`:

Description
-----------

Adjust the amount of the owning user's key data quota that a key reserves.
If the amount is increased, then -EDQUOT may be returned if there isn't
enough free quota available.

If successful, 0 is returned.

.. _`key_instantiate_and_link`:

key_instantiate_and_link
========================

.. c:function:: int key_instantiate_and_link(struct key *key, const void *data, size_t datalen, struct key *keyring, struct key *authkey)

    Instantiate a key and link it into the keyring.

    :param key:
        The key to instantiate.
    :type key: struct key \*

    :param data:
        The data to use to instantiate the keyring.
    :type data: const void \*

    :param datalen:
        The length of \ ``data``\ .
    :type datalen: size_t

    :param keyring:
        Keyring to create a link in on success (or NULL).
    :type keyring: struct key \*

    :param authkey:
        The authorisation token permitting instantiation.
    :type authkey: struct key \*

.. _`key_instantiate_and_link.description`:

Description
-----------

Instantiate a key that's in the uninstantiated state using the provided data
and, if successful, link it in to the destination keyring if one is
supplied.

If successful, 0 is returned, the authorisation token is revoked and anyone
waiting for the key is woken up.  If the key was already instantiated,
-EBUSY will be returned.

.. _`key_reject_and_link`:

key_reject_and_link
===================

.. c:function:: int key_reject_and_link(struct key *key, unsigned timeout, unsigned error, struct key *keyring, struct key *authkey)

    Negatively instantiate a key and link it into the keyring.

    :param key:
        The key to instantiate.
    :type key: struct key \*

    :param timeout:
        The timeout on the negative key.
    :type timeout: unsigned

    :param error:
        The error to return when the key is hit.
    :type error: unsigned

    :param keyring:
        Keyring to create a link in on success (or NULL).
    :type keyring: struct key \*

    :param authkey:
        The authorisation token permitting instantiation.
    :type authkey: struct key \*

.. _`key_reject_and_link.description`:

Description
-----------

Negatively instantiate a key that's in the uninstantiated state and, if
successful, set its timeout and stored error and link it in to the
destination keyring if one is supplied.  The key and any links to the key
will be automatically garbage collected after the timeout expires.

Negative keys are used to rate limit repeated \ :c:func:`request_key`\  calls by causing
them to return the stored error code (typically ENOKEY) until the negative
key expires.

If successful, 0 is returned, the authorisation token is revoked and anyone
waiting for the key is woken up.  If the key was already instantiated,
-EBUSY will be returned.

.. _`key_put`:

key_put
=======

.. c:function:: void key_put(struct key *key)

    Discard a reference to a key.

    :param key:
        The key to discard a reference from.
    :type key: struct key \*

.. _`key_put.description`:

Description
-----------

Discard a reference to a key, and when all the references are gone, we
schedule the cleanup task to come and pull it out of the tree in process
context at some later time.

.. _`key_create_or_update`:

key_create_or_update
====================

.. c:function:: key_ref_t key_create_or_update(key_ref_t keyring_ref, const char *type, const char *description, const void *payload, size_t plen, key_perm_t perm, unsigned long flags)

    Update or create and instantiate a key.

    :param keyring_ref:
        A pointer to the destination keyring with possession flag.
    :type keyring_ref: key_ref_t

    :param type:
        The type of key.
    :type type: const char \*

    :param description:
        The searchable description for the key.
    :type description: const char \*

    :param payload:
        The data to use to instantiate or update the key.
    :type payload: const void \*

    :param plen:
        The length of \ ``payload``\ .
    :type plen: size_t

    :param perm:
        The permissions mask for a new key.
    :type perm: key_perm_t

    :param flags:
        The quota flags for a new key.
    :type flags: unsigned long

.. _`key_create_or_update.description`:

Description
-----------

Search the destination keyring for a key of the same description and if one
is found, update it, otherwise create and instantiate a new one and create a
link to it from that keyring.

If perm is KEY_PERM_UNDEF then an appropriate key permissions mask will be
concocted.

Returns a pointer to the new key if successful, -ENODEV if the key type
wasn't available, -ENOTDIR if the keyring wasn't a keyring, -EACCES if the
caller isn't permitted to modify the keyring or the LSM did not permit
creation of the key.

On success, the possession flag from the keyring ref will be tacked on to
the key ref before it is returned.

.. _`key_update`:

key_update
==========

.. c:function:: int key_update(key_ref_t key_ref, const void *payload, size_t plen)

    Update a key's contents.

    :param key_ref:
        The pointer (plus possession flag) to the key.
    :type key_ref: key_ref_t

    :param payload:
        The data to be used to update the key.
    :type payload: const void \*

    :param plen:
        The length of \ ``payload``\ .
    :type plen: size_t

.. _`key_update.description`:

Description
-----------

Attempt to update the contents of a key with the given payload data.  The
caller must be granted Write permission on the key.  Negative keys can be
instantiated by this method.

Returns 0 on success, -EACCES if not permitted and -EOPNOTSUPP if the key
type does not support updating.  The key type may return other errors.

.. _`key_revoke`:

key_revoke
==========

.. c:function:: void key_revoke(struct key *key)

    Revoke a key.

    :param key:
        The key to be revoked.
    :type key: struct key \*

.. _`key_revoke.description`:

Description
-----------

Mark a key as being revoked and ask the type to free up its resources.  The
revocation timeout is set and the key and all its links will be
automatically garbage collected after key_gc_delay amount of time if they
are not manually dealt with first.

.. _`key_invalidate`:

key_invalidate
==============

.. c:function:: void key_invalidate(struct key *key)

    Invalidate a key.

    :param key:
        The key to be invalidated.
    :type key: struct key \*

.. _`key_invalidate.description`:

Description
-----------

Mark a key as being invalidated and have it cleaned up immediately.  The key
is ignored by all searches and other operations from this point.

.. _`generic_key_instantiate`:

generic_key_instantiate
=======================

.. c:function:: int generic_key_instantiate(struct key *key, struct key_preparsed_payload *prep)

    Simple instantiation of a key from preparsed data

    :param key:
        The key to be instantiated
    :type key: struct key \*

    :param prep:
        The preparsed data to load.
    :type prep: struct key_preparsed_payload \*

.. _`generic_key_instantiate.description`:

Description
-----------

Instantiate a key from preparsed data.  We assume we can just copy the data
in directly and clear the old pointers.

This can be pointed to directly by the key type instantiate op pointer.

.. _`register_key_type`:

register_key_type
=================

.. c:function:: int register_key_type(struct key_type *ktype)

    Register a type of key.

    :param ktype:
        The new key type.
    :type ktype: struct key_type \*

.. _`register_key_type.description`:

Description
-----------

Register a new key type.

Returns 0 on success or -EEXIST if a type of this name already exists.

.. _`unregister_key_type`:

unregister_key_type
===================

.. c:function:: void unregister_key_type(struct key_type *ktype)

    Unregister a type of key.

    :param ktype:
        The key type.
    :type ktype: struct key_type \*

.. _`unregister_key_type.description`:

Description
-----------

Unregister a key type and mark all the extant keys of this type as dead.
Those keys of this type are then destroyed to get rid of their payloads and
they and their links will be garbage collected as soon as possible.

.. This file was automatic generated / don't edit.

