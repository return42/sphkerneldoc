.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fsi/fsi-sbefifo.c

.. _`sbefifo_submit`:

sbefifo_submit
==============

.. c:function:: int sbefifo_submit(struct device *dev, const __be32 *command, size_t cmd_len, __be32 *response, size_t *resp_len)

    Submit and SBE fifo command and receive response

    :param dev:
        The sbefifo device
    :type dev: struct device \*

    :param command:
        The raw command data
    :type command: const __be32 \*

    :param cmd_len:
        The command size (in 32-bit words)
    :type cmd_len: size_t

    :param response:
        The output response buffer
    :type response: __be32 \*

    :param resp_len:
        In: Response buffer size, Out: Response size
    :type resp_len: size_t \*

.. _`sbefifo_submit.description`:

Description
-----------

This will perform the entire operation. If the reponse buffer
overflows, returns -EOVERFLOW

.. This file was automatic generated / don't edit.

