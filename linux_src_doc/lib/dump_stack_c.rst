.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/dump_stack.c

.. _`dump_stack_set_arch_desc`:

dump_stack_set_arch_desc
========================

.. c:function:: void dump_stack_set_arch_desc(const char *fmt,  ...)

    set arch-specific str to show with task dumps

    :param fmt:
        printf-style format string
    :type fmt: const char \*

    :param ellipsis ellipsis:
        arguments for the format string

.. _`dump_stack_set_arch_desc.description`:

Description
-----------

The configured string will be printed right after utsname during task
dumps.  Usually used to add arch-specific system identifiers.  If an
arch wants to make use of such an ID string, it should initialize this
as soon as possible during boot.

.. _`dump_stack_print_info`:

dump_stack_print_info
=====================

.. c:function:: void dump_stack_print_info(const char *log_lvl)

    print generic debug info for \ :c:func:`dump_stack`\ 

    :param log_lvl:
        log level
    :type log_lvl: const char \*

.. _`dump_stack_print_info.description`:

Description
-----------

Arch-specific \ :c:func:`dump_stack`\  implementations can use this function to
print out the same debug information as the generic \ :c:func:`dump_stack`\ .

.. _`show_regs_print_info`:

show_regs_print_info
====================

.. c:function:: void show_regs_print_info(const char *log_lvl)

    print generic debug info for \ :c:func:`show_regs`\ 

    :param log_lvl:
        log level
    :type log_lvl: const char \*

.. _`show_regs_print_info.description`:

Description
-----------

\ :c:func:`show_regs`\  implementations can use this function to print out generic
debug information.

.. This file was automatic generated / don't edit.

