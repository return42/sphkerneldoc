.. -*- coding: utf-8; mode: rst -*-

=============
core-device.c
=============


.. _`fw_csr_string`:

fw_csr_string
=============

.. c:function:: int fw_csr_string (const u32 *directory, int key, char *buf, size_t size)

    reads a string from the configuration ROM

    :param const u32 \*directory:
        e.g. root directory or unit directory

    :param int key:
        the key of the preceding directory entry

    :param char \*buf:
        where to put the string

    :param size_t size:
        size of ``buf``\ , in bytes



.. _`fw_csr_string.description`:

Description
-----------

The string is taken from a minimal ASCII text descriptor leaf after
the immediate entry with ``key``\ .  The string is zero-terminated.
An overlong string is silently truncated such that it and the
zero byte fit into ``size``\ .

Returns strlen(buf) or a negative error code.

