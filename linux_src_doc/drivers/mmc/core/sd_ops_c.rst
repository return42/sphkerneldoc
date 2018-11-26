.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/core/sd_ops.c

.. _`mmc_wait_for_app_cmd`:

mmc_wait_for_app_cmd
====================

.. c:function:: int mmc_wait_for_app_cmd(struct mmc_host *host, struct mmc_card *card, struct mmc_command *cmd, int retries)

    start an application command and wait for

    :param host:
        MMC host to start command
    :type host: struct mmc_host \*

    :param card:
        Card to send MMC_APP_CMD to
    :type card: struct mmc_card \*

    :param cmd:
        MMC command to start
    :type cmd: struct mmc_command \*

    :param retries:
        maximum number of retries
    :type retries: int

.. _`mmc_wait_for_app_cmd.description`:

Description
-----------

Sends a MMC_APP_CMD, checks the card response, sends the command
in the parameter and waits for it to complete. Return any error
that occurred while the command was executing.  Do not attempt to
parse the response.

.. This file was automatic generated / don't edit.

