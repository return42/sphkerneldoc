.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/md/bcache/util.c

.. _`bch_hprint`:

bch_hprint
==========

.. c:function:: ssize_t bch_hprint(char *buf, int64_t v)

    formats \ ``v``\  to human readable string for sysfs.

    :param buf:
        the (at least 8 byte) buffer to format the result into.
    :type buf: char \*

    :param v:
        signed 64 bit integer
    :type v: int64_t

.. _`bch_hprint.description`:

Description
-----------

Returns the number of bytes used by format.

.. _`bch_next_delay`:

bch_next_delay
==============

.. c:function:: uint64_t bch_next_delay(struct bch_ratelimit *d, uint64_t done)

    update ratelimiting statistics and calculate next delay

    :param d:
        the struct bch_ratelimit to update
    :type d: struct bch_ratelimit \*

    :param done:
        the amount of work done, in arbitrary units
    :type done: uint64_t

.. _`bch_next_delay.description`:

Description
-----------

Increment \ ``d``\  by the amount of work done, and return how long to delay in
jiffies until the next time to do some work.

.. _`bch_bio_alloc_pages`:

bch_bio_alloc_pages
===================

.. c:function:: int bch_bio_alloc_pages(struct bio *bio, gfp_t gfp_mask)

    allocates a single page for each bvec in a bio

    :param bio:
        bio to allocate pages for
    :type bio: struct bio \*

    :param gfp_mask:
        flags for allocation
    :type gfp_mask: gfp_t

.. _`bch_bio_alloc_pages.description`:

Description
-----------

Allocates pages up to \ ``bio->bi_vcnt``\ .

Returns 0 on success, -ENOMEM on failure. On failure, any allocated pages are
freed.

.. This file was automatic generated / don't edit.

