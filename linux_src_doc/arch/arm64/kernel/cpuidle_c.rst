.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/kernel/cpuidle.c

.. _`arm_cpuidle_suspend`:

arm_cpuidle_suspend
===================

.. c:function:: int arm_cpuidle_suspend(int index)

    function to enter a low-power idle state

    :param index:
        *undescribed*
    :type index: int

.. _`arm_cpuidle_suspend.return`:

Return
------

0 on success, -EOPNOTSUPP if CPU suspend hook not initialized, CPU
operations back-end error code otherwise.

.. This file was automatic generated / don't edit.

