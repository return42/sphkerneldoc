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

.. This file was automatic generated / don't edit.

