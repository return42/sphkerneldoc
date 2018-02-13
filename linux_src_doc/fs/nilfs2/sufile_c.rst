.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/sufile.c

.. _`nilfs_sufile_info`:

struct nilfs_sufile_info
========================

.. c:type:: struct nilfs_sufile_info

    on-memory private data of sufile

.. _`nilfs_sufile_info.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_sufile_info {
        struct nilfs_mdt_info mi;
        unsigned long ncleansegs;
        __u64 allocmin;
        __u64 allocmax;
    }

.. _`nilfs_sufile_info.members`:

Members
-------

mi
    on-memory private data of metadata file

ncleansegs
    number of clean segments

allocmin
    lower limit of allocatable segment range

allocmax
    upper limit of allocatable segment range

.. _`nilfs_sufile_get_ncleansegs`:

nilfs_sufile_get_ncleansegs
===========================

.. c:function:: unsigned long nilfs_sufile_get_ncleansegs(struct inode *sufile)

    return the number of clean segments

    :param struct inode \*sufile:
        inode of segment usage file

.. _`nilfs_sufile_updatev`:

nilfs_sufile_updatev
====================

.. c:function:: int nilfs_sufile_updatev(struct inode *sufile, __u64 *segnumv, size_t nsegs, int create, size_t *ndone, void (*dofunc)(struct inode *, __u64, struct buffer_head *, struct buffer_head *))

    modify multiple segment usages at a time

    :param struct inode \*sufile:
        inode of segment usage file

    :param __u64 \*segnumv:
        array of segment numbers

    :param size_t nsegs:
        size of \ ``segnumv``\  array

    :param int create:
        creation flag

    :param size_t \*ndone:
        place to store number of modified segments on \ ``segnumv``\ 

    :param void (\*dofunc)(struct inode \*, __u64, struct buffer_head \*, struct buffer_head \*):
        primitive operation for the update

.. _`nilfs_sufile_updatev.description`:

Description
-----------

nilfs_sufile_updatev() repeatedly calls \ ``dofunc``\ 
against the given array of segments.  The \ ``dofunc``\  is called with
buffers of a header block and the sufile block in which the target
segment usage entry is contained.  If \ ``ndone``\  is given, the number
of successfully modified segments from the head is stored in the
place \ ``ndone``\  points to.

.. _`nilfs_sufile_updatev.return-value`:

Return Value
------------

On success, zero is returned.  On error, one of the
following negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-ENOENT``\  - Given segment usage is in hole block (may be returned if
\ ``create``\  is zero)

\ ``-EINVAL``\  - Invalid segment usage number

.. _`nilfs_sufile_set_alloc_range`:

nilfs_sufile_set_alloc_range
============================

.. c:function:: int nilfs_sufile_set_alloc_range(struct inode *sufile, __u64 start, __u64 end)

    limit range of segment to be allocated

    :param struct inode \*sufile:
        inode of segment usage file

    :param __u64 start:
        minimum segment number of allocatable region (inclusive)

    :param __u64 end:
        maximum segment number of allocatable region (inclusive)

.. _`nilfs_sufile_set_alloc_range.return-value`:

Return Value
------------

On success, 0 is returned.  On error, one of the
following negative error codes is returned.

\ ``-ERANGE``\  - invalid segment region

.. _`nilfs_sufile_alloc`:

nilfs_sufile_alloc
==================

.. c:function:: int nilfs_sufile_alloc(struct inode *sufile, __u64 *segnump)

    allocate a segment

    :param struct inode \*sufile:
        inode of segment usage file

    :param __u64 \*segnump:
        pointer to segment number

.. _`nilfs_sufile_alloc.description`:

Description
-----------

nilfs_sufile_alloc() allocates a clean segment.

.. _`nilfs_sufile_alloc.return-value`:

Return Value
------------

On success, 0 is returned and the segment number of the
allocated segment is stored in the place pointed by \ ``segnump``\ . On error, one
of the following negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-ENOSPC``\  - No clean segment left.

.. _`nilfs_sufile_mark_dirty`:

nilfs_sufile_mark_dirty
=======================

.. c:function:: int nilfs_sufile_mark_dirty(struct inode *sufile, __u64 segnum)

    mark the buffer having a segment usage dirty

    :param struct inode \*sufile:
        inode of segment usage file

    :param __u64 segnum:
        segment number

.. _`nilfs_sufile_set_segment_usage`:

nilfs_sufile_set_segment_usage
==============================

.. c:function:: int nilfs_sufile_set_segment_usage(struct inode *sufile, __u64 segnum, unsigned long nblocks, time64_t modtime)

    set usage of a segment

    :param struct inode \*sufile:
        inode of segment usage file

    :param __u64 segnum:
        segment number

    :param unsigned long nblocks:
        number of live blocks in the segment

    :param time64_t modtime:
        modification time (option)

.. _`nilfs_sufile_get_stat`:

nilfs_sufile_get_stat
=====================

.. c:function:: int nilfs_sufile_get_stat(struct inode *sufile, struct nilfs_sustat *sustat)

    get segment usage statistics

    :param struct inode \*sufile:
        inode of segment usage file

    :param struct nilfs_sustat \*sustat:
        *undescribed*

.. _`nilfs_sufile_get_stat.description`:

Description
-----------

nilfs_sufile_get_stat() returns information about segment
usage.

.. _`nilfs_sufile_get_stat.return-value`:

Return Value
------------

On success, 0 is returned, and segment usage information is
stored in the place pointed by \ ``stat``\ . On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

.. _`nilfs_sufile_truncate_range`:

nilfs_sufile_truncate_range
===========================

.. c:function:: int nilfs_sufile_truncate_range(struct inode *sufile, __u64 start, __u64 end)

    truncate range of segment array

    :param struct inode \*sufile:
        inode of segment usage file

    :param __u64 start:
        start segment number (inclusive)

    :param __u64 end:
        end segment number (inclusive)

.. _`nilfs_sufile_truncate_range.return-value`:

Return Value
------------

On success, 0 is returned.  On error, one of the
following negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-EINVAL``\  - Invalid number of segments specified

\ ``-EBUSY``\  - Dirty or active segments are present in the range

.. _`nilfs_sufile_resize`:

nilfs_sufile_resize
===================

.. c:function:: int nilfs_sufile_resize(struct inode *sufile, __u64 newnsegs)

    resize segment array

    :param struct inode \*sufile:
        inode of segment usage file

    :param __u64 newnsegs:
        new number of segments

.. _`nilfs_sufile_resize.return-value`:

Return Value
------------

On success, 0 is returned.  On error, one of the
following negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-ENOSPC``\  - Enough free space is not left for shrinking

\ ``-EBUSY``\  - Dirty or active segments exist in the region to be truncated

.. _`nilfs_sufile_get_suinfo`:

nilfs_sufile_get_suinfo
=======================

.. c:function:: ssize_t nilfs_sufile_get_suinfo(struct inode *sufile, __u64 segnum, void *buf, unsigned int sisz, size_t nsi)

    :param struct inode \*sufile:
        inode of segment usage file

    :param __u64 segnum:
        segment number to start looking

    :param void \*buf:
        array of suinfo

    :param unsigned int sisz:
        byte size of suinfo

    :param size_t nsi:
        size of suinfo array

.. _`nilfs_sufile_get_suinfo.return-value`:

Return Value
------------

On success, 0 is returned and .... On error, one of the
following negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

.. _`nilfs_sufile_set_suinfo`:

nilfs_sufile_set_suinfo
=======================

.. c:function:: ssize_t nilfs_sufile_set_suinfo(struct inode *sufile, void *buf, unsigned int supsz, size_t nsup)

    sets segment usage info

    :param struct inode \*sufile:
        inode of segment usage file

    :param void \*buf:
        array of suinfo_update

    :param unsigned int supsz:
        byte size of suinfo_update

    :param size_t nsup:
        size of suinfo_update array

.. _`nilfs_sufile_set_suinfo.description`:

Description
-----------

Takes an array of nilfs_suinfo_update structs and updates
segment usage accordingly. Only the fields indicated by the sup_flags
are updated.

.. _`nilfs_sufile_set_suinfo.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the
following negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-EINVAL``\  - Invalid values in input (segment number, flags or nblocks)

.. _`nilfs_sufile_trim_fs`:

nilfs_sufile_trim_fs
====================

.. c:function:: int nilfs_sufile_trim_fs(struct inode *sufile, struct fstrim_range *range)

    trim ioctl handle function

    :param struct inode \*sufile:
        inode of segment usage file

    :param struct fstrim_range \*range:
        fstrim_range structure

.. _`nilfs_sufile_trim_fs.start`:

start
-----

First Byte to trim

.. _`nilfs_sufile_trim_fs.len`:

len
---

number of Bytes to trim from start

.. _`nilfs_sufile_trim_fs.minlen`:

minlen
------

minimum extent length in Bytes

.. _`nilfs_sufile_trim_fs.decription`:

Decription
----------

nilfs_sufile_trim_fs goes through all segments containing bytes
from start to start+len. start is rounded up to the next block boundary
and start+len is rounded down. For each clean segment blkdev_issue_discard
function is invoked.

.. _`nilfs_sufile_trim_fs.return-value`:

Return Value
------------

On success, 0 is returned or negative error code, otherwise.

.. _`nilfs_sufile_read`:

nilfs_sufile_read
=================

.. c:function:: int nilfs_sufile_read(struct super_block *sb, size_t susize, struct nilfs_inode *raw_inode, struct inode **inodep)

    read or get sufile inode

    :param struct super_block \*sb:
        super block instance

    :param size_t susize:
        size of a segment usage entry

    :param struct nilfs_inode \*raw_inode:
        on-disk sufile inode

    :param struct inode \*\*inodep:
        buffer to store the inode

.. This file was automatic generated / don't edit.

