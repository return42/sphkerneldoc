.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_debugfs.c

.. _`ixgbe_dbg_reg_ops_read`:

ixgbe_dbg_reg_ops_read
======================

.. c:function:: ssize_t ixgbe_dbg_reg_ops_read(struct file *filp, char __user *buffer, size_t count, loff_t *ppos)

    read for reg_ops datum

    :param filp:
        the opened file
    :type filp: struct file \*

    :param buffer:
        where to write the data for the user to read
    :type buffer: char __user \*

    :param count:
        the size of the user's buffer
    :type count: size_t

    :param ppos:
        file position offset
    :type ppos: loff_t \*

.. _`ixgbe_dbg_reg_ops_write`:

ixgbe_dbg_reg_ops_write
=======================

.. c:function:: ssize_t ixgbe_dbg_reg_ops_write(struct file *filp, const char __user *buffer, size_t count, loff_t *ppos)

    write into reg_ops datum

    :param filp:
        the opened file
    :type filp: struct file \*

    :param buffer:
        where to find the user's data
    :type buffer: const char __user \*

    :param count:
        the length of the user's data
    :type count: size_t

    :param ppos:
        file position offset
    :type ppos: loff_t \*

.. _`ixgbe_dbg_netdev_ops_read`:

ixgbe_dbg_netdev_ops_read
=========================

.. c:function:: ssize_t ixgbe_dbg_netdev_ops_read(struct file *filp, char __user *buffer, size_t count, loff_t *ppos)

    read for netdev_ops datum

    :param filp:
        the opened file
    :type filp: struct file \*

    :param buffer:
        where to write the data for the user to read
    :type buffer: char __user \*

    :param count:
        the size of the user's buffer
    :type count: size_t

    :param ppos:
        file position offset
    :type ppos: loff_t \*

.. _`ixgbe_dbg_netdev_ops_write`:

ixgbe_dbg_netdev_ops_write
==========================

.. c:function:: ssize_t ixgbe_dbg_netdev_ops_write(struct file *filp, const char __user *buffer, size_t count, loff_t *ppos)

    write into netdev_ops datum

    :param filp:
        the opened file
    :type filp: struct file \*

    :param buffer:
        where to find the user's data
    :type buffer: const char __user \*

    :param count:
        the length of the user's data
    :type count: size_t

    :param ppos:
        file position offset
    :type ppos: loff_t \*

.. _`ixgbe_dbg_adapter_init`:

ixgbe_dbg_adapter_init
======================

.. c:function:: void ixgbe_dbg_adapter_init(struct ixgbe_adapter *adapter)

    setup the debugfs directory for the adapter

    :param adapter:
        the adapter that is starting up
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_dbg_adapter_exit`:

ixgbe_dbg_adapter_exit
======================

.. c:function:: void ixgbe_dbg_adapter_exit(struct ixgbe_adapter *adapter)

    clear out the adapter's debugfs entries

    :param adapter:
        the adapter that is exiting
    :type adapter: struct ixgbe_adapter \*

.. _`ixgbe_dbg_init`:

ixgbe_dbg_init
==============

.. c:function:: void ixgbe_dbg_init( void)

    start up debugfs for the driver

    :param void:
        no arguments
    :type void: 

.. _`ixgbe_dbg_exit`:

ixgbe_dbg_exit
==============

.. c:function:: void ixgbe_dbg_exit( void)

    clean out the driver's debugfs entries

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

