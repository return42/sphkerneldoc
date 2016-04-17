.. -*- coding: utf-8; mode: rst -*-

======
core.c
======


.. _`reset_control`:

struct reset_control
====================

.. c:type:: reset_control

    a reset control


.. _`reset_control.definition`:

Definition
----------

.. code-block:: c

  struct reset_control {
    struct reset_controller_dev * rcdev;
    unsigned int id;
  };


.. _`reset_control.members`:

Members
-------

:``rcdev``:
    a pointer to the reset controller device
    this reset control belongs to

:``id``:
    ID of the reset controller in the reset
    controller device




.. _`of_reset_simple_xlate`:

of_reset_simple_xlate
=====================

.. c:function:: int of_reset_simple_xlate (struct reset_controller_dev *rcdev, const struct of_phandle_args *reset_spec)

    translate reset_spec to the reset line number

    :param struct reset_controller_dev \*rcdev:
        a pointer to the reset controller device

    :param const struct of_phandle_args \*reset_spec:
        reset line specifier as found in the device tree



.. _`of_reset_simple_xlate.description`:

Description
-----------

This simple translation function should be used for reset controllers



.. _`of_reset_simple_xlate.with-1`:

with 1
------

1 mapping, where reset lines can be indexed by number without gaps.



.. _`reset_controller_register`:

reset_controller_register
=========================

.. c:function:: int reset_controller_register (struct reset_controller_dev *rcdev)

    register a reset controller device

    :param struct reset_controller_dev \*rcdev:
        a pointer to the initialized reset controller device



.. _`reset_controller_unregister`:

reset_controller_unregister
===========================

.. c:function:: void reset_controller_unregister (struct reset_controller_dev *rcdev)

    unregister a reset controller device

    :param struct reset_controller_dev \*rcdev:
        a pointer to the reset controller device



.. _`reset_control_reset`:

reset_control_reset
===================

.. c:function:: int reset_control_reset (struct reset_control *rstc)

    reset the controlled device

    :param struct reset_control \*rstc:
        reset controller



.. _`reset_control_assert`:

reset_control_assert
====================

.. c:function:: int reset_control_assert (struct reset_control *rstc)

    asserts the reset line

    :param struct reset_control \*rstc:
        reset controller



.. _`reset_control_deassert`:

reset_control_deassert
======================

.. c:function:: int reset_control_deassert (struct reset_control *rstc)

    deasserts the reset line

    :param struct reset_control \*rstc:
        reset controller



.. _`reset_control_status`:

reset_control_status
====================

.. c:function:: int reset_control_status (struct reset_control *rstc)

    returns a negative errno if not supported, a positive value if the reset line is asserted, or zero if the reset line is not asserted.

    :param struct reset_control \*rstc:
        reset controller



.. _`of_reset_control_get_by_index`:

of_reset_control_get_by_index
=============================

.. c:function:: struct reset_control *of_reset_control_get_by_index (struct device_node *node, int index)

    Lookup and obtain a reference to a reset controller by index.

    :param struct device_node \*node:
        device to be reset by the controller

    :param int index:
        index of the reset controller



.. _`of_reset_control_get_by_index.description`:

Description
-----------

This is to be used to perform a list of resets for a device or power domain
in whatever order. Returns a struct reset_control or :c:func:`IS_ERR` condition
containing errno.



.. _`of_reset_control_get`:

of_reset_control_get
====================

.. c:function:: struct reset_control *of_reset_control_get (struct device_node *node, const char *id)

    Lookup and obtain a reference to a reset controller.

    :param struct device_node \*node:
        device to be reset by the controller

    :param const char \*id:
        reset line name



.. _`of_reset_control_get.description`:

Description
-----------

Returns a struct reset_control or :c:func:`IS_ERR` condition containing errno.

Use of id names is optional.



.. _`reset_control_get`:

reset_control_get
=================

.. c:function:: struct reset_control *reset_control_get (struct device *dev, const char *id)

    Lookup and obtain a reference to a reset controller.

    :param struct device \*dev:
        device to be reset by the controller

    :param const char \*id:
        reset line name



.. _`reset_control_get.description`:

Description
-----------

Returns a struct reset_control or :c:func:`IS_ERR` condition containing errno.

Use of id names is optional.



.. _`reset_control_put`:

reset_control_put
=================

.. c:function:: void reset_control_put (struct reset_control *rstc)

    free the reset controller

    :param struct reset_control \*rstc:
        reset controller



.. _`devm_reset_control_get`:

devm_reset_control_get
======================

.. c:function:: struct reset_control *devm_reset_control_get (struct device *dev, const char *id)

    resource managed reset_control_get()

    :param struct device \*dev:
        device to be reset by the controller

    :param const char \*id:
        reset line name



.. _`devm_reset_control_get.description`:

Description
-----------

Managed :c:func:`reset_control_get`. For reset controllers returned from this
function, :c:func:`reset_control_put` is called automatically on driver detach.
See :c:func:`reset_control_get` for more information.



.. _`device_reset`:

device_reset
============

.. c:function:: int device_reset (struct device *dev)

    find reset controller associated with the device and perform reset

    :param struct device \*dev:
        device to be reset by the controller



.. _`device_reset.description`:

Description
-----------

Convenience wrapper for :c:func:`reset_control_get` and :c:func:`reset_control_reset`.
This is useful for the common case of devices with single, dedicated reset
lines.

