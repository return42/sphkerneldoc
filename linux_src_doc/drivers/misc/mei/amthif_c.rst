.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/amthif.c

.. _`mei_amthif_reset_params`:

mei_amthif_reset_params
=======================

.. c:function:: void mei_amthif_reset_params(struct mei_device *dev)

    initializes mei device iamthif

    :param struct mei_device \*dev:
        the device structure

.. _`mei_amthif_host_init`:

mei_amthif_host_init
====================

.. c:function:: int mei_amthif_host_init(struct mei_device *dev, struct mei_me_client *me_cl)

    mei initialization amthif client.

    :param struct mei_device \*dev:
        the device structure

    :param struct mei_me_client \*me_cl:
        me client

.. _`mei_amthif_host_init.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_amthif_read`:

mei_amthif_read
===============

.. c:function:: int mei_amthif_read(struct mei_device *dev, struct file *file, char __user *ubuf, size_t length, loff_t *offset)

    read data from AMTHIF client

    :param struct mei_device \*dev:
        the device structure

    :param struct file \*file:
        pointer to file object

    :param char __user \*ubuf:
        pointer to user data in user space

    :param size_t length:
        data length to read

    :param loff_t \*offset:
        data read offset

.. _`mei_amthif_read.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_amthif_read.return`:

Return
------

returned data length on success,
zero if no data to read,
negative on failure.

.. _`mei_amthif_read_start`:

mei_amthif_read_start
=====================

.. c:function:: int mei_amthif_read_start(struct mei_cl *cl, const struct file *file)

    queue message for sending read credential

    :param struct mei_cl \*cl:
        host client

    :param const struct file \*file:
        file pointer of message recipient

.. _`mei_amthif_read_start.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_amthif_send_cmd`:

mei_amthif_send_cmd
===================

.. c:function:: int mei_amthif_send_cmd(struct mei_cl *cl, struct mei_cl_cb *cb)

    send amthif command to the ME

    :param struct mei_cl \*cl:
        the host client

    :param struct mei_cl_cb \*cb:
        mei call back struct

.. _`mei_amthif_send_cmd.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_amthif_run_next_cmd`:

mei_amthif_run_next_cmd
=======================

.. c:function:: int mei_amthif_run_next_cmd(struct mei_device *dev)

    send next amt command from queue

    :param struct mei_device \*dev:
        the device structure

.. _`mei_amthif_run_next_cmd.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_amthif_write`:

mei_amthif_write
================

.. c:function:: int mei_amthif_write(struct mei_cl *cl, struct mei_cl_cb *cb)

    write amthif data to amthif client

    :param struct mei_cl \*cl:
        host client

    :param struct mei_cl_cb \*cb:
        mei call back struct

.. _`mei_amthif_write.return`:

Return
------

0 on success, <0 on failure.

.. _`mei_amthif_poll`:

mei_amthif_poll
===============

.. c:function:: unsigned int mei_amthif_poll(struct mei_device *dev, struct file *file, poll_table *wait)

    the amthif poll function

    :param struct mei_device \*dev:
        the device structure

    :param struct file \*file:
        pointer to file structure

    :param poll_table \*wait:
        pointer to poll_table structure

.. _`mei_amthif_poll.return`:

Return
------

poll mask

.. _`mei_amthif_poll.locking`:

Locking
-------

called under "dev->device_lock" lock

.. _`mei_amthif_irq_write`:

mei_amthif_irq_write
====================

.. c:function:: int mei_amthif_irq_write(struct mei_cl *cl, struct mei_cl_cb *cb, struct mei_cl_cb *cmpl_list)

    write iamthif command in irq thread context.

    :param struct mei_cl \*cl:
        private data of the file object.

    :param struct mei_cl_cb \*cb:
        callback block.

    :param struct mei_cl_cb \*cmpl_list:
        complete list.

.. _`mei_amthif_irq_write.return`:

Return
------

0, OK; otherwise, error.

.. _`mei_amthif_irq_read_msg`:

mei_amthif_irq_read_msg
=======================

.. c:function:: int mei_amthif_irq_read_msg(struct mei_cl *cl, struct mei_msg_hdr *mei_hdr, struct mei_cl_cb *cmpl_list)

    read routine after ISR to handle the read amthif message

    :param struct mei_cl \*cl:
        mei client

    :param struct mei_msg_hdr \*mei_hdr:
        header of amthif message

    :param struct mei_cl_cb \*cmpl_list:
        completed callbacks list

.. _`mei_amthif_irq_read_msg.return`:

Return
------

-ENODEV if cb is NULL 0 otherwise; error message is in cb->status

.. _`mei_amthif_complete`:

mei_amthif_complete
===================

.. c:function:: void mei_amthif_complete(struct mei_cl *cl, struct mei_cl_cb *cb)

    complete amthif callback.

    :param struct mei_cl \*cl:
        host client

    :param struct mei_cl_cb \*cb:
        callback block.

.. _`mei_clear_list`:

mei_clear_list
==============

.. c:function:: bool mei_clear_list(struct mei_device *dev, const struct file *file, struct list_head *mei_cb_list)

    removes all callbacks associated with file from mei_cb_list

    :param struct mei_device \*dev:
        device structure.

    :param const struct file \*file:
        file structure

    :param struct list_head \*mei_cb_list:
        callbacks list

.. _`mei_clear_list.description`:

Description
-----------

mei_clear_list is called to clear resources associated with file
when application calls close function or Ctrl-C was pressed

.. _`mei_clear_list.return`:

Return
------

true if callback removed from the list, false otherwise

.. _`mei_clear_lists`:

mei_clear_lists
===============

.. c:function:: bool mei_clear_lists(struct mei_device *dev, const struct file *file)

    removes all callbacks associated with file

    :param struct mei_device \*dev:
        device structure

    :param const struct file \*file:
        file structure

.. _`mei_clear_lists.description`:

Description
-----------

mei_clear_lists is called to clear resources associated with file
when application calls close function or Ctrl-C was pressed

.. _`mei_clear_lists.return`:

Return
------

true if callback removed from the list, false otherwise

.. _`mei_amthif_release`:

mei_amthif_release
==================

.. c:function:: int mei_amthif_release(struct mei_device *dev, struct file *file)

    the release function

    :param struct mei_device \*dev:
        device structure

    :param struct file \*file:
        pointer to file structure

.. _`mei_amthif_release.return`:

Return
------

0 on success, <0 on error

.. This file was automatic generated / don't edit.

