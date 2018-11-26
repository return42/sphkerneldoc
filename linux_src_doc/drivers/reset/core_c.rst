.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/reset/core.c

.. _`reset_control`:

struct reset_control
====================

.. c:type:: struct reset_control

    a reset control

.. _`reset_control.definition`:

Definition
----------

.. code-block:: c

    struct reset_control {
        struct reset_controller_dev *rcdev;
        struct list_head list;
        unsigned int id;
        struct kref refcnt;
        bool shared;
        bool array;
        atomic_t deassert_count;
        atomic_t triggered_count;
    }

.. _`reset_control.members`:

Members
-------

rcdev
    a pointer to the reset controller device
    this reset control belongs to

list
    list entry for the rcdev's reset controller list

id
    ID of the reset controller in the reset
    controller device

refcnt
    Number of gets of this reset_control

shared
    Is this a shared (1), or an exclusive (0) reset_control?

array
    *undescribed*

deassert_count
    *undescribed*

triggered_count
    Number of times this reset line has been reset. Currently
    only used for shared resets, which means that the value
    will be either 0 or 1.

.. _`reset_control_array`:

struct reset_control_array
==========================

.. c:type:: struct reset_control_array

    an array of reset controls

.. _`reset_control_array.definition`:

Definition
----------

.. code-block:: c

    struct reset_control_array {
        struct reset_control base;
        unsigned int num_rstcs;
        struct reset_control *rstc[];
    }

.. _`reset_control_array.members`:

Members
-------

base
    reset control for compatibility with reset control API functions

num_rstcs
    number of reset controls

rstc
    array of reset controls

.. _`of_reset_simple_xlate`:

of_reset_simple_xlate
=====================

.. c:function:: int of_reset_simple_xlate(struct reset_controller_dev *rcdev, const struct of_phandle_args *reset_spec)

    translate reset_spec to the reset line number

    :param rcdev:
        a pointer to the reset controller device
    :type rcdev: struct reset_controller_dev \*

    :param reset_spec:
        reset line specifier as found in the device tree
    :type reset_spec: const struct of_phandle_args \*

.. _`of_reset_simple_xlate.description`:

Description
-----------

This simple translation function should be used for reset controllers
with 1:1 mapping, where reset lines can be indexed by number without gaps.

.. _`reset_controller_register`:

reset_controller_register
=========================

.. c:function:: int reset_controller_register(struct reset_controller_dev *rcdev)

    register a reset controller device

    :param rcdev:
        a pointer to the initialized reset controller device
    :type rcdev: struct reset_controller_dev \*

.. _`reset_controller_unregister`:

reset_controller_unregister
===========================

.. c:function:: void reset_controller_unregister(struct reset_controller_dev *rcdev)

    unregister a reset controller device

    :param rcdev:
        a pointer to the reset controller device
    :type rcdev: struct reset_controller_dev \*

.. _`devm_reset_controller_register`:

devm_reset_controller_register
==============================

.. c:function:: int devm_reset_controller_register(struct device *dev, struct reset_controller_dev *rcdev)

    resource managed \ :c:func:`reset_controller_register`\ 

    :param dev:
        device that is registering this reset controller
    :type dev: struct device \*

    :param rcdev:
        a pointer to the initialized reset controller device
    :type rcdev: struct reset_controller_dev \*

.. _`devm_reset_controller_register.description`:

Description
-----------

Managed \ :c:func:`reset_controller_register`\ . For reset controllers registered by
this function, \ :c:func:`reset_controller_unregister`\  is automatically called on
driver detach. See \ :c:func:`reset_controller_register`\  for more information.

.. _`reset_controller_add_lookup`:

reset_controller_add_lookup
===========================

.. c:function:: void reset_controller_add_lookup(struct reset_control_lookup *lookup, unsigned int num_entries)

    register a set of lookup entries

    :param lookup:
        array of reset lookup entries
    :type lookup: struct reset_control_lookup \*

    :param num_entries:
        number of entries in the lookup array
    :type num_entries: unsigned int

.. _`reset_control_reset`:

reset_control_reset
===================

.. c:function:: int reset_control_reset(struct reset_control *rstc)

    reset the controlled device

    :param rstc:
        reset controller
    :type rstc: struct reset_control \*

.. _`reset_control_reset.description`:

Description
-----------

On a shared reset line the actual reset pulse is only triggered once for the

.. _`reset_control_reset.lifetime-of-the-reset_control-instance`:

lifetime of the reset_control instance
--------------------------------------

for all but the first caller this is
a no-op.
Consumers must not use reset_control_(de)assert on shared reset lines when
reset_control_reset has been used.

If rstc is NULL it is an optional reset and the function will just
return 0.

.. _`reset_control_assert`:

reset_control_assert
====================

.. c:function:: int reset_control_assert(struct reset_control *rstc)

    asserts the reset line

    :param rstc:
        reset controller
    :type rstc: struct reset_control \*

.. _`reset_control_assert.description`:

Description
-----------

Calling this on an exclusive reset controller guarantees that the reset
will be asserted. When called on a shared reset controller the line may
still be deasserted, as long as other users keep it so.

For shared reset controls a driver cannot expect the hw's registers and
internal state to be reset, but must be prepared for this to happen.
Consumers must not use reset_control_reset on shared reset lines when
reset_control_(de)assert has been used.
return 0.

If rstc is NULL it is an optional reset and the function will just
return 0.

.. _`reset_control_deassert`:

reset_control_deassert
======================

.. c:function:: int reset_control_deassert(struct reset_control *rstc)

    deasserts the reset line

    :param rstc:
        reset controller
    :type rstc: struct reset_control \*

.. _`reset_control_deassert.description`:

Description
-----------

After calling this function, the reset is guaranteed to be deasserted.
Consumers must not use reset_control_reset on shared reset lines when
reset_control_(de)assert has been used.
return 0.

If rstc is NULL it is an optional reset and the function will just
return 0.

.. _`reset_control_status`:

reset_control_status
====================

.. c:function:: int reset_control_status(struct reset_control *rstc)

    returns a negative errno if not supported, a positive value if the reset line is asserted, or zero if the reset line is not asserted or if the desc is NULL (optional reset).

    :param rstc:
        reset controller
    :type rstc: struct reset_control \*

.. _`reset_control_put`:

reset_control_put
=================

.. c:function:: void reset_control_put(struct reset_control *rstc)

    free the reset controller

    :param rstc:
        reset controller
    :type rstc: struct reset_control \*

.. _`__device_reset`:

\__device_reset
===============

.. c:function:: int __device_reset(struct device *dev, bool optional)

    find reset controller associated with the device and perform reset

    :param dev:
        device to be reset by the controller
    :type dev: struct device \*

    :param optional:
        whether it is optional to reset the device
    :type optional: bool

.. _`__device_reset.description`:

Description
-----------

Convenience wrapper for \__reset_control_get() and \ :c:func:`reset_control_reset`\ .
This is useful for the common case of devices with single, dedicated reset
lines.

.. _`of_reset_control_get_count`:

of_reset_control_get_count
==========================

.. c:function:: int of_reset_control_get_count(struct device_node *node)

    :param node:
        *undescribed*
    :type node: struct device_node \*

.. _`of_reset_control_array_get`:

of_reset_control_array_get
==========================

.. c:function:: struct reset_control *of_reset_control_array_get(struct device_node *np, bool shared, bool optional)

    Get a list of reset controls using device node.

    :param np:
        device node for the device that requests the reset controls array
    :type np: struct device_node \*

    :param shared:
        whether reset controls are shared or not
    :type shared: bool

    :param optional:
        whether it is optional to get the reset controls
    :type optional: bool

.. _`of_reset_control_array_get.description`:

Description
-----------

Returns pointer to allocated reset_control_array on success or
error on failure

.. _`devm_reset_control_array_get`:

devm_reset_control_array_get
============================

.. c:function:: struct reset_control *devm_reset_control_array_get(struct device *dev, bool shared, bool optional)

    Resource managed reset control array get

    :param dev:
        device that requests the list of reset controls
    :type dev: struct device \*

    :param shared:
        whether reset controls are shared or not
    :type shared: bool

    :param optional:
        whether it is optional to get the reset controls
    :type optional: bool

.. _`devm_reset_control_array_get.description`:

Description
-----------

The reset control array APIs are intended for a list of resets
that just have to be asserted or deasserted, without any
requirements on the order.

Returns pointer to allocated reset_control_array on success or
error on failure

.. This file was automatic generated / don't edit.

