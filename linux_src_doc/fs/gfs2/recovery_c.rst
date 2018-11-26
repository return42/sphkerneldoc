.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/recovery.c

.. _`get_log_header`:

get_log_header
==============

.. c:function:: int get_log_header(struct gfs2_jdesc *jd, unsigned int blk, struct gfs2_log_header_host *head)

    read the log header for a given segment

    :param jd:
        the journal
    :type jd: struct gfs2_jdesc \*

    :param blk:
        the block to look at
    :type blk: unsigned int

    :param head:
        *undescribed*
    :type head: struct gfs2_log_header_host \*

.. _`get_log_header.description`:

Description
-----------

Read the log header for a given segement in a given journal.  Do a few
sanity checks on it.

.. _`get_log_header.return`:

Return
------

0 on success,
1 if the header was invalid or incomplete,
errno on error

.. _`find_good_lh`:

find_good_lh
============

.. c:function:: int find_good_lh(struct gfs2_jdesc *jd, unsigned int *blk, struct gfs2_log_header_host *head)

    find a good log header

    :param jd:
        the journal
    :type jd: struct gfs2_jdesc \*

    :param blk:
        the segment to start searching from
    :type blk: unsigned int \*

    :param head:
        *undescribed*
    :type head: struct gfs2_log_header_host \*

.. _`find_good_lh.description`:

Description
-----------

Call \ :c:func:`get_log_header`\  to get a log header for a segment, but if the
segment is bad, either scan forward or backward until we find a good one.

.. _`find_good_lh.return`:

Return
------

errno

.. _`jhead_scan`:

jhead_scan
==========

.. c:function:: int jhead_scan(struct gfs2_jdesc *jd, struct gfs2_log_header_host *head)

    make sure we've found the head of the log

    :param jd:
        the journal
    :type jd: struct gfs2_jdesc \*

    :param head:
        this is filled in with the log descriptor of the head
    :type head: struct gfs2_log_header_host \*

.. _`jhead_scan.description`:

Description
-----------

At this point, seg and lh should be either the head of the log or just
before.  Scan forward until we find the head.

.. _`jhead_scan.return`:

Return
------

errno

.. _`gfs2_find_jhead`:

gfs2_find_jhead
===============

.. c:function:: int gfs2_find_jhead(struct gfs2_jdesc *jd, struct gfs2_log_header_host *head)

    find the head of a log

    :param jd:
        the journal
    :type jd: struct gfs2_jdesc \*

    :param head:
        the log descriptor for the head of the log is returned here
    :type head: struct gfs2_log_header_host \*

.. _`gfs2_find_jhead.description`:

Description
-----------

Do a binary search of a journal and find the valid log entry with the
highest sequence number.  (i.e. the log head)

.. _`gfs2_find_jhead.return`:

Return
------

errno

.. _`foreach_descriptor`:

foreach_descriptor
==================

.. c:function:: int foreach_descriptor(struct gfs2_jdesc *jd, unsigned int start, unsigned int end, int pass)

    go through the active part of the log

    :param jd:
        the journal
    :type jd: struct gfs2_jdesc \*

    :param start:
        the first log header in the active region
    :type start: unsigned int

    :param end:
        the last log header (don't process the contents of this entry))
    :type end: unsigned int

    :param pass:
        *undescribed*
    :type pass: int

.. _`foreach_descriptor.description`:

Description
-----------

Call a given function once for every log descriptor in the active
portion of the log.

.. _`foreach_descriptor.return`:

Return
------

errno

.. _`clean_journal`:

clean_journal
=============

.. c:function:: void clean_journal(struct gfs2_jdesc *jd, struct gfs2_log_header_host *head)

    mark a dirty journal as being clean

    :param jd:
        the journal
    :type jd: struct gfs2_jdesc \*

    :param head:
        the head journal to start from
    :type head: struct gfs2_log_header_host \*

.. _`clean_journal.return`:

Return
------

errno

.. This file was automatic generated / don't edit.

