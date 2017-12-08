.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/lib/insn-eval.c

.. _`is_string_insn`:

is_string_insn
==============

.. c:function:: bool is_string_insn(struct insn *insn)

    Determine if instruction is a string instruction

    :param struct insn \*insn:
        Instruction containing the opcode to inspect

.. _`is_string_insn.return`:

Return
------


true if the instruction, determined by the opcode, is any of the
string instructions as defined in the Intel Software Development manual.
False otherwise.

.. _`get_seg_reg_override_idx`:

get_seg_reg_override_idx
========================

.. c:function:: int get_seg_reg_override_idx(struct insn *insn)

    obtain segment register override index

    :param struct insn \*insn:
        Valid instruction with segment override prefixes

.. _`get_seg_reg_override_idx.description`:

Description
-----------

Inspect the instruction prefixes in \ ``insn``\  and find segment overrides, if any.

.. _`get_seg_reg_override_idx.return`:

Return
------


A constant identifying the segment register to use, among CS, SS, DS,
ES, FS, or GS. INAT_SEG_REG_DEFAULT is returned if no segment override
prefixes were found.

-EINVAL in case of error.

.. _`check_seg_overrides`:

check_seg_overrides
===================

.. c:function:: bool check_seg_overrides(struct insn *insn, int regoff)

    check if segment override prefixes are allowed

    :param struct insn \*insn:
        Valid instruction with segment override prefixes

    :param int regoff:
        Operand offset, in pt_regs, for which the check is performed

.. _`check_seg_overrides.description`:

Description
-----------

For a particular register used in register-indirect addressing, determine if
segment override prefixes can be used. Specifically, no overrides are allowed
for rDI if used with a string instruction.

.. _`check_seg_overrides.return`:

Return
------


True if segment override prefixes can be used with the register indicated
in \ ``regoff``\ . False if otherwise.

.. _`resolve_default_seg`:

resolve_default_seg
===================

.. c:function:: int resolve_default_seg(struct insn *insn, struct pt_regs *regs, int off)

    resolve default segment register index for an operand

    :param struct insn \*insn:
        Instruction with opcode and address size. Must be valid.

    :param struct pt_regs \*regs:
        Register values as seen when entering kernel mode

    :param int off:
        Operand offset, in pt_regs, for which resolution is needed

.. _`resolve_default_seg.description`:

Description
-----------

Resolve the default segment register index associated with the instruction
operand register indicated by \ ``off``\ . Such index is resolved based on defaults
described in the Intel Software Development Manual.

.. _`resolve_default_seg.return`:

Return
------


If in protected mode, a constant identifying the segment register to use,
among CS, SS, ES or DS. If in long mode, INAT_SEG_REG_IGNORE.

-EINVAL in case of error.

.. _`resolve_seg_reg`:

resolve_seg_reg
===============

.. c:function:: int resolve_seg_reg(struct insn *insn, struct pt_regs *regs, int regoff)

    obtain segment register index

    :param struct insn \*insn:
        Instruction with operands

    :param struct pt_regs \*regs:
        Register values as seen when entering kernel mode

    :param int regoff:
        Operand offset, in pt_regs, used to deterimine segment register

.. _`resolve_seg_reg.description`:

Description
-----------

Determine the segment register associated with the operands and, if
applicable, prefixes and the instruction pointed by \ ``insn``\ .

The segment register associated to an operand used in register-indirect

.. _`resolve_seg_reg.addressing-depends-on`:

addressing depends on
---------------------


a) Whether running in long mode (in such a case segments are ignored, except
if FS or GS are used).

b) Whether segment override prefixes can be used. Certain instructions and
registers do not allow override prefixes.

c) Whether segment overrides prefixes are found in the instruction prefixes.

d) If there are not segment override prefixes or they cannot be used, the
default segment register associated with the operand register is used.

The function checks first if segment override prefixes can be used with the
operand indicated by \ ``regoff``\ . If allowed, obtain such overridden segment
register index. Lastly, if not prefixes were found or cannot be used, resolve
the segment register index to use based on the defaults described in the
Intel documentation. In long mode, all segment register indexes will be
ignored, except if overrides were found for FS or GS. All these operations
are done using helper functions.

The operand register, \ ``regoff``\ , is represented as the offset from the base of
pt_regs.

As stated, the main use of this function is to determine the segment register
index based on the instruction, its operands and prefixes. Hence, \ ``insn``\ 
must be valid. However, if \ ``regoff``\  indicates rIP, we don't need to inspect
\ ``insn``\  at all as in this case CS is used in all cases. This case is checked
before proceeding further.

Please note that this function does not return the value in the segment
register (i.e., the segment selector) but our defined index. The segment
selector needs to be obtained using \ :c:func:`get_segment_selector`\  and passing the
segment register index resolved by this function.

.. _`resolve_seg_reg.return`:

Return
------


An index identifying the segment register to use, among CS, SS, DS,
ES, FS, or GS. INAT_SEG_REG_IGNORE is returned if running in long mode.

-EINVAL in case of error.

.. _`get_segment_selector`:

get_segment_selector
====================

.. c:function:: short get_segment_selector(struct pt_regs *regs, int seg_reg_idx)

    obtain segment selector

    :param struct pt_regs \*regs:
        Register values as seen when entering kernel mode

    :param int seg_reg_idx:
        Segment register index to use

.. _`get_segment_selector.description`:

Description
-----------

Obtain the segment selector from any of the CS, SS, DS, ES, FS, GS segment
registers. In CONFIG_X86_32, the segment is obtained from either pt_regs or
kernel_vm86_regs as applicable. In CONFIG_X86_64, CS and SS are obtained
from pt_regs. DS, ES, FS and GS are obtained by reading the actual CPU
registers. This done for only for completeness as in CONFIG_X86_64 segment
registers are ignored.

.. _`get_segment_selector.return`:

Return
------


Value of the segment selector, including null when running in
long mode.

-EINVAL on error.

.. _`get_reg_offset_16`:

get_reg_offset_16
=================

.. c:function:: int get_reg_offset_16(struct insn *insn, struct pt_regs *regs, int *offs1, int *offs2)

    Obtain offset of register indicated by instruction

    :param struct insn \*insn:
        Instruction containing ModRM byte

    :param struct pt_regs \*regs:
        Register values as seen when entering kernel mode

    :param int \*offs1:
        Offset of the first operand register

    :param int \*offs2:
        Offset of the second opeand register, if applicable

.. _`get_reg_offset_16.description`:

Description
-----------

Obtain the offset, in pt_regs, of the registers indicated by the ModRM byte
in \ ``insn``\ . This function is to be used with 16-bit address encodings. The
\ ``offs1``\  and \ ``offs2``\  will be written with the offset of the two registers
indicated by the instruction. In cases where any of the registers is not
referenced by the instruction, the value will be set to -EDOM.

.. _`get_reg_offset_16.return`:

Return
------


0 on success, -EINVAL on error.

.. _`get_desc`:

get_desc
========

.. c:function:: struct desc_struct *get_desc(unsigned short sel)

    Obtain pointer to a segment descriptor

    :param unsigned short sel:
        Segment selector

.. _`get_desc.description`:

Description
-----------

Given a segment selector, obtain a pointer to the segment descriptor.
Both global and local descriptor tables are supported.

.. _`get_desc.return`:

Return
------


Pointer to segment descriptor on success.

NULL on error.

.. _`insn_get_seg_base`:

insn_get_seg_base
=================

.. c:function:: unsigned long insn_get_seg_base(struct pt_regs *regs, int seg_reg_idx)

    Obtain base address of segment descriptor.

    :param struct pt_regs \*regs:
        Register values as seen when entering kernel mode

    :param int seg_reg_idx:
        Index of the segment register pointing to seg descriptor

.. _`insn_get_seg_base.description`:

Description
-----------

Obtain the base address of the segment as indicated by the segment descriptor
pointed by the segment selector. The segment selector is obtained from the
input segment register index \ ``seg_reg_idx``\ .

.. _`insn_get_seg_base.return`:

Return
------


In protected mode, base address of the segment. Zero in long mode,
except when FS or GS are used. In virtual-8086 mode, the segment
selector shifted 4 bits to the right.

-1L in case of error.

.. _`get_seg_limit`:

get_seg_limit
=============

.. c:function:: unsigned long get_seg_limit(struct pt_regs *regs, int seg_reg_idx)

    Obtain the limit of a segment descriptor

    :param struct pt_regs \*regs:
        Register values as seen when entering kernel mode

    :param int seg_reg_idx:
        Index of the segment register pointing to seg descriptor

.. _`get_seg_limit.description`:

Description
-----------

Obtain the limit of the segment as indicated by the segment descriptor
pointed by the segment selector. The segment selector is obtained from the
input segment register index \ ``seg_reg_idx``\ .

.. _`get_seg_limit.return`:

Return
------


In protected mode, the limit of the segment descriptor in bytes.
In long mode and virtual-8086 mode, segment limits are not enforced. Thus,
limit is returned as -1L to imply a limit-less segment.

Zero is returned on error.

.. _`insn_get_code_seg_params`:

insn_get_code_seg_params
========================

.. c:function:: int insn_get_code_seg_params(struct pt_regs *regs)

    Obtain code segment parameters

    :param struct pt_regs \*regs:
        Structure with register values as seen when entering kernel mode

.. _`insn_get_code_seg_params.description`:

Description
-----------

Obtain address and operand sizes of the code segment. It is obtained from the
selector contained in the CS register in regs. In protected mode, the default
address is determined by inspecting the L and D bits of the segment
descriptor. In virtual-8086 mode, the default is always two bytes for both
address and operand sizes.

.. _`insn_get_code_seg_params.return`:

Return
------


An int containing ORed-in default parameters on success.

-EINVAL on error.

.. _`insn_get_modrm_rm_off`:

insn_get_modrm_rm_off
=====================

.. c:function:: int insn_get_modrm_rm_off(struct insn *insn, struct pt_regs *regs)

    Obtain register in r/m part of the ModRM byte

    :param struct insn \*insn:
        Instruction containing the ModRM byte

    :param struct pt_regs \*regs:
        Register values as seen when entering kernel mode

.. _`insn_get_modrm_rm_off.return`:

Return
------


The register indicated by the r/m part of the ModRM byte. The
register is obtained as an offset from the base of pt_regs. In specific
cases, the returned value can be -EDOM to indicate that the particular value
of ModRM does not refer to a register and shall be ignored.

.. _`get_seg_base_limit`:

get_seg_base_limit
==================

.. c:function:: int get_seg_base_limit(struct insn *insn, struct pt_regs *regs, int regoff, unsigned long *base, unsigned long *limit)

    obtain base address and limit of a segment

    :param struct insn \*insn:
        Instruction. Must be valid.

    :param struct pt_regs \*regs:
        Register values as seen when entering kernel mode

    :param int regoff:
        Operand offset, in pt_regs, used to resolve segment descriptor

    :param unsigned long \*base:
        Obtained segment base

    :param unsigned long \*limit:
        Obtained segment limit

.. _`get_seg_base_limit.description`:

Description
-----------

Obtain the base address and limit of the segment associated with the operand
\ ``regoff``\  and, if any or allowed, override prefixes in \ ``insn``\ . This function is
different from \ :c:func:`insn_get_seg_base`\  as the latter does not resolve the segment
associated with the instruction operand. If a limit is not needed (e.g.,
when running in long mode), \ ``limit``\  can be NULL.

.. _`get_seg_base_limit.return`:

Return
------


0 on success. \ ``base``\  and \ ``limit``\  will contain the base address and of the
resolved segment, respectively.

-EINVAL on error.

.. _`get_eff_addr_reg`:

get_eff_addr_reg
================

.. c:function:: int get_eff_addr_reg(struct insn *insn, struct pt_regs *regs, int *regoff, long *eff_addr)

    Obtain effective address from register operand

    :param struct insn \*insn:
        Instruction. Must be valid.

    :param struct pt_regs \*regs:
        Register values as seen when entering kernel mode

    :param int \*regoff:
        Obtained operand offset, in pt_regs, with the effective address

    :param long \*eff_addr:
        Obtained effective address

.. _`get_eff_addr_reg.description`:

Description
-----------

Obtain the effective address stored in the register operand as indicated by
the ModRM byte. This function is to be used only with register addressing
(i.e.,  ModRM.mod is 3). The effective address is saved in \ ``eff_addr``\ . The
register operand, as an offset from the base of pt_regs, is saved in \ ``regoff``\ ;
such offset can then be used to resolve the segment associated with the
operand. This function can be used with any of the supported address sizes
in x86.

.. _`get_eff_addr_reg.return`:

Return
------


0 on success. \ ``eff_addr``\  will have the effective address stored in the
operand indicated by ModRM. \ ``regoff``\  will have such operand as an offset from
the base of pt_regs.

-EINVAL on error.

.. _`get_eff_addr_modrm`:

get_eff_addr_modrm
==================

.. c:function:: int get_eff_addr_modrm(struct insn *insn, struct pt_regs *regs, int *regoff, long *eff_addr)

    Obtain referenced effective address via ModRM

    :param struct insn \*insn:
        Instruction. Must be valid.

    :param struct pt_regs \*regs:
        Register values as seen when entering kernel mode

    :param int \*regoff:
        Obtained operand offset, in pt_regs, associated with segment

    :param long \*eff_addr:
        Obtained effective address

.. _`get_eff_addr_modrm.description`:

Description
-----------

Obtain the effective address referenced by the ModRM byte of \ ``insn``\ . After
identifying the registers involved in the register-indirect memory reference,
its value is obtained from the operands in \ ``regs``\ . The computed address is
stored \ ``eff_addr``\ . Also, the register operand that indicates the associated
segment is stored in \ ``regoff``\ , this parameter can later be used to determine
such segment.

.. _`get_eff_addr_modrm.return`:

Return
------


0 on success. \ ``eff_addr``\  will have the referenced effective address. \ ``regoff``\ 
will have a register, as an offset from the base of pt_regs, that can be used
to resolve the associated segment.

-EINVAL on error.

.. _`get_eff_addr_modrm_16`:

get_eff_addr_modrm_16
=====================

.. c:function:: int get_eff_addr_modrm_16(struct insn *insn, struct pt_regs *regs, int *regoff, short *eff_addr)

    Obtain referenced effective address via ModRM

    :param struct insn \*insn:
        Instruction. Must be valid.

    :param struct pt_regs \*regs:
        Register values as seen when entering kernel mode

    :param int \*regoff:
        Obtained operand offset, in pt_regs, associated with segment

    :param short \*eff_addr:
        Obtained effective address

.. _`get_eff_addr_modrm_16.description`:

Description
-----------

Obtain the 16-bit effective address referenced by the ModRM byte of \ ``insn``\ .
After identifying the registers involved in the register-indirect memory
reference, its value is obtained from the operands in \ ``regs``\ . The computed
address is stored \ ``eff_addr``\ . Also, the register operand that indicates
the associated segment is stored in \ ``regoff``\ , this parameter can later be used
to determine such segment.

.. _`get_eff_addr_modrm_16.return`:

Return
------


0 on success. \ ``eff_addr``\  will have the referenced effective address. \ ``regoff``\ 
will have a register, as an offset from the base of pt_regs, that can be used
to resolve the associated segment.

-EINVAL on error.

.. _`get_eff_addr_sib`:

get_eff_addr_sib
================

.. c:function:: int get_eff_addr_sib(struct insn *insn, struct pt_regs *regs, int *base_offset, long *eff_addr)

    Obtain referenced effective address via SIB

    :param struct insn \*insn:
        Instruction. Must be valid.

    :param struct pt_regs \*regs:
        Register values as seen when entering kernel mode

    :param int \*base_offset:
        *undescribed*

    :param long \*eff_addr:
        Obtained effective address

.. _`get_eff_addr_sib.description`:

Description
-----------

Obtain the effective address referenced by the SIB byte of \ ``insn``\ . After
identifying the registers involved in the indexed, register-indirect memory
reference, its value is obtained from the operands in \ ``regs``\ . The computed
address is stored \ ``eff_addr``\ . Also, the register operand that indicates the
associated segment is stored in \ ``regoff``\ , this parameter can later be used to
determine such segment.

.. _`get_eff_addr_sib.return`:

Return
------


0 on success. \ ``eff_addr``\  will have the referenced effective address.
\ ``base_offset``\  will have a register, as an offset from the base of pt_regs,
that can be used to resolve the associated segment.

-EINVAL on error.

.. _`get_addr_ref_16`:

get_addr_ref_16
===============

.. c:function:: void __user *get_addr_ref_16(struct insn *insn, struct pt_regs *regs)

    Obtain the 16-bit address referred by instruction

    :param struct insn \*insn:
        Instruction containing ModRM byte and displacement

    :param struct pt_regs \*regs:
        Register values as seen when entering kernel mode

.. _`get_addr_ref_16.description`:

Description
-----------

This function is to be used with 16-bit address encodings. Obtain the memory
address referred by the instruction's ModRM and displacement bytes. Also, the
segment used as base is determined by either any segment override prefixes in
\ ``insn``\  or the default segment of the registers involved in the address
computation. In protected mode, segment limits are enforced.

.. _`get_addr_ref_16.return`:

Return
------


Linear address referenced by the instruction operands on success.

-1L on error.

.. _`get_addr_ref_32`:

get_addr_ref_32
===============

.. c:function:: void __user *get_addr_ref_32(struct insn *insn, struct pt_regs *regs)

    Obtain a 32-bit linear address

    :param struct insn \*insn:
        Instruction with ModRM, SIB bytes and displacement

    :param struct pt_regs \*regs:
        Register values as seen when entering kernel mode

.. _`get_addr_ref_32.description`:

Description
-----------

This function is to be used with 32-bit address encodings to obtain the
linear memory address referred by the instruction's ModRM, SIB,
displacement bytes and segment base address, as applicable. If in protected
mode, segment limits are enforced.

.. _`get_addr_ref_32.return`:

Return
------


Linear address referenced by instruction and registers on success.

-1L on error.

.. _`get_addr_ref_64`:

get_addr_ref_64
===============

.. c:function:: void __user *get_addr_ref_64(struct insn *insn, struct pt_regs *regs)

    Obtain a 64-bit linear address

    :param struct insn \*insn:
        Instruction struct with ModRM and SIB bytes and displacement

    :param struct pt_regs \*regs:
        Structure with register values as seen when entering kernel mode

.. _`get_addr_ref_64.description`:

Description
-----------

This function is to be used with 64-bit address encodings to obtain the
linear memory address referred by the instruction's ModRM, SIB,
displacement bytes and segment base address, as applicable.

.. _`get_addr_ref_64.return`:

Return
------


Linear address referenced by instruction and registers on success.

-1L on error.

.. _`insn_get_addr_ref`:

insn_get_addr_ref
=================

.. c:function:: void __user *insn_get_addr_ref(struct insn *insn, struct pt_regs *regs)

    Obtain the linear address referred by instruction

    :param struct insn \*insn:
        Instruction structure containing ModRM byte and displacement

    :param struct pt_regs \*regs:
        Structure with register values as seen when entering kernel mode

.. _`insn_get_addr_ref.description`:

Description
-----------

Obtain the linear address referred by the instruction's ModRM, SIB and
displacement bytes, and segment base, as applicable. In protected mode,
segment limits are enforced.

.. _`insn_get_addr_ref.return`:

Return
------


Linear address referenced by instruction and registers on success.

-1L on error.

.. This file was automatic generated / don't edit.

