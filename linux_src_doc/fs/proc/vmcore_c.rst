.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/proc/vmcore.c

.. _`vmcore_alloc_buf`:

vmcore_alloc_buf
================

.. c:function:: char *vmcore_alloc_buf(size_t size)

    allocate buffer in vmalloc memory

    :param size:
        *undescribed*
    :type size: size_t

.. _`vmcore_alloc_buf.description`:

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

    :param ehdr_ptr:
        ELF header
    :type ehdr_ptr: const Elf64_Ehdr \*

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

    :param ehdr_ptr:
        ELF header
    :type ehdr_ptr: const Elf64_Ehdr \*

    :param nr_ptnote:
        buffer for the number of PT_NOTE program headers
    :type nr_ptnote: int \*

    :param sz_ptnote:
        buffer for size of unique PT_NOTE program header
    :type sz_ptnote: u64 \*

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

    :param ehdr_ptr:
        ELF header
    :type ehdr_ptr: const Elf64_Ehdr \*

    :param notes_buf:
        buffer into which ELF note segments are copied
    :type notes_buf: char \*

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

    :param ehdr_ptr:
        ELF header
    :type ehdr_ptr: const Elf32_Ehdr \*

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

    :param ehdr_ptr:
        ELF header
    :type ehdr_ptr: const Elf32_Ehdr \*

    :param nr_ptnote:
        buffer for the number of PT_NOTE program headers
    :type nr_ptnote: int \*

    :param sz_ptnote:
        buffer for size of unique PT_NOTE program header
    :type sz_ptnote: u64 \*

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

    :param ehdr_ptr:
        ELF header
    :type ehdr_ptr: const Elf32_Ehdr \*

    :param notes_buf:
        buffer into which ELF note segments are copied
    :type notes_buf: char \*

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

.. _`vmcoredd_write_header`:

vmcoredd_write_header
=====================

.. c:function:: void vmcoredd_write_header(void *buf, struct vmcoredd_data *data, u32 size)

    Write vmcore device dump header at the beginning of the dump's buffer.

    :param buf:
        Output buffer where the note is written
    :type buf: void \*

    :param data:
        Dump info
    :type data: struct vmcoredd_data \*

    :param size:
        Size of the dump
    :type size: u32

.. _`vmcoredd_write_header.description`:

Description
-----------

Fills beginning of the dump's buffer with vmcore device dump header.

.. _`vmcoredd_update_program_headers`:

vmcoredd_update_program_headers
===============================

.. c:function:: void vmcoredd_update_program_headers(char *elfptr, size_t elfnotesz, size_t vmcoreddsz)

    Update all Elf program headers

    :param elfptr:
        Pointer to elf header
    :type elfptr: char \*

    :param elfnotesz:
        Size of elf notes aligned to page size
    :type elfnotesz: size_t

    :param vmcoreddsz:
        Size of device dumps to be added to elf note header
    :type vmcoreddsz: size_t

.. _`vmcoredd_update_program_headers.description`:

Description
-----------

Determine type of Elf header (Elf64 or Elf32) and update the elf note size.
Also update the offsets of all the program headers after the elf note header.

.. _`vmcoredd_update_size`:

vmcoredd_update_size
====================

.. c:function:: void vmcoredd_update_size(size_t dump_size)

    Update the total size of the device dumps and update Elf header

    :param dump_size:
        Size of the current device dump to be added to total size
    :type dump_size: size_t

.. _`vmcoredd_update_size.description`:

Description
-----------

Update the total size of all the device dumps and update the Elf program
headers. Calculate the new offsets for the vmcore list and update the
total vmcore size.

.. _`vmcore_add_device_dump`:

vmcore_add_device_dump
======================

.. c:function:: int vmcore_add_device_dump(struct vmcoredd_data *data)

    Add a buffer containing device dump to vmcore

    :param data:
        dump info.
    :type data: struct vmcoredd_data \*

.. _`vmcore_add_device_dump.description`:

Description
-----------

Allocate a buffer and invoke the calling driver's dump collect routine.
Write Elf note at the beginning of the buffer to indicate vmcore device
dump and add the dump to global list.

.. This file was automatic generated / don't edit.

