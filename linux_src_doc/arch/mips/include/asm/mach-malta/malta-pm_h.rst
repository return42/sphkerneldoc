.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/mach-malta/malta-pm.h

.. _`mips_pm_suspend`:

mips_pm_suspend
===============

.. c:function:: int mips_pm_suspend(unsigned state)

    enter a suspend state

    :param unsigned state:
        the state to enter, one of PIIX4_FUNC3IO_PMCNTRL_SUS_TYP\_\*

.. _`mips_pm_suspend.description`:

Description
-----------

Enters a suspend state via the Malta's PIIX4. If the state to be entered
is one which loses context (eg. SOFF) then this function will never
return.

.. This file was automatic generated / don't edit.

