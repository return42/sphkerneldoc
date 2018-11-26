.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/marvell/libertas/debugfs.c

.. _`lbs_debugfs_read`:

lbs_debugfs_read
================

.. c:function:: ssize_t lbs_debugfs_read(struct file *file, char __user *userbuf, size_t count, loff_t *ppos)

    proc read function

    :param file:
        file to read
    :type file: struct file \*

    :param userbuf:
        pointer to buffer
    :type userbuf: char __user \*

    :param count:
        number of bytes to read
    :type count: size_t

    :param ppos:
        read data starting position
    :type ppos: loff_t \*

.. _`lbs_debugfs_read.return`:

Return
------

amount of data read or negative error code

.. _`lbs_debugfs_write`:

lbs_debugfs_write
=================

.. c:function:: ssize_t lbs_debugfs_write(struct file *f, const char __user *buf, size_t cnt, loff_t *ppos)

    proc write function

    :param f:
        file pointer
    :type f: struct file \*

    :param buf:
        pointer to data buffer
    :type buf: const char __user \*

    :param cnt:
        data number to write
    :type cnt: size_t

    :param ppos:
        file position
    :type ppos: loff_t \*

.. _`lbs_debugfs_write.return`:

Return
------

amount of data written

.. _`lbs_debug_init`:

lbs_debug_init
==============

.. c:function:: void lbs_debug_init(struct lbs_private *priv)

    create debug proc file

    :param priv:
        pointer to \ :c:type:`struct lbs_private <lbs_private>`\ 
    :type priv: struct lbs_private \*

.. _`lbs_debug_init.return`:

Return
------

N/A

.. This file was automatic generated / don't edit.

