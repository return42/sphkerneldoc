.. -*- coding: utf-8; mode: rst -*-

=============
request_key.c
=============


.. _`complete_request_key`:

complete_request_key
====================

.. c:function:: void complete_request_key (struct key_construction *cons, int error)

    Complete the construction of a key.

    :param struct key_construction \*cons:
        The key construction record.

    :param int error:
        The success or failute of the construction.



.. _`complete_request_key.description`:

Description
-----------

Complete the attempt to construct a key.  The key will be negated
if an error is indicated.  The authorisation key will be revoked
unconditionally.



.. _`request_key_and_link`:

request_key_and_link
====================

.. c:function:: struct key *request_key_and_link (struct key_type *type, const char *description, const void *callout_info, size_t callout_len, void *aux, struct key *dest_keyring, unsigned long flags)

    Request a key and cache it in a keyring.

    :param struct key_type \*type:
        The type of key we want.

    :param const char \*description:
        The searchable description of the key.

    :param const void \*callout_info:
        The data to pass to the instantiation upcall (or NULL).

    :param size_t callout_len:
        The length of callout_info.

    :param void \*aux:
        Auxiliary data for the upcall.

    :param struct key \*dest_keyring:
        Where to cache the key.

    :param unsigned long flags:
        Flags to :c:func:`key_alloc`.



.. _`request_key_and_link.description`:

Description
-----------

A key matching the specified criteria is searched for in the process's
keyrings and returned with its usage count incremented if found.  Otherwise,
if callout_info is not NULL, a key will be allocated and some service
(probably in userspace) will be asked to instantiate it.

If successfully found or created, the key will be linked to the destination
keyring if one is provided.

Returns a pointer to the key if successful; -EACCES, -ENOKEY, -EKEYREVOKED
or -EKEYEXPIRED if an inaccessible, negative, revoked or expired key was
found; -ENOKEY if no key was found and no ``callout_info`` was given; -EDQUOT
if insufficient key quota was available to create a new key; or -ENOMEM if
insufficient memory was available.

If the returned key was created, then it may still be under construction,
and :c:func:`wait_for_key_construction` should be used to wait for that to complete.



.. _`wait_for_key_construction`:

wait_for_key_construction
=========================

.. c:function:: int wait_for_key_construction (struct key *key, bool intr)

    Wait for construction of a key to complete

    :param struct key \*key:
        The key being waited for.

    :param bool intr:
        Whether to wait interruptibly.



.. _`wait_for_key_construction.description`:

Description
-----------

Wait for a key to finish being constructed.

Returns 0 if successful; -ERESTARTSYS if the wait was interrupted; -ENOKEY
if the key was negated; or -EKEYREVOKED or -EKEYEXPIRED if the key was
revoked or expired.



.. _`request_key`:

request_key
===========

.. c:function:: struct key *request_key (struct key_type *type, const char *description, const char *callout_info)

    Request a key and wait for construction

    :param struct key_type \*type:
        Type of key.

    :param const char \*description:
        The searchable description of the key.

    :param const char \*callout_info:
        The data to pass to the instantiation upcall (or NULL).



.. _`request_key.description`:

Description
-----------

As for :c:func:`request_key_and_link` except that it does not add the returned key
to a keyring if found, new keys are always allocated in the user's quota,
the callout_info must be a NUL-terminated string and no auxiliary data can
be passed.

Furthermore, it then works as :c:func:`wait_for_key_construction` to wait for the
completion of keys undergoing construction with a non-interruptible wait.



.. _`request_key_with_auxdata`:

request_key_with_auxdata
========================

.. c:function:: struct key *request_key_with_auxdata (struct key_type *type, const char *description, const void *callout_info, size_t callout_len, void *aux)

    Request a key with auxiliary data for the upcaller

    :param struct key_type \*type:
        The type of key we want.

    :param const char \*description:
        The searchable description of the key.

    :param const void \*callout_info:
        The data to pass to the instantiation upcall (or NULL).

    :param size_t callout_len:
        The length of callout_info.

    :param void \*aux:
        Auxiliary data for the upcall.



.. _`request_key_with_auxdata.description`:

Description
-----------

As for :c:func:`request_key_and_link` except that it does not add the returned key
to a keyring if found and new keys are always allocated in the user's quota.

Furthermore, it then works as :c:func:`wait_for_key_construction` to wait for the
completion of keys undergoing construction with a non-interruptible wait.

