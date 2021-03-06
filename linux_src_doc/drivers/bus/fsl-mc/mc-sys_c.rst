.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/bus/fsl-mc/mc-sys.c

.. _`mc_cmd_completion_timeout_ms`:

MC_CMD_COMPLETION_TIMEOUT_MS
============================

.. c:function::  MC_CMD_COMPLETION_TIMEOUT_MS()

.. _`mc_write_command`:

mc_write_command
================

.. c:function:: void mc_write_command(struct fsl_mc_command __iomem *portal, struct fsl_mc_command *cmd)

    writes a command to a Management Complex (MC) portal

    :param portal:
        pointer to an MC portal
    :type portal: struct fsl_mc_command __iomem \*

    :param cmd:
        pointer to a filled command
    :type cmd: struct fsl_mc_command \*

.. _`mc_read_response`:

mc_read_response
================

.. c:function:: enum mc_cmd_status mc_read_response(struct fsl_mc_command __iomem *portal, struct fsl_mc_command *resp)

    reads the response for the last MC command from a Management Complex (MC) portal

    :param portal:
        pointer to an MC portal
    :type portal: struct fsl_mc_command __iomem \*

    :param resp:
        pointer to command response buffer
    :type resp: struct fsl_mc_command \*

.. _`mc_read_response.description`:

Description
-----------

Returns MC_CMD_STATUS_OK on Success; Error code otherwise.

.. _`mc_polling_wait_preemptible`:

mc_polling_wait_preemptible
===========================

.. c:function:: int mc_polling_wait_preemptible(struct fsl_mc_io *mc_io, struct fsl_mc_command *cmd, enum mc_cmd_status *mc_status)

    \ :c:func:`uslepp_range`\  is called between polling iterations.

    :param mc_io:
        MC I/O object to be used
    :type mc_io: struct fsl_mc_io \*

    :param cmd:
        command buffer to receive MC response
    :type cmd: struct fsl_mc_command \*

    :param mc_status:
        MC command completion status
    :type mc_status: enum mc_cmd_status \*

.. _`mc_polling_wait_atomic`:

mc_polling_wait_atomic
======================

.. c:function:: int mc_polling_wait_atomic(struct fsl_mc_io *mc_io, struct fsl_mc_command *cmd, enum mc_cmd_status *mc_status)

    \ :c:func:`udelay`\  is called between polling iterations.

    :param mc_io:
        MC I/O object to be used
    :type mc_io: struct fsl_mc_io \*

    :param cmd:
        command buffer to receive MC response
    :type cmd: struct fsl_mc_command \*

    :param mc_status:
        MC command completion status
    :type mc_status: enum mc_cmd_status \*

.. _`mc_send_command`:

mc_send_command
===============

.. c:function:: int mc_send_command(struct fsl_mc_io *mc_io, struct fsl_mc_command *cmd)

    :param mc_io:
        MC I/O object to be used
    :type mc_io: struct fsl_mc_io \*

    :param cmd:
        command to be sent
    :type cmd: struct fsl_mc_command \*

.. _`mc_send_command.description`:

Description
-----------

Returns '0' on Success; Error code otherwise.

.. This file was automatic generated / don't edit.

