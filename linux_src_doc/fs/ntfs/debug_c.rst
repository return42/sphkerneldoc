.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/debug.c

.. _`__ntfs_warning`:

__ntfs_warning
==============

.. c:function:: void __ntfs_warning(const char *function, const struct super_block *sb, const char *fmt,  ...)

    output a warning to the syslog

    :param const char \*function:
        name of function outputting the warning

    :param const struct super_block \*sb:
        super block of mounted ntfs filesystem

    :param const char \*fmt:
        warning string containing format specifications

    :param ... :
        a variable number of arguments specified in \ ``fmt``\ 

.. _`__ntfs_warning.description`:

Description
-----------

Outputs a warning to the syslog for the mounted ntfs filesystem described
by \ ``sb``\ .

\ ``fmt``\  and the corresponding @... is printf style format string containing
the warning string and the corresponding format arguments, respectively.

\ ``function``\  is the name of the function from which \__ntfs_warning is being
called.

Note, you should be using debug.h::ntfs_warning(\ ``sb``\ , \ ``fmt``\ , @...) instead
as this provides the \ ``function``\  parameter automatically.

.. _`__ntfs_error`:

__ntfs_error
============

.. c:function:: void __ntfs_error(const char *function, const struct super_block *sb, const char *fmt,  ...)

    output an error to the syslog

    :param const char \*function:
        name of function outputting the error

    :param const struct super_block \*sb:
        super block of mounted ntfs filesystem

    :param const char \*fmt:
        error string containing format specifications

    :param ... :
        a variable number of arguments specified in \ ``fmt``\ 

.. _`__ntfs_error.description`:

Description
-----------

Outputs an error to the syslog for the mounted ntfs filesystem described
by \ ``sb``\ .

\ ``fmt``\  and the corresponding @... is printf style format string containing
the error string and the corresponding format arguments, respectively.

\ ``function``\  is the name of the function from which \__ntfs_error is being
called.

Note, you should be using debug.h::ntfs_error(\ ``sb``\ , \ ``fmt``\ , @...) instead
as this provides the \ ``function``\  parameter automatically.

.. This file was automatic generated / don't edit.

