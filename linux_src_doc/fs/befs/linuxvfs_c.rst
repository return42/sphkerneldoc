.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/befs/linuxvfs.c

.. _`befs_nls2utf`:

befs_nls2utf
============

.. c:function:: int befs_nls2utf(struct super_block *sb, const char *in, int in_len, char **out, int *out_len)

    Convert NLS string to utf8 encodeing

    :param sb:
        Superblock
    :type sb: struct super_block \*

    :param in:
        Input string buffer in NLS format
    :type in: const char \*

    :param in_len:
        Length of input string in bytes
    :type in_len: int

    :param out:
        The output string in UTF-8 format
    :type out: char \*\*

    :param out_len:
        Length of the output buffer
    :type out_len: int \*

.. _`befs_nls2utf.description`:

Description
-----------

Converts input string \ ``in``\ , which is in the format of the loaded NLS map,
into a utf8 string.

The destination string \ ``out``\  is allocated by this function and the caller is
responsible for freeing it with \ :c:func:`kfree`\ 

On return, \*@out_len is the length of \ ``out``\  in bytes.

On success, the return value is the number of utf8 characters written to
the output buffer \ ``out``\ .

On Failure, a negative number coresponding to the error code is returned.

.. This file was automatic generated / don't edit.

