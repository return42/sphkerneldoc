.. -*- coding: utf-8; mode: rst -*-

==========
ide-proc.c
==========


.. _`ide_find_setting`:

ide_find_setting
================

.. c:function:: const struct ide_proc_devset *ide_find_setting (const struct ide_proc_devset *st, char *name)

    find a specific setting

    :param const struct ide_proc_devset \*st:
        setting table pointer

    :param char \*name:
        setting name



.. _`ide_find_setting.description`:

Description
-----------

Scan's the setting table for a matching entry and returns
this or NULL if no entry is found. The caller must hold the
setting semaphore



.. _`ide_read_setting`:

ide_read_setting
================

.. c:function:: int ide_read_setting (ide_drive_t *drive, const struct ide_proc_devset *setting)

    read an IDE setting

    :param ide_drive_t \*drive:
        drive to read from

    :param const struct ide_proc_devset \*setting:
        drive setting



.. _`ide_read_setting.description`:

Description
-----------

Read a drive setting and return the value. The caller
must hold the ide_setting_mtx when making this call.



.. _`ide_read_setting.bugs`:

BUGS
----

the data return and error are the same return value
so an error -EINVAL and true return of the same value cannot
be told apart



.. _`ide_write_setting`:

ide_write_setting
=================

.. c:function:: int ide_write_setting (ide_drive_t *drive, const struct ide_proc_devset *setting, int val)

    read an IDE setting

    :param ide_drive_t \*drive:
        drive to read from

    :param const struct ide_proc_devset \*setting:
        drive setting

    :param int val:
        value



.. _`ide_write_setting.description`:

Description
-----------

Write a drive setting if it is possible. The caller
must hold the ide_setting_mtx when making this call.



.. _`ide_write_setting.bugs`:

BUGS
----

the data return and error are the same return value
so an error -EINVAL and true return of the same value cannot
be told apart



.. _`ide_write_setting.fixme`:

FIXME
-----

This should be changed to enqueue a special request
to the driver to change settings, and then wait on a sema for completion.
The current scheme of polling is kludgy, though safe enough.



.. _`ide_proc_unregister_driver`:

ide_proc_unregister_driver
==========================

.. c:function:: void ide_proc_unregister_driver (ide_drive_t *drive, struct ide_driver *driver)

    remove driver specific data

    :param ide_drive_t \*drive:
        drive

    :param struct ide_driver \*driver:
        driver



.. _`ide_proc_unregister_driver.description`:

Description
-----------

Clean up the driver specific /proc files and IDE settings
for a given drive.

Takes ide_setting_mtx.

