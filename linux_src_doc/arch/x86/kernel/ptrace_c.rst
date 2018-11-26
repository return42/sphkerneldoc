.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/ptrace.c

.. _`regs_query_register_offset`:

regs_query_register_offset
==========================

.. c:function:: int regs_query_register_offset(const char *name)

    query register offset from its name

    :param name:
        the name of a register
    :type name: const char \*

.. _`regs_query_register_offset.description`:

Description
-----------

\ :c:func:`regs_query_register_offset`\  returns the offset of a register in struct
pt_regs from its name. If the name is invalid, this returns -EINVAL;

.. _`regs_query_register_name`:

regs_query_register_name
========================

.. c:function:: const char *regs_query_register_name(unsigned int offset)

    query register name from its offset

    :param offset:
        the offset of a register in struct pt_regs.
    :type offset: unsigned int

.. _`regs_query_register_name.description`:

Description
-----------

\ :c:func:`regs_query_register_name`\  returns the name of a register from its
offset in struct pt_regs. If the \ ``offset``\  is invalid, this returns NULL;

.. This file was automatic generated / don't edit.

