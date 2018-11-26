.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/zcrypt_api.c

.. _`zcrypt_process_rescan`:

zcrypt_process_rescan
=====================

.. c:function:: int zcrypt_process_rescan( void)

    :param void:
        no arguments
    :type void: 

.. _`zcrypt_process_rescan.description`:

Description
-----------

Returns 1, if the rescan has been processed, otherwise 0.

.. _`zcrypt_read`:

zcrypt_read
===========

.. c:function:: ssize_t zcrypt_read(struct file *filp, char __user *buf, size_t count, loff_t *f_pos)

    Not supported beyond zcrypt 1.3.1.

    :param filp:
        *undescribed*
    :type filp: struct file \*

    :param buf:
        *undescribed*
    :type buf: char __user \*

    :param count:
        *undescribed*
    :type count: size_t

    :param f_pos:
        *undescribed*
    :type f_pos: loff_t \*

.. _`zcrypt_read.description`:

Description
-----------

This function is not supported beyond zcrypt 1.3.1.

.. _`zcrypt_write`:

zcrypt_write
============

.. c:function:: ssize_t zcrypt_write(struct file *filp, const char __user *buf, size_t count, loff_t *f_pos)

    Not allowed.

    :param filp:
        *undescribed*
    :type filp: struct file \*

    :param buf:
        *undescribed*
    :type buf: const char __user \*

    :param count:
        *undescribed*
    :type count: size_t

    :param f_pos:
        *undescribed*
    :type f_pos: loff_t \*

.. _`zcrypt_write.description`:

Description
-----------

Write is is not allowed

.. _`zcrypt_open`:

zcrypt_open
===========

.. c:function:: int zcrypt_open(struct inode *inode, struct file *filp)

    Count number of users.

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param filp:
        *undescribed*
    :type filp: struct file \*

.. _`zcrypt_open.description`:

Description
-----------

Device open function to count number of users.

.. _`zcrypt_release`:

zcrypt_release
==============

.. c:function:: int zcrypt_release(struct inode *inode, struct file *filp)

    Count number of users.

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param filp:
        *undescribed*
    :type filp: struct file \*

.. _`zcrypt_release.description`:

Description
-----------

Device close function to count number of users.

.. _`zcrypt_api_init`:

zcrypt_api_init
===============

.. c:function:: int zcrypt_api_init( void)

    Module initialization.

    :param void:
        no arguments
    :type void: 

.. _`zcrypt_api_init.description`:

Description
-----------

The module initialization code.

.. _`zcrypt_api_exit`:

zcrypt_api_exit
===============

.. c:function:: void __exit zcrypt_api_exit( void)

    Module termination.

    :param void:
        no arguments
    :type void: 

.. _`zcrypt_api_exit.description`:

Description
-----------

The module termination code.

.. This file was automatic generated / don't edit.

