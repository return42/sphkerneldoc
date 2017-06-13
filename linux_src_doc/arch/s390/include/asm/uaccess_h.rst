.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/include/asm/uaccess.h

.. _`strlen_user`:

strlen_user
===========

.. c:function::  strlen_user( str)

    - Get the size of a string in user space.

    :param  str:
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

