.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/sgi-ip22/ip22-gio.c

.. _`gio_match_device`:

gio_match_device
================

.. c:function:: const struct gio_device_id *gio_match_device(const struct gio_device_id *match, const struct gio_device *dev)

    Tell if an of_device structure has a matching gio_match structure

    :param const struct gio_device_id \*match:
        *undescribed*

    :param const struct gio_device \*dev:
        the of device structure to match against

.. _`gio_match_device.description`:

Description
-----------

Used by a driver to check whether an of_device present in the
system is in its list of supported devices.

.. _`gio_release_dev`:

gio_release_dev
===============

.. c:function:: void gio_release_dev(struct device *dev)

    free an gio device structure when all users of it are finished.

    :param struct device \*dev:
        device that's been disconnected

.. _`gio_release_dev.description`:

Description
-----------

Will be called only by the device core when all users of this gio device are
done.

.. This file was automatic generated / don't edit.

