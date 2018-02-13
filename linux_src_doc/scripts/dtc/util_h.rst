.. -*- coding: utf-8; mode: rst -*-
.. src-file: scripts/dtc/util.h

.. _`util_is_printable_string`:

util_is_printable_string
========================

.. c:function:: bool util_is_printable_string(const void *data, int len)

    has a valid terminator. The property can contain either a single string, or multiple strings each of non-zero length.

    :param const void \*data:
        *undescribed*

    :param int len:
        *undescribed*

.. _`util_is_printable_string.description`:

Description
-----------

\ ``param``\  data  The string to check
\ ``param``\  len   The string length including terminator
\ ``return``\  1 if a valid printable string, 0 if not

.. _`utilfdt_read`:

utilfdt_read
============

.. c:function:: char *utilfdt_read(const char *filename)

    stderr.

    :param const char \*filename:
        *undescribed*

.. _`utilfdt_read.description`:

Description
-----------

\ ``param``\  filename      The filename to read, or - for stdin
\ ``return``\  Pointer to allocated buffer containing fdt, or NULL on error

.. _`utilfdt_read_len`:

utilfdt_read_len
================

.. c:function:: char *utilfdt_read_len(const char *filename, off_t *len)

    :param const char \*filename:
        *undescribed*

    :param off_t \*len:
        *undescribed*

.. _`utilfdt_read_len.description`:

Description
-----------

\ ``param``\  len           If non-NULL, the amount of data we managed to read

.. _`utilfdt_read_err`:

utilfdt_read_err
================

.. c:function:: int utilfdt_read_err(const char *filename, char **buffp)

    returns them. The value returned can be passed to \ :c:func:`strerror`\  to obtain an error message for the user.

    :param const char \*filename:
        *undescribed*

    :param char \*\*buffp:
        *undescribed*

.. _`utilfdt_read_err.description`:

Description
-----------

\ ``param``\  filename      The filename to read, or - for stdin
\ ``param``\  buffp         Returns pointer to buffer containing fdt
\ ``return``\  0 if ok, else an errno value representing the error

.. _`utilfdt_read_err_len`:

utilfdt_read_err_len
====================

.. c:function:: int utilfdt_read_err_len(const char *filename, char **buffp, off_t *len)

    :param const char \*filename:
        *undescribed*

    :param char \*\*buffp:
        *undescribed*

    :param off_t \*len:
        *undescribed*

.. _`utilfdt_read_err_len.description`:

Description
-----------

\ ``param``\  len           If non-NULL, the amount of data we managed to read

.. _`utilfdt_write`:

utilfdt_write
=============

.. c:function:: int utilfdt_write(const char *filename, const void *blob)

    stderr.

    :param const char \*filename:
        *undescribed*

    :param const void \*blob:
        *undescribed*

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

    :param const char \*filename:
        *undescribed*

    :param const void \*blob:
        *undescribed*

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

    :param const char \*fmt:
        *undescribed*

    :param int \*type:
        *undescribed*

    :param int \*size:
        *undescribed*

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

    :param const char \*data:
        *undescribed*

    :param int len:
        *undescribed*

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

    :param  void:
        no arguments

.. _`util_usage`:

util_usage
==========

.. c:function:: void NORETURN util_usage(const char *errmsg, const char *synopsis, const char *short_opts, struct option const long_opts, const char * const opts_help)

    :param const char \*errmsg:
        *undescribed*

    :param const char \*synopsis:
        *undescribed*

    :param const char \*short_opts:
        *undescribed*

    :param struct option const long_opts:
        *undescribed*

    :param const char \* const opts_help:
        *undescribed*

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

    :param  errmsg:
        *undescribed*

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

    :param  void:
        no arguments

.. _`util_getopt_long.description`:

Description
-----------

Since all util code runs getopt in the same way, provide a helper.

.. This file was automatic generated / don't edit.

