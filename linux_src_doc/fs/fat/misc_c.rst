.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/fat/misc.c

.. _`fat_msg`:

fat_msg
=======

.. c:function:: void fat_msg(struct super_block *sb, const char *level, const char *fmt,  ...)

    print preformated FAT specific messages. Every thing what is not \ :c:func:`fat_fs_error`\  should be \ :c:func:`fat_msg`\ .

    :param sb:
        *undescribed*
    :type sb: struct super_block \*

    :param level:
        *undescribed*
    :type level: const char \*

    :param fmt:
        *undescribed*
    :type fmt: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. This file was automatic generated / don't edit.

