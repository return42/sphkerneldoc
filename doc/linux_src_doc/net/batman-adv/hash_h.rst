.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/hash.h

.. _`batadv_hash_add`:

batadv_hash_add
===============

.. c:function:: int batadv_hash_add(struct batadv_hashtable *hash, batadv_hashdata_compare_cb compare, batadv_hashdata_choose_cb choose, const void *data, struct hlist_node *data_node)

    adds data to the hashtable

    :param struct batadv_hashtable \*hash:
        storage hash table

    :param batadv_hashdata_compare_cb compare:
        callback to determine if 2 hash elements are identical

    :param batadv_hashdata_choose_cb choose:
        callback calculating the hash index

    :param const void \*data:
        data passed to the aforementioned callbacks as argument

    :param struct hlist_node \*data_node:
        to be added element

.. _`batadv_hash_add.return`:

Return
------

0 on success, 1 if the element already is in the hash
and -1 on error.

.. This file was automatic generated / don't edit.

