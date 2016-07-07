.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/ops_fstype.c

.. _`gfs2_tune_init`:

gfs2_tune_init
==============

.. c:function:: void gfs2_tune_init(struct gfs2_tune *gt)

    Fill a gfs2_tune structure with default values

    :param struct gfs2_tune \*gt:
        tune

.. _`gfs2_check_sb`:

gfs2_check_sb
=============

.. c:function:: int gfs2_check_sb(struct gfs2_sbd *sdp, int silent)

    Check superblock

    :param struct gfs2_sbd \*sdp:
        the filesystem

    :param int silent:
        Don't print a message if the check fails

.. _`gfs2_check_sb.description`:

Description
-----------

Checks the version code of the FS is one that we understand how to
read and that the sizes of the various on-disk structures have not
changed.

.. _`gfs2_read_super`:

gfs2_read_super
===============

.. c:function:: int gfs2_read_super(struct gfs2_sbd *sdp, sector_t sector, int silent)

    Read the gfs2 super block from disk

    :param struct gfs2_sbd \*sdp:
        The GFS2 super block

    :param sector_t sector:
        The location of the super block

    :param int silent:
        *undescribed*

.. _`gfs2_read_super.description`:

Description
-----------

This uses the bio functions to read the super block from disk
because we want to be 100% sure that we never read cached data.
A super block is read twice only during each GFS2 mount and is
never written to by the filesystem. The first time its read no
locks are held, and the only details which are looked at are those
relating to the locking protocol. Once locking is up and working,
the sb is read again under the lock to establish the location of
the master directory (contains pointers to journals etc) and the
root directory.

.. _`gfs2_read_super.return`:

Return
------

0 on success or error

.. _`gfs2_read_sb`:

gfs2_read_sb
============

.. c:function:: int gfs2_read_sb(struct gfs2_sbd *sdp, int silent)

    Read super block

    :param struct gfs2_sbd \*sdp:
        The GFS2 superblock

    :param int silent:
        Don't print message if mount fails

.. _`gfs2_jindex_hold`:

gfs2_jindex_hold
================

.. c:function:: int gfs2_jindex_hold(struct gfs2_sbd *sdp, struct gfs2_holder *ji_gh)

    Grab a lock on the jindex

    :param struct gfs2_sbd \*sdp:
        The GFS2 superblock

    :param struct gfs2_holder \*ji_gh:
        the holder for the jindex glock

.. _`gfs2_jindex_hold.return`:

Return
------

errno

.. _`check_journal_clean`:

check_journal_clean
===================

.. c:function:: int check_journal_clean(struct gfs2_sbd *sdp, struct gfs2_jdesc *jd)

    Make sure a journal is clean for a spectator mount

    :param struct gfs2_sbd \*sdp:
        The GFS2 superblock

    :param struct gfs2_jdesc \*jd:
        The journal descriptor

.. _`check_journal_clean.return`:

Return
------

0 if the journal is clean or locked, else an error

.. _`gfs2_lm_mount`:

gfs2_lm_mount
=============

.. c:function:: int gfs2_lm_mount(struct gfs2_sbd *sdp, int silent)

    mount a locking protocol

    :param struct gfs2_sbd \*sdp:
        the filesystem

    :param int silent:
        if 1, don't complain if the FS isn't a GFS2 fs

.. _`gfs2_lm_mount.return`:

Return
------

errno

.. _`fill_super`:

fill_super
==========

.. c:function:: int fill_super(struct super_block *sb, struct gfs2_args *args, int silent)

    Read in superblock

    :param struct super_block \*sb:
        The VFS superblock

    :param struct gfs2_args \*args:
        *undescribed*

    :param int silent:
        Don't complain if it's not a GFS2 filesystem

.. _`fill_super.return`:

Return
------

errno

.. _`gfs2_mount`:

gfs2_mount
==========

.. c:function:: struct dentry *gfs2_mount(struct file_system_type *fs_type, int flags, const char *dev_name, void *data)

    Get the GFS2 superblock

    :param struct file_system_type \*fs_type:
        The GFS2 filesystem type

    :param int flags:
        Mount flags

    :param const char \*dev_name:
        The name of the device

    :param void \*data:
        The mount arguments

.. _`gfs2_mount.description`:

Description
-----------

Q. Why not use \ :c:func:`get_sb_bdev`\  ?
A. We need to select one of two root directories to mount, independent
of whether this is the initial, or subsequent, mount of this sb

.. _`gfs2_mount.return`:

Return
------

0 or -ve on error

.. This file was automatic generated / don't edit.

