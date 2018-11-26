.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/super.c

.. _`simple_getbool`:

simple_getbool
==============

.. c:function:: int simple_getbool(char *s, bool *setval)

    :param s:
        *undescribed*
    :type s: char \*

    :param setval:
        *undescribed*
    :type setval: bool \*

.. _`simple_getbool.description`:

Description
-----------

Copied from old ntfs driver (which copied from vfat driver).

.. _`parse_options`:

parse_options
=============

.. c:function:: bool parse_options(ntfs_volume *vol, char *opt)

    parse the (re)mount options

    :param vol:
        ntfs volume
    :type vol: ntfs_volume \*

    :param opt:
        string containing the (re)mount options
    :type opt: char \*

.. _`parse_options.description`:

Description
-----------

Parse the recognized options in \ ``opt``\  for the ntfs volume described by \ ``vol``\ .

.. _`ntfs_write_volume_flags`:

ntfs_write_volume_flags
=======================

.. c:function:: int ntfs_write_volume_flags(ntfs_volume *vol, const VOLUME_FLAGS flags)

    write new flags to the volume information flags

    :param vol:
        ntfs volume on which to modify the flags
    :type vol: ntfs_volume \*

    :param flags:
        new flags value for the volume information flags
    :type flags: const VOLUME_FLAGS

.. _`ntfs_write_volume_flags.description`:

Description
-----------

Internal function.  You probably want to use ntfs_{set,clear}_volume_flags()
instead (see below).

Replace the volume information flags on the volume \ ``vol``\  with the value
supplied in \ ``flags``\ .  Note, this overwrites the volume information flags, so
make sure to combine the flags you want to modify with the old flags and use
the result when calling \ :c:func:`ntfs_write_volume_flags`\ .

Return 0 on success and -errno on error.

.. _`ntfs_set_volume_flags`:

ntfs_set_volume_flags
=====================

.. c:function:: int ntfs_set_volume_flags(ntfs_volume *vol, VOLUME_FLAGS flags)

    set bits in the volume information flags

    :param vol:
        ntfs volume on which to modify the flags
    :type vol: ntfs_volume \*

    :param flags:
        flags to set on the volume
    :type flags: VOLUME_FLAGS

.. _`ntfs_set_volume_flags.description`:

Description
-----------

Set the bits in \ ``flags``\  in the volume information flags on the volume \ ``vol``\ .

Return 0 on success and -errno on error.

.. _`ntfs_clear_volume_flags`:

ntfs_clear_volume_flags
=======================

.. c:function:: int ntfs_clear_volume_flags(ntfs_volume *vol, VOLUME_FLAGS flags)

    clear bits in the volume information flags

    :param vol:
        ntfs volume on which to modify the flags
    :type vol: ntfs_volume \*

    :param flags:
        flags to clear on the volume
    :type flags: VOLUME_FLAGS

.. _`ntfs_clear_volume_flags.description`:

Description
-----------

Clear the bits in \ ``flags``\  in the volume information flags on the volume \ ``vol``\ .

Return 0 on success and -errno on error.

.. _`ntfs_remount`:

ntfs_remount
============

.. c:function:: int ntfs_remount(struct super_block *sb, int *flags, char *opt)

    change the mount options of a mounted ntfs filesystem

    :param sb:
        superblock of mounted ntfs filesystem
    :type sb: struct super_block \*

    :param flags:
        remount flags
    :type flags: int \*

    :param opt:
        remount options string
    :type opt: char \*

.. _`ntfs_remount.description`:

Description
-----------

Change the mount options of an already mounted ntfs filesystem.

.. _`ntfs_remount.note`:

NOTE
----

The VFS sets the \ ``sb->s_flags``\  remount flags to \ ``flags``\  after
\ :c:func:`ntfs_remount`\  returns successfully (i.e. returns 0).  Otherwise,
\ ``sb->s_flags``\  are not changed.

.. _`is_boot_sector_ntfs`:

is_boot_sector_ntfs
===================

.. c:function:: bool is_boot_sector_ntfs(const struct super_block *sb, const NTFS_BOOT_SECTOR *b, const bool silent)

    check whether a boot sector is a valid NTFS boot sector

    :param sb:
        Super block of the device to which \ ``b``\  belongs.
    :type sb: const struct super_block \*

    :param b:
        Boot sector of device \ ``sb``\  to check.
    :type b: const NTFS_BOOT_SECTOR \*

    :param silent:
        If 'true', all output will be silenced.
    :type silent: const bool

.. _`is_boot_sector_ntfs.description`:

Description
-----------

\ :c:func:`is_boot_sector_ntfs`\  checks whether the boot sector \ ``b``\  is a valid NTFS boot
sector. Returns 'true' if it is valid and 'false' if not.

\ ``sb``\  is only needed for warning/error output, i.e. it can be NULL when silent
is 'true'.

.. _`read_ntfs_boot_sector`:

read_ntfs_boot_sector
=====================

.. c:function:: struct buffer_head *read_ntfs_boot_sector(struct super_block *sb, const int silent)

    read the NTFS boot sector of a device

    :param sb:
        super block of device to read the boot sector from
    :type sb: struct super_block \*

    :param silent:
        if true, suppress all output
    :type silent: const int

.. _`read_ntfs_boot_sector.description`:

Description
-----------

Reads the boot sector from the device and validates it. If that fails, tries
to read the backup boot sector, first from the end of the device a-la NT4 and
later and then from the middle of the device a-la NT3.51 and before.

If a valid boot sector is found but it is not the primary boot sector, we
repair the primary boot sector silently (unless the device is read-only or
the primary boot sector is not accessible).

.. _`read_ntfs_boot_sector.note`:

NOTE
----

To call this function, \ ``sb``\  must have the fields s_dev, the ntfs super
block (u.ntfs_sb), nr_blocks and the device flags (s_flags) initialized
to their respective values.

Return the unlocked buffer head containing the boot sector or NULL on error.

.. _`parse_ntfs_boot_sector`:

parse_ntfs_boot_sector
======================

.. c:function:: bool parse_ntfs_boot_sector(ntfs_volume *vol, const NTFS_BOOT_SECTOR *b)

    parse the boot sector and store the data in \ ``vol``\ 

    :param vol:
        volume structure to initialise with data from boot sector
    :type vol: ntfs_volume \*

    :param b:
        boot sector to parse
    :type b: const NTFS_BOOT_SECTOR \*

.. _`parse_ntfs_boot_sector.description`:

Description
-----------

Parse the ntfs boot sector \ ``b``\  and store all imporant information therein in
the ntfs super block \ ``vol``\ .  Return 'true' on success and 'false' on error.

.. _`ntfs_setup_allocators`:

ntfs_setup_allocators
=====================

.. c:function:: void ntfs_setup_allocators(ntfs_volume *vol)

    initialize the cluster and mft allocators

    :param vol:
        volume structure for which to setup the allocators
    :type vol: ntfs_volume \*

.. _`ntfs_setup_allocators.description`:

Description
-----------

Setup the cluster (lcn) and mft allocators to the starting values.

.. _`load_and_init_mft_mirror`:

load_and_init_mft_mirror
========================

.. c:function:: bool load_and_init_mft_mirror(ntfs_volume *vol)

    load and setup the mft mirror inode for a volume

    :param vol:
        ntfs super block describing device whose mft mirror to load
    :type vol: ntfs_volume \*

.. _`load_and_init_mft_mirror.description`:

Description
-----------

Return 'true' on success or 'false' on error.

.. _`check_mft_mirror`:

check_mft_mirror
================

.. c:function:: bool check_mft_mirror(ntfs_volume *vol)

    compare contents of the mft mirror with the mft

    :param vol:
        ntfs super block describing device whose mft mirror to check
    :type vol: ntfs_volume \*

.. _`check_mft_mirror.description`:

Description
-----------

Return 'true' on success or 'false' on error.

Note, this function also results in the mft mirror runlist being completely
mapped into memory.  The mft mirror write code requires this and will \ :c:func:`BUG`\ 
should it find an unmapped runlist element.

.. _`load_and_check_logfile`:

load_and_check_logfile
======================

.. c:function:: bool load_and_check_logfile(ntfs_volume *vol, RESTART_PAGE_HEADER **rp)

    load and check the logfile inode for a volume

    :param vol:
        ntfs super block describing device whose logfile to load
    :type vol: ntfs_volume \*

    :param rp:
        *undescribed*
    :type rp: RESTART_PAGE_HEADER \*\*

.. _`load_and_check_logfile.description`:

Description
-----------

Return 'true' on success or 'false' on error.

.. _`check_windows_hibernation_status`:

check_windows_hibernation_status
================================

.. c:function:: int check_windows_hibernation_status(ntfs_volume *vol)

    check if Windows is suspended on a volume

    :param vol:
        ntfs super block of device to check
    :type vol: ntfs_volume \*

.. _`check_windows_hibernation_status.description`:

Description
-----------

Check if Windows is hibernated on the ntfs volume \ ``vol``\ .  This is done by
looking for the file hiberfil.sys in the root directory of the volume.  If
the file is not present Windows is definitely not suspended.

If hiberfil.sys exists and is less than 4kiB in size it means Windows is
definitely suspended (this volume is not the system volume).  Caveat:  on a
system with many volumes it is possible that the < 4kiB check is bogus but
for now this should do fine.

If hiberfil.sys exists and is larger than 4kiB in size, we need to read the
hiberfil header (which is the first 4kiB).  If this begins with "hibr",
Windows is definitely suspended.  If it is completely full of zeroes,
Windows is definitely not hibernated.  Any other case is treated as if
Windows is suspended.  This caters for the above mentioned caveat of a
system with many volumes where no "hibr" magic would be present and there is
no zero header.

Return 0 if Windows is not hibernated on the volume, >0 if Windows is
hibernated on the volume, and -errno on error.

.. _`load_and_init_quota`:

load_and_init_quota
===================

.. c:function:: bool load_and_init_quota(ntfs_volume *vol)

    load and setup the quota file for a volume if present

    :param vol:
        ntfs super block describing device whose quota file to load
    :type vol: ntfs_volume \*

.. _`load_and_init_quota.description`:

Description
-----------

Return 'true' on success or 'false' on error.  If \ ``$Quota``\  is not present, we
leave vol->quota_ino as NULL and return success.

.. _`load_and_init_usnjrnl`:

load_and_init_usnjrnl
=====================

.. c:function:: bool load_and_init_usnjrnl(ntfs_volume *vol)

    load and setup the transaction log if present

    :param vol:
        ntfs super block describing device whose usnjrnl file to load
    :type vol: ntfs_volume \*

.. _`load_and_init_usnjrnl.description`:

Description
-----------

Return 'true' on success or 'false' on error.

If \ ``$UsnJrnl``\  is not present or in the process of being disabled, we set
\ :c:func:`NVolUsnJrnlStamped`\  and return success.

If the \ ``$UsnJrnl``\  \ ``$DATA``\ /$J attribute has a size equal to the lowest valid usn,
i.e. transaction logging has only just been enabled or the journal has been
stamped and nothing has been logged since, we also set \ :c:func:`NVolUsnJrnlStamped`\ 
and return success.

.. _`load_and_init_attrdef`:

load_and_init_attrdef
=====================

.. c:function:: bool load_and_init_attrdef(ntfs_volume *vol)

    load the attribute definitions table for a volume

    :param vol:
        ntfs super block describing device whose attrdef to load
    :type vol: ntfs_volume \*

.. _`load_and_init_attrdef.description`:

Description
-----------

Return 'true' on success or 'false' on error.

.. _`load_and_init_upcase`:

load_and_init_upcase
====================

.. c:function:: bool load_and_init_upcase(ntfs_volume *vol)

    load the upcase table for an ntfs volume

    :param vol:
        ntfs super block describing device whose upcase to load
    :type vol: ntfs_volume \*

.. _`load_and_init_upcase.description`:

Description
-----------

Return 'true' on success or 'false' on error.

.. _`load_system_files`:

load_system_files
=================

.. c:function:: bool load_system_files(ntfs_volume *vol)

    open the system files using normal functions

    :param vol:
        ntfs super block describing device whose system files to load
    :type vol: ntfs_volume \*

.. _`load_system_files.description`:

Description
-----------

Open the system files with normal access functions and complete setting up
the ntfs super block \ ``vol``\ .

Return 'true' on success or 'false' on error.

.. _`ntfs_put_super`:

ntfs_put_super
==============

.. c:function:: void ntfs_put_super(struct super_block *sb)

    called by the vfs to unmount a volume

    :param sb:
        vfs superblock of volume to unmount
    :type sb: struct super_block \*

.. _`ntfs_put_super.description`:

Description
-----------

\ :c:func:`ntfs_put_super`\  is called by the VFS (from fs/super.c::do_umount()) when
the volume is being unmounted (umount system call has been invoked) and it
releases all inodes and memory belonging to the NTFS specific part of the
super block.

.. _`get_nr_free_clusters`:

get_nr_free_clusters
====================

.. c:function:: s64 get_nr_free_clusters(ntfs_volume *vol)

    return the number of free clusters on a volume

    :param vol:
        ntfs volume for which to obtain free cluster count
    :type vol: ntfs_volume \*

.. _`get_nr_free_clusters.description`:

Description
-----------

Calculate the number of free clusters on the mounted NTFS volume \ ``vol``\ . We
actually calculate the number of clusters in use instead because this
allows us to not care about partial pages as these will be just zero filled
and hence not be counted as allocated clusters.

The only particularity is that clusters beyond the end of the logical ntfs
volume will be marked as allocated to prevent errors which means we have to
discount those at the end. This is important as the cluster bitmap always
has a size in multiples of 8 bytes, i.e. up to 63 clusters could be outside
the logical volume and marked in use when they are not as they do not exist.

If any pages cannot be read we assume all clusters in the erroring pages are
in use. This means we return an underestimate on errors which is better than
an overestimate.

.. _`__get_nr_free_mft_records`:

\__get_nr_free_mft_records
==========================

.. c:function:: unsigned long __get_nr_free_mft_records(ntfs_volume *vol, s64 nr_free, const pgoff_t max_index)

    return the number of free inodes on a volume

    :param vol:
        ntfs volume for which to obtain free inode count
    :type vol: ntfs_volume \*

    :param nr_free:
        number of mft records in filesystem
    :type nr_free: s64

    :param max_index:
        maximum number of pages containing set bits
    :type max_index: const pgoff_t

.. _`__get_nr_free_mft_records.description`:

Description
-----------

Calculate the number of free mft records (inodes) on the mounted NTFS
volume \ ``vol``\ . We actually calculate the number of mft records in use instead
because this allows us to not care about partial pages as these will be just
zero filled and hence not be counted as allocated mft record.

If any pages cannot be read we assume all mft records in the erroring pages
are in use. This means we return an underestimate on errors which is better
than an overestimate.

.. _`__get_nr_free_mft_records.note`:

NOTE
----

Caller must hold mftbmp_lock rw_semaphore for reading or writing.

.. _`ntfs_statfs`:

ntfs_statfs
===========

.. c:function:: int ntfs_statfs(struct dentry *dentry, struct kstatfs *sfs)

    return information about mounted NTFS volume

    :param dentry:
        dentry from mounted volume
    :type dentry: struct dentry \*

    :param sfs:
        statfs structure in which to return the information
    :type sfs: struct kstatfs \*

.. _`ntfs_statfs.description`:

Description
-----------

Return information about the mounted NTFS volume \ ``dentry``\  in the statfs structure
pointed to by \ ``sfs``\  (this is initialized with zeros before ntfs_statfs is
called). We interpret the values to be correct of the moment in time at
which we are called. Most values are variable otherwise and this isn't just
the free values but the totals as well. For example we can increase the
total number of file nodes if we run out and we can keep doing this until
there is no more space on the volume left at all.

Called from vfs_statfs which is used to handle the statfs, fstatfs, and
ustat system calls.

Return 0 on success or -errno on error.

.. _`ntfs_fill_super`:

ntfs_fill_super
===============

.. c:function:: int ntfs_fill_super(struct super_block *sb, void *opt, const int silent)

    mount an ntfs filesystem

    :param sb:
        super block of ntfs filesystem to mount
    :type sb: struct super_block \*

    :param opt:
        string containing the mount options
    :type opt: void \*

    :param silent:
        silence error output
    :type silent: const int

.. _`ntfs_fill_super.description`:

Description
-----------

\ :c:func:`ntfs_fill_super`\  is called by the VFS to mount the device described by \ ``sb``\ 
with the mount otions in \ ``data``\  with the NTFS filesystem.

If \ ``silent``\  is true, remain silent even if errors are detected. This is used
during bootup, when the kernel tries to mount the root filesystem with all
registered filesystems one after the other until one succeeds. This implies
that all filesystems except the correct one will quite correctly and
expectedly return an error, but nobody wants to see error messages when in
fact this is what is supposed to happen.

.. _`ntfs_fill_super.note`:

NOTE
----

\ ``sb->s_flags``\  contains the mount options flags.

.. This file was automatic generated / don't edit.

