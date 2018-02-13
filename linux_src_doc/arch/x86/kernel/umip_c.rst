.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/umip.c

.. _`__printf`:

\__printf
=========

.. c:function::  __printf( 3,  4)

    Print a rate-limited message

    :param  3:
        *undescribed*

    :param  4:
        *undescribed*

.. _`__printf.description`:

Description
-----------

Print the text contained in \ ``fmt``\ . The print rate is limited to bursts of 5
messages every two minutes. The purpose of this customized version of
\ :c:func:`printk`\  is to print messages when user space processes use any of the
UMIP-protected instructions. Thus, the printed text is prepended with the
task name and process ID number of the current task as well as the
instruction and stack pointers in \ ``regs``\  as seen when entering kernel mode.

.. _`__printf.return`:

Return
------


None.

.. _`identify_insn`:

identify_insn
=============

.. c:function:: int identify_insn(struct insn *insn)

    Identify a UMIP-protected instruction

    :param struct insn \*insn:
        Instruction structure with opcode and ModRM byte.

.. _`identify_insn.description`:

Description
-----------

From the opcode and ModRM.reg in \ ``insn``\  identify, if any, a UMIP-protected
instruction that can be emulated.

.. _`identify_insn.return`:

Return
------


On success, a constant identifying a specific UMIP-protected instruction that
can be emulated.

-EINVAL on error or when not an UMIP-protected instruction that can be
emulated.

.. _`emulate_umip_insn`:

emulate_umip_insn
=================

.. c:function:: int emulate_umip_insn(struct insn *insn, int umip_inst, unsigned char *data, int *data_size)

    Emulate UMIP instructions and return dummy values

    :param struct insn \*insn:
        Instruction structure with operands

    :param int umip_inst:
        A constant indicating the instruction to emulate

    :param unsigned char \*data:
        Buffer into which the dummy result is stored

    :param int \*data_size:
        Size of the emulated result

.. _`emulate_umip_insn.description`:

Description
-----------

Emulate an instruction protected by UMIP and provide a dummy result. The
result of the emulation is saved in \ ``data``\ . The size of the results depends
on both the instruction and type of operand (register vs memory address).
The size of the result is updated in \ ``data_size``\ . Caller is responsible
of providing a \ ``data``\  buffer of at least UMIP_GDT_IDT_BASE_SIZE +
UMIP_GDT_IDT_LIMIT_SIZE bytes.

.. _`emulate_umip_insn.return`:

Return
------


0 on success, -EINVAL on error while emulating.

.. _`force_sig_info_umip_fault`:

force_sig_info_umip_fault
=========================

.. c:function:: void force_sig_info_umip_fault(void __user *addr, struct pt_regs *regs)

    Force a SIGSEGV with SEGV_MAPERR

    :param void __user \*addr:
        Address that caused the signal

    :param struct pt_regs \*regs:
        Register set containing the instruction pointer

.. _`force_sig_info_umip_fault.description`:

Description
-----------

Force a SIGSEGV signal with SEGV_MAPERR as the error code. This function is
intended to be used to provide a segmentation fault when the result of the
UMIP emulation could not be copied to the user space memory.

.. _`force_sig_info_umip_fault.return`:

Return
------

none

.. _`fixup_umip_exception`:

fixup_umip_exception
====================

.. c:function:: bool fixup_umip_exception(struct pt_regs *regs)

    Fixup a general protection fault caused by UMIP

    :param struct pt_regs \*regs:
        Registers as saved when entering the #GP handler

.. _`fixup_umip_exception.description`:

Description
-----------

The instructions sgdt, sidt, str, smsw, sldt cause a general protection
fault if executed with CPL > 0 (i.e., from user space). If the offending
user-space process is not in long mode, this function fixes the exception
up and provides dummy results for sgdt, sidt and smsw; str and sldt are not
fixed up. Also long mode user-space processes are not fixed up.

If operands are memory addresses, results are copied to user-space memory as
indicated by the instruction pointed by eIP using the registers indicated in
the instruction operands. If operands are registers, results are copied into
the context that was saved when entering kernel mode.

.. _`fixup_umip_exception.return`:

Return
------


True if emulation was successful; false if not.

.. This file was automatic generated / don't edit.

