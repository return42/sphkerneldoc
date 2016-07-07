.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/strnlen_user.c

.. _`strnlen_user`:

strnlen_user
============

.. c:function:: long strnlen_user(const char __user *str, long count)

    - Get the size of a user string INCLUDING final NUL.

    :param const char __user \*str:
        The string to measure.

    :param long count:
        Maximum count (including NUL character)

.. _`strnlen_user.context`:

Context
-------

User context only. This function may sleep if pagefaults are
enabled.

.. _`strnlen_user.description`:

Description
-----------

Get the size of a NUL-terminated string in user space.

Returns the size of the string INCLUDING the terminating NUL.
If the string is too long, returns a number larger than \ ``count``\ . User
has to check the return value against "> count".
On exception (or invalid count), returns 0.

NOTE! You should basically never use this function. There is
almost never any valid case for using the length of a user space
string, since the string can be changed at any time by other
threads. Use "\ :c:func:`strncpy_from_user`\ " instead to get a stable copy
of the string.

.. _`strlen_user`:

strlen_user
===========

.. c:function:: long strlen_user(const char __user *str)

    - Get the size of a user string INCLUDING final NUL.

    :param const char __user \*str:
        The string to measure.

.. _`strlen_user.context`:

Context
-------

User context only. This function may sleep if pagefaults are
enabled.

.. _`strlen_user.description`:

Description
-----------

Get the size of a NUL-terminated string in user space.

Returns the size of the string INCLUDING the terminating NUL.
On exception, returns 0.

If there is a limit on the length of a valid string, you may wish to
consider using \ :c:func:`strnlen_user`\  instead.

.. This file was automatic generated / don't edit.

