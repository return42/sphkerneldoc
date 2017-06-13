.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/keys/keyring.c

.. _`restrict_link_reject`:

restrict_link_reject
====================

.. c:function:: int restrict_link_reject(struct key *keyring, const struct key_type *type, const union key_payload *payload, struct key *restriction_key)

    Give -EPERM to restrict link

    :param struct key \*keyring:
        The keyring being added to.

    :param const struct key_type \*type:
        The type of key being added.

    :param const union key_payload \*payload:
        The payload of the key intended to be added.

    :param struct key \*restriction_key:
        *undescribed*

.. _`restrict_link_reject.description`:

Description
-----------

Reject the addition of any links to a keyring.  It can be overridden by
passing KEY_ALLOC_BYPASS_RESTRICTION to \ :c:func:`key_instantiate_and_link`\  when
adding a key to a keyring.

This is meant to be stored in a key_restriction structure which is passed
in the restrict_link parameter to \ :c:func:`keyring_alloc`\ .

.. _`keyring_search_aux`:

keyring_search_aux
==================

.. c:function:: key_ref_t keyring_search_aux(key_ref_t keyring_ref, struct keyring_search_context *ctx)

    Search a keyring tree for a key matching some criteria

    :param key_ref_t keyring_ref:
        A pointer to the keyring with possession indicator.

    :param struct keyring_search_context \*ctx:
        The keyring search context.

.. _`keyring_search_aux.description`:

Description
-----------

Search the supplied keyring tree for a key that matches the criteria given.
The root keyring and any linked keyrings must grant Search permission to the
caller to be searchable and keys can only be found if they too grant Search
to the caller. The possession flag on the root keyring pointer controls use
of the possessor bits in permissions checking of the entire tree.  In
addition, the LSM gets to forbid keyring searches and key matches.

The search is performed as a breadth-then-depth search up to the prescribed
limit (KEYRING_SEARCH_MAX_DEPTH).

Keys are matched to the type provided and are then filtered by the match
function, which is given the description to use in any way it sees fit.  The
match function may use any attributes of a key that it wishes to to
determine the match.  Normally the match function from the key type would be
used.

RCU can be used to prevent the keyring key lists from disappearing without
the need to take lots of locks.

Returns a pointer to the found key and increments the key usage count if
successful; -EAGAIN if no matching keys were found, or if expired or revoked
keys were found; -ENOKEY if only negative keys were found; -ENOTDIR if the
specified keyring wasn't a keyring.

In the case of a successful return, the possession attribute from
\ ``keyring_ref``\  is propagated to the returned key reference.

.. _`keyring_search`:

keyring_search
==============

.. c:function:: key_ref_t keyring_search(key_ref_t keyring, struct key_type *type, const char *description)

    Search the supplied keyring tree for a matching key

    :param key_ref_t keyring:
        The root of the keyring tree to be searched.

    :param struct key_type \*type:
        The type of keyring we want to find.

    :param const char \*description:
        The name of the keyring we want to find.

.. _`keyring_search.description`:

Description
-----------

As \ :c:func:`keyring_search_aux`\  above, but using the current task's credentials and
type's default matching function and preferred search method.

.. _`keyring_restrict`:

keyring_restrict
================

.. c:function:: int keyring_restrict(key_ref_t keyring_ref, const char *type, const char *restriction)

    Look up and apply a restriction to a keyring

    :param key_ref_t keyring_ref:
        *undescribed*

    :param const char \*type:
        *undescribed*

    :param const char \*restriction:
        The restriction options to apply to the keyring

.. _`key_link`:

key_link
========

.. c:function:: int key_link(struct key *keyring, struct key *key)

    Link a key to a keyring

    :param struct key \*keyring:
        The keyring to make the link in.

    :param struct key \*key:
        The key to link to.

.. _`key_link.description`:

Description
-----------

Make a link in a keyring to a key, such that the keyring holds a reference
on that key and the key can potentially be found by searching that keyring.

This function will write-lock the keyring's semaphore and will consume some
of the user's key data quota to hold the link.

Returns 0 if successful, -ENOTDIR if the keyring isn't a keyring,
-EKEYREVOKED if the keyring has been revoked, -ENFILE if the keyring is
full, -EDQUOT if there is insufficient key data quota remaining to add
another link or -ENOMEM if there's insufficient memory.

It is assumed that the caller has checked that it is permitted for a link to
be made (the keyring should have Write permission and the key Link
permission).

.. _`key_unlink`:

key_unlink
==========

.. c:function:: int key_unlink(struct key *keyring, struct key *key)

    Unlink the first link to a key from a keyring.

    :param struct key \*keyring:
        The keyring to remove the link from.

    :param struct key \*key:
        The key the link is to.

.. _`key_unlink.description`:

Description
-----------

Remove a link from a keyring to a key.

This function will write-lock the keyring's semaphore.

Returns 0 if successful, -ENOTDIR if the keyring isn't a keyring, -ENOENT if
the key isn't linked to by the keyring or -ENOMEM if there's insufficient
memory.

It is assumed that the caller has checked that it is permitted for a link to
be removed (the keyring should have Write permission; no permissions are
required on the key).

.. _`keyring_clear`:

keyring_clear
=============

.. c:function:: int keyring_clear(struct key *keyring)

    Clear a keyring

    :param struct key \*keyring:
        The keyring to clear.

.. _`keyring_clear.description`:

Description
-----------

Clear the contents of the specified keyring.

Returns 0 if successful or -ENOTDIR if the keyring isn't a keyring.

.. This file was automatic generated / don't edit.

