.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/cavium/liquidio/octeon_mailbox.c

.. _`octeon_mbox_read`:

octeon_mbox_read
================

.. c:function:: int octeon_mbox_read(struct octeon_mbox *mbox)

    :param mbox:
        *undescribed*
    :type mbox: struct octeon_mbox \*

.. _`octeon_mbox_read.description`:

Description
-----------

Reads the 8-bytes of data from the mbox register
Writes back the acknowldgement inidcating completion of read

.. _`octeon_mbox_write`:

octeon_mbox_write
=================

.. c:function:: int octeon_mbox_write(struct octeon_device *oct, struct octeon_mbox_cmd *mbox_cmd)

    :param oct:
        Pointer Octeon Device
    :type oct: struct octeon_device \*

    :param mbox_cmd:
        Cmd to send to mailbox.
    :type mbox_cmd: struct octeon_mbox_cmd \*

.. _`octeon_mbox_write.description`:

Description
-----------

Populates the queue specific mbox structure
with cmd information.
Write the cmd to mbox register

.. _`octeon_mbox_process_cmd`:

octeon_mbox_process_cmd
=======================

.. c:function:: int octeon_mbox_process_cmd(struct octeon_mbox *mbox, struct octeon_mbox_cmd *mbox_cmd)

    :param mbox:
        Pointer mailbox
    :type mbox: struct octeon_mbox \*

    :param mbox_cmd:
        Pointer to command received
    :type mbox_cmd: struct octeon_mbox_cmd \*

.. _`octeon_mbox_process_cmd.description`:

Description
-----------

Process the cmd received in mbox

.. _`octeon_mbox_process_message`:

octeon_mbox_process_message
===========================

.. c:function:: int octeon_mbox_process_message(struct octeon_mbox *mbox)

    :param mbox:
        *undescribed*
    :type mbox: struct octeon_mbox \*

.. _`octeon_mbox_process_message.description`:

Description
-----------

Process the received mbox message.

.. This file was automatic generated / don't edit.

