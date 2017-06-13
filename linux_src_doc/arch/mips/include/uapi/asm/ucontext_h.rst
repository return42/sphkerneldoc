.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/uapi/asm/ucontext.h

.. _`extcontext`:

struct extcontext
=================

.. c:type:: struct extcontext

    extended context header structure

.. _`extcontext.definition`:

Definition
----------

.. code-block:: c

    struct extcontext {
        unsigned int magic;
        unsigned int size;
    }

.. _`extcontext.members`:

Members
-------

magic
    magic value identifying the type of extended context

size
    the size in bytes of the enclosing structure

.. _`extcontext.description`:

Description
-----------

Extended context structures provide context which does not fit within struct
sigcontext. They are placed sequentially in memory at the end of struct
ucontext and struct sigframe, with each extended context structure beginning
with a header defined by this struct. The type of context represented is
indicated by the magic field. Userland may check each extended context
structure against magic values that it recognises. The size field allows any
unrecognised context to be skipped, allowing for future expansion. The end
of the extended context data is indicated by the magic value
END_EXTCONTEXT_MAGIC.

.. _`msa_extcontext`:

struct msa_extcontext
=====================

.. c:type:: struct msa_extcontext

    MSA extended context structure

.. _`msa_extcontext.definition`:

Definition
----------

.. code-block:: c

    struct msa_extcontext {
        struct extcontext ext;
    #define MSA_EXTCONTEXT_MAGIC 0x784d5341
        unsigned long long wr;
        unsigned int csr;
    }

.. _`msa_extcontext.members`:

Members
-------

ext
    the extended context header, with magic == MSA_EXTCONTEXT_MAGIC

wr
    the most significant 64 bits of each MSA vector register

csr
    the value of the MSA control & status register

.. _`msa_extcontext.description`:

Description
-----------

If MSA context is live for a task at the time a signal is delivered to it,
this structure will hold the MSA context of the task as it was prior to the
signal delivery.

.. _`ucontext`:

struct ucontext
===============

.. c:type:: struct ucontext

    user context structure

.. _`ucontext.definition`:

Definition
----------

.. code-block:: c

    struct ucontext {
        unsigned long uc_flags;
        struct ucontext *uc_link;
        stack_t uc_stack;
        struct sigcontext uc_mcontext;
        sigset_t uc_sigmask;
        unsigned long long uc_extcontext;
    }

.. _`ucontext.members`:

Members
-------

uc_flags
    *undescribed*

uc_link
    *undescribed*

uc_stack
    *undescribed*

uc_mcontext
    holds basic processor state

uc_sigmask
    *undescribed*

uc_extcontext
    holds extended processor state

.. This file was automatic generated / don't edit.

