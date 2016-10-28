.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sh/kernel/dwarf.c

.. _`dwarf_frame_alloc_reg`:

dwarf_frame_alloc_reg
=====================

.. c:function:: struct dwarf_reg *dwarf_frame_alloc_reg(struct dwarf_frame *frame, unsigned int reg_num)

    allocate memory for a DWARF register

    :param struct dwarf_frame \*frame:
        the DWARF frame whose list of registers we insert on

    :param unsigned int reg_num:
        the register number

.. _`dwarf_frame_alloc_reg.description`:

Description
-----------

Allocate space for, and initialise, a dwarf reg from
dwarf_reg_pool and insert it onto the (unsorted) linked-list of
dwarf registers for \ ``frame``\ .

Return the initialised DWARF reg.

.. _`dwarf_frame_reg`:

dwarf_frame_reg
===============

.. c:function:: struct dwarf_reg *dwarf_frame_reg(struct dwarf_frame *frame, unsigned int reg_num)

    return a DWARF register

    :param struct dwarf_frame \*frame:
        the DWARF frame to search in for \ ``reg_num``\ 

    :param unsigned int reg_num:
        the register number to search for

.. _`dwarf_frame_reg.description`:

Description
-----------

Lookup and return the dwarf reg \ ``reg_num``\  for this frame. Return
NULL if \ ``reg_num``\  is an register invalid number.

.. _`dwarf_read_addr`:

dwarf_read_addr
===============

.. c:function:: int dwarf_read_addr(unsigned long *src, unsigned long *dst)

    read dwarf data

    :param unsigned long \*src:
        source address of data

    :param unsigned long \*dst:
        destination address to store the data to

.. _`dwarf_read_addr.description`:

Description
-----------

Read 'n' bytes from \ ``src``\ , where 'n' is the size of an address on
the native machine. We return the number of bytes read, which
should always be 'n'. We also have to be careful when reading
from \ ``src``\  and writing to \ ``dst``\ , because they can be arbitrarily
aligned. Return 'n' - the number of bytes read.

.. _`dwarf_read_uleb128`:

dwarf_read_uleb128
==================

.. c:function:: unsigned long dwarf_read_uleb128(char *addr, unsigned int *ret)

    read unsigned LEB128 data

    :param char \*addr:
        the address where the ULEB128 data is stored

    :param unsigned int \*ret:
        address to store the result

.. _`dwarf_read_uleb128.description`:

Description
-----------

Decode an unsigned LEB128 encoded datum. The algorithm is taken
from Appendix C of the DWARF 3 spec. For information on the
encodings refer to section "7.6 - Variable Length Data". Return
the number of bytes read.

.. _`dwarf_read_leb128`:

dwarf_read_leb128
=================

.. c:function:: unsigned long dwarf_read_leb128(char *addr, int *ret)

    read signed LEB128 data

    :param char \*addr:
        the address of the LEB128 encoded data

    :param int \*ret:
        address to store the result

.. _`dwarf_read_leb128.description`:

Description
-----------

Decode signed LEB128 data. The algorithm is taken from Appendix
C of the DWARF 3 spec. Return the number of bytes read.

.. _`dwarf_read_encoded_value`:

dwarf_read_encoded_value
========================

.. c:function:: int dwarf_read_encoded_value(char *addr, unsigned long *val, char encoding)

    return the decoded value at \ ``addr``\ 

    :param char \*addr:
        the address of the encoded value

    :param unsigned long \*val:
        where to write the decoded value

    :param char encoding:
        the encoding with which we can decode \ ``addr``\ 

.. _`dwarf_read_encoded_value.description`:

Description
-----------

GCC emits encoded address in the .eh_frame FDE entries. Decode
the value at \ ``addr``\  using \ ``encoding``\ . The decoded value is written
to \ ``val``\  and the number of bytes read is returned.

.. _`dwarf_entry_len`:

dwarf_entry_len
===============

.. c:function:: int dwarf_entry_len(char *addr, unsigned long *len)

    return the length of an FDE or CIE

    :param char \*addr:
        the address of the entry

    :param unsigned long \*len:
        the length of the entry

.. _`dwarf_entry_len.description`:

Description
-----------

Read the initial_length field of the entry and store the size of
the entry in \ ``len``\ . We return the number of bytes read. Return a
count of 0 on error.

.. _`dwarf_lookup_cie`:

dwarf_lookup_cie
================

.. c:function:: struct dwarf_cie *dwarf_lookup_cie(unsigned long cie_ptr)

    locate the cie

    :param unsigned long cie_ptr:
        pointer to help with lookup

.. _`dwarf_lookup_fde`:

dwarf_lookup_fde
================

.. c:function:: struct dwarf_fde *dwarf_lookup_fde(unsigned long pc)

    locate the FDE that covers pc

    :param unsigned long pc:
        the program counter

.. _`dwarf_cfa_execute_insns`:

dwarf_cfa_execute_insns
=======================

.. c:function:: int dwarf_cfa_execute_insns(unsigned char *insn_start, unsigned char *insn_end, struct dwarf_cie *cie, struct dwarf_fde *fde, struct dwarf_frame *frame, unsigned long pc)

    execute instructions to calculate a CFA

    :param unsigned char \*insn_start:
        address of the first instruction

    :param unsigned char \*insn_end:
        address of the last instruction

    :param struct dwarf_cie \*cie:
        the CIE for this function

    :param struct dwarf_fde \*fde:
        the FDE for this function

    :param struct dwarf_frame \*frame:
        the instructions calculate the CFA for this frame

    :param unsigned long pc:
        the program counter of the address we're interested in

.. _`dwarf_cfa_execute_insns.description`:

Description
-----------

Execute the Call Frame instruction sequence starting at
\ ``insn_start``\  and ending at \ ``insn_end``\ . The instructions describe
how to calculate the Canonical Frame Address of a stackframe.
Store the results in \ ``frame``\ .

.. _`dwarf_free_frame`:

dwarf_free_frame
================

.. c:function:: void dwarf_free_frame(struct dwarf_frame *frame)

    free the memory allocated for \ ``frame``\ 

    :param struct dwarf_frame \*frame:
        the frame to free

.. _`dwarf_unwind_stack`:

dwarf_unwind_stack
==================

.. c:function:: struct dwarf_frame *dwarf_unwind_stack(unsigned long pc, struct dwarf_frame *prev)

    unwind the stack

    :param unsigned long pc:
        address of the function to unwind

    :param struct dwarf_frame \*prev:
        struct dwarf_frame of the previous stackframe on the callstack

.. _`dwarf_unwind_stack.description`:

Description
-----------

Return a struct dwarf_frame representing the most recent frame
on the callstack. Each of the lower (older) stack frames are
linked via the "prev" member.

.. _`dwarf_parse_section`:

dwarf_parse_section
===================

.. c:function:: int dwarf_parse_section(char *eh_frame_start, char *eh_frame_end, struct module *mod)

    parse DWARF section

    :param char \*eh_frame_start:
        start address of the .eh_frame section

    :param char \*eh_frame_end:
        end address of the .eh_frame section

    :param struct module \*mod:
        the kernel module containing the .eh_frame section

.. _`dwarf_parse_section.description`:

Description
-----------

Parse the information in a .eh_frame section.

.. _`module_dwarf_cleanup`:

module_dwarf_cleanup
====================

.. c:function:: void module_dwarf_cleanup(struct module *mod)

    remove FDE/CIEs associated with \ ``mod``\ 

    :param struct module \*mod:
        the module that is being unloaded

.. _`module_dwarf_cleanup.description`:

Description
-----------

Remove any FDEs and CIEs from the global lists that came from
\ ``mod``\ 's .eh_frame section because \ ``mod``\  is being unloaded.

.. _`dwarf_unwinder_init`:

dwarf_unwinder_init
===================

.. c:function:: int dwarf_unwinder_init( void)

    initialise the dwarf unwinder

    :param  void:
        no arguments

.. _`dwarf_unwinder_init.description`:

Description
-----------

Build the data structures describing the .dwarf_frame section to
make it easier to lookup CIE and FDE entries. Because the
.eh_frame section is packed as tightly as possible it is not
easy to lookup the FDE for a given PC, so we build a list of FDE
and CIE entries that make it easier.

.. This file was automatic generated / don't edit.

