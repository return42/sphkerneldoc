.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/events/uprobes.c

.. _`__replace_page`:

__replace_page
==============

.. c:function:: int __replace_page(struct vm_area_struct *vma, unsigned long addr, struct page *old_page, struct page *new_page)

    replace page in vma by new page. based on replace_page in mm/ksm.c

    :param struct vm_area_struct \*vma:
        vma that holds the pte pointing to page

    :param unsigned long addr:
        address the old \ ``page``\  is mapped at

    :param struct page \*old_page:
        *undescribed*

    :param struct page \*new_page:
        *undescribed*

.. _`__replace_page.description`:

Description
-----------

Returns 0 on success, -EFAULT on failure.

.. _`is_swbp_insn`:

is_swbp_insn
============

.. c:function:: bool is_swbp_insn(uprobe_opcode_t *insn)

    check if instruction is breakpoint instruction.

    :param uprobe_opcode_t \*insn:
        instruction to be checked.
        Default implementation of is_swbp_insn
        Returns true if \ ``insn``\  is a breakpoint instruction.

.. _`is_trap_insn`:

is_trap_insn
============

.. c:function:: bool is_trap_insn(uprobe_opcode_t *insn)

    check if instruction is breakpoint instruction.

    :param uprobe_opcode_t \*insn:
        instruction to be checked.
        Default implementation of is_trap_insn
        Returns true if \ ``insn``\  is a breakpoint instruction.

.. _`is_trap_insn.description`:

Description
-----------

This function is needed for the case where an architecture has multiple
trap instructions (like powerpc).

.. _`set_swbp`:

set_swbp
========

.. c:function:: int set_swbp(struct arch_uprobe *auprobe, struct mm_struct *mm, unsigned long vaddr)

    store breakpoint at a given address.

    :param struct arch_uprobe \*auprobe:
        arch specific probepoint information.

    :param struct mm_struct \*mm:
        the probed process address space.

    :param unsigned long vaddr:
        the virtual address to insert the opcode.

.. _`set_swbp.description`:

Description
-----------

For mm \ ``mm``\ , store the breakpoint instruction at \ ``vaddr``\ .
Return 0 (success) or a negative errno.

.. _`set_orig_insn`:

set_orig_insn
=============

.. c:function:: int set_orig_insn(struct arch_uprobe *auprobe, struct mm_struct *mm, unsigned long vaddr)

    Restore the original instruction.

    :param struct arch_uprobe \*auprobe:
        arch specific probepoint information.

    :param struct mm_struct \*mm:
        the probed process address space.

    :param unsigned long vaddr:
        the virtual address to insert the opcode.

.. _`set_orig_insn.description`:

Description
-----------

For mm \ ``mm``\ , restore the original opcode (opcode) at \ ``vaddr``\ .
Return 0 (success) or a negative errno.

.. _`uprobe_get_swbp_addr`:

uprobe_get_swbp_addr
====================

.. c:function:: unsigned long uprobe_get_swbp_addr(struct pt_regs *regs)

    compute address of swbp given post-swbp regs

    :param struct pt_regs \*regs:
        Reflects the saved state of the task after it has hit a breakpoint
        instruction.
        Return the address of the breakpoint instruction.

.. This file was automatic generated / don't edit.

