.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/xen-netback/xenbus.c

.. _`netback_probe`:

netback_probe
=============

.. c:function:: int netback_probe(struct xenbus_device *dev, const struct xenbus_device_id *id)

    structures and switch to InitWait.

    :param dev:
        *undescribed*
    :type dev: struct xenbus_device \*

    :param id:
        *undescribed*
    :type id: const struct xenbus_device_id \*

.. _`frontend_changed`:

frontend_changed
================

.. c:function:: void frontend_changed(struct xenbus_device *dev, enum xenbus_state frontend_state)

    :param dev:
        *undescribed*
    :type dev: struct xenbus_device \*

    :param frontend_state:
        *undescribed*
    :type frontend_state: enum xenbus_state

.. This file was automatic generated / don't edit.

