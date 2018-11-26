.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpuidle/governors/menu.c

.. _`menu_select`:

menu_select
===========

.. c:function:: int menu_select(struct cpuidle_driver *drv, struct cpuidle_device *dev, bool *stop_tick)

    selects the next idle state to enter

    :param drv:
        cpuidle driver containing state data
    :type drv: struct cpuidle_driver \*

    :param dev:
        the CPU
    :type dev: struct cpuidle_device \*

    :param stop_tick:
        indication on whether or not to stop the tick
    :type stop_tick: bool \*

.. _`menu_reflect`:

menu_reflect
============

.. c:function:: void menu_reflect(struct cpuidle_device *dev, int index)

    records that data structures need update

    :param dev:
        the CPU
    :type dev: struct cpuidle_device \*

    :param index:
        the index of actual entered state
    :type index: int

.. _`menu_reflect.note`:

NOTE
----

it's important to be fast here because this operation will add to
the overall exit latency.

.. _`menu_update`:

menu_update
===========

.. c:function:: void menu_update(struct cpuidle_driver *drv, struct cpuidle_device *dev)

    attempts to guess what happened after entry

    :param drv:
        cpuidle driver containing state data
    :type drv: struct cpuidle_driver \*

    :param dev:
        the CPU
    :type dev: struct cpuidle_device \*

.. _`menu_enable_device`:

menu_enable_device
==================

.. c:function:: int menu_enable_device(struct cpuidle_driver *drv, struct cpuidle_device *dev)

    scans a CPU's states and does setup

    :param drv:
        cpuidle driver
    :type drv: struct cpuidle_driver \*

    :param dev:
        the CPU
    :type dev: struct cpuidle_device \*

.. _`init_menu`:

init_menu
=========

.. c:function:: int init_menu( void)

    initializes the governor

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

