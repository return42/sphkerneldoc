.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/super.c

.. _`validate_inode`:

validate_inode
==============

.. c:function:: int validate_inode(struct ubifs_info *c, const struct inode *inode)

    validate inode.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param inode:
        the inode to validate
    :type inode: const struct inode \*

.. _`validate_inode.description`:

Description
-----------

This is a helper function for 'ubifs_iget()' which validates various fields
of a newly built inode to make sure they contain sane values and prevent
possible vulnerabilities. Returns zero if the inode is all right and
a non-zero error code if not.

.. _`init_constants_early`:

init_constants_early
====================

.. c:function:: int init_constants_early(struct ubifs_info *c)

    initialize UBIFS constants.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`init_constants_early.description`:

Description
-----------

This function initialize UBIFS constants which do not need the superblock to
be read. It also checks that the UBI volume satisfies basic UBIFS
requirements. Returns zero in case of success and a negative error code in
case of failure.

.. _`bud_wbuf_callback`:

bud_wbuf_callback
=================

.. c:function:: int bud_wbuf_callback(struct ubifs_info *c, int lnum, int free, int pad)

    bud LEB write-buffer synchronization call-back.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param lnum:
        LEB the write-buffer was synchronized to
    :type lnum: int

    :param free:
        how many free bytes left in this LEB
    :type free: int

    :param pad:
        how many bytes were padded
    :type pad: int

.. _`bud_wbuf_callback.description`:

Description
-----------

This is a callback function which is called by the I/O unit when the
write-buffer is synchronized. We need this to correctly maintain space
accounting in bud logical eraseblocks. This function returns zero in case of
success and a negative error code in case of failure.

This function actually belongs to the journal, but we keep it here because
we want to keep it static.

.. _`take_gc_lnum`:

take_gc_lnum
============

.. c:function:: int take_gc_lnum(struct ubifs_info *c)

    reserve GC LEB.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`take_gc_lnum.description`:

Description
-----------

This function ensures that the LEB reserved for garbage collection is marked
as "taken" in lprops. We also have to set free space to LEB size and dirty
space to zero, because lprops may contain out-of-date information if the
file-system was un-mounted before it has been committed. This function
returns zero in case of success and a negative error code in case of
failure.

.. _`alloc_wbufs`:

alloc_wbufs
===========

.. c:function:: int alloc_wbufs(struct ubifs_info *c)

    allocate write-buffers.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`alloc_wbufs.description`:

Description
-----------

This helper function allocates and initializes UBIFS write-buffers. Returns
zero in case of success and \ ``-ENOMEM``\  in case of failure.

.. _`free_wbufs`:

free_wbufs
==========

.. c:function:: void free_wbufs(struct ubifs_info *c)

    free write-buffers.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`free_orphans`:

free_orphans
============

.. c:function:: void free_orphans(struct ubifs_info *c)

    free orphans.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`free_buds`:

free_buds
=========

.. c:function:: void free_buds(struct ubifs_info *c)

    free per-bud objects.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`check_volume_empty`:

check_volume_empty
==================

.. c:function:: int check_volume_empty(struct ubifs_info *c)

    check if the UBI volume is empty.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`check_volume_empty.description`:

Description
-----------

This function checks if the UBIFS volume is empty by looking if its LEBs are
mapped or not. The result of checking is stored in the \ ``c->empty``\  variable.
Returns zero in case of success and a negative error code in case of
failure.

.. _`parse_standard_option`:

parse_standard_option
=====================

.. c:function:: int parse_standard_option(const char *option)

    parse a standard mount option.

    :param option:
        the option to parse
    :type option: const char \*

.. _`parse_standard_option.description`:

Description
-----------

Normally, standard mount options like "sync" are passed to file-systems as
flags. However, when a "rootflags=" kernel boot parameter is used, they may
be present in the options string. This function tries to deal with this
situation and parse standard options. Returns 0 if the option was not
recognized, and the corresponding integer flag if it was.

UBIFS is only interested in the "sync" option, so do not check for anything
else.

.. _`ubifs_parse_options`:

ubifs_parse_options
===================

.. c:function:: int ubifs_parse_options(struct ubifs_info *c, char *options, int is_remount)

    parse mount parameters.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param options:
        parameters to parse
    :type options: char \*

    :param is_remount:
        non-zero if this is FS re-mount
    :type is_remount: int

.. _`ubifs_parse_options.description`:

Description
-----------

This function parses UBIFS mount options and returns zero in case success
and a negative error code in case of failure.

.. _`destroy_journal`:

destroy_journal
===============

.. c:function:: void destroy_journal(struct ubifs_info *c)

    destroy journal data structures.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`destroy_journal.description`:

Description
-----------

This function destroys journal data structures including those that may have
been created by recovery functions.

.. _`bu_init`:

bu_init
=======

.. c:function:: void bu_init(struct ubifs_info *c)

    initialize bulk-read information.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`check_free_space`:

check_free_space
================

.. c:function:: int check_free_space(struct ubifs_info *c)

    check if there is enough free space to mount.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`check_free_space.description`:

Description
-----------

This function makes sure UBIFS has enough free space to be mounted in
read/write mode. UBIFS must always have some free space to allow deletions.

.. _`mount_ubifs`:

mount_ubifs
===========

.. c:function:: int mount_ubifs(struct ubifs_info *c)

    mount UBIFS file-system.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`mount_ubifs.description`:

Description
-----------

This function mounts UBIFS file system. Returns zero in case of success and
a negative error code in case of failure.

.. _`ubifs_umount`:

ubifs_umount
============

.. c:function:: void ubifs_umount(struct ubifs_info *c)

    un-mount UBIFS file-system.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`ubifs_umount.description`:

Description
-----------

Note, this function is called to free allocated resourced when un-mounting,
as well as free resources when an error occurred while we were half way
through mounting (error path cleanup function). So it has to make sure the
resource was actually allocated before freeing it.

.. _`ubifs_remount_rw`:

ubifs_remount_rw
================

.. c:function:: int ubifs_remount_rw(struct ubifs_info *c)

    re-mount in read-write mode.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`ubifs_remount_rw.description`:

Description
-----------

UBIFS avoids allocating many unnecessary resources when mounted in read-only
mode. This function allocates the needed resources and re-mounts UBIFS in
read-write mode.

.. _`ubifs_remount_ro`:

ubifs_remount_ro
================

.. c:function:: void ubifs_remount_ro(struct ubifs_info *c)

    re-mount in read-only mode.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`ubifs_remount_ro.description`:

Description
-----------

We assume VFS has stopped writing. Possibly the background thread could be
running a commit, however kthread_stop will wait in that case.

.. _`open_ubi`:

open_ubi
========

.. c:function:: struct ubi_volume_desc *open_ubi(const char *name, int mode)

    parse UBI device name string and open the UBI device.

    :param name:
        UBI volume name
    :type name: const char \*

    :param mode:
        UBI volume open mode
    :type mode: int

.. _`open_ubi.description`:

Description
-----------

The primary method of mounting UBIFS is by specifying the UBI volume
character device node path. However, UBIFS may also be mounted withoug any

.. _`open_ubi.character-device-node-using-one-of-the-following-methods`:

character device node using one of the following methods
--------------------------------------------------------


o ubiX_Y    - mount UBI device number X, volume Y;
o ubiY      - mount UBI device number 0, volume Y;
o ubiX:NAME - mount UBI device X, volume with name NAME;
o ubi:NAME  - mount UBI device 0, volume with name NAME.

Alternative '!' separator may be used instead of ':' (because some shells
like busybox may interpret ':' as an NFS host name separator). This function
returns UBI volume description object in case of success and a negative
error code in case of failure.

.. This file was automatic generated / don't edit.

