.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/bus/dpio/dpio.c

.. _`dpio_open`:

dpio_open
=========

.. c:function:: int dpio_open(struct fsl_mc_io *mc_io, u32 cmd_flags, int dpio_id, u16 *token)

    Open a control session for the specified object

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param int dpio_id:
        DPIO unique ID

    :param u16 \*token:
        Returned token; use in subsequent API calls

.. _`dpio_open.description`:

Description
-----------

This function can be used to open a control session for an
already created object; an object may have been declared in
the DPL or by calling the \ :c:func:`dpio_create`\  function.
This function returns a unique authentication token,
associated with the specific object ID and the specific MC
portal; this token must be used in all subsequent commands for
this specific object.

.. _`dpio_open.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpio_close`:

dpio_close
==========

.. c:function:: int dpio_close(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Close the control session of the object

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPIO object

.. _`dpio_close.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpio_enable`:

dpio_enable
===========

.. c:function:: int dpio_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Enable the DPIO, allow I/O portal operations.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPIO object

.. _`dpio_enable.return`:

Return
------

'0' on Success; Error code otherwise

.. _`dpio_disable`:

dpio_disable
============

.. c:function:: int dpio_disable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Disable the DPIO, stop any I/O portal operation.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPIO object

.. _`dpio_disable.return`:

Return
------

'0' on Success; Error code otherwise

.. _`dpio_get_attributes`:

dpio_get_attributes
===================

.. c:function:: int dpio_get_attributes(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dpio_attr *attr)

    Retrieve DPIO attributes

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPIO object

    :param struct dpio_attr \*attr:
        Returned object's attributes

.. _`dpio_get_attributes.return`:

Return
------

'0' on Success; Error code otherwise

.. _`dpio_get_api_version`:

dpio_get_api_version
====================

.. c:function:: int dpio_get_api_version(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 *major_ver, u16 *minor_ver)

    Get Data Path I/O API version

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's DPIO object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 \*major_ver:
        Major version of DPIO API

    :param u16 \*minor_ver:
        Minor version of DPIO API

.. _`dpio_get_api_version.return`:

Return
------

'0' on Success; Error code otherwise

.. This file was automatic generated / don't edit.

