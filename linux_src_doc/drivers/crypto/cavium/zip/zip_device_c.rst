.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/cavium/zip/zip_device.c

.. _`zip_cmd_queue_consumed`:

zip_cmd_queue_consumed
======================

.. c:function:: u32 zip_cmd_queue_consumed(struct zip_device *zip_dev, int queue)

    Calculates the space consumed in the command queue.

    :param zip_dev:
        Pointer to zip device structure
    :type zip_dev: struct zip_device \*

    :param queue:
        Queue number
    :type queue: int

.. _`zip_cmd_queue_consumed.return`:

Return
------

Bytes consumed in the command queue buffer.

.. _`zip_load_instr`:

zip_load_instr
==============

.. c:function:: u32 zip_load_instr(union zip_inst_s *instr, struct zip_device *zip_dev)

    Submits the instruction into the ZIP command queue

    :param instr:
        Pointer to the instruction to be submitted
    :type instr: union zip_inst_s \*

    :param zip_dev:
        Pointer to ZIP device structure to which the instruction is to
        be submitted
    :type zip_dev: struct zip_device \*

.. _`zip_load_instr.description`:

Description
-----------

This function copies the ZIP instruction to the command queue and rings the
doorbell to notify the engine of the instruction submission. The command
queue is maintained in a circular fashion. When there is space for exactly
one instruction in the queue, next chunk pointer of the queue is made to
point to the head of the queue, thus maintaining a circular queue.

.. _`zip_load_instr.return`:

Return
------

Queue number to which the instruction was submitted

.. _`zip_update_cmd_bufs`:

zip_update_cmd_bufs
===================

.. c:function:: void zip_update_cmd_bufs(struct zip_device *zip_dev, u32 queue)

    Updates the queue statistics after posting the instruction

    :param zip_dev:
        Pointer to zip device structure
    :type zip_dev: struct zip_device \*

    :param queue:
        Queue number
    :type queue: u32

.. This file was automatic generated / don't edit.

