.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/lc-rc.c

.. _`uwb_rc_sys_release`:

uwb_rc_sys_release
==================

.. c:function:: void uwb_rc_sys_release(struct device *dev)

    :param struct device \*dev:
        *undescribed*

.. _`uwb_rc_mac_addr_setup`:

uwb_rc_mac_addr_setup
=====================

.. c:function:: int uwb_rc_mac_addr_setup(struct uwb_rc *rc)

    get an RC's EUI-48 address or set it

    :param struct uwb_rc \*rc:
        the radio controller.

.. _`uwb_rc_mac_addr_setup.description`:

Description
-----------

If the EUI-48 address is 00:00:00:00:00:00 or FF:FF:FF:FF:FF:FF
then a random locally administered EUI-48 is generated and set on
the device.  The probability of address collisions is sufficiently
unlikely (1/2^40 = 9.1e-13) that they're not checked for.

.. _`uwb_rc_add`:

uwb_rc_add
==========

.. c:function:: int uwb_rc_add(struct uwb_rc *rc, struct device *parent_dev, void *priv)

    :param struct uwb_rc \*rc:
        *undescribed*

    :param struct device \*parent_dev:
        *undescribed*

    :param void \*priv:
        *undescribed*

.. _`uwb_rc_add.description`:

Description
-----------

Did you call \ :c:func:`uwb_rc_init`\  on your rc?

We assume that this is being called with a > 0 refcount on
it [through ops->{get\|put}\ :c:func:`_device`\ . We'll take our own, though.

\ ``parent_dev``\  is our real device, the one that provides the actual UWB device

.. _`__uwb_rc_try_get`:

__uwb_rc_try_get
================

.. c:function:: struct uwb_rc *__uwb_rc_try_get(struct uwb_rc *target_rc)

    :param struct uwb_rc \*target_rc:
        *undescribed*

.. _`__uwb_rc_try_get.description`:

Description
-----------

\ ``returns``\  NULL if the rc does not exist or is quiescing; the ptr to
it otherwise.

.. _`uwb_rc_get_by_grandpa`:

uwb_rc_get_by_grandpa
=====================

.. c:function:: struct uwb_rc *uwb_rc_get_by_grandpa(const struct device *grandpa_dev)

    parent

    :param const struct device \*grandpa_dev:
        *undescribed*

.. _`uwb_rc_get_by_grandpa.description`:

Description
-----------

\ ``grandpa_dev``\   Pointer to the 'grandparent' device structure.
\ ``returns``\  NULL If the rc does not exist or is quiescing; the ptr to
it otherwise, properly referenced.

The Radio Control interface (or the UWB Radio Controller) is always
an interface of a device. The parent is the interface, the
grandparent is the device that encapsulates the interface.

There is no need to lock around as the "grandpa" would be
refcounted by the target, and to remove the referemes, the
uwb_rc_class->sem would have to be taken--we hold it, ergo we
should be safe.

.. _`find_rc_dev`:

find_rc_dev
===========

.. c:function:: int find_rc_dev(struct device *dev, const void *data)

    :param struct device \*dev:
        *undescribed*

    :param const void \*data:
        *undescribed*

.. _`find_rc_dev.description`:

Description
-----------

\ ``returns``\  the pointer to the radio controller, properly referenced

.. _`uwb_rc_put`:

uwb_rc_put
==========

.. c:function:: void uwb_rc_put(struct uwb_rc *rc)

    :param struct uwb_rc \*rc:
        *undescribed*

.. _`uwb_rc_put.description`:

Description
-----------

This is the version that should be done by entities external to the
UWB Radio Control stack (ie: clients of the API).

.. This file was automatic generated / don't edit.

