.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_debugfs.c

.. _`ixgbe_dbg_reg_ops_read`:

ixgbe_dbg_reg_ops_read
======================

.. c:function:: ssize_t ixgbe_dbg_reg_ops_read(struct file *filp, char __user *buffer, size_t count, loff_t *ppos)

    read for reg_ops datum

    :param struct file \*filp:
        the opened file

    :param char __user \*buffer:
        where to write the data for the user to read

    :param size_t count:
        the size of the user's buffer

    :param loff_t \*ppos:
        file position offset

.. _`ixgbe_dbg_reg_ops_write`:

ixgbe_dbg_reg_ops_write
=======================

.. c:function:: ssize_t ixgbe_dbg_reg_ops_write(struct file *filp, const char __user *buffer, size_t count, loff_t *ppos)

    write into reg_ops datum

    :param struct file \*filp:
        the opened file

    :param const char __user \*buffer:
        where to find the user's data

    :param size_t count:
        the length of the user's data

    :param loff_t \*ppos:
        file position offset

.. _`ixgbe_dbg_netdev_ops_read`:

ixgbe_dbg_netdev_ops_read
=========================

.. c:function:: ssize_t ixgbe_dbg_netdev_ops_read(struct file *filp, char __user *buffer, size_t count, loff_t *ppos)

    read for netdev_ops datum

    :param struct file \*filp:
        the opened file

    :param char __user \*buffer:
        where to write the data for the user to read

    :param size_t count:
        the size of the user's buffer

    :param loff_t \*ppos:
        file position offset

.. _`ixgbe_dbg_netdev_ops_write`:

ixgbe_dbg_netdev_ops_write
==========================

.. c:function:: ssize_t ixgbe_dbg_netdev_ops_write(struct file *filp, const char __user *buffer, size_t count, loff_t *ppos)

    write into netdev_ops datum

    :param struct file \*filp:
        the opened file

    :param const char __user \*buffer:
        where to find the user's data

    :param size_t count:
        the length of the user's data

    :param loff_t \*ppos:
        file position offset

.. _`ixgbe_dbg_adapter_init`:

ixgbe_dbg_adapter_init
======================

.. c:function:: void ixgbe_dbg_adapter_init(struct ixgbe_adapter *adapter)

    setup the debugfs directory for the adapter

    :param struct ixgbe_adapter \*adapter:
        the adapter that is starting up

.. _`ixgbe_dbg_adapter_exit`:

ixgbe_dbg_adapter_exit
======================

.. c:function:: void ixgbe_dbg_adapter_exit(struct ixgbe_adapter *adapter)

    clear out the adapter's debugfs entries

    :param struct ixgbe_adapter \*adapter:
        *undescribed*

.. _`ixgbe_dbg_init`:

ixgbe_dbg_init
==============

.. c:function:: void ixgbe_dbg_init( void)

    start up debugfs for the driver

    :param  void:
        no arguments

.. _`ixgbe_dbg_exit`:

ixgbe_dbg_exit
==============

.. c:function:: void ixgbe_dbg_exit( void)

    clean out the driver's debugfs entries

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

