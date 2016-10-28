.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/bus/mc-sys.c

.. _`mc_cmd_completion_timeout_ms`:

MC_CMD_COMPLETION_TIMEOUT_MS
============================

.. c:function::  MC_CMD_COMPLETION_TIMEOUT_MS()

.. _`fsl_create_mc_io`:

fsl_create_mc_io
================

.. c:function:: int fsl_create_mc_io(struct device *dev, phys_addr_t mc_portal_phys_addr, u32 mc_portal_size, struct fsl_mc_device *dpmcp_dev, u32 flags, struct fsl_mc_io **new_mc_io)

    :param struct device \*dev:
        device to be associated with the MC I/O object

    :param phys_addr_t mc_portal_phys_addr:
        physical address of the MC portal to use

    :param u32 mc_portal_size:
        size in bytes of the MC portal

    :param struct fsl_mc_device \*dpmcp_dev:
        *undescribed*

    :param u32 flags:
        flags for the new MC I/O object

    :param struct fsl_mc_io \*\*new_mc_io:
        Area to return pointer to newly created MC I/O object

.. _`fsl_create_mc_io.description`:

Description
-----------

Returns '0' on Success; Error code otherwise.

.. _`fsl_destroy_mc_io`:

fsl_destroy_mc_io
=================

.. c:function:: void fsl_destroy_mc_io(struct fsl_mc_io *mc_io)

    :param struct fsl_mc_io \*mc_io:
        MC I/O object to destroy

.. _`mc_write_command`:

mc_write_command
================

.. c:function:: void mc_write_command(struct mc_command __iomem *portal, struct mc_command *cmd)

    writes a command to a Management Complex (MC) portal

    :param struct mc_command __iomem \*portal:
        pointer to an MC portal

    :param struct mc_command \*cmd:
        pointer to a filled command

.. _`mc_read_response`:

mc_read_response
================

.. c:function:: enum mc_cmd_status mc_read_response(struct mc_command __iomem *portal, struct mc_command *resp)

    reads the response for the last MC command from a Management Complex (MC) portal

    :param struct mc_command __iomem \*portal:
        pointer to an MC portal

    :param struct mc_command \*resp:
        pointer to command response buffer

.. _`mc_read_response.description`:

Description
-----------

Returns MC_CMD_STATUS_OK on Success; Error code otherwise.

.. _`mc_polling_wait_preemptible`:

mc_polling_wait_preemptible
===========================

.. c:function:: int mc_polling_wait_preemptible(struct fsl_mc_io *mc_io, struct mc_command *cmd, enum mc_cmd_status *mc_status)

    \ :c:func:`uslepp_range`\  is called between polling iterations.

    :param struct fsl_mc_io \*mc_io:
        MC I/O object to be used

    :param struct mc_command \*cmd:
        command buffer to receive MC response

    :param enum mc_cmd_status \*mc_status:
        MC command completion status

.. _`mc_polling_wait_atomic`:

mc_polling_wait_atomic
======================

.. c:function:: int mc_polling_wait_atomic(struct fsl_mc_io *mc_io, struct mc_command *cmd, enum mc_cmd_status *mc_status)

    \ :c:func:`udelay`\  is called between polling iterations.

    :param struct fsl_mc_io \*mc_io:
        MC I/O object to be used

    :param struct mc_command \*cmd:
        command buffer to receive MC response

    :param enum mc_cmd_status \*mc_status:
        MC command completion status

.. _`mc_send_command`:

mc_send_command
===============

.. c:function:: int mc_send_command(struct fsl_mc_io *mc_io, struct mc_command *cmd)

    :param struct fsl_mc_io \*mc_io:
        MC I/O object to be used

    :param struct mc_command \*cmd:
        command to be sent

.. _`mc_send_command.description`:

Description
-----------

Returns '0' on Success; Error code otherwise.

.. This file was automatic generated / don't edit.

