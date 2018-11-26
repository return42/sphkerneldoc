.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpuidle/governors/ladder.c

.. _`ladder_do_selection`:

ladder_do_selection
===================

.. c:function:: void ladder_do_selection(struct ladder_device *ldev, int old_idx, int new_idx)

    prepares private data for a state change

    :param ldev:
        the ladder device
    :type ldev: struct ladder_device \*

    :param old_idx:
        the current state index
    :type old_idx: int

    :param new_idx:
        the new target state index
    :type new_idx: int

.. _`ladder_select_state`:

ladder_select_state
===================

.. c:function:: int ladder_select_state(struct cpuidle_driver *drv, struct cpuidle_device *dev, bool *dummy)

    selects the next state to enter

    :param drv:
        cpuidle driver
    :type drv: struct cpuidle_driver \*

    :param dev:
        the CPU
    :type dev: struct cpuidle_device \*

    :param dummy:
        not used
    :type dummy: bool \*

.. _`ladder_enable_device`:

ladder_enable_device
====================

.. c:function:: int ladder_enable_device(struct cpuidle_driver *drv, struct cpuidle_device *dev)

    setup for the governor

    :param drv:
        cpuidle driver
    :type drv: struct cpuidle_driver \*

    :param dev:
        the CPU
    :type dev: struct cpuidle_device \*

.. _`ladder_reflect`:

ladder_reflect
==============

.. c:function:: void ladder_reflect(struct cpuidle_device *dev, int index)

    update the correct last_state_idx

    :param dev:
        the CPU
    :type dev: struct cpuidle_device \*

    :param index:
        the index of actual state entered
    :type index: int

.. _`init_ladder`:

init_ladder
===========

.. c:function:: int init_ladder( void)

    initializes the governor

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

