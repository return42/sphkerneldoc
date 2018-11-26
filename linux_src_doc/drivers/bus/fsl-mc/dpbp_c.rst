.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/bus/fsl-mc/dpbp.c

.. _`dpbp_open`:

dpbp_open
=========

.. c:function:: int dpbp_open(struct fsl_mc_io *mc_io, u32 cmd_flags, int dpbp_id, u16 *token)

    Open a control session for the specified object.

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param dpbp_id:
        DPBP unique ID
    :type dpbp_id: int

    :param token:
        Returned token; use in subsequent API calls
    :type token: u16 \*

.. _`dpbp_open.description`:

Description
-----------

This function can be used to open a control session for an
already created object; an object may have been declared in
the DPL or by calling the dpbp_create function.
This function returns a unique authentication token,
associated with the specific object ID and the specific MC
portal; this token must be used in all subsequent commands for
this specific object

.. _`dpbp_open.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_close`:

dpbp_close
==========

.. c:function:: int dpbp_close(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Close the control session of the object

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPBP object
    :type token: u16

.. _`dpbp_close.description`:

Description
-----------

After this function is called, no further operations are
allowed on the object without opening a new control session.

.. _`dpbp_close.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_enable`:

dpbp_enable
===========

.. c:function:: int dpbp_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Enable the DPBP.

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPBP object
    :type token: u16

.. _`dpbp_enable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_disable`:

dpbp_disable
============

.. c:function:: int dpbp_disable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Disable the DPBP.

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPBP object
    :type token: u16

.. _`dpbp_disable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_reset`:

dpbp_reset
==========

.. c:function:: int dpbp_reset(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Reset the DPBP, returns the object to initial state.

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPBP object
    :type token: u16

.. _`dpbp_reset.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpbp_get_attributes`:

dpbp_get_attributes
===================

.. c:function:: int dpbp_get_attributes(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dpbp_attr *attr)

    Retrieve DPBP attributes.

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPBP object
    :type token: u16

    :param attr:
        Returned object's attributes
    :type attr: struct dpbp_attr \*

.. _`dpbp_get_attributes.return`:

Return
------

'0' on Success; Error code otherwise.

.. This file was automatic generated / don't edit.

