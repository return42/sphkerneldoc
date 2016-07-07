.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kernel/elf.c

.. _`mode_req`:

struct mode_req
===============

.. c:type:: struct mode_req

    ABI FPU mode requirements

.. _`mode_req.definition`:

Definition
----------

.. code-block:: c

    struct mode_req {
        bool single;
        bool soft;
        bool fr1;
        bool frdefault;
        bool fre;
    }

.. _`mode_req.members`:

Members
-------

single
    The program being loaded needs an FPU but it will only issue
    single precision instructions meaning that it can execute in
    either FR0 or FR1.

soft
    The soft(-float) requirement means that the program being
    loaded needs has no FPU dependency at all (i.e. it has no
    FPU instructions).

fr1
    The program being loaded depends on FPU being in FR=1 mode.

frdefault
    The program being loaded depends on the default FPU mode.
    That is FR0 for O32 and FR1 for N32/N64.

fre
    The program being loaded depends on FPU with FRE=1. This mode is
    a bridge which uses FR=1 whilst still being able to maintain
    full compatibility with pre-existing code using the O32 FP32
    ABI.

.. _`mode_req.more-information-about-the-fp-abis-can-be-found-here`:

More information about the FP ABIs can be found here
----------------------------------------------------


https://dmz-portal.mips.com/wiki/MIPS_O32_ABI_-_FR0_and_FR1_Interlinking#10.4.1._Basic_mode_set-up

.. This file was automatic generated / don't edit.

