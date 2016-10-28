.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/power/opp/debugfs.c

.. _`opp_debug_register`:

opp_debug_register
==================

.. c:function:: int opp_debug_register(struct opp_device *opp_dev, struct opp_table *opp_table)

    add a device opp node to the debugfs 'opp' directory

    :param struct opp_device \*opp_dev:
        opp-dev pointer for device

    :param struct opp_table \*opp_table:
        the device-opp being added

.. _`opp_debug_register.description`:

Description
-----------

Dynamically adds device specific directory in debugfs 'opp' directory. If the
device-opp is shared with other devices, then links will be created for all
devices except the first.

.. _`opp_debug_register.return`:

Return
------

0 on success, otherwise negative error.

.. _`opp_debug_unregister`:

opp_debug_unregister
====================

.. c:function:: void opp_debug_unregister(struct opp_device *opp_dev, struct opp_table *opp_table)

    remove a device opp node from debugfs opp directory

    :param struct opp_device \*opp_dev:
        opp-dev pointer for device

    :param struct opp_table \*opp_table:
        the device-opp being removed

.. _`opp_debug_unregister.description`:

Description
-----------

Dynamically removes device specific directory from debugfs 'opp' directory.

.. This file was automatic generated / don't edit.

