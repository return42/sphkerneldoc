.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/segbuf.c

.. _`nilfs_segbuf_map_cont`:

nilfs_segbuf_map_cont
=====================

.. c:function:: void nilfs_segbuf_map_cont(struct nilfs_segment_buffer *segbuf, struct nilfs_segment_buffer *prev)

    map a new log behind a given log

    :param segbuf:
        new segment buffer
    :type segbuf: struct nilfs_segment_buffer \*

    :param prev:
        segment buffer containing a log to be continued
    :type prev: struct nilfs_segment_buffer \*

.. _`nilfs_add_checksums_on_logs`:

nilfs_add_checksums_on_logs
===========================

.. c:function:: void nilfs_add_checksums_on_logs(struct list_head *logs, u32 seed)

    add checksums on the logs

    :param logs:
        list of segment buffers storing target logs
    :type logs: struct list_head \*

    :param seed:
        checksum seed value
    :type seed: u32

.. _`nilfs_alloc_seg_bio`:

nilfs_alloc_seg_bio
===================

.. c:function:: struct bio *nilfs_alloc_seg_bio(struct the_nilfs *nilfs, sector_t start, int nr_vecs)

    allocate a new bio for writing log

    :param nilfs:
        nilfs object
    :type nilfs: struct the_nilfs \*

    :param start:
        start block number of the bio
    :type start: sector_t

    :param nr_vecs:
        request size of page vector.
    :type nr_vecs: int

.. _`nilfs_alloc_seg_bio.return-value`:

Return Value
------------

On success, pointer to the struct bio is returned.
On error, NULL is returned.

.. _`nilfs_segbuf_write`:

nilfs_segbuf_write
==================

.. c:function:: int nilfs_segbuf_write(struct nilfs_segment_buffer *segbuf, struct the_nilfs *nilfs)

    submit write requests of a log

    :param segbuf:
        buffer storing a log to be written
    :type segbuf: struct nilfs_segment_buffer \*

    :param nilfs:
        nilfs object
    :type nilfs: struct the_nilfs \*

.. _`nilfs_segbuf_write.return-value`:

Return Value
------------

On Success, 0 is returned. On Error, one of the following
negative error code is returned.

\ ``-EIO``\  - I/O error

\ ``-ENOMEM``\  - Insufficient memory available.

.. _`nilfs_segbuf_wait`:

nilfs_segbuf_wait
=================

.. c:function:: int nilfs_segbuf_wait(struct nilfs_segment_buffer *segbuf)

    wait for completion of requested BIOs

    :param segbuf:
        segment buffer
    :type segbuf: struct nilfs_segment_buffer \*

.. _`nilfs_segbuf_wait.return-value`:

Return Value
------------

On Success, 0 is returned. On Error, one of the following
negative error code is returned.

\ ``-EIO``\  - I/O error

.. This file was automatic generated / don't edit.

