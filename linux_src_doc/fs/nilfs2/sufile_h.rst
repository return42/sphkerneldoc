.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/sufile.h

.. _`nilfs_sufile_scrap`:

nilfs_sufile_scrap
==================

.. c:function:: int nilfs_sufile_scrap(struct inode *sufile, __u64 segnum)

    make a segment garbage

    :param struct inode \*sufile:
        inode of segment usage file

    :param __u64 segnum:
        segment number to be freed

.. _`nilfs_sufile_free`:

nilfs_sufile_free
=================

.. c:function:: int nilfs_sufile_free(struct inode *sufile, __u64 segnum)

    free segment

    :param struct inode \*sufile:
        inode of segment usage file

    :param __u64 segnum:
        segment number to be freed

.. _`nilfs_sufile_freev`:

nilfs_sufile_freev
==================

.. c:function:: int nilfs_sufile_freev(struct inode *sufile, __u64 *segnumv, size_t nsegs, size_t *ndone)

    free segments

    :param struct inode \*sufile:
        inode of segment usage file

    :param __u64 \*segnumv:
        array of segment numbers

    :param size_t nsegs:
        size of \ ``segnumv``\  array

    :param size_t \*ndone:
        place to store the number of freed segments

.. _`nilfs_sufile_cancel_freev`:

nilfs_sufile_cancel_freev
=========================

.. c:function:: int nilfs_sufile_cancel_freev(struct inode *sufile, __u64 *segnumv, size_t nsegs, size_t *ndone)

    reallocate freeing segments

    :param struct inode \*sufile:
        inode of segment usage file

    :param __u64 \*segnumv:
        array of segment numbers

    :param size_t nsegs:
        size of \ ``segnumv``\  array

    :param size_t \*ndone:
        place to store the number of cancelled segments

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

    :param struct inode \*sufile:
        inode of segment usage file

    :param __u64 segnum:
        segment number

.. _`nilfs_sufile_set_error.description`:

Description
-----------

nilfs_sufile_set_error() marks the segment specified by
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

