.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/arch/x86/util/dwarf-regs.c

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

.. This file was automatic generated / don't edit.

