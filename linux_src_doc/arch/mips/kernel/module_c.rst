.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kernel/module.c

.. _`reloc_handler`:

reloc_handler
=============

.. c:function:: int reloc_handler(struct module *me, u32 *location, u32 base, Elf_Addr v, bool rela)

    Apply a particular relocation to a module

    :param me:
        the module to apply the reloc to
    :type me: struct module \*

    :param location:
        the address at which the reloc is to be applied
    :type location: u32 \*

    :param base:
        the existing value at location for REL-style; 0 for RELA-style
    :type base: u32

    :param v:
        the value of the reloc, with addend for RELA-style
    :type v: Elf_Addr

    :param rela:
        *undescribed*
    :type rela: bool

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

