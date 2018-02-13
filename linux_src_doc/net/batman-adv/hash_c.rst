.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/hash.c

.. _`batadv_hash_destroy`:

batadv_hash_destroy
===================

.. c:function:: void batadv_hash_destroy(struct batadv_hashtable *hash)

    Free only the hashtable and the hash itself

    :param struct batadv_hashtable \*hash:
        hash object to destroy

.. _`batadv_hash_new`:

batadv_hash_new
===============

.. c:function:: struct batadv_hashtable *batadv_hash_new(u32 size)

    Allocates and clears the hashtable

    :param u32 size:
        number of hash buckets to allocate

.. _`batadv_hash_new.return`:

Return
------

newly allocated hashtable, NULL on errors

.. _`batadv_hash_set_lock_class`:

batadv_hash_set_lock_class
==========================

.. c:function:: void batadv_hash_set_lock_class(struct batadv_hashtable *hash, struct lock_class_key *key)

    Set specific lockdep class for hash spinlocks

    :param struct batadv_hashtable \*hash:
        hash object to modify

    :param struct lock_class_key \*key:
        lockdep class key address

.. This file was automatic generated / don't edit.

