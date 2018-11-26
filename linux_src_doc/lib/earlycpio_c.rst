.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/earlycpio.c

.. _`find_cpio_data`:

find_cpio_data
==============

.. c:function:: struct cpio_data find_cpio_data(const char *path, void *data, size_t len, long *nextoff)

    Search for files in an uncompressed cpio

    :param path:
        The directory to search for, including a slash at the end
    :type path: const char \*

    :param data:
        Pointer to the the cpio archive or a header inside
    :type data: void \*

    :param len:
        Remaining length of the cpio based on data pointer
    :type len: size_t

    :param nextoff:
        When a matching file is found, this is the offset from the
        beginning of the cpio to the beginning of the next file, not the
        matching file itself. It can be used to iterate through the cpio
        to find all files inside of a directory path.
    :type nextoff: long \*

.. This file was automatic generated / don't edit.

