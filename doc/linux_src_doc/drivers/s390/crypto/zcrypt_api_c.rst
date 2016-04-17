.. -*- coding: utf-8; mode: rst -*-

============
zcrypt_api.c
============


.. _`zcrypt_process_rescan`:

zcrypt_process_rescan
=====================

.. c:function:: int zcrypt_process_rescan ( void)

    :param void:
        no arguments



.. _`zcrypt_process_rescan.description`:

Description
-----------


Returns 1, if the rescan has been processed, otherwise 0.



.. _`__zcrypt_increase_preference`:

__zcrypt_increase_preference
============================

.. c:function:: void __zcrypt_increase_preference (struct zcrypt_device *zdev)

    :param struct zcrypt_device \*zdev:
        Pointer the crypto device



.. _`__zcrypt_increase_preference.description`:

Description
-----------

Move the device towards the head of the device list.
Need to be called while holding the zcrypt device list lock.



.. _`__zcrypt_increase_preference.note`:

Note
----

cards with speed_rating of 0 are kept at the end of the list.



.. _`__zcrypt_decrease_preference`:

__zcrypt_decrease_preference
============================

.. c:function:: void __zcrypt_decrease_preference (struct zcrypt_device *zdev)

    :param struct zcrypt_device \*zdev:
        Pointer to a crypto device.



.. _`__zcrypt_decrease_preference.description`:

Description
-----------

Move the device towards the tail of the device list.
Need to be called while holding the zcrypt device list lock.



.. _`__zcrypt_decrease_preference.note`:

Note
----

cards with speed_rating of 0 are kept at the end of the list.



.. _`zcrypt_device_register`:

zcrypt_device_register
======================

.. c:function:: int zcrypt_device_register (struct zcrypt_device *zdev)

    Register a crypto device.

    :param struct zcrypt_device \*zdev:
        Pointer to a crypto device



.. _`zcrypt_device_register.description`:

Description
-----------

Register a crypto device. Returns 0 if successful.



.. _`zcrypt_device_unregister`:

zcrypt_device_unregister
========================

.. c:function:: void zcrypt_device_unregister (struct zcrypt_device *zdev)

    :param struct zcrypt_device \*zdev:
        Pointer to crypto device



.. _`zcrypt_device_unregister.description`:

Description
-----------

Unregister a crypto device.



.. _`zcrypt_read`:

zcrypt_read
===========

.. c:function:: ssize_t zcrypt_read (struct file *filp, char __user *buf, size_t count, loff_t *f_pos)

    :param struct file \*filp:

        *undescribed*

    :param char __user \*buf:

        *undescribed*

    :param size_t count:

        *undescribed*

    :param loff_t \*f_pos:

        *undescribed*



.. _`zcrypt_read.description`:

Description
-----------


This function is not supported beyond zcrypt 1.3.1.



.. _`zcrypt_write`:

zcrypt_write
============

.. c:function:: ssize_t zcrypt_write (struct file *filp, const char __user *buf, size_t count, loff_t *f_pos)

    :param struct file \*filp:

        *undescribed*

    :param const char __user \*buf:

        *undescribed*

    :param size_t count:

        *undescribed*

    :param loff_t \*f_pos:

        *undescribed*



.. _`zcrypt_write.description`:

Description
-----------


Write is is not allowed



.. _`zcrypt_open`:

zcrypt_open
===========

.. c:function:: int zcrypt_open (struct inode *inode, struct file *filp)

    :param struct inode \*inode:

        *undescribed*

    :param struct file \*filp:

        *undescribed*



.. _`zcrypt_open.description`:

Description
-----------


Device open function to count number of users.



.. _`zcrypt_release`:

zcrypt_release
==============

.. c:function:: int zcrypt_release (struct inode *inode, struct file *filp)

    :param struct inode \*inode:

        *undescribed*

    :param struct file \*filp:

        *undescribed*



.. _`zcrypt_release.description`:

Description
-----------


Device close function to count number of users.



.. _`zcrypt_ica_status`:

zcrypt_ica_status
=================

.. c:function:: long zcrypt_ica_status (struct file *filp, unsigned long arg)

    :param struct file \*filp:

        *undescribed*

    :param unsigned long arg:

        *undescribed*



.. _`zcrypt_ica_status.description`:

Description
-----------


Old, deprecated combi status call.



.. _`zcrypt_api_init`:

zcrypt_api_init
===============

.. c:function:: int zcrypt_api_init ( void)

    :param void:
        no arguments



.. _`zcrypt_api_init.description`:

Description
-----------


The module initialization code.



.. _`zcrypt_api_exit`:

zcrypt_api_exit
===============

.. c:function:: void zcrypt_api_exit ( void)

    :param void:
        no arguments



.. _`zcrypt_api_exit.description`:

Description
-----------


The module termination code.

