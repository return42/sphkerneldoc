.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/binfmt_elf.c

.. _`load_elf_phdrs`:

load_elf_phdrs
==============

.. c:function:: struct elf_phdr *load_elf_phdrs(struct elfhdr *elf_ex, struct file *elf_file)

    load ELF program headers

    :param elf_ex:
        ELF header of the binary whose program headers should be loaded
    :type elf_ex: struct elfhdr \*

    :param elf_file:
        the opened ELF binary file
    :type elf_file: struct file \*

.. _`load_elf_phdrs.description`:

Description
-----------

Loads ELF program headers from the binary file elf_file, which has the ELF
header pointed to by elf_ex, into a newly allocated array. The caller is
responsible for freeing the allocated data. Returns an ERR_PTR upon failure.

.. _`arch_elf_state`:

struct arch_elf_state
=====================

.. c:type:: struct arch_elf_state

    arch-specific ELF loading state

.. _`arch_elf_state.definition`:

Definition
----------

.. code-block:: c

    struct arch_elf_state {
    }

.. _`arch_elf_state.members`:

Members
-------

void
    no arguments

.. _`arch_elf_state.description`:

Description
-----------

This structure is used to preserve architecture specific data during
the loading of an ELF file, throughout the checking of architecture
specific ELF headers & through to the point where the ELF load is
known to be proceeding (ie. SET_PERSONALITY).

This implementation is a dummy for architectures which require no
specific state.

.. _`arch_elf_pt_proc`:

arch_elf_pt_proc
================

.. c:function:: int arch_elf_pt_proc(struct elfhdr *ehdr, struct elf_phdr *phdr, struct file *elf, bool is_interp, struct arch_elf_state *state)

    check a PT_LOPROC..PT_HIPROC ELF program header

    :param ehdr:
        The main ELF header
    :type ehdr: struct elfhdr \*

    :param phdr:
        The program header to check
    :type phdr: struct elf_phdr \*

    :param elf:
        The open ELF file
    :type elf: struct file \*

    :param is_interp:
        True if the phdr is from the interpreter of the ELF being
        loaded, else false.
    :type is_interp: bool

    :param state:
        Architecture-specific state preserved throughout the process
        of loading the ELF.
    :type state: struct arch_elf_state \*

.. _`arch_elf_pt_proc.description`:

Description
-----------

Inspects the program header phdr to validate its correctness and/or
suitability for the system. Called once per ELF program header in the
range PT_LOPROC to PT_HIPROC, for both the ELF being loaded and its
interpreter.

.. _`arch_elf_pt_proc.return`:

Return
------

Zero to proceed with the ELF load, non-zero to fail the ELF load
with that return code.

.. _`arch_check_elf`:

arch_check_elf
==============

.. c:function:: int arch_check_elf(struct elfhdr *ehdr, bool has_interp, struct elfhdr *interp_ehdr, struct arch_elf_state *state)

    check an ELF executable

    :param ehdr:
        The main ELF header
    :type ehdr: struct elfhdr \*

    :param has_interp:
        True if the ELF has an interpreter, else false.
    :type has_interp: bool

    :param interp_ehdr:
        The interpreter's ELF header
    :type interp_ehdr: struct elfhdr \*

    :param state:
        Architecture-specific state preserved throughout the process
        of loading the ELF.
    :type state: struct arch_elf_state \*

.. _`arch_check_elf.description`:

Description
-----------

Provides a final opportunity for architecture code to reject the loading
of the ELF & cause an exec syscall to return an error. This is called after
all program headers to be checked by arch_elf_pt_proc have been.

.. _`arch_check_elf.return`:

Return
------

Zero to proceed with the ELF load, non-zero to fail the ELF load
with that return code.

.. This file was automatic generated / don't edit.

