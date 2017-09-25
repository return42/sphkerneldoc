.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/parisc/include/uapi/asm/ptrace.h

.. _`user_regs_struct`:

struct user_regs_struct
=======================

.. c:type:: struct user_regs_struct

    User general purpose registers

.. _`user_regs_struct.definition`:

Definition
----------

.. code-block:: c

    struct user_regs_struct {
        unsigned long gr[32];
        unsigned long sr[8];
        unsigned long iaoq[2];
        unsigned long iasq[2];
        unsigned long sar;
        unsigned long iir;
        unsigned long isr;
        unsigned long ior;
        unsigned long ipsw;
        unsigned long cr0;
        unsigned long cr24, cr25, cr26, cr27, cr28, cr29, cr30, cr31;
        unsigned long cr8, cr9, cr12, cr13, cr10, cr15;
        unsigned long _pad[80-64];
    }

.. _`user_regs_struct.members`:

Members
-------

gr
    *undescribed*

sr
    *undescribed*

iaoq
    *undescribed*

iasq
    *undescribed*

sar
    *undescribed*

iir
    *undescribed*

isr
    *undescribed*

ior
    *undescribed*

ipsw
    *undescribed*

cr0
    *undescribed*

cr24
    *undescribed*

cr25
    *undescribed*

cr26
    *undescribed*

cr27
    *undescribed*

cr28
    *undescribed*

cr29
    *undescribed*

cr30
    *undescribed*

cr31
    *undescribed*

cr8
    *undescribed*

cr9
    *undescribed*

cr12
    *undescribed*

cr13
    *undescribed*

cr10
    *undescribed*

cr15
    *undescribed*

_pad
    *undescribed*

.. _`user_regs_struct.description`:

Description
-----------

This is the user-visible general purpose register state structure
which is used to define the elf_gregset_t.

It can be accessed through PTRACE_GETREGSET with NT_PRSTATUS
and through PTRACE_GETREGS.

.. _`user_fp_struct`:

struct user_fp_struct
=====================

.. c:type:: struct user_fp_struct

    User floating point registers

.. _`user_fp_struct.definition`:

Definition
----------

.. code-block:: c

    struct user_fp_struct {
        __u64 fr[32];
    }

.. _`user_fp_struct.members`:

Members
-------

fr
    *undescribed*

.. _`user_fp_struct.description`:

Description
-----------

This is the user-visible floating point register state structure.
It uses the same layout and size as elf_fpregset_t.

It can be accessed through PTRACE_GETREGSET with NT_PRFPREG
and through PTRACE_GETFPREGS.

.. This file was automatic generated / don't edit.

