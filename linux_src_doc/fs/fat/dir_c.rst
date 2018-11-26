.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/fat/dir.c

.. _`fat_parse_long`:

fat_parse_long
==============

.. c:function:: int fat_parse_long(struct inode *dir, loff_t *pos, struct buffer_head **bh, struct msdos_dir_entry **de, wchar_t **unicode, unsigned char *nr_slots)

    Parse extended directory entry.

    :param dir:
        *undescribed*
    :type dir: struct inode \*

    :param pos:
        *undescribed*
    :type pos: loff_t \*

    :param bh:
        *undescribed*
    :type bh: struct buffer_head \*\*

    :param de:
        *undescribed*
    :type de: struct msdos_dir_entry \*\*

    :param unicode:
        *undescribed*
    :type unicode: wchar_t \*\*

    :param nr_slots:
        *undescribed*
    :type nr_slots: unsigned char \*

.. _`fat_parse_long.description`:

Description
-----------

This function returns zero on success, negative value on error, or one of

.. _`fat_parse_long.the-following`:

the following
-------------


\ ``PARSE_INVALID``\  - Directory entry is invalid.
\ ``PARSE_NOT_LONGNAME``\  - Directory entry does not contain longname.
\ ``PARSE_EOF``\  - Directory has no more entries.

.. _`fat_parse_short`:

fat_parse_short
===============

.. c:function:: int fat_parse_short(struct super_block *sb, const struct msdos_dir_entry *de, unsigned char *name, int dot_hidden)

    Parse MS-DOS (short) directory entry.

    :param sb:
        superblock
    :type sb: struct super_block \*

    :param de:
        directory entry to parse
    :type de: const struct msdos_dir_entry \*

    :param name:
        FAT_MAX_SHORT_SIZE array in which to place extracted name
    :type name: unsigned char \*

    :param dot_hidden:
        Nonzero == prepend '.' to names with ATTR_HIDDEN
    :type dot_hidden: int

.. _`fat_parse_short.description`:

Description
-----------

Returns the number of characters extracted into 'name'.

.. This file was automatic generated / don't edit.

