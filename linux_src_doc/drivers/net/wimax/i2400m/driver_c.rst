.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wimax/i2400m/driver.c

.. _`__i2400m_dev_start`:

__i2400m_dev_start
==================

.. c:function:: int __i2400m_dev_start(struct i2400m *i2400m, enum i2400m_bri flags)

    Bring up driver communication with the device

    :param struct i2400m \*i2400m:
        device descriptor

    :param enum i2400m_bri flags:
        boot mode flags

.. _`__i2400m_dev_start.return`:

Return
------

0 if ok, < 0 errno code on error.

Uploads firmware and brings up all the resources needed to be able
to communicate with the device.

The workqueue has to be setup early, at least before RX handling
(it's only real user for now) so it can process reports as they
arrive. We also want to destroy it if we retry, to make sure it is
flushed...easier like this.

TX needs to be setup before the bus-specific code (otherwise on
shutdown, the bus-tx code could try to access it).

.. _`__i2400m_dev_stop`:

__i2400m_dev_stop
=================

.. c:function:: void __i2400m_dev_stop(struct i2400m *i2400m)

    Tear down driver communication with the device

    :param struct i2400m \*i2400m:
        device descriptor

.. _`__i2400m_dev_stop.return`:

Return
------

0 if ok, < 0 errno code on error.

Releases all the resources allocated to communicate with the
device. Note we cannot destroy the workqueue earlier as until RX is
fully destroyed, it could still try to schedule jobs.

.. _`i2400m_dev_reset_handle`:

i2400m_dev_reset_handle
=======================

.. c:function:: int i2400m_dev_reset_handle(struct i2400m *i2400m, const char *reason)

    Handle a device's reset in a thread context

    :param struct i2400m \*i2400m:
        *undescribed*

    :param const char \*reason:
        *undescribed*

.. _`i2400m_dev_reset_handle.description`:

Description
-----------

Schedule a device reset handling out on a thread context, so it
is safe to call from atomic context. We can't use the i2400m's
queue as we are going to destroy it and reinitialize it as part of
the driver bringup/bringup process.

See \\ :c:func:`__i2400m_dev_reset_handle`\  for details; that takes care of
reinitializing the driver to handle the reset, calling into the
bus-specific functions ops as needed.

.. _`i2400m_init`:

i2400m_init
===========

.. c:function:: void i2400m_init(struct i2400m *i2400m)

    Initialize a 'struct i2400m' from all zeroes

    :param struct i2400m \*i2400m:
        *undescribed*

.. _`i2400m_init.description`:

Description
-----------

This is a bus-generic API call.

.. _`i2400m_setup`:

i2400m_setup
============

.. c:function:: int i2400m_setup(struct i2400m *i2400m, enum i2400m_bri bm_flags)

    bus-generic setup function for the i2400m device

    :param struct i2400m \*i2400m:
        device descriptor (bus-specific parts have been initialized)

    :param enum i2400m_bri bm_flags:
        *undescribed*

.. _`i2400m_setup.return`:

Return
------

0 if ok, < 0 errno code on error.

Sets up basic device comunication infrastructure, boots the ROM to
read the MAC address, registers with the WiMAX and network stacks
and then brings up the device.

.. _`i2400m_release`:

i2400m_release
==============

.. c:function:: void i2400m_release(struct i2400m *i2400m)

    release the bus-generic driver resources

    :param struct i2400m \*i2400m:
        *undescribed*

.. _`i2400m_release.description`:

Description
-----------

Sends a disconnect message and undoes any setup done by \ :c:func:`i2400m_setup`\ 

.. This file was automatic generated / don't edit.

