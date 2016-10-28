.. -*- coding: utf-8; mode: rst -*-
.. src-file: scripts/mod/modpost.c

.. _`alloc_symbol`:

alloc_symbol
============

.. c:function:: struct symbol *alloc_symbol(const char *name, unsigned int weak, struct symbol *next)

    the list of unresolved symbols per module

    :param const char \*name:
        *undescribed*

    :param unsigned int weak:
        *undescribed*

    :param struct symbol \*next:
        *undescribed*

.. _`sym_add_exported`:

sym_add_exported
================

.. c:function:: struct symbol *sym_add_exported(const char *name, struct module *mod, enum export export)

    it may have already been added without a CRC, in this case just update the CRC

    :param const char \*name:
        *undescribed*

    :param struct module \*mod:
        *undescribed*

    :param enum export export:
        *undescribed*

.. _`get_next_line`:

get_next_line
=============

.. c:function:: char *get_next_line(unsigned long *pos, void *file, unsigned long size)

    spaces in the beginning of the line is trimmed away. Return a pointer to a static buffer.

    :param unsigned long \*pos:
        *undescribed*

    :param void \*file:
        *undescribed*

    :param unsigned long size:
        *undescribed*

.. _`next_string`:

next_string
===========

.. c:function:: char *next_string(char *string, unsigned long *secsize)

    :param char \*string:
        *undescribed*

    :param unsigned long \*secsize:
        *undescribed*

.. _`strrcmp`:

strrcmp
=======

.. c:function:: int strrcmp(const char *s, const char *sub)

    return 0 if match

    :param const char \*s:
        *undescribed*

    :param const char \*sub:
        *undescribed*

.. _`secref_whitelist`:

secref_whitelist
================

.. c:function:: int secref_whitelist(const struct sectioncheck *mismatch, const char *fromsec, const char *fromsym, const char *tosec, const char *tosym)

    :param const struct sectioncheck \*mismatch:
        *undescribed*

    :param const char \*fromsec:
        *undescribed*

    :param const char \*fromsym:
        *undescribed*

    :param const char \*tosec:
        *undescribed*

    :param const char \*tosym:
        *undescribed*

.. _`secref_whitelist.pattern-1`:

Pattern 1
---------

If a module parameter is declared \__initdata and permissions=0
then this is legal despite the warning generated.
We cannot see value of permissions here, so just ignore
this pattern.

.. _`secref_whitelist.the-pattern-is-identified-by`:

The pattern is identified by
----------------------------

tosec   = .init.data
fromsec = .data\*
atsym   =__param\*

tosec   = .init.text
fromsec = .data\*
atsym   = \__param_ops\_\*

.. _`secref_whitelist.pattern-1a`:

Pattern 1a
----------

\ :c:func:`module_param_call`\  ops can refer to \__init set function if permissions=0

.. _`secref_whitelist.pattern-2`:

Pattern 2
---------

Many drivers utilise a \*driver container with references to
add, remove, probe functions etc.

.. _`secref_whitelist.the-pattern-is-identified-by`:

the pattern is identified by
----------------------------

tosec   = init or exit section
fromsec = data section
atsym = \*driver, \*\_template, \*\_sht, \*\_ops, \*\_probe,
\*probe_one, \*\_console, \*\_timer

.. _`secref_whitelist.pattern-3`:

Pattern 3
---------

Whitelist all references from .head.text to any init section

.. _`secref_whitelist.pattern-4`:

Pattern 4
---------

Some symbols belong to init section but still it is ok to reference
these from non-init sections as these symbols don't have any memory
allocated for them and symbol address and value are same. So even
if init section is freed, its ok to reference those symbols.
For ex. symbols marking the init section boundaries.
This pattern is identified by
refsymname = \__init_begin, \_sinittext, \_einittext

.. _`secref_whitelist.pattern-5`:

Pattern 5
---------

GCC may optimize static inlines when fed constant arg(s) resulting
in functions like \ :c:func:`cpumask_empty`\  -- generating an associated symbol
cpumask_empty.constprop.3 that appears in the audit.  If the const that
is passed in comes from \__init, like say nmi_ipi_mask, we get a
meaningless section warning.  May need to add isra symbols too...
This pattern is identified by
tosec   = init section
fromsec = text section
refsymname = \*.constprop.\*

.. _`find_elf_symbol`:

find_elf_symbol
===============

.. c:function:: Elf_Sym *find_elf_symbol(struct elf_info *elf, Elf64_Sword addr, Elf_Sym *relsym)

    In some cases the symbol supplied is a valid symbol so return refsym. If st_name != 0 we assume this is a valid symbol. In other cases the symbol needs to be looked up in the symbol table based on section and address.

    :param struct elf_info \*elf:
        *undescribed*

    :param Elf64_Sword addr:
        *undescribed*

    :param Elf_Sym \*relsym:
        *undescribed*

.. _`check_sec_ref`:

check_sec_ref
=============

.. c:function:: void check_sec_ref(struct module *mod, const char *modname, struct elf_info *elf)

    either when loaded or when used as built-in. For loaded modules all functions marked \__init and all data marked \__initdata will be discarded when the module has been initialized. Likewise for modules used built-in the sections marked \__exit are discarded because \__exit marked function are supposed to be called only when a module is unloaded which never happens for built-in modules. The \ :c:func:`check_sec_ref`\  function traverses all relocation records to find all references to a section that reference a section that will be discarded and warns about it.

    :param struct module \*mod:
        *undescribed*

    :param const char \*modname:
        *undescribed*

    :param struct elf_info \*elf:
        *undescribed*

.. _`add_header`:

add_header
==========

.. c:function:: void add_header(struct buffer *b, struct module *mod)

    :param struct buffer \*b:
        *undescribed*

    :param struct module \*mod:
        *undescribed*

.. _`add_versions`:

add_versions
============

.. c:function:: int add_versions(struct buffer *b, struct module *mod)

    :param struct buffer \*b:
        *undescribed*

    :param struct module \*mod:
        *undescribed*

.. This file was automatic generated / don't edit.

