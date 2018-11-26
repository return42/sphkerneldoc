.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/hexdump.c

.. _`hex_to_bin`:

hex_to_bin
==========

.. c:function:: int hex_to_bin(char ch)

    convert a hex digit to its real value

    :param ch:
        ascii character represents hex digit
    :type ch: char

.. _`hex_to_bin.description`:

Description
-----------

\ :c:func:`hex_to_bin`\  converts one hex digit to its actual value or -1 in case of bad
input.

.. _`hex2bin`:

hex2bin
=======

.. c:function:: int hex2bin(u8 *dst, const char *src, size_t count)

    convert an ascii hexadecimal string to its binary representation

    :param dst:
        binary result
    :type dst: u8 \*

    :param src:
        ascii hexadecimal string
    :type src: const char \*

    :param count:
        result length
    :type count: size_t

.. _`hex2bin.description`:

Description
-----------

Return 0 on success, -EINVAL in case of bad input.

.. _`bin2hex`:

bin2hex
=======

.. c:function:: char *bin2hex(char *dst, const void *src, size_t count)

    convert binary data to an ascii hexadecimal string

    :param dst:
        ascii hexadecimal result
    :type dst: char \*

    :param src:
        binary data
    :type src: const void \*

    :param count:
        binary data length
    :type count: size_t

.. _`hex_dump_to_buffer`:

hex_dump_to_buffer
==================

.. c:function:: int hex_dump_to_buffer(const void *buf, size_t len, int rowsize, int groupsize, char *linebuf, size_t linebuflen, bool ascii)

    convert a blob of data to "hex ASCII" in memory

    :param buf:
        data blob to dump
    :type buf: const void \*

    :param len:
        number of bytes in the \ ``buf``\ 
    :type len: size_t

    :param rowsize:
        number of bytes to print per line; must be 16 or 32
    :type rowsize: int

    :param groupsize:
        number of bytes to print at a time (1, 2, 4, 8; default = 1)
    :type groupsize: int

    :param linebuf:
        where to put the converted data
    :type linebuf: char \*

    :param linebuflen:
        total size of \ ``linebuf``\ , including space for terminating NUL
    :type linebuflen: size_t

    :param ascii:
        include ASCII after the hex output
    :type ascii: bool

.. _`hex_dump_to_buffer.description`:

Description
-----------

\ :c:func:`hex_dump_to_buffer`\  works on one "line" of output at a time, i.e.,
16 or 32 bytes of input data converted to hex + ASCII output.

Given a buffer of u8 data, \ :c:func:`hex_dump_to_buffer`\  converts the input data
to a hex + ASCII dump at the supplied memory location.
The converted output is always NUL-terminated.

E.g.:
hex_dump_to_buffer(frame->data, frame->len, 16, 1,
linebuf, sizeof(linebuf), true);

.. _`hex_dump_to_buffer.example-output-buffer`:

example output buffer
---------------------

40 41 42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e 4f  \ ``ABCDEFGHIJKLMNO``\ 

.. _`hex_dump_to_buffer.return`:

Return
------

The amount of bytes placed in the buffer without terminating NUL. If the
output was truncated, then the return value is the number of bytes
(excluding the terminating NUL) which would have been written to the final
string if enough space had been available.

.. _`print_hex_dump`:

print_hex_dump
==============

.. c:function:: void print_hex_dump(const char *level, const char *prefix_str, int prefix_type, int rowsize, int groupsize, const void *buf, size_t len, bool ascii)

    print a text hex dump to syslog for a binary blob of data

    :param level:
        kernel log level (e.g. KERN_DEBUG)
    :type level: const char \*

    :param prefix_str:
        string to prefix each line with;
        caller supplies trailing spaces for alignment if desired
    :type prefix_str: const char \*

    :param prefix_type:
        controls whether prefix of an offset, address, or none
        is printed (%DUMP_PREFIX_OFFSET, \ ``DUMP_PREFIX_ADDRESS``\ , \ ``DUMP_PREFIX_NONE``\ )
    :type prefix_type: int

    :param rowsize:
        number of bytes to print per line; must be 16 or 32
    :type rowsize: int

    :param groupsize:
        number of bytes to print at a time (1, 2, 4, 8; default = 1)
    :type groupsize: int

    :param buf:
        data blob to dump
    :type buf: const void \*

    :param len:
        number of bytes in the \ ``buf``\ 
    :type len: size_t

    :param ascii:
        include ASCII after the hex output
    :type ascii: bool

.. _`print_hex_dump.description`:

Description
-----------

Given a buffer of u8 data, \ :c:func:`print_hex_dump`\  prints a hex + ASCII dump
to the kernel log at the specified kernel log level, with an optional
leading prefix.

\ :c:func:`print_hex_dump`\  works on one "line" of output at a time, i.e.,
16 or 32 bytes of input data converted to hex + ASCII output.
\ :c:func:`print_hex_dump`\  iterates over the entire input \ ``buf``\ , breaking it into
"line size" chunks to format and print.

E.g.:
print_hex_dump(KERN_DEBUG, "raw data: ", DUMP_PREFIX_ADDRESS,
16, 1, frame->data, frame->len, true);

Example output using \ ``DUMP_PREFIX_OFFSET``\  and 1-byte mode:

.. _`print_hex_dump.0009ab42`:

0009ab42
--------

40 41 42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e 4f  \ ``ABCDEFGHIJKLMNO``\ 
Example output using \ ``DUMP_PREFIX_ADDRESS``\  and 4-byte mode:

.. _`print_hex_dump.ffffffff88089af0`:

ffffffff88089af0
----------------

73727170 77767574 7b7a7978 7f7e7d7c  pqrstuvwxyz{\|}~.

.. _`print_hex_dump_bytes`:

print_hex_dump_bytes
====================

.. c:function:: void print_hex_dump_bytes(const char *prefix_str, int prefix_type, const void *buf, size_t len)

    shorthand form of \ :c:func:`print_hex_dump`\  with default params

    :param prefix_str:
        string to prefix each line with;
        caller supplies trailing spaces for alignment if desired
    :type prefix_str: const char \*

    :param prefix_type:
        controls whether prefix of an offset, address, or none
        is printed (%DUMP_PREFIX_OFFSET, \ ``DUMP_PREFIX_ADDRESS``\ , \ ``DUMP_PREFIX_NONE``\ )
    :type prefix_type: int

    :param buf:
        data blob to dump
    :type buf: const void \*

    :param len:
        number of bytes in the \ ``buf``\ 
    :type len: size_t

.. _`print_hex_dump_bytes.description`:

Description
-----------

Calls \ :c:func:`print_hex_dump`\ , with log level of KERN_DEBUG,
rowsize of 16, groupsize of 1, and ASCII output included.

.. This file was automatic generated / don't edit.

