.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/wdrtas.c

.. _`wdrtas_set_interval`:

wdrtas_set_interval
===================

.. c:function:: int wdrtas_set_interval(int interval)

    sets the watchdog interval

    :param interval:
        new interval
    :type interval: int

.. _`wdrtas_set_interval.description`:

Description
-----------

returns 0 on success, <0 on failures

wdrtas_set_interval sets the watchdog keepalive interval by calling the
RTAS function set-indicator (surveillance). The unit of interval is
seconds.

.. _`wdrtas_get_interval`:

wdrtas_get_interval
===================

.. c:function:: int wdrtas_get_interval(int fallback_value)

    returns the current watchdog interval

    :param fallback_value:
        value (in seconds) to use, if the RTAS call fails
    :type fallback_value: int

.. _`wdrtas_get_interval.description`:

Description
-----------

returns the interval

wdrtas_get_interval returns the current watchdog keepalive interval
as reported by the RTAS function ibm,get-system-parameter. The unit
of the return value is seconds.

.. _`wdrtas_timer_start`:

wdrtas_timer_start
==================

.. c:function:: void wdrtas_timer_start( void)

    starts watchdog

    :param void:
        no arguments
    :type void: 

.. _`wdrtas_timer_start.description`:

Description
-----------

wdrtas_timer_start starts the watchdog by calling the RTAS function
set-interval (surveillance)

.. _`wdrtas_timer_stop`:

wdrtas_timer_stop
=================

.. c:function:: void wdrtas_timer_stop( void)

    stops watchdog

    :param void:
        no arguments
    :type void: 

.. _`wdrtas_timer_stop.description`:

Description
-----------

wdrtas_timer_stop stops the watchdog timer by calling the RTAS function
set-interval (surveillance)

.. _`wdrtas_timer_keepalive`:

wdrtas_timer_keepalive
======================

.. c:function:: void wdrtas_timer_keepalive( void)

    resets watchdog timer to keep system alive

    :param void:
        no arguments
    :type void: 

.. _`wdrtas_timer_keepalive.description`:

Description
-----------

wdrtas_timer_keepalive restarts the watchdog timer by calling the
RTAS function event-scan and repeats these calls as long as there are
events available. All events will be dumped.

.. _`wdrtas_get_temperature`:

wdrtas_get_temperature
======================

.. c:function:: int wdrtas_get_temperature( void)

    returns current temperature

    :param void:
        no arguments
    :type void: 

.. _`wdrtas_get_temperature.description`:

Description
-----------

returns temperature or <0 on failures

wdrtas_get_temperature returns the current temperature in Fahrenheit. It
uses the RTAS call get-sensor-state, token 3 to do so

.. _`wdrtas_get_status`:

wdrtas_get_status
=================

.. c:function:: int wdrtas_get_status( void)

    returns the status of the watchdog

    :param void:
        no arguments
    :type void: 

.. _`wdrtas_get_status.description`:

Description
-----------

returns a bitmask of defines WDIOF_... as defined in
include/linux/watchdog.h

.. _`wdrtas_get_boot_status`:

wdrtas_get_boot_status
======================

.. c:function:: int wdrtas_get_boot_status( void)

    returns the reason for the last boot

    :param void:
        no arguments
    :type void: 

.. _`wdrtas_get_boot_status.description`:

Description
-----------

returns a bitmask of defines WDIOF_... as defined in
include/linux/watchdog.h, indicating why the watchdog rebooted the system

.. _`wdrtas_ioctl`:

wdrtas_ioctl
============

.. c:function:: long wdrtas_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    ioctl function for the watchdog device

    :param file:
        file structure
    :type file: struct file \*

    :param cmd:
        command for ioctl
    :type cmd: unsigned int

    :param arg:
        argument pointer
    :type arg: unsigned long

.. _`wdrtas_ioctl.description`:

Description
-----------

returns 0 on success, <0 on failure

wdrtas_ioctl implements the watchdog API ioctls

.. _`wdrtas_open`:

wdrtas_open
===========

.. c:function:: int wdrtas_open(struct inode *inode, struct file *file)

    open function of watchdog device

    :param inode:
        inode structure
    :type inode: struct inode \*

    :param file:
        file structure
    :type file: struct file \*

.. _`wdrtas_open.description`:

Description
-----------

returns 0 on success, -EBUSY if the file has been opened already, <0 on
other failures

function called when watchdog device is opened

.. _`wdrtas_close`:

wdrtas_close
============

.. c:function:: int wdrtas_close(struct inode *inode, struct file *file)

    close function of watchdog device

    :param inode:
        inode structure
    :type inode: struct inode \*

    :param file:
        file structure
    :type file: struct file \*

.. _`wdrtas_close.description`:

Description
-----------

returns 0 on success

close function. Always succeeds

.. _`wdrtas_temp_read`:

wdrtas_temp_read
================

.. c:function:: ssize_t wdrtas_temp_read(struct file *file, char __user *buf, size_t count, loff_t *ppos)

    gives back the temperature in fahrenheit

    :param file:
        file structure
    :type file: struct file \*

    :param buf:
        user buffer
    :type buf: char __user \*

    :param count:
        number of bytes to be read
    :type count: size_t

    :param ppos:
        position in file
    :type ppos: loff_t \*

.. _`wdrtas_temp_read.description`:

Description
-----------

returns always 1 or -EFAULT in case of user space copy failures, <0 on
other failures

wdrtas_temp_read gives the temperature to the users by copying this
value as one byte into the user space buffer. The unit is Fahrenheit...

.. _`wdrtas_temp_open`:

wdrtas_temp_open
================

.. c:function:: int wdrtas_temp_open(struct inode *inode, struct file *file)

    open function of temperature device

    :param inode:
        inode structure
    :type inode: struct inode \*

    :param file:
        file structure
    :type file: struct file \*

.. _`wdrtas_temp_open.description`:

Description
-----------

returns 0 on success, <0 on failure

function called when temperature device is opened

.. _`wdrtas_temp_close`:

wdrtas_temp_close
=================

.. c:function:: int wdrtas_temp_close(struct inode *inode, struct file *file)

    close function of temperature device

    :param inode:
        inode structure
    :type inode: struct inode \*

    :param file:
        file structure
    :type file: struct file \*

.. _`wdrtas_temp_close.description`:

Description
-----------

returns 0 on success

close function. Always succeeds

.. _`wdrtas_reboot`:

wdrtas_reboot
=============

.. c:function:: int wdrtas_reboot(struct notifier_block *this, unsigned long code, void *ptr)

    reboot notifier function

    :param this:
        *undescribed*
    :type this: struct notifier_block \*

    :param code:
        reboot code
    :type code: unsigned long

    :param ptr:
        unused
    :type ptr: void \*

.. _`wdrtas_reboot.description`:

Description
-----------

returns NOTIFY_DONE

wdrtas_reboot stops the watchdog in case of a reboot

.. _`wdrtas_get_tokens`:

wdrtas_get_tokens
=================

.. c:function:: int wdrtas_get_tokens( void)

    reads in RTAS tokens

    :param void:
        no arguments
    :type void: 

.. _`wdrtas_get_tokens.description`:

Description
-----------

returns 0 on success, <0 on failure

wdrtas_get_tokens reads in the tokens for the RTAS calls used in
this watchdog driver. It tolerates, if "get-sensor-state" and
"ibm,get-system-parameter" are not available.

.. _`wdrtas_unregister_devs`:

wdrtas_unregister_devs
======================

.. c:function:: void wdrtas_unregister_devs( void)

    unregisters the misc dev handlers

    :param void:
        no arguments
    :type void: 

.. _`wdrtas_unregister_devs.description`:

Description
-----------

wdrtas_register_devs unregisters the watchdog and temperature watchdog
misc devs

.. _`wdrtas_register_devs`:

wdrtas_register_devs
====================

.. c:function:: int wdrtas_register_devs( void)

    registers the misc dev handlers

    :param void:
        no arguments
    :type void: 

.. _`wdrtas_register_devs.description`:

Description
-----------

returns 0 on success, <0 on failure

wdrtas_register_devs registers the watchdog and temperature watchdog
misc devs

.. _`wdrtas_init`:

wdrtas_init
===========

.. c:function:: int wdrtas_init( void)

    init function of the watchdog driver

    :param void:
        no arguments
    :type void: 

.. _`wdrtas_init.description`:

Description
-----------

returns 0 on success, <0 on failure

registers the file handlers and the reboot notifier

.. _`wdrtas_exit`:

wdrtas_exit
===========

.. c:function:: void __exit wdrtas_exit( void)

    exit function of the watchdog driver

    :param void:
        no arguments
    :type void: 

.. _`wdrtas_exit.description`:

Description
-----------

unregisters the file handlers and the reboot notifier

.. This file was automatic generated / don't edit.

