.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/metag/include/uapi/asm/ptrace.h

.. _`user_gp_regs`:

struct user_gp_regs
===================

.. c:type:: struct user_gp_regs

    User general purpose registers

.. _`user_gp_regs.definition`:

Definition
----------

.. code-block:: c

    struct user_gp_regs {
        unsigned long dx[8][2];
        unsigned long ax[4][2];
        unsigned long pc;
        unsigned long status;
        unsigned long rpt;
        unsigned long bpobits;
        unsigned long mode;
        unsigned long _pad1;
    }

.. _`user_gp_regs.members`:

Members
-------

dx
    GP data unit regs (dx[reg][unit] = D{unit:0-1}.{reg:0-7})

ax
    GP address unit regs (ax[reg][unit] = A{unit:0-1}.{reg:0-3})

pc
    PC register

status
    TXSTATUS register (condition flags, LSM_STEP etc)

rpt
    TXRPT registers (branch repeat counter)

bpobits
    TXBPOBITS register ("branch prediction other" bits)

mode
    TXMODE register

\_pad1
    Reserved padding to make sizeof obviously 64bit aligned

.. _`user_gp_regs.description`:

Description
-----------

This is the user-visible general purpose register state structure.

It can be accessed through PTRACE_GETREGSET with NT_PRSTATUS.

It is also used in the signal context.

.. _`user_cb_regs`:

struct user_cb_regs
===================

.. c:type:: struct user_cb_regs

    User catch buffer registers

.. _`user_cb_regs.definition`:

Definition
----------

.. code-block:: c

    struct user_cb_regs {
        unsigned long flags;
        unsigned long addr;
        unsigned long long data;
    }

.. _`user_cb_regs.members`:

Members
-------

flags
    TXCATCH0 register (fault flags)

addr
    TXCATCH1 register (fault address)

data
    TXCATCH2 and TXCATCH3 registers (low and high data word)

.. _`user_cb_regs.description`:

Description
-----------

This is the user-visible catch buffer register state structure containing
information about a failed memory access, and allowing the access to be
modified and replayed.

It can be accessed through PTRACE_GETREGSET with NT_METAG_CBUF.

.. _`user_rp_state`:

struct user_rp_state
====================

.. c:type:: struct user_rp_state

    User read pipeline state

.. _`user_rp_state.definition`:

Definition
----------

.. code-block:: c

    struct user_rp_state {
        unsigned long long entries[6];
        unsigned long mask;
    }

.. _`user_rp_state.members`:

Members
-------

entries
    Read pipeline entries

mask
    Mask of valid pipeline entries (RPMask from TXDIVTIME register)

.. _`user_rp_state.description`:

Description
-----------

This is the user-visible read pipeline state structure containing the entries
currently in the read pipeline and the mask of valid entries.

It can be accessed through PTRACE_GETREGSET with NT_METAG_RPIPE.

.. This file was automatic generated / don't edit.

