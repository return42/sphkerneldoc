.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpuidle/governors/ladder.c

.. _`ladder_do_selection`:

ladder_do_selection
===================

.. c:function:: void ladder_do_selection(struct ladder_device *ldev, int old_idx, int new_idx)

    prepares private data for a state change

    :param struct ladder_device \*ldev:
        the ladder device

    :param int old_idx:
        the current state index

    :param int new_idx:
        the new target state index

.. _`ladder_select_state`:

ladder_select_state
===================

.. c:function:: int ladder_select_state(struct cpuidle_driver *drv, struct cpuidle_device *dev, bool *dummy)

    selects the next state to enter

    :param struct cpuidle_driver \*drv:
        cpuidle driver

    :param struct cpuidle_device \*dev:
        the CPU

    :param bool \*dummy:
        not used

.. _`ladder_enable_device`:

ladder_enable_device
====================

.. c:function:: int ladder_enable_device(struct cpuidle_driver *drv, struct cpuidle_device *dev)

    setup for the governor

    :param struct cpuidle_driver \*drv:
        cpuidle driver

    :param struct cpuidle_device \*dev:
        the CPU

.. _`ladder_reflect`:

ladder_reflect
==============

.. c:function:: void ladder_reflect(struct cpuidle_device *dev, int index)

    update the correct last_state_idx

    :param struct cpuidle_device \*dev:
        the CPU

    :param int index:
        the index of actual state entered

.. _`init_ladder`:

init_ladder
===========

.. c:function:: int init_ladder( void)

    initializes the governor

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

