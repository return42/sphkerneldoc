.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/debugfs.c

.. _`mei_dbgfs_deregister`:

mei_dbgfs_deregister
====================

.. c:function:: void mei_dbgfs_deregister(struct mei_device *dev)

    Remove the debugfs files and directories

    :param dev:
        the mei device structure
    :type dev: struct mei_device \*

.. _`mei_dbgfs_register`:

mei_dbgfs_register
==================

.. c:function:: int mei_dbgfs_register(struct mei_device *dev, const char *name)

    Add the debugfs files

    :param dev:
        the mei device structure
    :type dev: struct mei_device \*

    :param name:
        the mei device name
    :type name: const char \*

.. _`mei_dbgfs_register.return`:

Return
------

0 on success, <0 on failure.

.. This file was automatic generated / don't edit.

