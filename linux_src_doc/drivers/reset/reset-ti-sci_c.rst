.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/reset/reset-ti-sci.c

.. _`ti_sci_reset_control`:

struct ti_sci_reset_control
===========================

.. c:type:: struct ti_sci_reset_control

    reset control structure

.. _`ti_sci_reset_control.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_reset_control {
        u32 dev_id;
        u32 reset_mask;
        struct mutex lock;
    }

.. _`ti_sci_reset_control.members`:

Members
-------

dev_id
    SoC-specific device identifier

reset_mask
    reset mask to use for toggling reset

lock
    synchronize reset_mask read-modify-writes

.. _`ti_sci_reset_data`:

struct ti_sci_reset_data
========================

.. c:type:: struct ti_sci_reset_data

    reset controller information structure

.. _`ti_sci_reset_data.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_reset_data {
        struct reset_controller_dev rcdev;
        struct device *dev;
        const struct ti_sci_handle *sci;
        struct idr idr;
    }

.. _`ti_sci_reset_data.members`:

Members
-------

rcdev
    reset controller entity

dev
    reset controller device pointer

sci
    TI SCI handle used for communication with system controller

idr
    idr structure for mapping ids to reset control structures

.. _`ti_sci_reset_set`:

ti_sci_reset_set
================

.. c:function:: int ti_sci_reset_set(struct reset_controller_dev *rcdev, unsigned long id, bool assert)

    program a device's reset

    :param rcdev:
        reset controller entity
    :type rcdev: struct reset_controller_dev \*

    :param id:
        ID of the reset to toggle
    :type id: unsigned long

    :param assert:
        boolean flag to indicate assert or deassert
    :type assert: bool

.. _`ti_sci_reset_set.description`:

Description
-----------

This is a common internal function used to assert or deassert a device's
reset using the TI SCI protocol. The device's reset is asserted if the
\ ``assert``\  argument is true, or deasserted if \ ``assert``\  argument is false.
The mechanism itself is a read-modify-write procedure, the current device
reset register is read using a TI SCI device operation, the new value is
set or un-set using the reset's mask, and the new reset value written by
using another TI SCI device operation.

.. _`ti_sci_reset_set.return`:

Return
------

0 for successful request, else a corresponding error value

.. _`ti_sci_reset_assert`:

ti_sci_reset_assert
===================

.. c:function:: int ti_sci_reset_assert(struct reset_controller_dev *rcdev, unsigned long id)

    assert device reset

    :param rcdev:
        reset controller entity
    :type rcdev: struct reset_controller_dev \*

    :param id:
        ID of the reset to be asserted
    :type id: unsigned long

.. _`ti_sci_reset_assert.description`:

Description
-----------

This function implements the reset driver op to assert a device's reset
using the TI SCI protocol. This invokes the function \ :c:func:`ti_sci_reset_set`\ 
with the corresponding parameters as passed in, but with the \ ``assert``\ 
argument set to true for asserting the reset.

.. _`ti_sci_reset_assert.return`:

Return
------

0 for successful request, else a corresponding error value

.. _`ti_sci_reset_deassert`:

ti_sci_reset_deassert
=====================

.. c:function:: int ti_sci_reset_deassert(struct reset_controller_dev *rcdev, unsigned long id)

    deassert device reset

    :param rcdev:
        reset controller entity
    :type rcdev: struct reset_controller_dev \*

    :param id:
        ID of the reset to be deasserted
    :type id: unsigned long

.. _`ti_sci_reset_deassert.description`:

Description
-----------

This function implements the reset driver op to deassert a device's reset
using the TI SCI protocol. This invokes the function \ :c:func:`ti_sci_reset_set`\ 
with the corresponding parameters as passed in, but with the \ ``assert``\ 
argument set to false for deasserting the reset.

.. _`ti_sci_reset_deassert.return`:

Return
------

0 for successful request, else a corresponding error value

.. _`ti_sci_reset_status`:

ti_sci_reset_status
===================

.. c:function:: int ti_sci_reset_status(struct reset_controller_dev *rcdev, unsigned long id)

    check device reset status

    :param rcdev:
        reset controller entity
    :type rcdev: struct reset_controller_dev \*

    :param id:
        ID of reset to be checked
    :type id: unsigned long

.. _`ti_sci_reset_status.description`:

Description
-----------

This function implements the reset driver op to return the status of a
device's reset using the TI SCI protocol. The reset register value is read
by invoking the TI SCI device operation .get_device_resets(), and the
status of the specific reset is extracted and returned using this reset's
reset mask.

.. _`ti_sci_reset_status.return`:

Return
------

0 if reset is deasserted, or a non-zero value if reset is asserted

.. _`ti_sci_reset_of_xlate`:

ti_sci_reset_of_xlate
=====================

.. c:function:: int ti_sci_reset_of_xlate(struct reset_controller_dev *rcdev, const struct of_phandle_args *reset_spec)

    translate a set of OF arguments to a reset ID

    :param rcdev:
        reset controller entity
    :type rcdev: struct reset_controller_dev \*

    :param reset_spec:
        OF reset argument specifier
    :type reset_spec: const struct of_phandle_args \*

.. _`ti_sci_reset_of_xlate.description`:

Description
-----------

This function performs the translation of the reset argument specifier
values defined in a reset consumer device node. The function allocates a
reset control structure for that device reset, and will be used by the
driver for performing any reset functions on that reset. An idr structure
is allocated and used to map to the reset control structure. This idr
is used by the driver to do reset lookups.

.. _`ti_sci_reset_of_xlate.return`:

Return
------

0 for successful request, else a corresponding error value

.. This file was automatic generated / don't edit.

