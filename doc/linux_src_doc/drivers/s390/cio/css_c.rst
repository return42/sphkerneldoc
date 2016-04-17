.. -*- coding: utf-8; mode: rst -*-

=====
css.c
=====


.. _`css_sch_device_unregister`:

css_sch_device_unregister
=========================

.. c:function:: void css_sch_device_unregister (struct subchannel *sch)

    unregister a subchannel

    :param struct subchannel \*sch:
        subchannel to be unregistered



.. _`css_sch_is_valid`:

css_sch_is_valid
================

.. c:function:: int css_sch_is_valid (struct schib *schib)

    check if a subchannel is valid

    :param struct schib \*schib:
        subchannel information block for the subchannel



.. _`css_sched_sch_todo`:

css_sched_sch_todo
==================

.. c:function:: void css_sched_sch_todo (struct subchannel *sch, enum sch_todo todo)

    schedule a subchannel operation

    :param struct subchannel \*sch:
        subchannel

    :param enum sch_todo todo:
        todo



.. _`css_sched_sch_todo.description`:

Description
-----------

Schedule the operation identified by ``todo`` to be performed on the slow path
workqueue. Do nothing if another operation with higher priority is already
scheduled. Needs to be called with subchannel lock held.



.. _`css_driver_register`:

css_driver_register
===================

.. c:function:: int css_driver_register (struct css_driver *cdrv)

    register a css driver

    :param struct css_driver \*cdrv:
        css driver to register



.. _`css_driver_register.description`:

Description
-----------

This is mainly a wrapper around driver_register that sets name
and bus_type in the embedded struct device_driver correctly.



.. _`css_driver_unregister`:

css_driver_unregister
=====================

.. c:function:: void css_driver_unregister (struct css_driver *cdrv)

    unregister a css driver

    :param struct css_driver \*cdrv:
        css driver to unregister



.. _`css_driver_unregister.description`:

Description
-----------

This is a wrapper around driver_unregister.

