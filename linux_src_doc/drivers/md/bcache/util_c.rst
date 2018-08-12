.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/md/bcache/util.c

.. _`bch_hprint`:

bch_hprint
==========

.. c:function:: ssize_t bch_hprint(char *buf, int64_t v)

    formats \ ``v``\  to human readable string for sysfs.

    :param char \*buf:
        the (at least 8 byte) buffer to format the result into.

    :param int64_t v:
        signed 64 bit integer

.. _`bch_hprint.description`:

Description
-----------

Returns the number of bytes used by format.

.. _`bch_next_delay`:

bch_next_delay
==============

.. c:function:: uint64_t bch_next_delay(struct bch_ratelimit *d, uint64_t done)

    update ratelimiting statistics and calculate next delay

    :param struct bch_ratelimit \*d:
        the struct bch_ratelimit to update

    :param uint64_t done:
        the amount of work done, in arbitrary units

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

    :param struct bio \*bio:
        bio to allocate pages for

    :param gfp_t gfp_mask:
        flags for allocation

.. _`bch_bio_alloc_pages.description`:

Description
-----------

Allocates pages up to \ ``bio``\ ->bi_vcnt.

Returns 0 on success, -ENOMEM on failure. On failure, any allocated pages are
freed.

.. This file was automatic generated / don't edit.

