.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/power/clock_ops.c

.. _`__pm_clk_enable`:

__pm_clk_enable
===============

.. c:function:: void __pm_clk_enable(struct device *dev, struct pm_clock_entry *ce)

    Enable a clock, reporting any errors

    :param struct device \*dev:
        The device for the given clock

    :param struct pm_clock_entry \*ce:
        PM clock entry corresponding to the clock.

.. _`pm_clk_acquire`:

pm_clk_acquire
==============

.. c:function:: void pm_clk_acquire(struct device *dev, struct pm_clock_entry *ce)

    Acquire a device clock.

    :param struct device \*dev:
        Device whose clock is to be acquired.

    :param struct pm_clock_entry \*ce:
        PM clock entry corresponding to the clock.

.. _`pm_clk_add`:

pm_clk_add
==========

.. c:function:: int pm_clk_add(struct device *dev, const char *con_id)

    Start using a device clock for power management.

    :param struct device \*dev:
        Device whose clock is going to be used for power management.

    :param const char \*con_id:
        Connection ID of the clock.

.. _`pm_clk_add.description`:

Description
-----------

Add the clock represented by \ ``con_id``\  to the list of clocks used for
the power management of \ ``dev``\ .

.. _`pm_clk_add_clk`:

pm_clk_add_clk
==============

.. c:function:: int pm_clk_add_clk(struct device *dev, struct clk *clk)

    Start using a device clock for power management.

    :param struct device \*dev:
        Device whose clock is going to be used for power management.

    :param struct clk \*clk:
        Clock pointer

.. _`pm_clk_add_clk.description`:

Description
-----------

Add the clock to the list of clocks used for the power management of \ ``dev``\ .
The power-management code will take control of the clock reference, so
callers should not call \ :c:func:`clk_put`\  on \ ``clk``\  after this function sucessfully
returned.

.. _`of_pm_clk_add_clk`:

of_pm_clk_add_clk
=================

.. c:function:: int of_pm_clk_add_clk(struct device *dev, const char *name)

    Start using a device clock for power management.

    :param struct device \*dev:
        Device whose clock is going to be used for power management.

    :param const char \*name:
        Name of clock that is going to be used for power management.

.. _`of_pm_clk_add_clk.description`:

Description
-----------

Add the clock described in the 'clocks' device-tree node that matches
with the 'name' provided, to the list of clocks used for the power
management of \ ``dev``\ . On success, returns 0. Returns a negative error
code if the clock is not found or cannot be added.

.. _`of_pm_clk_add_clks`:

of_pm_clk_add_clks
==================

.. c:function:: int of_pm_clk_add_clks(struct device *dev)

    Start using device clock(s) for power management.

    :param struct device \*dev:
        Device whose clock(s) is going to be used for power management.

.. _`of_pm_clk_add_clks.description`:

Description
-----------

Add a series of clocks described in the 'clocks' device-tree node for
a device to the list of clocks used for the power management of \ ``dev``\ .
On success, returns the number of clocks added. Returns a negative
error code if there are no clocks in the device node for the device
or if adding a clock fails.

.. _`__pm_clk_remove`:

__pm_clk_remove
===============

.. c:function:: void __pm_clk_remove(struct pm_clock_entry *ce)

    Destroy PM clock entry.

    :param struct pm_clock_entry \*ce:
        PM clock entry to destroy.

.. _`pm_clk_remove`:

pm_clk_remove
=============

.. c:function:: void pm_clk_remove(struct device *dev, const char *con_id)

    Stop using a device clock for power management.

    :param struct device \*dev:
        Device whose clock should not be used for PM any more.

    :param const char \*con_id:
        Connection ID of the clock.

.. _`pm_clk_remove.description`:

Description
-----------

Remove the clock represented by \ ``con_id``\  from the list of clocks used for
the power management of \ ``dev``\ .

.. _`pm_clk_remove_clk`:

pm_clk_remove_clk
=================

.. c:function:: void pm_clk_remove_clk(struct device *dev, struct clk *clk)

    Stop using a device clock for power management.

    :param struct device \*dev:
        Device whose clock should not be used for PM any more.

    :param struct clk \*clk:
        Clock pointer

.. _`pm_clk_remove_clk.description`:

Description
-----------

Remove the clock pointed to by \ ``clk``\  from the list of clocks used for
the power management of \ ``dev``\ .

.. _`pm_clk_init`:

pm_clk_init
===========

.. c:function:: void pm_clk_init(struct device *dev)

    Initialize a device's list of power management clocks.

    :param struct device \*dev:
        Device to initialize the list of PM clocks for.

.. _`pm_clk_init.description`:

Description
-----------

Initialize the lock and clock_list members of the device's pm_subsys_data
object.

.. _`pm_clk_create`:

pm_clk_create
=============

.. c:function:: int pm_clk_create(struct device *dev)

    Create and initialize a device's list of PM clocks.

    :param struct device \*dev:
        Device to create and initialize the list of PM clocks for.

.. _`pm_clk_create.description`:

Description
-----------

Allocate a struct pm_subsys_data object, initialize its lock and clock_list
members and make the \ ``dev``\ 's power.subsys_data field point to it.

.. _`pm_clk_destroy`:

pm_clk_destroy
==============

.. c:function:: void pm_clk_destroy(struct device *dev)

    Destroy a device's list of power management clocks.

    :param struct device \*dev:
        Device to destroy the list of PM clocks for.

.. _`pm_clk_destroy.description`:

Description
-----------

Clear the \ ``dev``\ 's power.subsys_data field, remove the list of clock entries
from the struct pm_subsys_data object pointed to by it before and free
that object.

.. _`pm_clk_suspend`:

pm_clk_suspend
==============

.. c:function:: int pm_clk_suspend(struct device *dev)

    Disable clocks in a device's PM clock list.

    :param struct device \*dev:
        Device to disable the clocks for.

.. _`pm_clk_resume`:

pm_clk_resume
=============

.. c:function:: int pm_clk_resume(struct device *dev)

    Enable clocks in a device's PM clock list.

    :param struct device \*dev:
        Device to enable the clocks for.

.. _`pm_clk_notify`:

pm_clk_notify
=============

.. c:function:: int pm_clk_notify(struct notifier_block *nb, unsigned long action, void *data)

    Notify routine for device addition and removal.

    :param struct notifier_block \*nb:
        Notifier block object this function is a member of.

    :param unsigned long action:
        Operation being carried out by the caller.

    :param void \*data:
        Device the routine is being run for.

.. _`pm_clk_notify.description`:

Description
-----------

For this function to work, \ ``nb``\  must be a member of an object of type
struct pm_clk_notifier_block containing all of the requisite data.
Specifically, the pm_domain member of that object is copied to the device's
pm_domain field and its con_ids member is used to populate the device's list
of PM clocks, depending on \ ``action``\ .

If the device's pm_domain field is already populated with a value different
from the one stored in the struct pm_clk_notifier_block object, the function
does nothing.

.. _`enable_clock`:

enable_clock
============

.. c:function:: void enable_clock(struct device *dev, const char *con_id)

    Enable a device clock.

    :param struct device \*dev:
        Device whose clock is to be enabled.

    :param const char \*con_id:
        Connection ID of the clock.

.. _`disable_clock`:

disable_clock
=============

.. c:function:: void disable_clock(struct device *dev, const char *con_id)

    Disable a device clock.

    :param struct device \*dev:
        Device whose clock is to be disabled.

    :param const char \*con_id:
        Connection ID of the clock.

.. _`pm_clk_notify`:

pm_clk_notify
=============

.. c:function:: int pm_clk_notify(struct notifier_block *nb, unsigned long action, void *data)

    Notify routine for device addition and removal.

    :param struct notifier_block \*nb:
        Notifier block object this function is a member of.

    :param unsigned long action:
        Operation being carried out by the caller.

    :param void \*data:
        Device the routine is being run for.

.. _`pm_clk_notify.description`:

Description
-----------

For this function to work, \ ``nb``\  must be a member of an object of type
struct pm_clk_notifier_block containing all of the requisite data.
Specifically, the con_ids member of that object is used to enable or disable
the device's clocks, depending on \ ``action``\ .

.. _`pm_clk_add_notifier`:

pm_clk_add_notifier
===================

.. c:function:: void pm_clk_add_notifier(struct bus_type *bus, struct pm_clk_notifier_block *clknb)

    Add bus type notifier for power management clocks.

    :param struct bus_type \*bus:
        Bus type to add the notifier to.

    :param struct pm_clk_notifier_block \*clknb:
        Notifier to be added to the given bus type.

.. _`pm_clk_add_notifier.description`:

Description
-----------

The nb member of \ ``clknb``\  is not expected to be initialized and its
notifier_call member will be replaced with \ :c:func:`pm_clk_notify`\ .  However,
the remaining members of \ ``clknb``\  should be populated prior to calling this
routine.

.. This file was automatic generated / don't edit.

