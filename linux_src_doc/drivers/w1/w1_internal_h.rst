.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/w1/w1_internal.h

.. _`w1_async_cmd`:

struct w1_async_cmd
===================

.. c:type:: struct w1_async_cmd

    execute callback from the w1_process kthread

.. _`w1_async_cmd.definition`:

Definition
----------

.. code-block:: c

    struct w1_async_cmd {
        struct list_head async_entry;
        void (*cb)(struct w1_master *dev, struct w1_async_cmd *async_cmd);
    }

.. _`w1_async_cmd.members`:

Members
-------

async_entry
    link entry

cb
    callback function, must list_del and destroy this list before
    returning

.. _`w1_async_cmd.description`:

Description
-----------

When inserted into the w1_master async_list, w1_process will execute
the callback.  Embed this into the structure with the command details.

.. This file was automatic generated / don't edit.

