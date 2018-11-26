.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ceph/crush/crush.c

.. _`crush_get_bucket_item_weight`:

crush_get_bucket_item_weight
============================

.. c:function:: int crush_get_bucket_item_weight(const struct crush_bucket *b, int p)

    Get weight of an item in given bucket

    :param b:
        bucket pointer
    :type b: const struct crush_bucket \*

    :param p:
        item index in bucket
    :type p: int

.. _`crush_destroy`:

crush_destroy
=============

.. c:function:: void crush_destroy(struct crush_map *map)

    Destroy a crush_map

    :param map:
        crush_map pointer
    :type map: struct crush_map \*

.. This file was automatic generated / don't edit.

