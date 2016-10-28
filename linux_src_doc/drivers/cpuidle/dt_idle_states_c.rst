.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpuidle/dt_idle_states.c

.. _`dt_init_idle_driver`:

dt_init_idle_driver
===================

.. c:function:: int dt_init_idle_driver(struct cpuidle_driver *drv, const struct of_device_id *matches, unsigned int start_idx)

    Parse the DT idle states and initialize the idle driver states array

    :param struct cpuidle_driver \*drv:
        Pointer to CPU idle driver to be initialized

    :param const struct of_device_id \*matches:
        Array of of_device_id match structures to search in for
        compatible idle state nodes. The data pointer for each valid
        struct of_device_id entry in the matches array must point to
        a function with the following signature, that corresponds to
        the CPUidle state enter function signature:

    :param unsigned int start_idx:
        First idle state index to be initialized

.. _`dt_init_idle_driver.description`:

Description
-----------

int (\*)(struct cpuidle_device \*dev,
struct cpuidle_driver \*drv,
int index);

If DT idle states are detected and are valid the state count and states
array entries in the cpuidle driver are initialized accordingly starting
from index start_idx.

.. _`dt_init_idle_driver.return`:

Return
------

number of valid DT idle states parsed, <0 on failure

.. This file was automatic generated / don't edit.

