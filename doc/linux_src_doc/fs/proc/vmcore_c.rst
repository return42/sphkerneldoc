.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/proc/vmcore.c

.. _`alloc_elfnotes_buf`:

alloc_elfnotes_buf
==================

.. c:function:: char *alloc_elfnotes_buf(size_t notes_sz)

    allocate buffer for ELF note segment in vmalloc memory

    :param size_t notes_sz:
        size of buffer

.. _`alloc_elfnotes_buf.description`:

Description
-----------

If CONFIG_MMU is defined, use \ :c:func:`vmalloc_user`\  to allow users to mmap
the buffer to user-space by means of \ :c:func:`remap_vmalloc_range`\ .

If CONFIG_MMU is not defined, use \ :c:func:`vzalloc`\  since \ :c:func:`mmap_vmcore`\  is
disabled and there's no need to allow users to mmap the buffer.

.. _`update_note_header_size_elf64`:

update_note_header_size_elf64
=============================

.. c:function:: int update_note_header_size_elf64(const Elf64_Ehdr *ehdr_ptr)

    update p_memsz member of each PT_NOTE entry

    :param const Elf64_Ehdr \*ehdr_ptr:
        ELF header

.. _`update_note_header_size_elf64.description`:

Description
-----------

This function updates p_memsz member of each PT_NOTE entry in the
program header table pointed to by \ ``ehdr_ptr``\  to real size of ELF
note segment.

.. _`get_note_number_and_size_elf64`:

get_note_number_and_size_elf64
==============================

.. c:function:: int get_note_number_and_size_elf64(const Elf64_Ehdr *ehdr_ptr, int *nr_ptnote, u64 *sz_ptnote)

    get the number of PT_NOTE program headers and sum of real size of their ELF note segment headers and data.

    :param const Elf64_Ehdr \*ehdr_ptr:
        ELF header

    :param int \*nr_ptnote:
        buffer for the number of PT_NOTE program headers

    :param u64 \*sz_ptnote:
        buffer for size of unique PT_NOTE program header

.. _`get_note_number_and_size_elf64.description`:

Description
-----------

This function is used to merge multiple PT_NOTE program headers
into a unique single one. The resulting unique entry will have
\ ``sz_ptnote``\  in its phdr->p_mem.

It is assumed that program headers with PT_NOTE type pointed to by
\ ``ehdr_ptr``\  has already been updated by update_note_header_size_elf64
and each of PT_NOTE program headers has actual ELF note segment
size in its p_memsz member.

.. _`copy_notes_elf64`:

copy_notes_elf64
================

.. c:function:: int copy_notes_elf64(const Elf64_Ehdr *ehdr_ptr, char *notes_buf)

    copy ELF note segments in a given buffer

    :param const Elf64_Ehdr \*ehdr_ptr:
        ELF header

    :param char \*notes_buf:
        buffer into which ELF note segments are copied

.. _`copy_notes_elf64.description`:

Description
-----------

This function is used to copy ELF note segment in the 1st kernel
into the buffer \ ``notes_buf``\  in the 2nd kernel. It is assumed that
size of the buffer \ ``notes_buf``\  is equal to or larger than sum of the
real ELF note segment headers and data.

It is assumed that program headers with PT_NOTE type pointed to by
\ ``ehdr_ptr``\  has already been updated by update_note_header_size_elf64
and each of PT_NOTE program headers has actual ELF note segment
size in its p_memsz member.

.. _`update_note_header_size_elf32`:

update_note_header_size_elf32
=============================

.. c:function:: int update_note_header_size_elf32(const Elf32_Ehdr *ehdr_ptr)

    update p_memsz member of each PT_NOTE entry

    :param const Elf32_Ehdr \*ehdr_ptr:
        ELF header

.. _`update_note_header_size_elf32.description`:

Description
-----------

This function updates p_memsz member of each PT_NOTE entry in the
program header table pointed to by \ ``ehdr_ptr``\  to real size of ELF
note segment.

.. _`get_note_number_and_size_elf32`:

get_note_number_and_size_elf32
==============================

.. c:function:: int get_note_number_and_size_elf32(const Elf32_Ehdr *ehdr_ptr, int *nr_ptnote, u64 *sz_ptnote)

    get the number of PT_NOTE program headers and sum of real size of their ELF note segment headers and data.

    :param const Elf32_Ehdr \*ehdr_ptr:
        ELF header

    :param int \*nr_ptnote:
        buffer for the number of PT_NOTE program headers

    :param u64 \*sz_ptnote:
        buffer for size of unique PT_NOTE program header

.. _`get_note_number_and_size_elf32.description`:

Description
-----------

This function is used to merge multiple PT_NOTE program headers
into a unique single one. The resulting unique entry will have
\ ``sz_ptnote``\  in its phdr->p_mem.

It is assumed that program headers with PT_NOTE type pointed to by
\ ``ehdr_ptr``\  has already been updated by update_note_header_size_elf32
and each of PT_NOTE program headers has actual ELF note segment
size in its p_memsz member.

.. _`copy_notes_elf32`:

copy_notes_elf32
================

.. c:function:: int copy_notes_elf32(const Elf32_Ehdr *ehdr_ptr, char *notes_buf)

    copy ELF note segments in a given buffer

    :param const Elf32_Ehdr \*ehdr_ptr:
        ELF header

    :param char \*notes_buf:
        buffer into which ELF note segments are copied

.. _`copy_notes_elf32.description`:

Description
-----------

This function is used to copy ELF note segment in the 1st kernel
into the buffer \ ``notes_buf``\  in the 2nd kernel. It is assumed that
size of the buffer \ ``notes_buf``\  is equal to or larger than sum of the
real ELF note segment headers and data.

It is assumed that program headers with PT_NOTE type pointed to by
\ ``ehdr_ptr``\  has already been updated by update_note_header_size_elf32
and each of PT_NOTE program headers has actual ELF note segment
size in its p_memsz member.

.. This file was automatic generated / don't edit.

