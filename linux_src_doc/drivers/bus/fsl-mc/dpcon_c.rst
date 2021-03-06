.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/bus/fsl-mc/dpcon.c

.. _`dpcon_open`:

dpcon_open
==========

.. c:function:: int dpcon_open(struct fsl_mc_io *mc_io, u32 cmd_flags, int dpcon_id, u16 *token)

    Open a control session for the specified object

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param dpcon_id:
        DPCON unique ID
    :type dpcon_id: int

    :param token:
        Returned token; use in subsequent API calls
    :type token: u16 \*

.. _`dpcon_open.description`:

Description
-----------

This function can be used to open a control session for an
already created object; an object may have been declared in
the DPL or by calling the \ :c:func:`dpcon_create`\  function.
This function returns a unique authentication token,
associated with the specific object ID and the specific MC
portal; this token must be used in all subsequent commands for
this specific object.

.. _`dpcon_open.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpcon_close`:

dpcon_close
===========

.. c:function:: int dpcon_close(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Close the control session of the object

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPCON object
    :type token: u16

.. _`dpcon_close.description`:

Description
-----------

After this function is called, no further operations are
allowed on the object without opening a new control session.

.. _`dpcon_close.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpcon_enable`:

dpcon_enable
============

.. c:function:: int dpcon_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Enable the DPCON

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPCON object
    :type token: u16

.. _`dpcon_enable.return`:

Return
------

'0' on Success; Error code otherwise

.. _`dpcon_disable`:

dpcon_disable
=============

.. c:function:: int dpcon_disable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Disable the DPCON

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPCON object
    :type token: u16

.. _`dpcon_disable.return`:

Return
------

'0' on Success; Error code otherwise

.. _`dpcon_reset`:

dpcon_reset
===========

.. c:function:: int dpcon_reset(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Reset the DPCON, returns the object to initial state.

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPCON object
    :type token: u16

.. _`dpcon_reset.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpcon_get_attributes`:

dpcon_get_attributes
====================

.. c:function:: int dpcon_get_attributes(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dpcon_attr *attr)

    Retrieve DPCON attributes.

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPCON object
    :type token: u16

    :param attr:
        Object's attributes
    :type attr: struct dpcon_attr \*

.. _`dpcon_get_attributes.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dpcon_set_notification`:

dpcon_set_notification
======================

.. c:function:: int dpcon_set_notification(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dpcon_notification_cfg *cfg)

    Set DPCON notification destination

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPCON object
    :type token: u16

    :param cfg:
        Notification parameters
    :type cfg: struct dpcon_notification_cfg \*

.. _`dpcon_set_notification.return`:

Return
------

'0' on Success; Error code otherwise

.. This file was automatic generated / don't edit.

