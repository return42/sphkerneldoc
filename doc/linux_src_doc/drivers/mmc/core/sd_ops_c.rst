.. -*- coding: utf-8; mode: rst -*-

========
sd_ops.c
========


.. _`mmc_wait_for_app_cmd`:

mmc_wait_for_app_cmd
====================

.. c:function:: int mmc_wait_for_app_cmd (struct mmc_host *host, struct mmc_card *card, struct mmc_command *cmd, int retries)

    start an application command and wait for

    :param struct mmc_host \*host:
        MMC host to start command

    :param struct mmc_card \*card:
        Card to send MMC_APP_CMD to

    :param struct mmc_command \*cmd:
        MMC command to start

    :param int retries:
        maximum number of retries



.. _`mmc_wait_for_app_cmd.description`:

Description
-----------

Sends a MMC_APP_CMD, checks the card response, sends the command
in the parameter and waits for it to complete. Return any error
that occurred while the command was executing.  Do not attempt to
parse the response.

