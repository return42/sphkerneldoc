.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/edac/edac_device.c

.. _`edac_device_add_device`:

edac_device_add_device
======================

.. c:function:: int edac_device_add_device(struct edac_device_ctl_info *edac_dev)

    Insert the 'edac_dev' structure into the edac_device global list and create sysfs entries associated with edac_device structure.

    :param struct edac_device_ctl_info \*edac_dev:
        *undescribed*

.. _`edac_device_add_device.return`:

Return
------

0       Success
!0      Failure

.. _`edac_device_del_device`:

edac_device_del_device
======================

.. c:function:: struct edac_device_ctl_info *edac_device_del_device(struct device *dev)

    Remove sysfs entries for specified edac_device structure and then remove edac_device structure from global list

    :param struct device \*dev:
        Pointer to 'struct device' representing edac_device
        structure to remove.

.. _`edac_device_del_device.return`:

Return
------

Pointer to removed edac_device structure,
OR NULL if device not found.

.. This file was automatic generated / don't edit.

