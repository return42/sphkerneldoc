.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/seq/seq_clientmgr.c

.. _`snd_seq_kernel_client_ctl`:

snd_seq_kernel_client_ctl
=========================

.. c:function:: int snd_seq_kernel_client_ctl(int clientid, unsigned int cmd, void *arg)

    operate a command for a client with data in kernel space.

    :param int clientid:
        A numerical ID for a client.

    :param unsigned int cmd:
        An ioctl(2) command for ALSA sequencer operation.

    :param void \*arg:
        A pointer to data in kernel space.

.. _`snd_seq_kernel_client_ctl.description`:

Description
-----------

Against its name, both kernel/application client can be handled by this
kernel API. A pointer of 'arg' argument should be in kernel space.

.. _`snd_seq_kernel_client_ctl.return`:

Return
------

0 at success. Negative error code at failure.

.. This file was automatic generated / don't edit.

