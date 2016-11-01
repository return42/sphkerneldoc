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
        unsigned int refcnt;
        int shared;
        atomic_t deassert_count;
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

deassert_count
    *undescribed*

.. _`of_reset_simple_xlate`:

of_reset_simple_xlate
=====================

.. c:function:: int of_reset_simple_xlate(struct reset_controller_dev *rcdev, const struct of_phandle_args *reset_spec)

    translate reset_spec to the reset line number

    :param struct reset_controller_dev \*rcdev:
        a pointer to the reset controller device

    :param const struct of_phandle_args \*reset_spec:
        reset line specifier as found in the device tree

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

    :param struct reset_controller_dev \*rcdev:
        a pointer to the initialized reset controller device

.. _`reset_controller_unregister`:

reset_controller_unregister
===========================

.. c:function:: void reset_controller_unregister(struct reset_controller_dev *rcdev)

    unregister a reset controller device

    :param struct reset_controller_dev \*rcdev:
        a pointer to the reset controller device

.. _`devm_reset_controller_register`:

devm_reset_controller_register
==============================

.. c:function:: int devm_reset_controller_register(struct device *dev, struct reset_controller_dev *rcdev)

    resource managed \ :c:func:`reset_controller_register`\ 

    :param struct device \*dev:
        device that is registering this reset controller

    :param struct reset_controller_dev \*rcdev:
        a pointer to the initialized reset controller device

.. _`devm_reset_controller_register.description`:

Description
-----------

Managed \ :c:func:`reset_controller_register`\ . For reset controllers registered by
this function, \ :c:func:`reset_controller_unregister`\  is automatically called on
driver detach. See \ :c:func:`reset_controller_register`\  for more information.

.. _`reset_control_reset`:

reset_control_reset
===================

.. c:function:: int reset_control_reset(struct reset_control *rstc)

    reset the controlled device

    :param struct reset_control \*rstc:
        reset controller

.. _`reset_control_reset.description`:

Description
-----------

Calling this on a shared reset controller is an error.

.. _`reset_control_assert`:

reset_control_assert
====================

.. c:function:: int reset_control_assert(struct reset_control *rstc)

    asserts the reset line

    :param struct reset_control \*rstc:
        reset controller

.. _`reset_control_assert.description`:

Description
-----------

Calling this on an exclusive reset controller guarantees that the reset
will be asserted. When called on a shared reset controller the line may
still be deasserted, as long as other users keep it so.

For shared reset controls a driver cannot expect the hw's registers and
internal state to be reset, but must be prepared for this to happen.

.. _`reset_control_deassert`:

reset_control_deassert
======================

.. c:function:: int reset_control_deassert(struct reset_control *rstc)

    deasserts the reset line

    :param struct reset_control \*rstc:
        reset controller

.. _`reset_control_deassert.description`:

Description
-----------

After calling this function, the reset is guaranteed to be deasserted.

.. _`reset_control_status`:

reset_control_status
====================

.. c:function:: int reset_control_status(struct reset_control *rstc)

    returns a negative errno if not supported, a positive value if the reset line is asserted, or zero if the reset line is not asserted.

    :param struct reset_control \*rstc:
        reset controller

.. _`reset_control_put`:

reset_control_put
=================

.. c:function:: void reset_control_put(struct reset_control *rstc)

    free the reset controller

    :param struct reset_control \*rstc:
        reset controller

.. _`device_reset`:

device_reset
============

.. c:function:: int device_reset(struct device *dev)

    find reset controller associated with the device and perform reset

    :param struct device \*dev:
        device to be reset by the controller

.. _`device_reset.description`:

Description
-----------

Convenience wrapper for \ :c:func:`reset_control_get`\  and \ :c:func:`reset_control_reset`\ .
This is useful for the common case of devices with single, dedicated reset
lines.

.. This file was automatic generated / don't edit.

