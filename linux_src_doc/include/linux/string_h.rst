.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/string.h

.. _`sysfs_match_string`:

sysfs_match_string
==================

.. c:function::  sysfs_match_string( _a,  _s)

    matches given string in an array

    :param  _a:
        array of strings

    :param  _s:
        string to match with

.. _`sysfs_match_string.description`:

Description
-----------

Helper for \__sysfs_match_string(). Calculates the size of \ ``a``\  automatically.

.. _`strstarts`:

strstarts
=========

.. c:function:: bool strstarts(const char *str, const char *prefix)

    does \ ``str``\  start with \ ``prefix``\ ?

    :param const char \*str:
        string to examine

    :param const char \*prefix:
        prefix to look for.

.. _`kbasename`:

kbasename
=========

.. c:function:: const char *kbasename(const char *path)

    return the last part of a pathname.

    :param const char \*path:
        path to extract the filename from.

.. _`memcpy_and_pad`:

memcpy_and_pad
==============

.. c:function:: void memcpy_and_pad(void *dest, size_t dest_len, const void *src, size_t count, int pad)

    Copy one buffer to another with padding

    :param void \*dest:
        Where to copy to

    :param size_t dest_len:
        The destination buffer size

    :param const void \*src:
        Where to copy from

    :param size_t count:
        The number of bytes to copy

    :param int pad:
        Character to use for padding if space is left in destination.

.. This file was automatic generated / don't edit.

