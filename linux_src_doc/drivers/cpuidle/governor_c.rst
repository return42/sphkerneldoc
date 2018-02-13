.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpuidle/governor.c

.. _`__cpuidle_find_governor`:

__cpuidle_find_governor
=======================

.. c:function:: struct cpuidle_governor *__cpuidle_find_governor(const char *str)

    finds a governor of the specified name

    :param const char \*str:
        the name

.. _`__cpuidle_find_governor.description`:

Description
-----------

Must be called with cpuidle_lock acquired.

.. _`cpuidle_switch_governor`:

cpuidle_switch_governor
=======================

.. c:function:: int cpuidle_switch_governor(struct cpuidle_governor *gov)

    changes the governor

    :param struct cpuidle_governor \*gov:
        the new target governor
        Must be called with cpuidle_lock acquired.

.. _`cpuidle_register_governor`:

cpuidle_register_governor
=========================

.. c:function:: int cpuidle_register_governor(struct cpuidle_governor *gov)

    registers a governor

    :param struct cpuidle_governor \*gov:
        the governor

.. This file was automatic generated / don't edit.

