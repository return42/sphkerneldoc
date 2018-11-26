.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/fsl/dpio/dpio.c

.. _`dpio_open`:

dpio_open
=========

.. c:function:: int dpio_open(struct fsl_mc_io *mc_io, u32 cmd_flags, int dpio_id, u16 *token)

    Open a control session for the specified object

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param dpio_id:
        DPIO unique ID
    :type dpio_id: int

    :param token:
        Returned token; use in subsequent API calls
    :type token: u16 \*

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

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPIO object
    :type token: u16

.. _`dpio_close.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpio_enable`:

dpio_enable
===========

.. c:function:: int dpio_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Enable the DPIO, allow I/O portal operations.

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPIO object
    :type token: u16

.. _`dpio_enable.return`:

Return
------

'0' on Success; Error code otherwise

.. _`dpio_disable`:

dpio_disable
============

.. c:function:: int dpio_disable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Disable the DPIO, stop any I/O portal operation.

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPIO object
    :type token: u16

.. _`dpio_disable.return`:

Return
------

'0' on Success; Error code otherwise

.. _`dpio_get_attributes`:

dpio_get_attributes
===================

.. c:function:: int dpio_get_attributes(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dpio_attr *attr)

    Retrieve DPIO attributes

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPIO object
    :type token: u16

    :param attr:
        Returned object's attributes
    :type attr: struct dpio_attr \*

.. _`dpio_get_attributes.return`:

Return
------

'0' on Success; Error code otherwise

.. _`dpio_get_api_version`:

dpio_get_api_version
====================

.. c:function:: int dpio_get_api_version(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 *major_ver, u16 *minor_ver)

    Get Data Path I/O API version

    :param mc_io:
        Pointer to MC portal's DPIO object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param major_ver:
        Major version of DPIO API
    :type major_ver: u16 \*

    :param minor_ver:
        Minor version of DPIO API
    :type minor_ver: u16 \*

.. _`dpio_get_api_version.return`:

Return
------

'0' on Success; Error code otherwise

.. This file was automatic generated / don't edit.

