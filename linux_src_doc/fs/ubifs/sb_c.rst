.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/sb.c

.. _`create_default_filesystem`:

create_default_filesystem
=========================

.. c:function:: int create_default_filesystem(struct ubifs_info *c)

    format empty UBI volume.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`create_default_filesystem.description`:

Description
-----------

This function creates default empty file-system. Returns zero in case of
success and a negative error code in case of failure.

.. _`validate_sb`:

validate_sb
===========

.. c:function:: int validate_sb(struct ubifs_info *c, struct ubifs_sb_node *sup)

    validate superblock node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_sb_node \*sup:
        superblock node

.. _`validate_sb.description`:

Description
-----------

This function validates superblock node \ ``sup``\ . Since most of data was read
from the superblock and stored in \ ``c``\ , the function validates fields in \ ``c``\ 
instead. Returns zero in case of success and \ ``-EINVAL``\  in case of validation
failure.

.. _`ubifs_read_sb_node`:

ubifs_read_sb_node
==================

.. c:function:: struct ubifs_sb_node *ubifs_read_sb_node(struct ubifs_info *c)

    read superblock node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_read_sb_node.description`:

Description
-----------

This function returns a pointer to the superblock node or a negative error
code. Note, the user of this function is responsible of \ :c:func:`kfree`\ 'ing the
returned superblock buffer.

.. _`ubifs_write_sb_node`:

ubifs_write_sb_node
===================

.. c:function:: int ubifs_write_sb_node(struct ubifs_info *c, struct ubifs_sb_node *sup)

    write superblock node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_sb_node \*sup:
        superblock node read with '\ :c:func:`ubifs_read_sb_node`\ '

.. _`ubifs_write_sb_node.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`ubifs_read_superblock`:

ubifs_read_superblock
=====================

.. c:function:: int ubifs_read_superblock(struct ubifs_info *c)

    read superblock.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_read_superblock.description`:

Description
-----------

This function finds, reads and checks the superblock. If an empty UBI volume
is being mounted, this function creates default superblock. Returns zero in
case of success, and a negative error code in case of failure.

.. _`fixup_leb`:

fixup_leb
=========

.. c:function:: int fixup_leb(struct ubifs_info *c, int lnum, int len)

    fixup/unmap an LEB containing free space.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        the LEB number to fix up

    :param int len:
        number of used bytes in LEB (starting at offset 0)

.. _`fixup_leb.description`:

Description
-----------

This function reads the contents of the given LEB number \ ``lnum``\ , then fixes
it up, so that empty min. I/O units in the end of LEB are actually erased on
flash (rather than being just all-0xff real data). If the LEB is completely
empty, it is simply unmapped.

.. _`fixup_free_space`:

fixup_free_space
================

.. c:function:: int fixup_free_space(struct ubifs_info *c)

    find & remap all LEBs containing free space.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`fixup_free_space.description`:

Description
-----------

This function walks through all LEBs in the filesystem and fiexes up those
containing free/empty space.

.. _`ubifs_fixup_free_space`:

ubifs_fixup_free_space
======================

.. c:function:: int ubifs_fixup_free_space(struct ubifs_info *c)

    find & fix all LEBs with free space.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_fixup_free_space.description`:

Description
-----------

This function fixes up LEBs containing free space on first mount, if the
appropriate flag was set when the FS was created. Each LEB with one or more
empty min. I/O unit (i.e. free-space-count > 0) is re-written, to make sure
the free space is actually erased. E.g., this is necessary for some NAND
chips, since the free space may have been programmed like real "0xff" data
(generating a non-0xff ECC), causing future writes to the not-really-erased
NAND pages to behave badly. After the space is fixed up, the superblock flag
is cleared, so that this is skipped for all future mounts.

.. This file was automatic generated / don't edit.

