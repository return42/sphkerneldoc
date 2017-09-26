.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/fat/misc.c

.. _`fat_msg`:

fat_msg
=======

.. c:function:: void fat_msg(struct super_block *sb, const char *level, const char *fmt,  ...)

    print preformated FAT specific messages. Every thing what is not \ :c:func:`fat_fs_error`\  should be \ :c:func:`fat_msg`\ .

    :param struct super_block \*sb:
        *undescribed*

    :param const char \*level:
        *undescribed*

    :param const char \*fmt:
        *undescribed*

    :param ellipsis ellipsis:
        variable arguments

.. This file was automatic generated / don't edit.

