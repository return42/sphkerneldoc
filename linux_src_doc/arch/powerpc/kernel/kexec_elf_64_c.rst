.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/kexec_elf_64.c

.. _`elf_is_ehdr_sane`:

elf_is_ehdr_sane
================

.. c:function:: bool elf_is_ehdr_sane(const struct elfhdr *ehdr, size_t buf_len)

    check that it is safe to use the ELF header

    :param ehdr:
        *undescribed*
    :type ehdr: const struct elfhdr \*

    :param buf_len:
        size of the buffer in which the ELF file is loaded.
    :type buf_len: size_t

.. _`elf_is_phdr_sane`:

elf_is_phdr_sane
================

.. c:function:: bool elf_is_phdr_sane(const struct elf_phdr *phdr, size_t buf_len)

    check that it is safe to use the program header

    :param phdr:
        *undescribed*
    :type phdr: const struct elf_phdr \*

    :param buf_len:
        size of the buffer in which the ELF file is loaded.
    :type buf_len: size_t

.. _`elf_read_phdrs`:

elf_read_phdrs
==============

.. c:function:: int elf_read_phdrs(const char *buf, size_t len, struct elf_info *elf_info)

    read the program headers from the buffer

    :param buf:
        *undescribed*
    :type buf: const char \*

    :param len:
        *undescribed*
    :type len: size_t

    :param elf_info:
        *undescribed*
    :type elf_info: struct elf_info \*

.. _`elf_read_phdrs.description`:

Description
-----------

This function assumes that the program header table was checked for sanity.
Use \ :c:func:`elf_is_ehdr_sane`\  if it wasn't.

.. _`elf_is_shdr_sane`:

elf_is_shdr_sane
================

.. c:function:: bool elf_is_shdr_sane(const struct elf_shdr *shdr, size_t buf_len)

    check that it is safe to use the section header

    :param shdr:
        *undescribed*
    :type shdr: const struct elf_shdr \*

    :param buf_len:
        size of the buffer in which the ELF file is loaded.
    :type buf_len: size_t

.. _`elf_read_shdrs`:

elf_read_shdrs
==============

.. c:function:: int elf_read_shdrs(const char *buf, size_t len, struct elf_info *elf_info)

    read the section headers from the buffer

    :param buf:
        *undescribed*
    :type buf: const char \*

    :param len:
        *undescribed*
    :type len: size_t

    :param elf_info:
        *undescribed*
    :type elf_info: struct elf_info \*

.. _`elf_read_shdrs.description`:

Description
-----------

This function assumes that the section header table was checked for sanity.
Use \ :c:func:`elf_is_ehdr_sane`\  if it wasn't.

.. _`elf_read_from_buffer`:

elf_read_from_buffer
====================

.. c:function:: int elf_read_from_buffer(const char *buf, size_t len, struct elfhdr *ehdr, struct elf_info *elf_info)

    read ELF file and sets up ELF header and ELF info

    :param buf:
        Buffer to read ELF file from.
    :type buf: const char \*

    :param len:
        Size of \ ``buf``\ .
    :type len: size_t

    :param ehdr:
        Pointer to existing struct which will be populated.
    :type ehdr: struct elfhdr \*

    :param elf_info:
        Pointer to existing struct which will be populated.
    :type elf_info: struct elf_info \*

.. _`elf_read_from_buffer.description`:

Description
-----------

This function allows reading ELF files with different byte order than
the kernel, byte-swapping the fields as needed.

.. _`elf_read_from_buffer.return`:

Return
------

On success returns 0, and the caller should call elf_free_info(elf_info) to
free the memory allocated for the section and program headers.

.. _`elf_free_info`:

elf_free_info
=============

.. c:function:: void elf_free_info(struct elf_info *elf_info)

    free memory allocated by elf_read_from_buffer

    :param elf_info:
        *undescribed*
    :type elf_info: struct elf_info \*

.. _`build_elf_exec_info`:

build_elf_exec_info
===================

.. c:function:: int build_elf_exec_info(const char *buf, size_t len, struct elfhdr *ehdr, struct elf_info *elf_info)

    read ELF executable and check that we can use it

    :param buf:
        *undescribed*
    :type buf: const char \*

    :param len:
        *undescribed*
    :type len: size_t

    :param ehdr:
        *undescribed*
    :type ehdr: struct elfhdr \*

    :param elf_info:
        *undescribed*
    :type elf_info: struct elf_info \*

.. _`elf_exec_load`:

elf_exec_load
=============

.. c:function:: int elf_exec_load(struct kimage *image, struct elfhdr *ehdr, struct elf_info *elf_info, unsigned long *lowest_load_addr)

    load ELF executable image

    :param image:
        *undescribed*
    :type image: struct kimage \*

    :param ehdr:
        *undescribed*
    :type ehdr: struct elfhdr \*

    :param elf_info:
        *undescribed*
    :type elf_info: struct elf_info \*

    :param lowest_load_addr:
        On return, will be the address where the first PT_LOAD
        section will be loaded in memory.
    :type lowest_load_addr: unsigned long \*

.. _`elf_exec_load.return`:

Return
------

0 on success, negative value on failure.

.. This file was automatic generated / don't edit.

