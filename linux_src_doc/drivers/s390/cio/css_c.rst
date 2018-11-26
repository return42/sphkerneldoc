.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/css.c

.. _`css_sch_device_unregister`:

css_sch_device_unregister
=========================

.. c:function:: void css_sch_device_unregister(struct subchannel *sch)

    unregister a subchannel

    :param sch:
        subchannel to be unregistered
    :type sch: struct subchannel \*

.. _`css_sch_is_valid`:

css_sch_is_valid
================

.. c:function:: int css_sch_is_valid(struct schib *schib)

    check if a subchannel is valid

    :param schib:
        subchannel information block for the subchannel
    :type schib: struct schib \*

.. _`css_sched_sch_todo`:

css_sched_sch_todo
==================

.. c:function:: void css_sched_sch_todo(struct subchannel *sch, enum sch_todo todo)

    schedule a subchannel operation

    :param sch:
        subchannel
    :type sch: struct subchannel \*

    :param todo:
        todo
    :type todo: enum sch_todo

.. _`css_sched_sch_todo.description`:

Description
-----------

Schedule the operation identified by \ ``todo``\  to be performed on the slow path
workqueue. Do nothing if another operation with higher priority is already
scheduled. Needs to be called with subchannel lock held.

.. _`css_driver_register`:

css_driver_register
===================

.. c:function:: int css_driver_register(struct css_driver *cdrv)

    register a css driver

    :param cdrv:
        css driver to register
    :type cdrv: struct css_driver \*

.. _`css_driver_register.description`:

Description
-----------

This is mainly a wrapper around driver_register that sets name
and bus_type in the embedded struct device_driver correctly.

.. _`css_driver_unregister`:

css_driver_unregister
=====================

.. c:function:: void css_driver_unregister(struct css_driver *cdrv)

    unregister a css driver

    :param cdrv:
        css driver to unregister
    :type cdrv: struct css_driver \*

.. _`css_driver_unregister.description`:

Description
-----------

This is a wrapper around driver_unregister.

.. This file was automatic generated / don't edit.

