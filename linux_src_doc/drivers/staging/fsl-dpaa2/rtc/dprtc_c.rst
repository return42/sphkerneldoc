.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-dpaa2/rtc/dprtc.c

.. _`dprtc_open`:

dprtc_open
==========

.. c:function:: int dprtc_open(struct fsl_mc_io *mc_io, u32 cmd_flags, int dprtc_id, u16 *token)

    Open a control session for the specified object.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param int dprtc_id:
        DPRTC unique ID

    :param u16 \*token:
        Returned token; use in subsequent API calls

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

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRTC object

.. _`dprtc_close.description`:

Description
-----------

After this function is called, no further operations are
allowed on the object without opening a new control session.

.. _`dprtc_close.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_create`:

dprtc_create
============

.. c:function:: int dprtc_create(struct fsl_mc_io *mc_io, u16 dprc_token, u32 cmd_flags, const struct dprtc_cfg *cfg, u32 *obj_id)

    Create the DPRTC object.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u16 dprc_token:
        Parent container token; '0' for default container

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param const struct dprtc_cfg \*cfg:
        Configuration structure

    :param u32 \*obj_id:
        Returned object id

.. _`dprtc_create.description`:

Description
-----------

Create the DPRTC object, allocate required resources and
perform required initialization.

The function accepts an authentication token of a parent
container that this object should be assigned to. The token
can be '0' so the object will be assigned to the default container.
The newly created object can be opened with the returned
object id and using the container's associated tokens and MC portals.

.. _`dprtc_create.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_destroy`:

dprtc_destroy
=============

.. c:function:: int dprtc_destroy(struct fsl_mc_io *mc_io, u16 dprc_token, u32 cmd_flags, u32 object_id)

    Destroy the DPRTC object and release all its resources.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u16 dprc_token:
        Parent container token; '0' for default container

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u32 object_id:
        The object id; it must be a valid id within the container that
        created this object;

.. _`dprtc_destroy.description`:

Description
-----------

The function accepts the authentication token of the parent container that
created the object (not the one that currently owns the object). The object
is searched within parent using the provided 'object_id'.
All tokens to the object must be closed before calling destroy.

.. _`dprtc_destroy.return`:

Return
------

'0' on Success; error code otherwise.

.. _`dprtc_enable`:

dprtc_enable
============

.. c:function:: int dprtc_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Enable the DPRTC.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRTC object

.. _`dprtc_enable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_disable`:

dprtc_disable
=============

.. c:function:: int dprtc_disable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Disable the DPRTC.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRTC object

.. _`dprtc_disable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_is_enabled`:

dprtc_is_enabled
================

.. c:function:: int dprtc_is_enabled(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int *en)

    Check if the DPRTC is enabled.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRTC object

    :param int \*en:
        Returns '1' if object is enabled; '0' otherwise

.. _`dprtc_is_enabled.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_reset`:

dprtc_reset
===========

.. c:function:: int dprtc_reset(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Reset the DPRTC, returns the object to initial state.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRTC object

.. _`dprtc_reset.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_set_irq_enable`:

dprtc_set_irq_enable
====================

.. c:function:: int dprtc_set_irq_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u8 en)

    Set overall interrupt state.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRTC object

    :param u8 irq_index:
        The interrupt index to configure

    :param u8 en:
        Interrupt state - enable = 1, disable = 0

.. _`dprtc_set_irq_enable.description`:

Description
-----------

Allows GPP software to control when interrupts are generated.
Each interrupt can have up to 32 causes.  The enable/disable control's the
overall interrupt state. if the interrupt is disabled no causes will cause
an interrupt.

.. _`dprtc_set_irq_enable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_get_irq_enable`:

dprtc_get_irq_enable
====================

.. c:function:: int dprtc_get_irq_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u8 *en)

    Get overall interrupt state

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRTC object

    :param u8 irq_index:
        The interrupt index to configure

    :param u8 \*en:
        Returned interrupt state - enable = 1, disable = 0

.. _`dprtc_get_irq_enable.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_set_irq_mask`:

dprtc_set_irq_mask
==================

.. c:function:: int dprtc_set_irq_mask(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 mask)

    Set interrupt mask.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRTC object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 mask:
        Event mask to trigger interrupt;
        each bit:
        0 = ignore event
        1 = consider event for asserting IRQ

.. _`dprtc_set_irq_mask.description`:

Description
-----------

Every interrupt can have up to 32 causes and the interrupt model supports
masking/unmasking each cause independently

.. _`dprtc_set_irq_mask.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_get_irq_mask`:

dprtc_get_irq_mask
==================

.. c:function:: int dprtc_get_irq_mask(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 *mask)

    Get interrupt mask.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRTC object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 \*mask:
        Returned event mask to trigger interrupt

.. _`dprtc_get_irq_mask.description`:

Description
-----------

Every interrupt can have up to 32 causes and the interrupt model supports
masking/unmasking each cause independently

.. _`dprtc_get_irq_mask.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_get_irq_status`:

dprtc_get_irq_status
====================

.. c:function:: int dprtc_get_irq_status(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 *status)

    Get the current status of any pending interrupts.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRTC object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 \*status:
        Returned interrupts status - one bit per cause:
        0 = no interrupt pending
        1 = interrupt pending

.. _`dprtc_get_irq_status.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_clear_irq_status`:

dprtc_clear_irq_status
======================

.. c:function:: int dprtc_clear_irq_status(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 irq_index, u32 status)

    Clear a pending interrupt's status

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRTC object

    :param u8 irq_index:
        The interrupt index to configure

    :param u32 status:
        Bits to clear (W1C) - one bit per cause:
        0 = don't change
        1 = clear status bit

.. _`dprtc_clear_irq_status.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_get_attributes`:

dprtc_get_attributes
====================

.. c:function:: int dprtc_get_attributes(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dprtc_attr *attr)

    Retrieve DPRTC attributes.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRTC object

    :param struct dprtc_attr \*attr:
        Returned object's attributes

.. _`dprtc_get_attributes.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_set_clock_offset`:

dprtc_set_clock_offset
======================

.. c:function:: int dprtc_set_clock_offset(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int64_t offset)

    Sets the clock's offset (usually relative to another clock).

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRTC object

    :param int64_t offset:
        New clock offset (in nanoseconds).

.. _`dprtc_set_clock_offset.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_set_freq_compensation`:

dprtc_set_freq_compensation
===========================

.. c:function:: int dprtc_set_freq_compensation(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u32 freq_compensation)

    Sets a new frequency compensation value.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRTC object

    :param u32 freq_compensation:
        The new frequency compensation value to set.

.. _`dprtc_set_freq_compensation.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_get_freq_compensation`:

dprtc_get_freq_compensation
===========================

.. c:function:: int dprtc_get_freq_compensation(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u32 *freq_compensation)

    Retrieves the frequency compensation value

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRTC object

    :param u32 \*freq_compensation:
        Frequency compensation value

.. _`dprtc_get_freq_compensation.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_get_time`:

dprtc_get_time
==============

.. c:function:: int dprtc_get_time(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, uint64_t *time)

    Returns the current RTC time.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRTC object

    :param uint64_t \*time:
        Current RTC time.

.. _`dprtc_get_time.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_set_time`:

dprtc_set_time
==============

.. c:function:: int dprtc_set_time(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, uint64_t time)

    Updates current RTC time.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRTC object

    :param uint64_t time:
        New RTC time.

.. _`dprtc_set_time.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_set_alarm`:

dprtc_set_alarm
===============

.. c:function:: int dprtc_set_alarm(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, uint64_t time)

    Defines and sets alarm.

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 token:
        Token of DPRTC object

    :param uint64_t time:
        In nanoseconds, the time when the alarm
        should go off - must be a multiple of
        1 microsecond

.. _`dprtc_set_alarm.return`:

Return
------

'0' on Success; Error code otherwise.

.. _`dprtc_get_api_version`:

dprtc_get_api_version
=====================

.. c:function:: int dprtc_get_api_version(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 *major_ver, u16 *minor_ver)

    Get Data Path Real Time Counter API version

    :param struct fsl_mc_io \*mc_io:
        Pointer to MC portal's I/O object

    :param u32 cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'

    :param u16 \*major_ver:
        Major version of data path real time counter API

    :param u16 \*minor_ver:
        Minor version of data path real time counter API

.. _`dprtc_get_api_version.return`:

Return
------

'0' on Success; Error code otherwise.

.. This file was automatic generated / don't edit.

