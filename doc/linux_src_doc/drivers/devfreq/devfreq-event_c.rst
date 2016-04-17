.. -*- coding: utf-8; mode: rst -*-

===============
devfreq-event.c
===============


.. _`devfreq_event_enable_edev`:

devfreq_event_enable_edev
=========================

.. c:function:: int devfreq_event_enable_edev (struct devfreq_event_dev *edev)

    Enable the devfreq-event dev and increase the enable_count of devfreq-event dev.

    :param struct devfreq_event_dev \*edev:
        the devfreq-event device



.. _`devfreq_event_enable_edev.description`:

Description
-----------

Note that this function increase the enable_count and enable the
devfreq-event device. The devfreq-event device should be enabled before
using it by devfreq device.



.. _`devfreq_event_disable_edev`:

devfreq_event_disable_edev
==========================

.. c:function:: int devfreq_event_disable_edev (struct devfreq_event_dev *edev)

    Disable the devfreq-event dev and decrease the enable_count of the devfreq-event dev.

    :param struct devfreq_event_dev \*edev:
        the devfreq-event device



.. _`devfreq_event_disable_edev.description`:

Description
-----------

Note that this function decrease the enable_count and disable the
devfreq-event device. After the devfreq-event device is disabled,
devfreq device can't use the devfreq-event device for get/set/reset
operations.



.. _`devfreq_event_is_enabled`:

devfreq_event_is_enabled
========================

.. c:function:: bool devfreq_event_is_enabled (struct devfreq_event_dev *edev)

    Check whether devfreq-event dev is enabled or not.

    :param struct devfreq_event_dev \*edev:
        the devfreq-event device



.. _`devfreq_event_is_enabled.description`:

Description
-----------

Note that this function check whether devfreq-event dev is enabled or not.
If return true, the devfreq-event dev is enabeld. If return false, the
devfreq-event dev is disabled.



.. _`devfreq_event_set_event`:

devfreq_event_set_event
=======================

.. c:function:: int devfreq_event_set_event (struct devfreq_event_dev *edev)

    Set event to devfreq-event dev to start.

    :param struct devfreq_event_dev \*edev:
        the devfreq-event device



.. _`devfreq_event_set_event.description`:

Description
-----------

Note that this function set the event to the devfreq-event device to start
for getting the event data which could be various event type.



.. _`devfreq_event_get_event`:

devfreq_event_get_event
=======================

.. c:function:: int devfreq_event_get_event (struct devfreq_event_dev *edev, struct devfreq_event_data *edata)

    Get {load|total}_count from devfreq-event dev.

    :param struct devfreq_event_dev \*edev:
        the devfreq-event device

    :param struct devfreq_event_data \*edata:
        the calculated data of devfreq-event device



.. _`devfreq_event_get_event.description`:

Description
-----------

Note that this function get the calculated event data from devfreq-event dev
after stoping the progress of whole sequence of devfreq-event dev.



.. _`devfreq_event_reset_event`:

devfreq_event_reset_event
=========================

.. c:function:: int devfreq_event_reset_event (struct devfreq_event_dev *edev)

    Reset all opeations of devfreq-event dev.

    :param struct devfreq_event_dev \*edev:
        the devfreq-event device



.. _`devfreq_event_reset_event.description`:

Description
-----------

Note that this function stop all operations of devfreq-event dev and reset
the current event data to make the devfreq-event device into initial state.



.. _`devfreq_event_get_edev_by_phandle`:

devfreq_event_get_edev_by_phandle
=================================

.. c:function:: struct devfreq_event_dev *devfreq_event_get_edev_by_phandle (struct device *dev, int index)

    Get the devfreq-event dev from devicetree.

    :param struct device \*dev:
        the pointer to the given device

    :param int index:
        the index into list of devfreq-event device



.. _`devfreq_event_get_edev_by_phandle.description`:

Description
-----------

Note that this function return the pointer of devfreq-event device.



.. _`devfreq_event_get_edev_count`:

devfreq_event_get_edev_count
============================

.. c:function:: int devfreq_event_get_edev_count (struct device *dev)

    Get the count of devfreq-event dev

    :param struct device \*dev:
        the pointer to the given device



.. _`devfreq_event_get_edev_count.description`:

Description
-----------

Note that this function return the count of devfreq-event devices.



.. _`devfreq_event_add_edev`:

devfreq_event_add_edev
======================

.. c:function:: struct devfreq_event_dev *devfreq_event_add_edev (struct device *dev, struct devfreq_event_desc *desc)

    Add new devfreq-event device.

    :param struct device \*dev:
        the device owning the devfreq-event device being created

    :param struct devfreq_event_desc \*desc:
        the devfreq-event device's decriptor which include essential
        data for devfreq-event device.



.. _`devfreq_event_add_edev.description`:

Description
-----------

Note that this function add new devfreq-event device to devfreq-event class
list and register the device of the devfreq-event device.



.. _`devfreq_event_remove_edev`:

devfreq_event_remove_edev
=========================

.. c:function:: int devfreq_event_remove_edev (struct devfreq_event_dev *edev)

    Remove the devfreq-event device registered.

    :param struct devfreq_event_dev \*edev:

        *undescribed*



.. _`devfreq_event_remove_edev.description`:

Description
-----------

Note that this function remove the registered devfreq-event device.



.. _`devm_devfreq_event_add_edev`:

devm_devfreq_event_add_edev
===========================

.. c:function:: struct devfreq_event_dev *devm_devfreq_event_add_edev (struct device *dev, struct devfreq_event_desc *desc)

    Resource-managed devfreq_event_add_edev()

    :param struct device \*dev:
        the device owning the devfreq-event device being created

    :param struct devfreq_event_desc \*desc:
        the devfreq-event device's decriptor which include essential
        data for devfreq-event device.



.. _`devm_devfreq_event_add_edev.description`:

Description
-----------

Note that this function manages automatically the memory of devfreq-event
device using device resource management and simplify the free operation
for memory of devfreq-event device.



.. _`devm_devfreq_event_remove_edev`:

devm_devfreq_event_remove_edev
==============================

.. c:function:: void devm_devfreq_event_remove_edev (struct device *dev, struct devfreq_event_dev *edev)

    Resource-managed devfreq_event_remove_edev()

    :param struct device \*dev:
        the device owning the devfreq-event device being created

    :param struct devfreq_event_dev \*edev:
        the devfreq-event device



.. _`devm_devfreq_event_remove_edev.description`:

Description
-----------

Note that this function manages automatically the memory of devfreq-event
device using device resource management.

