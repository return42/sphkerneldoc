.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/host1x/bus.c

.. _`host1x_subdev_add`:

host1x_subdev_add
=================

.. c:function:: int host1x_subdev_add(struct host1x_device *device, struct device_node *np)

    add a new subdevice with an associated device node

    :param struct host1x_device \*device:
        *undescribed*

    :param struct device_node \*np:
        *undescribed*

.. _`host1x_subdev_del`:

host1x_subdev_del
=================

.. c:function:: void host1x_subdev_del(struct host1x_subdev *subdev)

    remove subdevice

    :param struct host1x_subdev \*subdev:
        *undescribed*

.. _`host1x_device_parse_dt`:

host1x_device_parse_dt
======================

.. c:function:: int host1x_device_parse_dt(struct host1x_device *device, struct host1x_driver *driver)

    scan device tree and add matching subdevices

    :param struct host1x_device \*device:
        *undescribed*

    :param struct host1x_driver \*driver:
        *undescribed*

.. This file was automatic generated / don't edit.

