.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/xilinx/zynqmp-debug.c

.. _`zynqmp_pm_argument_value`:

zynqmp_pm_argument_value
========================

.. c:function:: u64 zynqmp_pm_argument_value(char *arg)

    Extract argument value from a PM-API request

    :param arg:
        Entered PM-API argument in string format
    :type arg: char \*

.. _`zynqmp_pm_argument_value.return`:

Return
------

Argument value in unsigned integer format on success
0 otherwise

.. _`get_pm_api_id`:

get_pm_api_id
=============

.. c:function:: int get_pm_api_id(char *pm_api_req, u32 *pm_id)

    Extract API-ID from a PM-API request

    :param pm_api_req:
        Entered PM-API argument in string format
    :type pm_api_req: char \*

    :param pm_id:
        API-ID
    :type pm_id: u32 \*

.. _`get_pm_api_id.return`:

Return
------

0 on success else error code

.. _`zynqmp_pm_debugfs_api_write`:

zynqmp_pm_debugfs_api_write
===========================

.. c:function:: ssize_t zynqmp_pm_debugfs_api_write(struct file *file, const char __user *ptr, size_t len, loff_t *off)

    debugfs write function

    :param file:
        User file
    :type file: struct file \*

    :param ptr:
        User entered PM-API string
    :type ptr: const char __user \*

    :param len:
        Length of the userspace buffer
    :type len: size_t

    :param off:
        Offset within the file
    :type off: loff_t \*

.. _`zynqmp_pm_debugfs_api_write.description`:

Description
-----------

Used for triggering pm api functions by writing
echo <pm_api_id>     > /sys/kernel/debug/zynqmp_pm/power or
echo <pm_api_name>   > /sys/kernel/debug/zynqmp_pm/power

.. _`zynqmp_pm_debugfs_api_write.return`:

Return
------

Number of bytes copied if PM-API request succeeds,
the corresponding error code otherwise

.. _`zynqmp_pm_debugfs_api_read`:

zynqmp_pm_debugfs_api_read
==========================

.. c:function:: ssize_t zynqmp_pm_debugfs_api_read(struct file *file, char __user *ptr, size_t len, loff_t *off)

    debugfs read function

    :param file:
        User file
    :type file: struct file \*

    :param ptr:
        Requested pm_api_version string
    :type ptr: char __user \*

    :param len:
        Length of the userspace buffer
    :type len: size_t

    :param off:
        Offset within the file
    :type off: loff_t \*

.. _`zynqmp_pm_debugfs_api_read.return`:

Return
------

Length of the version string on success
else error code

.. _`zynqmp_pm_api_debugfs_init`:

zynqmp_pm_api_debugfs_init
==========================

.. c:function:: void zynqmp_pm_api_debugfs_init( void)

    Initialize debugfs interface

    :param void:
        no arguments
    :type void: 

.. _`zynqmp_pm_api_debugfs_init.return`:

Return
------

None

.. _`zynqmp_pm_api_debugfs_exit`:

zynqmp_pm_api_debugfs_exit
==========================

.. c:function:: void zynqmp_pm_api_debugfs_exit( void)

    Remove debugfs interface

    :param void:
        no arguments
    :type void: 

.. _`zynqmp_pm_api_debugfs_exit.return`:

Return
------

None

.. This file was automatic generated / don't edit.

