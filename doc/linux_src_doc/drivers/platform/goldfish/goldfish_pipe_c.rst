.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/goldfish/goldfish_pipe.c

.. _`goldfish_pipe_open`:

goldfish_pipe_open
==================

.. c:function:: int goldfish_pipe_open(struct inode *inode, struct file *file)

    open a channel to the AVD

    :param struct inode \*inode:
        inode of device

    :param struct file \*file:
        file struct of opener

.. _`goldfish_pipe_open.description`:

Description
-----------

Create a new pipe link between the emulator and the use application.
Each new request produces a new pipe.

.. _`goldfish_pipe_open.note`:

Note
----

we use the pipe ID as a mux. All goldfish emulations are 32bit
right now so this is fine. A move to 64bit will need this addressing

.. This file was automatic generated / don't edit.

