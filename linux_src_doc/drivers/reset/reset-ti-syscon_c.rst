.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/reset/reset-ti-syscon.c

.. _`ti_syscon_reset_control`:

struct ti_syscon_reset_control
==============================

.. c:type:: struct ti_syscon_reset_control

    reset control structure

.. _`ti_syscon_reset_control.definition`:

Definition
----------

.. code-block:: c

    struct ti_syscon_reset_control {
        unsigned int assert_offset;
        unsigned int assert_bit;
        unsigned int deassert_offset;
        unsigned int deassert_bit;
        unsigned int status_offset;
        unsigned int status_bit;
        u32 flags;
    }

.. _`ti_syscon_reset_control.members`:

Members
-------

assert_offset
    reset assert control register offset from syscon base

assert_bit
    reset assert bit in the reset assert control register

deassert_offset
    reset deassert control register offset from syscon base

deassert_bit
    reset deassert bit in the reset deassert control register

status_offset
    reset status register offset from syscon base

status_bit
    reset status bit in the reset status register

flags
    reset flag indicating how the (de)assert and status are handled

.. _`ti_syscon_reset_data`:

struct ti_syscon_reset_data
===========================

.. c:type:: struct ti_syscon_reset_data

    reset controller information structure

.. _`ti_syscon_reset_data.definition`:

Definition
----------

.. code-block:: c

    struct ti_syscon_reset_data {
        struct reset_controller_dev rcdev;
        struct regmap *regmap;
        struct ti_syscon_reset_control *controls;
        unsigned int nr_controls;
    }

.. _`ti_syscon_reset_data.members`:

Members
-------

rcdev
    reset controller entity

regmap
    regmap handle containing the memory-mapped reset registers

controls
    array of reset controls

nr_controls
    number of controls in control array

.. _`ti_syscon_reset_assert`:

ti_syscon_reset_assert
======================

.. c:function:: int ti_syscon_reset_assert(struct reset_controller_dev *rcdev, unsigned long id)

    assert device reset

    :param rcdev:
        reset controller entity
    :type rcdev: struct reset_controller_dev \*

    :param id:
        ID of the reset to be asserted
    :type id: unsigned long

.. _`ti_syscon_reset_assert.description`:

Description
-----------

This function implements the reset driver op to assert a device's reset.
This asserts the reset in a manner prescribed by the reset flags.

.. _`ti_syscon_reset_assert.return`:

Return
------

0 for successful request, else a corresponding error value

.. _`ti_syscon_reset_deassert`:

ti_syscon_reset_deassert
========================

.. c:function:: int ti_syscon_reset_deassert(struct reset_controller_dev *rcdev, unsigned long id)

    deassert device reset

    :param rcdev:
        reset controller entity
    :type rcdev: struct reset_controller_dev \*

    :param id:
        ID of reset to be deasserted
    :type id: unsigned long

.. _`ti_syscon_reset_deassert.description`:

Description
-----------

This function implements the reset driver op to deassert a device's reset.
This deasserts the reset in a manner prescribed by the reset flags.

.. _`ti_syscon_reset_deassert.return`:

Return
------

0 for successful request, else a corresponding error value

.. _`ti_syscon_reset_status`:

ti_syscon_reset_status
======================

.. c:function:: int ti_syscon_reset_status(struct reset_controller_dev *rcdev, unsigned long id)

    check device reset status

    :param rcdev:
        reset controller entity
    :type rcdev: struct reset_controller_dev \*

    :param id:
        ID of the reset for which the status is being requested
    :type id: unsigned long

.. _`ti_syscon_reset_status.description`:

Description
-----------

This function implements the reset driver op to return the status of a
device's reset.

.. _`ti_syscon_reset_status.return`:

Return
------

0 if reset is deasserted, true if reset is asserted, else a
corresponding error value

.. This file was automatic generated / don't edit.

