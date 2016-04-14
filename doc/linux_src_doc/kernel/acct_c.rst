.. -*- coding: utf-8; mode: rst -*-

======
acct.c
======

.. _`sys_acct`:

sys_acct
========

.. c:function:: long sys_acct (const char __user *name)

    enable/disable process accounting

    :param const char __user \*name:
        file name for accounting records or NULL to shutdown accounting


.. _`sys_acct.description`:

Description
-----------

Returns 0 for success or negative errno values for failure.

:c:func:`sys_acct` is the only system call needed to implement process
accounting. It takes the name of the file where accounting records
should be written. If the filename is NULL, accounting will be
shutdown.


.. _`acct_collect`:

acct_collect
============

.. c:function:: void acct_collect (long exitcode, int group_dead)

    collect accounting information into pacct_struct

    :param long exitcode:
        task exit code

    :param int group_dead:
        not 0, if this thread is the last one in the process.


.. _`acct_process`:

acct_process
============

.. c:function:: void acct_process ( void)

    :param void:
        no arguments


.. _`acct_process.description`:

Description
-----------


handles process accounting for an exiting task

