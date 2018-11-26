.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/intel-ish-hid/ishtp/init.c

.. _`ishtp_dev_state_str`:

ishtp_dev_state_str
===================

.. c:function:: const char *ishtp_dev_state_str(int state)

    Convert to string format

    :param state:
        state to convert
    :type state: int

.. _`ishtp_dev_state_str.description`:

Description
-----------

Convert state to string for prints

.. _`ishtp_dev_state_str.return`:

Return
------

character pointer to converted string

.. _`ishtp_device_init`:

ishtp_device_init
=================

.. c:function:: void ishtp_device_init(struct ishtp_device *dev)

    ishtp device init

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

.. _`ishtp_device_init.description`:

Description
-----------

After ISHTP device is alloacted, this function is used to initialize
each field which includes spin lock, work struct and lists

.. _`ishtp_start`:

ishtp_start
===========

.. c:function:: int ishtp_start(struct ishtp_device *dev)

    Start ISH processing

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

.. _`ishtp_start.description`:

Description
-----------

Start ISHTP processing by sending query subscriber message

.. _`ishtp_start.return`:

Return
------

0 on success else -ENODEV

.. This file was automatic generated / don't edit.

