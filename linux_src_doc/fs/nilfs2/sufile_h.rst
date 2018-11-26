.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/sufile.h

.. _`nilfs_sufile_scrap`:

nilfs_sufile_scrap
==================

.. c:function:: int nilfs_sufile_scrap(struct inode *sufile, __u64 segnum)

    make a segment garbage

    :param sufile:
        inode of segment usage file
    :type sufile: struct inode \*

    :param segnum:
        segment number to be freed
    :type segnum: __u64

.. _`nilfs_sufile_free`:

nilfs_sufile_free
=================

.. c:function:: int nilfs_sufile_free(struct inode *sufile, __u64 segnum)

    free segment

    :param sufile:
        inode of segment usage file
    :type sufile: struct inode \*

    :param segnum:
        segment number to be freed
    :type segnum: __u64

.. _`nilfs_sufile_freev`:

nilfs_sufile_freev
==================

.. c:function:: int nilfs_sufile_freev(struct inode *sufile, __u64 *segnumv, size_t nsegs, size_t *ndone)

    free segments

    :param sufile:
        inode of segment usage file
    :type sufile: struct inode \*

    :param segnumv:
        array of segment numbers
    :type segnumv: __u64 \*

    :param nsegs:
        size of \ ``segnumv``\  array
    :type nsegs: size_t

    :param ndone:
        place to store the number of freed segments
    :type ndone: size_t \*

.. _`nilfs_sufile_cancel_freev`:

nilfs_sufile_cancel_freev
=========================

.. c:function:: int nilfs_sufile_cancel_freev(struct inode *sufile, __u64 *segnumv, size_t nsegs, size_t *ndone)

    reallocate freeing segments

    :param sufile:
        inode of segment usage file
    :type sufile: struct inode \*

    :param segnumv:
        array of segment numbers
    :type segnumv: __u64 \*

    :param nsegs:
        size of \ ``segnumv``\  array
    :type nsegs: size_t

    :param ndone:
        place to store the number of cancelled segments
    :type ndone: size_t \*

.. _`nilfs_sufile_cancel_freev.return-value`:

Return Value
------------

On success, 0 is returned. On error, a negative error codes
is returned.

.. _`nilfs_sufile_set_error`:

nilfs_sufile_set_error
======================

.. c:function:: int nilfs_sufile_set_error(struct inode *sufile, __u64 segnum)

    mark a segment as erroneous

    :param sufile:
        inode of segment usage file
    :type sufile: struct inode \*

    :param segnum:
        segment number
    :type segnum: __u64

.. _`nilfs_sufile_set_error.description`:

Description
-----------

\ :c:func:`nilfs_sufile_set_error`\  marks the segment specified by
\ ``segnum``\  as erroneous. The error segment will never be used again.

.. _`nilfs_sufile_set_error.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-EINVAL``\  - Invalid segment usage number.

.. This file was automatic generated / don't edit.

