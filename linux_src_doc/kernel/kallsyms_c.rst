.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/kallsyms.c

.. _`sprint_symbol`:

sprint_symbol
=============

.. c:function:: int sprint_symbol(char *buffer, unsigned long address)

    Look up a kernel symbol and return it in a text buffer

    :param buffer:
        buffer to be stored
    :type buffer: char \*

    :param address:
        address to lookup
    :type address: unsigned long

.. _`sprint_symbol.description`:

Description
-----------

This function looks up a kernel symbol with \ ``address``\  and stores its name,
offset, size and module name to \ ``buffer``\  if possible. If no symbol was found,
just saves its \ ``address``\  as is.

This function returns the number of bytes stored in \ ``buffer``\ .

.. _`sprint_symbol_no_offset`:

sprint_symbol_no_offset
=======================

.. c:function:: int sprint_symbol_no_offset(char *buffer, unsigned long address)

    Look up a kernel symbol and return it in a text buffer

    :param buffer:
        buffer to be stored
    :type buffer: char \*

    :param address:
        address to lookup
    :type address: unsigned long

.. _`sprint_symbol_no_offset.description`:

Description
-----------

This function looks up a kernel symbol with \ ``address``\  and stores its name
and module name to \ ``buffer``\  if possible. If no symbol was found, just saves
its \ ``address``\  as is.

This function returns the number of bytes stored in \ ``buffer``\ .

.. _`sprint_backtrace`:

sprint_backtrace
================

.. c:function:: int sprint_backtrace(char *buffer, unsigned long address)

    Look up a backtrace symbol and return it in a text buffer

    :param buffer:
        buffer to be stored
    :type buffer: char \*

    :param address:
        address to lookup
    :type address: unsigned long

.. _`sprint_backtrace.description`:

Description
-----------

This function is for stack backtrace and does the same thing as
\ :c:func:`sprint_symbol`\  but with modified/decreased \ ``address``\ . If there is a
tail-call to the function marked "noreturn", gcc optimized out code after
the call so that the stack-saved return address could point outside of the
caller. This function ensures that kallsyms will find the original caller
by decreasing \ ``address``\ .

This function returns the number of bytes stored in \ ``buffer``\ .

.. This file was automatic generated / don't edit.

