.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/bio.h

.. _`bio_next_split`:

bio_next_split
==============

.. c:function:: struct bio *bio_next_split(struct bio *bio, int sectors, gfp_t gfp, struct bio_set *bs)

    get next \ ``sectors``\  from a bio, splitting if necessary

    :param bio:
        bio to split
    :type bio: struct bio \*

    :param sectors:
        number of sectors to split from the front of \ ``bio``\ 
    :type sectors: int

    :param gfp:
        gfp mask
    :type gfp: gfp_t

    :param bs:
        bio set to allocate from
    :type bs: struct bio_set \*

.. _`bio_next_split.description`:

Description
-----------

Returns a bio representing the next \ ``sectors``\  of \ ``bio``\  - if the bio is smaller
than \ ``sectors``\ , returns the original bio unchanged.

.. This file was automatic generated / don't edit.

