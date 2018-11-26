.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/lib/cmdline.c

.. _`__cmdline_find_option_bool`:

\__cmdline_find_option_bool
===========================

.. c:function:: int __cmdline_find_option_bool(const char *cmdline, int max_cmdline_size, const char *option)

    :param cmdline:
        the cmdline string
    :type cmdline: const char \*

    :param max_cmdline_size:
        *undescribed*
    :type max_cmdline_size: int

    :param option:
        option string to look for
    :type option: const char \*

.. _`__cmdline_find_option_bool.description`:

Description
-----------

Returns the position of that \ ``option``\  (starts counting with 1)
or 0 on not found.  \ ``option``\  will only be found if it is found
as an entire word in \ ``cmdline``\ .  For instance, if \ ``option``\ ="car"
then a cmdline which contains "cart" will not match.

.. This file was automatic generated / don't edit.

