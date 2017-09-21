.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/target/target_core_device.c

.. _`target_find_device`:

target_find_device
==================

.. c:function:: struct se_device *target_find_device(int id, bool do_depend)

    find a se_device by its dev_index

    :param int id:
        dev_index

    :param bool do_depend:
        true if caller needs target_depend_item to be done

.. _`target_find_device.description`:

Description
-----------

If do_depend is true, the caller must do a target_undepend_item
when finished using the device.

If do_depend is false, the caller must be called in a configfs
callback or during removal.

.. _`target_for_each_device`:

target_for_each_device
======================

.. c:function:: int target_for_each_device(int (*fn)(struct se_device *dev, void *data), void *data)

    iterate over configured devices

    :param int (\*fn)(struct se_device \*dev, void \*data):
        iterator function

    :param void \*data:
        pointer to data that will be passed to fn

.. _`target_for_each_device.description`:

Description
-----------

fn must return 0 to continue looping over devices. non-zero will break
from the loop and return that value to the caller.

.. This file was automatic generated / don't edit.

