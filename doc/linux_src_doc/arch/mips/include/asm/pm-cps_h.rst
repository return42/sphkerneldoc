.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/pm-cps.h

.. _`cps_pm_support_state`:

cps_pm_support_state
====================

.. c:function:: bool cps_pm_support_state(enum cps_pm_state state)

    determine whether the system supports a PM state

    :param enum cps_pm_state state:
        the state to test for support

.. _`cps_pm_support_state.description`:

Description
-----------

Returns true if the system supports the given state, otherwise false.

.. _`cps_pm_enter_state`:

cps_pm_enter_state
==================

.. c:function:: int cps_pm_enter_state(enum cps_pm_state state)

    enter a PM state

    :param enum cps_pm_state state:
        the state to enter

.. _`cps_pm_enter_state.description`:

Description
-----------

Enter the given PM state. If coupled_coherence is non-zero then it is
expected that this function be called at approximately the same time on
each coupled CPU. Returns 0 on successful entry & exit, otherwise -errno.

.. This file was automatic generated / don't edit.

