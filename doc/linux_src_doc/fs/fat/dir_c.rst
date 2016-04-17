.. -*- coding: utf-8; mode: rst -*-

=====
dir.c
=====


.. _`fat_parse_long`:

fat_parse_long
==============

.. c:function:: int fat_parse_long (struct inode *dir, loff_t *pos, struct buffer_head **bh, struct msdos_dir_entry **de, wchar_t **unicode, unsigned char *nr_slots)

    Parse extended directory entry.

    :param struct inode \*dir:

        *undescribed*

    :param loff_t \*pos:

        *undescribed*

    :param struct buffer_head \*\*bh:

        *undescribed*

    :param struct msdos_dir_entry \*\*de:

        *undescribed*

    :param wchar_t \*\*unicode:

        *undescribed*

    :param unsigned char \*nr_slots:

        *undescribed*



.. _`fat_parse_long.description`:

Description
-----------


This function returns zero on success, negative value on error, or one of



.. _`fat_parse_long.the-following`:

the following
-------------


``PARSE_INVALID`` - Directory entry is invalid.
``PARSE_NOT_LONGNAME`` - Directory entry does not contain longname.
``PARSE_EOF`` - Directory has no more entries.



.. _`fat_parse_short`:

fat_parse_short
===============

.. c:function:: int fat_parse_short (struct super_block *sb, const struct msdos_dir_entry *de, unsigned char *name, int dot_hidden)

    Parse MS-DOS (short) directory entry.

    :param struct super_block \*sb:
        superblock

    :param const struct msdos_dir_entry \*de:
        directory entry to parse

    :param unsigned char \*name:
        FAT_MAX_SHORT_SIZE array in which to place extracted name

    :param int dot_hidden:
        Nonzero == prepend '.' to names with ATTR_HIDDEN



.. _`fat_parse_short.description`:

Description
-----------

Returns the number of characters extracted into 'name'.

