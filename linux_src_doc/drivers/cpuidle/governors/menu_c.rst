.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpuidle/governors/menu.c

.. _`menu_select`:

menu_select
===========

.. c:function:: int menu_select(struct cpuidle_driver *drv, struct cpuidle_device *dev, bool *stop_tick)

    selects the next idle state to enter

    :param struct cpuidle_driver \*drv:
        cpuidle driver containing state data

    :param struct cpuidle_device \*dev:
        the CPU

    :param bool \*stop_tick:
        indication on whether or not to stop the tick

.. _`menu_reflect`:

menu_reflect
============

.. c:function:: void menu_reflect(struct cpuidle_device *dev, int index)

    records that data structures need update

    :param struct cpuidle_device \*dev:
        the CPU

    :param int index:
        the index of actual entered state

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

    :param struct cpuidle_driver \*drv:
        cpuidle driver containing state data

    :param struct cpuidle_device \*dev:
        the CPU

.. _`menu_enable_device`:

menu_enable_device
==================

.. c:function:: int menu_enable_device(struct cpuidle_driver *drv, struct cpuidle_device *dev)

    scans a CPU's states and does setup

    :param struct cpuidle_driver \*drv:
        cpuidle driver

    :param struct cpuidle_device \*dev:
        the CPU

.. _`init_menu`:

init_menu
=========

.. c:function:: int init_menu( void)

    initializes the governor

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

