.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/badblocks.c

.. _`badblocks_check`:

badblocks_check
===============

.. c:function:: int badblocks_check(struct badblocks *bb, sector_t s, int sectors, sector_t *first_bad, int *bad_sectors)

    check a given range for bad sectors

    :param bb:
        the badblocks structure that holds all badblock information
    :type bb: struct badblocks \*

    :param s:
        sector (start) at which to check for badblocks
    :type s: sector_t

    :param sectors:
        number of sectors to check for badblocks
    :type sectors: int

    :param first_bad:
        pointer to store location of the first badblock
    :type first_bad: sector_t \*

    :param bad_sectors:
        pointer to store number of badblocks after \ ``first_bad``\ 
    :type bad_sectors: int \*

.. _`badblocks_check.description`:

Description
-----------

We can record which blocks on each device are 'bad' and so just
fail those blocks, or that stripe, rather than the whole device.
Entries in the bad-block table are 64bits wide.  This comprises:
Length of bad-range, in sectors: 0-511 for lengths 1-512
Start of bad-range, sector offset, 54 bits (allows 8 exbibytes)
A 'shift' can be set so that larger blocks are tracked and
consequently larger devices can be covered.
'Acknowledged' flag - 1 bit. - the most significant bit.

Locking of the bad-block table uses a seqlock so badblocks_check
might need to retry if it is very unlucky.
We will sometimes want to check for bad blocks in a bi_end_io function,
so we use the write_seqlock_irq variant.

When looking for a bad block we specify a range and want to
know if any block in the range is bad.  So we binary-search
to the last range that starts at-or-before the given endpoint,
(or "before the sector after the target range")
then see if it ends after the given start.

.. _`badblocks_check.return`:

Return
------

0: there are no known bad blocks in the range
1: there are known bad block which are all acknowledged
-1: there are bad blocks which have not yet been acknowledged in metadata.
plus the start/length of the first bad section we overlap.

.. _`badblocks_set`:

badblocks_set
=============

.. c:function:: int badblocks_set(struct badblocks *bb, sector_t s, int sectors, int acknowledged)

    Add a range of bad blocks to the table.

    :param bb:
        the badblocks structure that holds all badblock information
    :type bb: struct badblocks \*

    :param s:
        first sector to mark as bad
    :type s: sector_t

    :param sectors:
        number of sectors to mark as bad
    :type sectors: int

    :param acknowledged:
        weather to mark the bad sectors as acknowledged
    :type acknowledged: int

.. _`badblocks_set.description`:

Description
-----------

This might extend the table, or might contract it if two adjacent ranges
can be merged. We binary-search to find the 'insertion' point, then
decide how best to handle it.

.. _`badblocks_set.return`:

Return
------

0: success
1: failed to set badblocks (out of space)

.. _`badblocks_clear`:

badblocks_clear
===============

.. c:function:: int badblocks_clear(struct badblocks *bb, sector_t s, int sectors)

    Remove a range of bad blocks to the table.

    :param bb:
        the badblocks structure that holds all badblock information
    :type bb: struct badblocks \*

    :param s:
        first sector to mark as bad
    :type s: sector_t

    :param sectors:
        number of sectors to mark as bad
    :type sectors: int

.. _`badblocks_clear.description`:

Description
-----------

This may involve extending the table if we spilt a region,
but it must not fail.  So if the table becomes full, we just
drop the remove request.

.. _`badblocks_clear.return`:

Return
------

0: success
1: failed to clear badblocks

.. _`ack_all_badblocks`:

ack_all_badblocks
=================

.. c:function:: void ack_all_badblocks(struct badblocks *bb)

    Acknowledge all bad blocks in a list.

    :param bb:
        the badblocks structure that holds all badblock information
    :type bb: struct badblocks \*

.. _`ack_all_badblocks.description`:

Description
-----------

This only succeeds if ->changed is clear.  It is used by
in-kernel metadata updates

.. _`badblocks_show`:

badblocks_show
==============

.. c:function:: ssize_t badblocks_show(struct badblocks *bb, char *page, int unack)

    sysfs access to bad-blocks list

    :param bb:
        the badblocks structure that holds all badblock information
    :type bb: struct badblocks \*

    :param page:
        buffer received from sysfs
    :type page: char \*

    :param unack:
        weather to show unacknowledged badblocks
    :type unack: int

.. _`badblocks_show.return`:

Return
------

Length of returned data

.. _`badblocks_store`:

badblocks_store
===============

.. c:function:: ssize_t badblocks_store(struct badblocks *bb, const char *page, size_t len, int unack)

    sysfs access to bad-blocks list

    :param bb:
        the badblocks structure that holds all badblock information
    :type bb: struct badblocks \*

    :param page:
        buffer received from sysfs
    :type page: const char \*

    :param len:
        length of data received from sysfs
    :type len: size_t

    :param unack:
        weather to show unacknowledged badblocks
    :type unack: int

.. _`badblocks_store.return`:

Return
------

Length of the buffer processed or -ve error.

.. _`badblocks_init`:

badblocks_init
==============

.. c:function:: int badblocks_init(struct badblocks *bb, int enable)

    initialize the badblocks structure

    :param bb:
        the badblocks structure that holds all badblock information
    :type bb: struct badblocks \*

    :param enable:
        weather to enable badblocks accounting
    :type enable: int

.. _`badblocks_init.return`:

Return
------

0: success
-ve errno: on error

.. _`badblocks_exit`:

badblocks_exit
==============

.. c:function:: void badblocks_exit(struct badblocks *bb)

    free the badblocks structure

    :param bb:
        the badblocks structure that holds all badblock information
    :type bb: struct badblocks \*

.. This file was automatic generated / don't edit.

