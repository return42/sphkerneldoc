.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/target/target_core_device.c

.. _`target_for_each_device`:

target_for_each_device
======================

.. c:function:: int target_for_each_device(int (*fn)(struct se_device *dev, void *data), void *data)

    iterate over configured devices

    :param int (\*fn)(struct se_device \*dev, void \*data):
        iterator function

    :param data:
        pointer to data that will be passed to fn
    :type data: void \*

.. _`target_for_each_device.description`:

Description
-----------

fn must return 0 to continue looping over devices. non-zero will break
from the loop and return that value to the caller.

.. This file was automatic generated / don't edit.

