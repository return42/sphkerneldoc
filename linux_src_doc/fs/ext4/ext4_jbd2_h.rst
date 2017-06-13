.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ext4/ext4_jbd2.h

.. _`ext4_journal_cb_entry`:

struct ext4_journal_cb_entry
============================

.. c:type:: struct ext4_journal_cb_entry

    Base structure for callback information.

.. _`ext4_journal_cb_entry.definition`:

Definition
----------

.. code-block:: c

    struct ext4_journal_cb_entry {
        struct list_head jce_list;
        void (*jce_func)(struct super_block *sb, struct ext4_journal_cb_entry *jce, int error);
    }

.. _`ext4_journal_cb_entry.members`:

Members
-------

jce_list
    *undescribed*

jce_func
    *undescribed*

.. _`ext4_journal_cb_entry.description`:

Description
-----------

This struct is a 'seed' structure for a using with your own callback
structs. If you are using callbacks you must allocate one of these
or another struct of your own definition which has this struct
as it's first element and pass it to \ :c:func:`ext4_journal_callback_add`\ .

.. _`_ext4_journal_callback_add`:

_ext4_journal_callback_add
==========================

.. c:function:: void _ext4_journal_callback_add(handle_t *handle, struct ext4_journal_cb_entry *jce)

    add a function to call after transaction commit

    :param handle_t \*handle:
        active journal transaction handle to register callback on

    :param struct ext4_journal_cb_entry \*jce:
        journal callback data (internal and function private data struct)

.. _`_ext4_journal_callback_add.description`:

Description
-----------

The registered function will be called in the context of the journal thread
after the transaction for which the handle was created has completed.

No locks are held when the callback function is called, so it is safe to
call blocking functions from within the callback, but the callback should
not block or run for too long, or the filesystem will be blocked waiting for
the next transaction to commit. No journaling functions can be used, or
there is a risk of deadlock.

There is no guaranteed calling order of multiple registered callbacks on
the same transaction.

.. _`ext4_journal_callback_try_del`:

ext4_journal_callback_try_del
=============================

.. c:function:: bool ext4_journal_callback_try_del(handle_t *handle, struct ext4_journal_cb_entry *jce)

    delete a registered callback

    :param handle_t \*handle:
        active journal transaction handle on which callback was registered

    :param struct ext4_journal_cb_entry \*jce:
        registered journal callback entry to unregister
        Return true if object was successfully removed

.. This file was automatic generated / don't edit.

