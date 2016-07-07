.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/keys/key.c

.. _`key_alloc`:

key_alloc
=========

.. c:function:: struct key *key_alloc(struct key_type *type, const char *desc, kuid_t uid, kgid_t gid, const struct cred *cred, key_perm_t perm, unsigned long flags, int (*) restrict_link (struct key *, const struct key_type *, const union key_payload *)

    Allocate a key of the specified type.

    :param struct key_type \*type:
        The type of key to allocate.

    :param const char \*desc:
        The key description to allow the key to be searched out.

    :param kuid_t uid:
        The owner of the new key.

    :param kgid_t gid:
        The group ID for the new key's group permissions.

    :param const struct cred \*cred:
        The credentials specifying UID namespace.

    :param key_perm_t perm:
        The permissions mask of the new key.

    :param unsigned long flags:
        Flags specifying quota properties.

    :param (int (\*) restrict_link (struct key \*, const struct key_type \*, const union key_payload \*):
        Optional link restriction method for new keyrings.

.. _`key_alloc.description`:

Description
-----------

Allocate a key of the specified type with the attributes given.  The key is
returned in an uninstantiated state and the caller needs to instantiate the
key before returning.

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

    :param struct key \*key:
        The key to make the reservation for.

    :param size_t datalen:
        The amount of data payload the caller now wants.

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

    :param struct key \*key:
        The key to instantiate.

    :param const void \*data:
        The data to use to instantiate the keyring.

    :param size_t datalen:
        The length of \ ``data``\ .

    :param struct key \*keyring:
        Keyring to create a link in on success (or NULL).

    :param struct key \*authkey:
        The authorisation token permitting instantiation.

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

    :param struct key \*key:
        The key to instantiate.

    :param unsigned timeout:
        The timeout on the negative key.

    :param unsigned error:
        The error to return when the key is hit.

    :param struct key \*keyring:
        Keyring to create a link in on success (or NULL).

    :param struct key \*authkey:
        The authorisation token permitting instantiation.

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

    :param struct key \*key:
        The key to discard a reference from.

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

    :param key_ref_t keyring_ref:
        A pointer to the destination keyring with possession flag.

    :param const char \*type:
        The type of key.

    :param const char \*description:
        The searchable description for the key.

    :param const void \*payload:
        The data to use to instantiate or update the key.

    :param size_t plen:
        The length of \ ``payload``\ .

    :param key_perm_t perm:
        The permissions mask for a new key.

    :param unsigned long flags:
        The quota flags for a new key.

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

    :param key_ref_t key_ref:
        The pointer (plus possession flag) to the key.

    :param const void \*payload:
        The data to be used to update the key.

    :param size_t plen:
        The length of \ ``payload``\ .

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

    :param struct key \*key:
        The key to be revoked.

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

    :param struct key \*key:
        The key to be invalidated.

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

    :param struct key \*key:
        The key to be instantiated

    :param struct key_preparsed_payload \*prep:
        The preparsed data to load.

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

    :param struct key_type \*ktype:
        The new key type.

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

    :param struct key_type \*ktype:
        The key type.

.. _`unregister_key_type.description`:

Description
-----------

Unregister a key type and mark all the extant keys of this type as dead.
Those keys of this type are then destroyed to get rid of their payloads and
they and their links will be garbage collected as soon as possible.

.. This file was automatic generated / don't edit.

