.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/bio.h

.. _`bio_next_split`:

bio_next_split
==============

.. c:function:: struct bio *bio_next_split(struct bio *bio, int sectors, gfp_t gfp, struct bio_set *bs)

    get next \ ``sectors``\  from a bio, splitting if necessary

    :param struct bio \*bio:
        bio to split

    :param int sectors:
        number of sectors to split from the front of \ ``bio``\ 

    :param gfp_t gfp:
        gfp mask

    :param struct bio_set \*bs:
        bio set to allocate from

.. _`bio_next_split.description`:

Description
-----------

Returns a bio representing the next \ ``sectors``\  of \ ``bio``\  - if the bio is smaller
than \ ``sectors``\ , returns the original bio unchanged.

.. This file was automatic generated / don't edit.

