.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/symbol-elf.c

.. _`elf_symtab__for_each_symbol`:

elf_symtab__for_each_symbol
===========================

.. c:function::  elf_symtab__for_each_symbol( syms,  nr_syms,  idx,  sym)

    iterate thru all the symbols

    :param  syms:
        struct elf_symtab instance to iterate

    :param  nr_syms:
        *undescribed*

    :param  idx:
        uint32_t idx

    :param  sym:
        GElf_Sym iterator

.. _`ref_reloc_sym_not_found`:

ref_reloc_sym_not_found
=======================

.. c:function:: bool ref_reloc_sym_not_found(struct kmap *kmap)

    has kernel relocation symbol been found.

    :param struct kmap \*kmap:
        kernel maps and relocation reference symbol

.. _`ref_reloc_sym_not_found.description`:

Description
-----------

This function returns \ ``true``\  if we are dealing with the kernel maps and the
relocation reference symbol has not yet been found.  Otherwise \ ``false``\  is
returned.

.. _`ref_reloc`:

ref_reloc
=========

.. c:function:: u64 ref_reloc(struct kmap *kmap)

    kernel relocation offset.

    :param struct kmap \*kmap:
        kernel maps and relocation reference symbol

.. _`ref_reloc.description`:

Description
-----------

This function returns the offset of kernel addresses as determined by using
the relocation reference symbol i.e. if the kernel has not been relocated
then the return value is zero.

.. _`kcore_copy`:

kcore_copy
==========

.. c:function:: int kcore_copy(const char *from_dir, const char *to_dir)

    copy kallsyms, modules and kcore from one directory to another.

    :param const char \*from_dir:
        from directory

    :param const char \*to_dir:
        to directory

.. _`kcore_copy.description`:

Description
-----------

This function copies kallsyms, modules and kcore files from one directory to
another.  kallsyms and modules are copied entirely.  Only code segments are
copied from kcore.  It is assumed that two segments suffice: one for the
kernel proper and one for all the modules.  The code segments are determined
from kallsyms and modules files.  The kernel map starts at \_stext or the
lowest function symbol, and ends at \_etext or the highest function symbol.
The module map starts at the lowest module address and ends at the highest
module symbol.  Start addresses are rounded down to the nearest page.  End
addresses are rounded up to the nearest page.  An extra page is added to the
highest kernel symbol and highest module symbol to, hopefully, encompass that
symbol too.  Because it contains only code sections, the resulting kcore is
unusual.  One significant peculiarity is that the mapping (start -> pgoff)
is not the same for the kernel map and the modules map.  That happens because
the data is copied adjacently whereas the original kcore has gaps.  Finally,
kallsyms and modules files are compared with their copies to check that
modules have not been loaded or unloaded while the copies were taking place.

.. _`kcore_copy.return`:

Return
------

\ ``0``\  on success, \ ``-1``\  on failure.

.. This file was automatic generated / don't edit.

