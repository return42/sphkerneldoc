.. -*- coding: utf-8; mode: rst -*-
.. src-file: scripts/dtc/util.h

.. _`util_is_printable_string`:

util_is_printable_string
========================

.. c:function:: bool util_is_printable_string(const void *data, int len)

    has a valid terminator. The property can contain either a single string, or multiple strings each of non-zero length.

    :param data:
        *undescribed*
    :type data: const void \*

    :param len:
        *undescribed*
    :type len: int

.. _`util_is_printable_string.description`:

Description
-----------

\ ``param``\  data  The string to check
\ ``param``\  len   The string length including terminator
\ ``return``\  1 if a valid printable string, 0 if not

.. _`utilfdt_read`:

utilfdt_read
============

.. c:function:: char *utilfdt_read(const char *filename, size_t *len)

    stderr.

    :param filename:
        *undescribed*
    :type filename: const char \*

    :param len:
        *undescribed*
    :type len: size_t \*

.. _`utilfdt_read.description`:

Description
-----------

\ ``param``\  filename      The filename to read, or - for stdin
\ ``param``\  len           If non-NULL, the amount of data we managed to read
\ ``return``\  Pointer to allocated buffer containing fdt, or NULL on error

.. _`utilfdt_read_err`:

utilfdt_read_err
================

.. c:function:: int utilfdt_read_err(const char *filename, char **buffp, size_t *len)

    returns them. The value returned can be passed to \ :c:func:`strerror`\  to obtain an error message for the user.

    :param filename:
        *undescribed*
    :type filename: const char \*

    :param buffp:
        *undescribed*
    :type buffp: char \*\*

    :param len:
        *undescribed*
    :type len: size_t \*

.. _`utilfdt_read_err.description`:

Description
-----------

\ ``param``\  filename      The filename to read, or - for stdin
\ ``param``\  buffp         Returns pointer to buffer containing fdt
\ ``param``\  len           If non-NULL, the amount of data we managed to read
\ ``return``\  0 if ok, else an errno value representing the error

.. _`utilfdt_write`:

utilfdt_write
=============

.. c:function:: int utilfdt_write(const char *filename, const void *blob)

    stderr.

    :param filename:
        *undescribed*
    :type filename: const char \*

    :param blob:
        *undescribed*
    :type blob: const void \*

.. _`utilfdt_write.description`:

Description
-----------

\ ``param``\  filename      The filename to write, or - for stdout
\ ``param``\  blob          Poiner to buffer containing fdt
\ ``return``\  0 if ok, -1 on error

.. _`utilfdt_write_err`:

utilfdt_write_err
=================

.. c:function:: int utilfdt_write_err(const char *filename, const void *blob)

    returns them. The value returned can be passed to \ :c:func:`strerror`\  to obtain an error message for the user.

    :param filename:
        *undescribed*
    :type filename: const char \*

    :param blob:
        *undescribed*
    :type blob: const void \*

.. _`utilfdt_write_err.description`:

Description
-----------

\ ``param``\  filename      The filename to write, or - for stdout
\ ``param``\  blob          Poiner to buffer containing fdt
\ ``return``\  0 if ok, else an errno value representing the error

.. _`utilfdt_decode_type`:

utilfdt_decode_type
===================

.. c:function:: int utilfdt_decode_type(const char *fmt, int *type, int *size)

    :param fmt:
        *undescribed*
    :type fmt: const char \*

    :param type:
        *undescribed*
    :type type: int \*

    :param size:
        *undescribed*
    :type size: int \*

.. _`utilfdt_decode_type.modifier-characters`:

Modifier characters
-------------------

hh or b 1 byte
h       2 byte
l       4 byte, default

.. _`utilfdt_decode_type.type-character`:

Type character
--------------

s       string
i       signed integer
u       unsigned integer
x       hex

.. _`utilfdt_decode_type.todo`:

TODO
----

Implement ll modifier (8 bytes)

Implement o type (octal)

\ ``param``\  fmt           Format string to process
\ ``param``\  type          Returns type found(s/d/u/x), or 0 if none
\ ``param``\  size          Returns size found(1,2,4,8) or 4 if none
\ ``return``\  0 if ok, -1 on error (no type given, or other invalid format)

.. _`utilfdt_print_data`:

utilfdt_print_data
==================

.. c:function:: void utilfdt_print_data(const char *data, int len)

    :param data:
        *undescribed*
    :type data: const char \*

    :param len:
        *undescribed*
    :type len: int

.. _`utilfdt_print_data.description`:

Description
-----------

Properties that look like strings will be printed as strings. Otherwise
the data will be displayed either as cells (if len is a multiple of 4
bytes) or bytes.

If len is 0 then this function does nothing.

\ ``param``\  data  Pointers to property data
\ ``param``\  len   Length of property data

.. _`util_version`:

util_version
============

.. c:function:: void NORETURN util_version( void)

    :param void:
        no arguments
    :type void: 

.. _`util_usage`:

util_usage
==========

.. c:function:: void NORETURN util_usage(const char *errmsg, const char *synopsis, const char *short_opts, struct option const long_opts, const char * const opts_help)

    :param errmsg:
        *undescribed*
    :type errmsg: const char \*

    :param synopsis:
        *undescribed*
    :type synopsis: const char \*

    :param short_opts:
        *undescribed*
    :type short_opts: const char \*

    :param long_opts:
        *undescribed*
    :type long_opts: struct option const

    :param opts_help:
        *undescribed*
    :type opts_help: const char \* const

.. _`util_usage.description`:

Description
-----------

This helps standardize the output of various utils.  You most likely want
to use the \ :c:func:`usage`\  helper below rather than call this.

\ ``param``\  errmsg        If non-NULL, an error message to display
\ ``param``\  synopsis      The initial example usage text (and possible examples)
\ ``param``\  short_opts    The string of short options
\ ``param``\  long_opts     The structure of long options
\ ``param``\  opts_help     An array of help strings (should align with long_opts)

.. _`usage`:

usage
=====

.. c:function::  usage( errmsg)

    :param errmsg:
        *undescribed*
    :type errmsg: 

.. _`usage.description`:

Description
-----------

If you name all your usage variables with usage_xxx, then you can call this
help macro rather than expanding all arguments yourself.

\ ``param``\  errmsg        If non-NULL, an error message to display

.. _`util_getopt_long`:

util_getopt_long
================

.. c:function::  util_getopt_long( void)

    :param void:
        no arguments
    :type void: 

.. _`util_getopt_long.description`:

Description
-----------

Since all util code runs getopt in the same way, provide a helper.

.. This file was automatic generated / don't edit.

