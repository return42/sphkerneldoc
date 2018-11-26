.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/tsacct.c

.. _`acct_update_integrals`:

acct_update_integrals
=====================

.. c:function:: void acct_update_integrals(struct task_struct *tsk)

    update mm integral fields in task_struct

    :param tsk:
        task_struct for accounting
    :type tsk: struct task_struct \*

.. _`acct_account_cputime`:

acct_account_cputime
====================

.. c:function:: void acct_account_cputime(struct task_struct *tsk)

    update mm integral after cputime update

    :param tsk:
        task_struct for accounting
    :type tsk: struct task_struct \*

.. _`acct_clear_integrals`:

acct_clear_integrals
====================

.. c:function:: void acct_clear_integrals(struct task_struct *tsk)

    clear the mm integral fields in task_struct

    :param tsk:
        task_struct whose accounting fields are cleared
    :type tsk: struct task_struct \*

.. This file was automatic generated / don't edit.

