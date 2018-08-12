.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/md/bcache/request.c

.. _`bch_data_insert`:

bch_data_insert
===============

.. c:function:: void bch_data_insert(struct closure *cl)

    stick some data in the cache

    :param struct closure \*cl:
        closure pointer.

.. _`bch_data_insert.description`:

Description
-----------

This is the starting point for any data to end up in a cache device; it could
be from a normal write, or a writeback write, or a write to a flash only
volume - it's also used by the moving garbage collector to compact data in
mostly empty buckets.

It first writes the data to the cache, creating a list of keys to be inserted
(if the data had to be fragmented there will be multiple keys); after the
data is written it calls bch_journal, and after the keys have been added to
the next journal write they're inserted into the btree.

It inserts the data in s->cache_bio; bi_sector is used for the key offset,
and op->inode is used for the key inode.

If s->bypass is true, instead of inserting the data it invalidates the
region of the cache represented by s->cache_bio and op->inode.

.. This file was automatic generated / don't edit.

