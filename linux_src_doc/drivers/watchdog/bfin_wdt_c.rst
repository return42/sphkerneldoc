.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/bfin_wdt.c

.. _`bfin_wdt_keepalive`:

bfin_wdt_keepalive
==================

.. c:function:: int bfin_wdt_keepalive( void)

    Keep the Userspace Watchdog Alive

    :param  void:
        no arguments

.. _`bfin_wdt_keepalive.the-userspace-watchdog-got-a-keepalive`:

The Userspace watchdog got a KeepAlive
--------------------------------------

schedule the next timeout.

.. _`bfin_wdt_stop`:

bfin_wdt_stop
=============

.. c:function:: int bfin_wdt_stop( void)

    Stop the Watchdog

    :param  void:
        no arguments

.. _`bfin_wdt_stop.description`:

Description
-----------

Stops the on-chip watchdog.

.. _`bfin_wdt_start`:

bfin_wdt_start
==============

.. c:function:: int bfin_wdt_start( void)

    Start the Watchdog

    :param  void:
        no arguments

.. _`bfin_wdt_start.description`:

Description
-----------

Starts the on-chip watchdog.  Automatically loads WDOG_CNT
into WDOG_STAT for us.

.. _`bfin_wdt_running`:

bfin_wdt_running
================

.. c:function:: int bfin_wdt_running( void)

    Check Watchdog status

    :param  void:
        no arguments

.. _`bfin_wdt_running.description`:

Description
-----------

See if the watchdog is running.

.. _`bfin_wdt_set_timeout`:

bfin_wdt_set_timeout
====================

.. c:function:: int bfin_wdt_set_timeout(unsigned long t)

    Set the Userspace Watchdog timeout

    :param unsigned long t:
        new timeout value (in seconds)

.. _`bfin_wdt_set_timeout.description`:

Description
-----------

Translate the specified timeout in seconds into System Clock
terms which is what the on-chip Watchdog requires.

.. _`bfin_wdt_open`:

bfin_wdt_open
=============

.. c:function:: int bfin_wdt_open(struct inode *inode, struct file *file)

    Open the Device

    :param struct inode \*inode:
        inode of device

    :param struct file \*file:
        file handle of device

.. _`bfin_wdt_open.description`:

Description
-----------

Watchdog device is opened and started.

.. _`bfin_wdt_release`:

bfin_wdt_release
================

.. c:function:: int bfin_wdt_release(struct inode *inode, struct file *file)

    Close the Device

    :param struct inode \*inode:
        inode of device

    :param struct file \*file:
        file handle of device

.. _`bfin_wdt_release.description`:

Description
-----------

Watchdog device is closed and stopped.

.. _`bfin_wdt_write`:

bfin_wdt_write
==============

.. c:function:: ssize_t bfin_wdt_write(struct file *file, const char __user *data, size_t len, loff_t *ppos)

    Write to Device

    :param struct file \*file:
        file handle of device

    :param const char __user \*data:
        *undescribed*

    :param size_t len:
        *undescribed*

    :param loff_t \*ppos:
        offset

.. _`bfin_wdt_write.description`:

Description
-----------

Pings the watchdog on write.

.. _`bfin_wdt_ioctl`:

bfin_wdt_ioctl
==============

.. c:function:: long bfin_wdt_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    Query Device

    :param struct file \*file:
        file handle of device

    :param unsigned int cmd:
        watchdog command

    :param unsigned long arg:
        argument

.. _`bfin_wdt_ioctl.description`:

Description
-----------

Query basic information from the device or ping it, as outlined by the
watchdog API.

.. _`bfin_wdt_suspend`:

bfin_wdt_suspend
================

.. c:function:: int bfin_wdt_suspend(struct platform_device *pdev, pm_message_t state)

    suspend the watchdog

    :param struct platform_device \*pdev:
        device being suspended

    :param pm_message_t state:
        requested suspend state

.. _`bfin_wdt_suspend.description`:

Description
-----------

Remember if the watchdog was running and stop it.

.. _`bfin_wdt_suspend.todo`:

TODO
----

is this even right?  Doesn't seem to be any
standard in the watchdog world ...

.. _`bfin_wdt_resume`:

bfin_wdt_resume
===============

.. c:function:: int bfin_wdt_resume(struct platform_device *pdev)

    resume the watchdog

    :param struct platform_device \*pdev:
        device being resumed

.. _`bfin_wdt_resume.description`:

Description
-----------

If the watchdog was running, turn it back on.

.. _`bfin_wdt_probe`:

bfin_wdt_probe
==============

.. c:function:: int bfin_wdt_probe(struct platform_device *pdev)

    Initialize module

    :param struct platform_device \*pdev:
        *undescribed*

.. _`bfin_wdt_probe.description`:

Description
-----------

Registers the misc device.  Actual device
initialization is handled by \ :c:func:`bfin_wdt_open`\ .

.. _`bfin_wdt_remove`:

bfin_wdt_remove
===============

.. c:function:: int bfin_wdt_remove(struct platform_device *pdev)

    Initialize module

    :param struct platform_device \*pdev:
        *undescribed*

.. _`bfin_wdt_remove.description`:

Description
-----------

Unregisters the misc device.  Actual device
deinitialization is handled by \ :c:func:`bfin_wdt_close`\ .

.. _`bfin_wdt_shutdown`:

bfin_wdt_shutdown
=================

.. c:function:: void bfin_wdt_shutdown(struct platform_device *pdev)

    Soft Shutdown Handler

    :param struct platform_device \*pdev:
        *undescribed*

.. _`bfin_wdt_shutdown.description`:

Description
-----------

Handles the soft shutdown event.

.. _`bfin_wdt_init`:

bfin_wdt_init
=============

.. c:function:: int bfin_wdt_init( void)

    Initialize module

    :param  void:
        no arguments

.. _`bfin_wdt_init.description`:

Description
-----------

Checks the module params and registers the platform device & driver.
Real work is in the platform probe function.

.. _`bfin_wdt_exit`:

bfin_wdt_exit
=============

.. c:function:: void __exit bfin_wdt_exit( void)

    Deinitialize module

    :param  void:
        no arguments

.. _`bfin_wdt_exit.description`:

Description
-----------

Back out the platform device & driver steps.  Real work is in the
platform remove function.

.. This file was automatic generated / don't edit.

