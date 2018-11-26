.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/freescale/dpaa2/dprtc.c

.. _`dprtc_open`:

dprtc_open
==========

.. c:function:: int dprtc_open(struct fsl_mc_io *mc_io, u32 cmd_flags, int dprtc_id, u16 *token)

    Open a control session for the specified object.

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param dprtc_id:
        DPRTC unique ID
    :type dprtc_id: int

    :param token:
        Returned token; use in subsequent API calls
    :type token: u16 \*

.. _`dprtc_open.description`:

Description
-----------

This function can be used to open a control session for an
already created object; an object may have been declared in
the DPL or by calling the dprtc_create function.
This function returns a unique authentication token,
associated with the specific object ID and the specific MC
portal; this token must be used in all subsequent commands for
this specific object

.. _`dprtc_open.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_close`:

dprtc_close
===========

.. c:function:: int dprtc_close(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Close the control session of the object

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPRTC object
    :type token: u16

.. _`dprtc_close.description`:

Description
-----------

After this function is called, no further operations are
allowed on the object without opening a new control session.

.. _`dprtc_close.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_set_freq_compensation`:

dprtc_set_freq_compensation
===========================

.. c:function:: int dprtc_set_freq_compensation(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u32 freq_compensation)

    Sets a new frequency compensation value.

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPRTC object
    :type token: u16

    :param freq_compensation:
        The new frequency compensation value to set.
    :type freq_compensation: u32

.. _`dprtc_set_freq_compensation.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_get_freq_compensation`:

dprtc_get_freq_compensation
===========================

.. c:function:: int dprtc_get_freq_compensation(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u32 *freq_compensation)

    Retrieves the frequency compensation value

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPRTC object
    :type token: u16

    :param freq_compensation:
        Frequency compensation value
    :type freq_compensation: u32 \*

.. _`dprtc_get_freq_compensation.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_get_time`:

dprtc_get_time
==============

.. c:function:: int dprtc_get_time(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, uint64_t *time)

    Returns the current RTC time.

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPRTC object
    :type token: u16

    :param time:
        Current RTC time.
    :type time: uint64_t \*

.. _`dprtc_get_time.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_set_time`:

dprtc_set_time
==============

.. c:function:: int dprtc_set_time(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, uint64_t time)

    Updates current RTC time.

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPRTC object
    :type token: u16

    :param time:
        New RTC time.
    :type time: uint64_t

.. _`dprtc_set_time.return`:

Return
------

'0' on Success; Error code otherwise.

.. This file was automatic generated / don't edit.

