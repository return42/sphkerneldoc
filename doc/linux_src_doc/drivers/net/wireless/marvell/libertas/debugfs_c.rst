.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/marvell/libertas/debugfs.c

.. _`lbs_debugfs_read`:

lbs_debugfs_read
================

.. c:function:: ssize_t lbs_debugfs_read(struct file *file, char __user *userbuf, size_t count, loff_t *ppos)

    proc read function

    :param struct file \*file:
        file to read

    :param char __user \*userbuf:
        pointer to buffer

    :param size_t count:
        number of bytes to read

    :param loff_t \*ppos:
        read data starting position

.. _`lbs_debugfs_read.return`:

Return
------

amount of data read or negative error code

.. _`lbs_debugfs_write`:

lbs_debugfs_write
=================

.. c:function:: ssize_t lbs_debugfs_write(struct file *f, const char __user *buf, size_t cnt, loff_t *ppos)

    proc write function

    :param struct file \*f:
        file pointer

    :param const char __user \*buf:
        pointer to data buffer

    :param size_t cnt:
        data number to write

    :param loff_t \*ppos:
        file position

.. _`lbs_debugfs_write.return`:

Return
------

amount of data written

.. _`lbs_debug_init`:

lbs_debug_init
==============

.. c:function:: void lbs_debug_init(struct lbs_private *priv)

    create debug proc file

    :param struct lbs_private \*priv:
        pointer to \ :c:type:`struct lbs_private <lbs_private>`\ 

.. _`lbs_debug_init.return`:

Return
------

N/A

.. This file was automatic generated / don't edit.

