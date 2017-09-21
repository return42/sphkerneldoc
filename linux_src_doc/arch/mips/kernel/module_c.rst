.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kernel/module.c

.. _`reloc_handler`:

reloc_handler
=============

.. c:function:: int reloc_handler(struct module *me, u32 *location, u32 base, Elf_Addr v, bool rela)

    Apply a particular relocation to a module

    :param struct module \*me:
        the module to apply the reloc to

    :param u32 \*location:
        the address at which the reloc is to be applied

    :param u32 base:
        the existing value at location for REL-style; 0 for RELA-style

    :param Elf_Addr v:
        the value of the reloc, with addend for RELA-style

    :param bool rela:
        *undescribed*

.. _`reloc_handler.description`:

Description
-----------

Each implemented reloc_handler function applies a particular type of
relocation to the module \ ``me``\ . Relocs that may be found in either REL or RELA
variants can be handled by making use of the \ ``base``\  & \ ``v``\  parameters which are
set to values which abstract the difference away from the particular reloc
implementations.

.. _`reloc_handler.return`:

Return
------

0 upon success, else -ERRNO

.. This file was automatic generated / don't edit.

