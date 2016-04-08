
.. _API-struct-w1-async-cmd:

===================
struct w1_async_cmd
===================

*man struct w1_async_cmd(9)*

*4.6.0-rc1*

execute callback from the w1_process kthread


Synopsis
========

.. code-block:: c

    struct w1_async_cmd {
      struct list_head async_entry;
      void (* cb) (struct w1_master *dev, struct w1_async_cmd *async_cmd);
    };


Members
=======

async_entry
    link entry

cb
    callback function, must list_del and destroy this list before returning


Description
===========

When inserted into the w1_master async_list, w1_process will execute the callback. Embed this into the structure with the command details.
