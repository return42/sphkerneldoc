.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/arch/arm/util/dwarf-regs.c

.. _`get_arch_regstr`:

get_arch_regstr
===============

.. c:function:: const char *get_arch_regstr(unsigned int n)

    lookup register name from it's DWARF register number

    :param unsigned int n:
        the DWARF register number

.. _`get_arch_regstr.description`:

Description
-----------

get_arch_regstr() returns the name of the register in struct
regdwarfnum_table from it's DWARF register number. If the register is not
found in the table, this returns NULL;

.. This file was automatic generated / don't edit.

