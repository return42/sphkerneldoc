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

    :param sufile:
        inode of segment usage file
    :type sufile: struct inode \*

.. _`nilfs_sufile_updatev`:

nilfs_sufile_updatev
====================

.. c:function:: int nilfs_sufile_updatev(struct inode *sufile, __u64 *segnumv, size_t nsegs, int create, size_t *ndone, void (*dofunc)(struct inode *, __u64, struct buffer_head *, struct buffer_head *))

    modify multiple segment usages at a time

    :param sufile:
        inode of segment usage file
    :type sufile: struct inode \*

    :param segnumv:
        array of segment numbers
    :type segnumv: __u64 \*

    :param nsegs:
        size of \ ``segnumv``\  array
    :type nsegs: size_t

    :param create:
        creation flag
    :type create: int

    :param ndone:
        place to store number of modified segments on \ ``segnumv``\ 
    :type ndone: size_t \*

    :param void (\*dofunc)(struct inode \*, __u64, struct buffer_head \*, struct buffer_head \*):
        primitive operation for the update

.. _`nilfs_sufile_updatev.description`:

Description
-----------

\ :c:func:`nilfs_sufile_updatev`\  repeatedly calls \ ``dofunc``\ 
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

    :param sufile:
        inode of segment usage file
    :type sufile: struct inode \*

    :param start:
        minimum segment number of allocatable region (inclusive)
    :type start: __u64

    :param end:
        maximum segment number of allocatable region (inclusive)
    :type end: __u64

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

    :param sufile:
        inode of segment usage file
    :type sufile: struct inode \*

    :param segnump:
        pointer to segment number
    :type segnump: __u64 \*

.. _`nilfs_sufile_alloc.description`:

Description
-----------

\ :c:func:`nilfs_sufile_alloc`\  allocates a clean segment.

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

    :param sufile:
        inode of segment usage file
    :type sufile: struct inode \*

    :param segnum:
        segment number
    :type segnum: __u64

.. _`nilfs_sufile_set_segment_usage`:

nilfs_sufile_set_segment_usage
==============================

.. c:function:: int nilfs_sufile_set_segment_usage(struct inode *sufile, __u64 segnum, unsigned long nblocks, time64_t modtime)

    set usage of a segment

    :param sufile:
        inode of segment usage file
    :type sufile: struct inode \*

    :param segnum:
        segment number
    :type segnum: __u64

    :param nblocks:
        number of live blocks in the segment
    :type nblocks: unsigned long

    :param modtime:
        modification time (option)
    :type modtime: time64_t

.. _`nilfs_sufile_get_stat`:

nilfs_sufile_get_stat
=====================

.. c:function:: int nilfs_sufile_get_stat(struct inode *sufile, struct nilfs_sustat *sustat)

    get segment usage statistics

    :param sufile:
        inode of segment usage file
    :type sufile: struct inode \*

    :param sustat:
        *undescribed*
    :type sustat: struct nilfs_sustat \*

.. _`nilfs_sufile_get_stat.description`:

Description
-----------

\ :c:func:`nilfs_sufile_get_stat`\  returns information about segment
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

    :param sufile:
        inode of segment usage file
    :type sufile: struct inode \*

    :param start:
        start segment number (inclusive)
    :type start: __u64

    :param end:
        end segment number (inclusive)
    :type end: __u64

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

    :param sufile:
        inode of segment usage file
    :type sufile: struct inode \*

    :param newnsegs:
        new number of segments
    :type newnsegs: __u64

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

    :param sufile:
        inode of segment usage file
    :type sufile: struct inode \*

    :param segnum:
        segment number to start looking
    :type segnum: __u64

    :param buf:
        array of suinfo
    :type buf: void \*

    :param sisz:
        byte size of suinfo
    :type sisz: unsigned int

    :param nsi:
        size of suinfo array
    :type nsi: size_t

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

    :param sufile:
        inode of segment usage file
    :type sufile: struct inode \*

    :param buf:
        array of suinfo_update
    :type buf: void \*

    :param supsz:
        byte size of suinfo_update
    :type supsz: unsigned int

    :param nsup:
        size of suinfo_update array
    :type nsup: size_t

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

    :param sufile:
        inode of segment usage file
    :type sufile: struct inode \*

    :param range:
        fstrim_range structure
    :type range: struct fstrim_range \*

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

    :param sb:
        super block instance
    :type sb: struct super_block \*

    :param susize:
        size of a segment usage entry
    :type susize: size_t

    :param raw_inode:
        on-disk sufile inode
    :type raw_inode: struct nilfs_inode \*

    :param inodep:
        buffer to store the inode
    :type inodep: struct inode \*\*

.. This file was automatic generated / don't edit.

