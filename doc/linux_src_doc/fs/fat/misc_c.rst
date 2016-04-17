.. -*- coding: utf-8; mode: rst -*-

======
misc.c
======


.. _`fat_msg`:

fat_msg
=======

.. c:function:: void fat_msg (struct super_block *sb, const char *level, const char *fmt,  ...)

    print preformated FAT specific messages. Every thing what is not fat_fs_error() should be fat_msg().

    :param struct super_block \*sb:

        *undescribed*

    :param const char \*level:

        *undescribed*

    :param const char \*fmt:

        *undescribed*

    :param ...:
        variable arguments

