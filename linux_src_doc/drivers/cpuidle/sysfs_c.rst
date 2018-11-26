.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpuidle/sysfs.c

.. _`cpuidle_add_interface`:

cpuidle_add_interface
=====================

.. c:function:: int cpuidle_add_interface(struct device *dev)

    add CPU global sysfs attributes

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`cpuidle_remove_interface`:

cpuidle_remove_interface
========================

.. c:function:: void cpuidle_remove_interface(struct device *dev)

    remove CPU global sysfs attributes

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`cpuidle_add_state_sysfs`:

cpuidle_add_state_sysfs
=======================

.. c:function:: int cpuidle_add_state_sysfs(struct cpuidle_device *device)

    adds cpuidle states sysfs attributes

    :param device:
        the target device
    :type device: struct cpuidle_device \*

.. _`cpuidle_remove_state_sysfs`:

cpuidle_remove_state_sysfs
==========================

.. c:function:: void cpuidle_remove_state_sysfs(struct cpuidle_device *device)

    removes the cpuidle states sysfs attributes

    :param device:
        the target device
    :type device: struct cpuidle_device \*

.. _`cpuidle_add_driver_sysfs`:

cpuidle_add_driver_sysfs
========================

.. c:function:: int cpuidle_add_driver_sysfs(struct cpuidle_device *dev)

    adds the driver name sysfs attribute

    :param dev:
        *undescribed*
    :type dev: struct cpuidle_device \*

.. _`cpuidle_remove_driver_sysfs`:

cpuidle_remove_driver_sysfs
===========================

.. c:function:: void cpuidle_remove_driver_sysfs(struct cpuidle_device *dev)

    removes the driver name sysfs attribute

    :param dev:
        *undescribed*
    :type dev: struct cpuidle_device \*

.. _`cpuidle_add_device_sysfs`:

cpuidle_add_device_sysfs
========================

.. c:function:: int cpuidle_add_device_sysfs(struct cpuidle_device *device)

    adds device specific sysfs attributes

    :param device:
        the target device
    :type device: struct cpuidle_device \*

.. _`cpuidle_remove_device_sysfs`:

cpuidle_remove_device_sysfs
===========================

.. c:function:: void cpuidle_remove_device_sysfs(struct cpuidle_device *device)

    removes device specific sysfs attributes

    :param device:
        the target device
    :type device: struct cpuidle_device \*

.. _`cpuidle_add_sysfs`:

cpuidle_add_sysfs
=================

.. c:function:: int cpuidle_add_sysfs(struct cpuidle_device *dev)

    creates a sysfs instance for the target device

    :param dev:
        the target device
    :type dev: struct cpuidle_device \*

.. _`cpuidle_remove_sysfs`:

cpuidle_remove_sysfs
====================

.. c:function:: void cpuidle_remove_sysfs(struct cpuidle_device *dev)

    deletes a sysfs instance on the target device

    :param dev:
        the target device
    :type dev: struct cpuidle_device \*

.. This file was automatic generated / don't edit.

