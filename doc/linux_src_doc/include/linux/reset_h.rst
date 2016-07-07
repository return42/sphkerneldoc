.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/reset.h

.. _`reset_control_get`:

reset_control_get
=================

.. c:function:: struct reset_control *reset_control_get(struct device *dev, const char *id)

    Lookup and obtain an exclusive reference to a reset controller.

    :param struct device \*dev:
        device to be reset by the controller

    :param const char \*id:
        reset line name

.. _`reset_control_get.description`:

Description
-----------

Returns a struct reset_control or \ :c:func:`IS_ERR`\  condition containing errno.
If this function is called more then once for the same reset_control it will
return -EBUSY.

See reset_control_get_shared for details on shared references to
reset-controls.

Use of id names is optional.

.. _`reset_control_get_shared`:

reset_control_get_shared
========================

.. c:function:: struct reset_control *reset_control_get_shared(struct device *dev, const char *id)

    Lookup and obtain a shared reference to a reset controller.

    :param struct device \*dev:
        device to be reset by the controller

    :param const char \*id:
        reset line name

.. _`reset_control_get_shared.description`:

Description
-----------

Returns a struct reset_control or \ :c:func:`IS_ERR`\  condition containing errno.
This function is intended for use with reset-controls which are shared
between hardware-blocks.

When a reset-control is shared, the behavior of reset_control_assert /
deassert is changed, the reset-core will keep track of a deassert_count
and only (re-)assert the reset after reset_control_assert has been called
as many times as reset_control_deassert was called. Also see the remark
about shared reset-controls in the reset_control_assert docs.

Calling reset_control_assert without first calling reset_control_deassert
is not allowed on a shared reset control. Calling reset_control_reset is
also not allowed on a shared reset control.

Use of id names is optional.

.. _`of_reset_control_get`:

of_reset_control_get
====================

.. c:function:: struct reset_control *of_reset_control_get(struct device_node *node, const char *id)

    Lookup and obtain an exclusive reference to a reset controller.

    :param struct device_node \*node:
        device to be reset by the controller

    :param const char \*id:
        reset line name

.. _`of_reset_control_get.description`:

Description
-----------

Returns a struct reset_control or \ :c:func:`IS_ERR`\  condition containing errno.

Use of id names is optional.

.. _`of_reset_control_get_by_index`:

of_reset_control_get_by_index
=============================

.. c:function:: struct reset_control *of_reset_control_get_by_index(struct device_node *node, int index)

    Lookup and obtain an exclusive reference to a reset controller by index.

    :param struct device_node \*node:
        device to be reset by the controller

    :param int index:
        index of the reset controller

.. _`of_reset_control_get_by_index.description`:

Description
-----------

This is to be used to perform a list of resets for a device or power domain
in whatever order. Returns a struct reset_control or \ :c:func:`IS_ERR`\  condition
containing errno.

.. _`devm_reset_control_get`:

devm_reset_control_get
======================

.. c:function:: struct reset_control *devm_reset_control_get(struct device *dev, const char *id)

    resource managed \ :c:func:`reset_control_get`\ 

    :param struct device \*dev:
        device to be reset by the controller

    :param const char \*id:
        reset line name

.. _`devm_reset_control_get.description`:

Description
-----------

Managed \ :c:func:`reset_control_get`\ . For reset controllers returned from this
function, \ :c:func:`reset_control_put`\  is called automatically on driver detach.
See \ :c:func:`reset_control_get`\  for more information.

.. _`devm_reset_control_get_by_index`:

devm_reset_control_get_by_index
===============================

.. c:function:: struct reset_control *devm_reset_control_get_by_index(struct device *dev, int index)

    resource managed reset_control_get

    :param struct device \*dev:
        device to be reset by the controller

    :param int index:
        index of the reset controller

.. _`devm_reset_control_get_by_index.description`:

Description
-----------

Managed \ :c:func:`reset_control_get`\ . For reset controllers returned from this
function, \ :c:func:`reset_control_put`\  is called automatically on driver detach.
See \ :c:func:`reset_control_get`\  for more information.

.. _`devm_reset_control_get_shared`:

devm_reset_control_get_shared
=============================

.. c:function:: struct reset_control *devm_reset_control_get_shared(struct device *dev, const char *id)

    resource managed \ :c:func:`reset_control_get_shared`\ 

    :param struct device \*dev:
        device to be reset by the controller

    :param const char \*id:
        reset line name

.. _`devm_reset_control_get_shared.description`:

Description
-----------

Managed \ :c:func:`reset_control_get_shared`\ . For reset controllers returned from
this function, \ :c:func:`reset_control_put`\  is called automatically on driver detach.
See \ :c:func:`reset_control_get_shared`\  for more information.

.. _`devm_reset_control_get_shared_by_index`:

devm_reset_control_get_shared_by_index
======================================

.. c:function:: struct reset_control *devm_reset_control_get_shared_by_index(struct device *dev, int index)

    resource managed reset_control_get_shared

    :param struct device \*dev:
        device to be reset by the controller

    :param int index:
        index of the reset controller

.. _`devm_reset_control_get_shared_by_index.description`:

Description
-----------

Managed \ :c:func:`reset_control_get_shared`\ . For reset controllers returned from
this function, \ :c:func:`reset_control_put`\  is called automatically on driver detach.
See \ :c:func:`reset_control_get_shared`\  for more information.

.. This file was automatic generated / don't edit.

