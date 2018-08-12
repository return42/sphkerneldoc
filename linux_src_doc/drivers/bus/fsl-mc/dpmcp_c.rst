.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/bus/fsl-mc/dpmcp.c

.. _`dpmcp_open`:

dpmcp_open
==========

.. c:function:: int dpmcp_open(struct fsl_mc_io *mc_io, u32 cmd_flags, int dpmcp_id, u16 *token)

    Open a control session for the specified object.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param int dpmcp_id:
        DPMCP unique ID

    :param u16 \*token:
        Returned token; use in subsequent API calls

.. _`dpmcp_open.description`:

Description
-----------

This function can be used to open a control session for an
already created object; an object may have been declared in
the DPL or by calling the dpmcp_create function.
This function returns a unique authentication token,
associated with the specific object ID and the specific MC
portal; this token must be used in all subsequent commands for
this specific object

.. _`dpmcp_open.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpmcp_close`:

dpmcp_close
===========

.. c:function:: int dpmcp_close(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Close the control session of the object

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPMCP object

.. _`dpmcp_close.description`:

Description
-----------

After this function is called, no further operations are
allowed on the object without opening a new control session.

.. _`dpmcp_close.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpmcp_reset`:

dpmcp_reset
===========

.. c:function:: int dpmcp_reset(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Reset the DPMCP, returns the object to initial state.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPMCP object

.. _`dpmcp_reset.return`:

Return
------

'0' on Success; Error code otherwise.

.. This file was automatic generated / don't edit.

