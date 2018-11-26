.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/realpath.c

.. _`tomoyo_encode2`:

tomoyo_encode2
==============

.. c:function:: char *tomoyo_encode2(const char *str, int str_len)

    Encode binary string to ascii string.

    :param str:
        String in binary format.
    :type str: const char \*

    :param str_len:
        Size of \ ``str``\  in byte.
    :type str_len: int

.. _`tomoyo_encode2.description`:

Description
-----------

Returns pointer to \ ``str``\  in ascii format on success, NULL otherwise.

This function uses \ :c:func:`kzalloc`\ , so caller must \ :c:func:`kfree`\  if this function
didn't return NULL.

.. _`tomoyo_encode`:

tomoyo_encode
=============

.. c:function:: char *tomoyo_encode(const char *str)

    Encode binary string to ascii string.

    :param str:
        String in binary format.
    :type str: const char \*

.. _`tomoyo_encode.description`:

Description
-----------

Returns pointer to \ ``str``\  in ascii format on success, NULL otherwise.

This function uses \ :c:func:`kzalloc`\ , so caller must \ :c:func:`kfree`\  if this function
didn't return NULL.

.. _`tomoyo_get_absolute_path`:

tomoyo_get_absolute_path
========================

.. c:function:: char *tomoyo_get_absolute_path(const struct path *path, char * const buffer, const int buflen)

    Get the path of a dentry but ignores chroot'ed root.

    :param path:
        Pointer to "struct path".
    :type path: const struct path \*

    :param buffer:
        Pointer to buffer to return value in.
    :type buffer: char \* const

    :param buflen:
        Sizeof \ ``buffer``\ .
    :type buflen: const int

.. _`tomoyo_get_absolute_path.description`:

Description
-----------

Returns the buffer on success, an error code otherwise.

If dentry is a directory, trailing '/' is appended.

.. _`tomoyo_get_dentry_path`:

tomoyo_get_dentry_path
======================

.. c:function:: char *tomoyo_get_dentry_path(struct dentry *dentry, char * const buffer, const int buflen)

    Get the path of a dentry.

    :param dentry:
        Pointer to "struct dentry".
    :type dentry: struct dentry \*

    :param buffer:
        Pointer to buffer to return value in.
    :type buffer: char \* const

    :param buflen:
        Sizeof \ ``buffer``\ .
    :type buflen: const int

.. _`tomoyo_get_dentry_path.description`:

Description
-----------

Returns the buffer on success, an error code otherwise.

If dentry is a directory, trailing '/' is appended.

.. _`tomoyo_get_local_path`:

tomoyo_get_local_path
=====================

.. c:function:: char *tomoyo_get_local_path(struct dentry *dentry, char * const buffer, const int buflen)

    Get the path of a dentry.

    :param dentry:
        Pointer to "struct dentry".
    :type dentry: struct dentry \*

    :param buffer:
        Pointer to buffer to return value in.
    :type buffer: char \* const

    :param buflen:
        Sizeof \ ``buffer``\ .
    :type buflen: const int

.. _`tomoyo_get_local_path.description`:

Description
-----------

Returns the buffer on success, an error code otherwise.

.. _`tomoyo_get_socket_name`:

tomoyo_get_socket_name
======================

.. c:function:: char *tomoyo_get_socket_name(const struct path *path, char * const buffer, const int buflen)

    Get the name of a socket.

    :param path:
        Pointer to "struct path".
    :type path: const struct path \*

    :param buffer:
        Pointer to buffer to return value in.
    :type buffer: char \* const

    :param buflen:
        Sizeof \ ``buffer``\ .
    :type buflen: const int

.. _`tomoyo_get_socket_name.description`:

Description
-----------

Returns the buffer.

.. _`tomoyo_realpath_from_path`:

tomoyo_realpath_from_path
=========================

.. c:function:: char *tomoyo_realpath_from_path(const struct path *path)

    Returns realpath(3) of the given pathname but ignores chroot'ed root.

    :param path:
        Pointer to "struct path".
    :type path: const struct path \*

.. _`tomoyo_realpath_from_path.description`:

Description
-----------

Returns the realpath of the given \ ``path``\  on success, NULL otherwise.

If dentry is a directory, trailing '/' is appended.
Characters out of 0x20 < c < 0x7F range are converted to
\ooo style octal string.
Character \ is converted to \\ string.

These functions use \ :c:func:`kzalloc`\ , so the caller must call \ :c:func:`kfree`\ 
if these functions didn't return NULL.

.. _`tomoyo_realpath_nofollow`:

tomoyo_realpath_nofollow
========================

.. c:function:: char *tomoyo_realpath_nofollow(const char *pathname)

    Get realpath of a pathname.

    :param pathname:
        The pathname to solve.
    :type pathname: const char \*

.. _`tomoyo_realpath_nofollow.description`:

Description
-----------

Returns the realpath of \ ``pathname``\  on success, NULL otherwise.

.. This file was automatic generated / don't edit.

