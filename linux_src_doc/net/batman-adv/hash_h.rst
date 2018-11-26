.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/hash.h

.. _`batadv_hashtable`:

struct batadv_hashtable
=======================

.. c:type:: struct batadv_hashtable

    Wrapper of simple hlist based hashtable

.. _`batadv_hashtable.definition`:

Definition
----------

.. code-block:: c

    struct batadv_hashtable {
        struct hlist_head *table;
        spinlock_t *list_locks;
        u32 size;
    }

.. _`batadv_hashtable.members`:

Members
-------

table
    the hashtable itself with the buckets

list_locks
    spinlock for each hash list entry

size
    size of hashtable

.. _`batadv_hash_add`:

batadv_hash_add
===============

.. c:function:: int batadv_hash_add(struct batadv_hashtable *hash, batadv_hashdata_compare_cb compare, batadv_hashdata_choose_cb choose, const void *data, struct hlist_node *data_node)

    adds data to the hashtable

    :param hash:
        storage hash table
    :type hash: struct batadv_hashtable \*

    :param compare:
        callback to determine if 2 hash elements are identical
    :type compare: batadv_hashdata_compare_cb

    :param choose:
        callback calculating the hash index
    :type choose: batadv_hashdata_choose_cb

    :param data:
        data passed to the aforementioned callbacks as argument
    :type data: const void \*

    :param data_node:
        to be added element
    :type data_node: struct hlist_node \*

.. _`batadv_hash_add.return`:

Return
------

0 on success, 1 if the element already is in the hash
and -1 on error.

.. _`batadv_hash_remove`:

batadv_hash_remove
==================

.. c:function:: void *batadv_hash_remove(struct batadv_hashtable *hash, batadv_hashdata_compare_cb compare, batadv_hashdata_choose_cb choose, void *data)

    Removes data from hash, if found

    :param hash:
        hash table
    :type hash: struct batadv_hashtable \*

    :param compare:
        callback to determine if 2 hash elements are identical
    :type compare: batadv_hashdata_compare_cb

    :param choose:
        callback calculating the hash index
    :type choose: batadv_hashdata_choose_cb

    :param data:
        data passed to the aforementioned callbacks as argument
    :type data: void \*

.. _`batadv_hash_remove.description`:

Description
-----------

ata could be the structure you use with  just the key filled, we just need
the key for comparing.

.. _`batadv_hash_remove.return`:

Return
------

returns pointer do data on success, so you can remove the used
structure yourself, or NULL on error

.. This file was automatic generated / don't edit.

