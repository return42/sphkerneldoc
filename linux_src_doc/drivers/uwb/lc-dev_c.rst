.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/lc-dev.c

.. _`__uwb_dev_sys_add`:

\__uwb_dev_sys_add
==================

.. c:function:: int __uwb_dev_sys_add(struct uwb_dev *uwb_dev, struct device *parent_dev)

    :param uwb_dev:
        *undescribed*
    :type uwb_dev: struct uwb_dev \*

    :param parent_dev:
        *undescribed*
    :type parent_dev: struct device \*

.. _`uwb_dev_add`:

uwb_dev_add
===========

.. c:function:: int uwb_dev_add(struct uwb_dev *uwb_dev, struct device *parent_dev, struct uwb_rc *parent_rc)

    :param uwb_dev:
        *undescribed*
    :type uwb_dev: struct uwb_dev \*

    :param parent_dev:
        *undescribed*
    :type parent_dev: struct device \*

    :param parent_rc:
        is the parent radio controller who has the link to the
        device. When registering the UWB device that is a UWB
        Radio Controller, we point back to it.
    :type parent_rc: struct uwb_rc \*

.. _`uwb_dev_add.description`:

Description
-----------

Did you call \ :c:func:`uwb_dev_init`\  on it?

If registering the device that is part of a radio, caller has set
rc->uwb_dev->dev. Otherwise it is to be left NULL--a new one will
be allocated.

.. _`uwb_dev_try_get`:

uwb_dev_try_get
===============

.. c:function:: struct uwb_dev *uwb_dev_try_get(struct uwb_rc *rc, struct uwb_dev *uwb_dev)

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

    :param uwb_dev:
        *undescribed*
    :type uwb_dev: struct uwb_dev \*

.. _`uwb_dev_try_get.description`:

Description
-----------

\ ``returns``\  NULL if the device does not exist or is quiescing; the ptr to
it otherwise.

.. _`__uwb_dev_offair`:

\__uwb_dev_offair
=================

.. c:function:: int __uwb_dev_offair(struct uwb_dev *uwb_dev, struct uwb_rc *rc)

    :param uwb_dev:
        *undescribed*
    :type uwb_dev: struct uwb_dev \*

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

.. _`uwbd_dev_offair`:

uwbd_dev_offair
===============

.. c:function:: void uwbd_dev_offair(struct uwb_beca_e *bce)

    :param bce:
        *undescribed*
    :type bce: struct uwb_beca_e \*

.. _`uwbd_dev_offair.description`:

Description
-----------

This is called by the UWB Daemon (through the beacon purge function
uwb_bcn_cache_purge) when it is detected that a device has been in
radio silence for a while.

If this device is actually a local radio controller we don't need
to go through the offair process, as it is not registered as that.

.. _`uwbd_dev_offair.note`:

NOTE
----

uwb_bcn_cache.mutex is held!

.. _`uwbd_dev_onair`:

uwbd_dev_onair
==============

.. c:function:: void uwbd_dev_onair(struct uwb_rc *rc, struct uwb_beca_e *bce)

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

    :param bce:
        *undescribed*
    :type bce: struct uwb_beca_e \*

.. _`uwbd_dev_onair.description`:

Description
-----------

This is called by the UWB Daemon when it is detected that a device
has popped up in the radio range of the radio controller.

It will just create the freaking device, register the beacon and
stuff and yatla, done.

.. _`uwbd_dev_onair.note`:

NOTE
----

uwb_beca.mutex is held, bce->mutex is held

.. _`uwb_dev_for_each`:

uwb_dev_for_each
================

.. c:function:: int uwb_dev_for_each(struct uwb_rc *rc, uwb_dev_for_each_f function, void *priv)

    :param rc:
        radio controller for the devices.
    :type rc: struct uwb_rc \*

    :param function:
        function to call.
    :type function: uwb_dev_for_each_f

    :param priv:
        data to pass to \ ``function``\ .
    :type priv: void \*

.. _`uwb_dev_for_each.description`:

Description
-----------

See docs for \ :c:func:`bus_for_each`\ ....

.. This file was automatic generated / don't edit.

