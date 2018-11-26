.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firewire/core-device.c

.. _`fw_csr_string`:

fw_csr_string
=============

.. c:function:: int fw_csr_string(const u32 *directory, int key, char *buf, size_t size)

    reads a string from the configuration ROM

    :param directory:
        e.g. root directory or unit directory
    :type directory: const u32 \*

    :param key:
        the key of the preceding directory entry
    :type key: int

    :param buf:
        where to put the string
    :type buf: char \*

    :param size:
        size of \ ``buf``\ , in bytes
    :type size: size_t

.. _`fw_csr_string.description`:

Description
-----------

The string is taken from a minimal ASCII text descriptor leaf after
the immediate entry with \ ``key``\ .  The string is zero-terminated.
An overlong string is silently truncated such that it and the
zero byte fit into \ ``size``\ .

Returns strlen(buf) or a negative error code.

.. This file was automatic generated / don't edit.

