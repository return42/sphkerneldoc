.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/caam/dpseci.c

.. _`dpseci_open`:

dpseci_open
===========

.. c:function:: int dpseci_open(struct fsl_mc_io *mc_io, u32 cmd_flags, int dpseci_id, u16 *token)

    Open a control session for the specified object

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param dpseci_id:
        DPSECI unique ID
    :type dpseci_id: int

    :param token:
        Returned token; use in subsequent API calls
    :type token: u16 \*

.. _`dpseci_open.description`:

Description
-----------

This function can be used to open a control session for an already created
object; an object may have been declared statically in the DPL
or created dynamically.
This function returns a unique authentication token, associated with the
specific object ID and the specific MC portal; this token must be used in all
subsequent commands for this specific object.

.. _`dpseci_open.return`:

Return
------

'0' on success, error code otherwise

.. _`dpseci_close`:

dpseci_close
============

.. c:function:: int dpseci_close(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Close the control session of the object

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPSECI object
    :type token: u16

.. _`dpseci_close.description`:

Description
-----------

After this function is called, no further operations are allowed on the
object without opening a new control session.

.. _`dpseci_close.return`:

Return
------

'0' on success, error code otherwise

.. _`dpseci_enable`:

dpseci_enable
=============

.. c:function:: int dpseci_enable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Enable the DPSECI, allow sending and receiving frames

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPSECI object
    :type token: u16

.. _`dpseci_enable.return`:

Return
------

'0' on success, error code otherwise

.. _`dpseci_disable`:

dpseci_disable
==============

.. c:function:: int dpseci_disable(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token)

    Disable the DPSECI, stop sending and receiving frames

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPSECI object
    :type token: u16

.. _`dpseci_disable.return`:

Return
------

'0' on success, error code otherwise

.. _`dpseci_is_enabled`:

dpseci_is_enabled
=================

.. c:function:: int dpseci_is_enabled(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, int *en)

    Check if the DPSECI is enabled.

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPSECI object
    :type token: u16

    :param en:
        Returns '1' if object is enabled; '0' otherwise
    :type en: int \*

.. _`dpseci_is_enabled.return`:

Return
------

'0' on success, error code otherwise

.. _`dpseci_get_attributes`:

dpseci_get_attributes
=====================

.. c:function:: int dpseci_get_attributes(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dpseci_attr *attr)

    Retrieve DPSECI attributes

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPSECI object
    :type token: u16

    :param attr:
        Returned object's attributes
    :type attr: struct dpseci_attr \*

.. _`dpseci_get_attributes.return`:

Return
------

'0' on success, error code otherwise

.. _`dpseci_set_rx_queue`:

dpseci_set_rx_queue
===================

.. c:function:: int dpseci_set_rx_queue(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 queue, const struct dpseci_rx_queue_cfg *cfg)

    Set Rx queue configuration

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPSECI object
    :type token: u16

    :param queue:
        Select the queue relative to number of priorities configured at
        DPSECI creation; use DPSECI_ALL_QUEUES to configure all
        Rx queues identically.
    :type queue: u8

    :param cfg:
        Rx queue configuration
    :type cfg: const struct dpseci_rx_queue_cfg \*

.. _`dpseci_set_rx_queue.return`:

Return
------

'0' on success, error code otherwise

.. _`dpseci_get_rx_queue`:

dpseci_get_rx_queue
===================

.. c:function:: int dpseci_get_rx_queue(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 queue, struct dpseci_rx_queue_attr *attr)

    Retrieve Rx queue attributes

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPSECI object
    :type token: u16

    :param queue:
        Select the queue relative to number of priorities configured at
        DPSECI creation
    :type queue: u8

    :param attr:
        Returned Rx queue attributes
    :type attr: struct dpseci_rx_queue_attr \*

.. _`dpseci_get_rx_queue.return`:

Return
------

'0' on success, error code otherwise

.. _`dpseci_get_tx_queue`:

dpseci_get_tx_queue
===================

.. c:function:: int dpseci_get_tx_queue(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, u8 queue, struct dpseci_tx_queue_attr *attr)

    Retrieve Tx queue attributes

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPSECI object
    :type token: u16

    :param queue:
        Select the queue relative to number of priorities configured at
        DPSECI creation
    :type queue: u8

    :param attr:
        Returned Tx queue attributes
    :type attr: struct dpseci_tx_queue_attr \*

.. _`dpseci_get_tx_queue.return`:

Return
------

'0' on success, error code otherwise

.. _`dpseci_get_sec_attr`:

dpseci_get_sec_attr
===================

.. c:function:: int dpseci_get_sec_attr(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dpseci_sec_attr *attr)

    Retrieve SEC accelerator attributes

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPSECI object
    :type token: u16

    :param attr:
        Returned SEC attributes
    :type attr: struct dpseci_sec_attr \*

.. _`dpseci_get_sec_attr.return`:

Return
------

'0' on success, error code otherwise

.. _`dpseci_get_api_version`:

dpseci_get_api_version
======================

.. c:function:: int dpseci_get_api_version(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 *major_ver, u16 *minor_ver)

    Get Data Path SEC Interface API version

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param major_ver:
        Major version of data path sec API
    :type major_ver: u16 \*

    :param minor_ver:
        Minor version of data path sec API
    :type minor_ver: u16 \*

.. _`dpseci_get_api_version.return`:

Return
------

'0' on success, error code otherwise

.. _`dpseci_set_congestion_notification`:

dpseci_set_congestion_notification
==================================

.. c:function:: int dpseci_set_congestion_notification(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, const struct dpseci_congestion_notification_cfg *cfg)

    Set congestion group notification configuration

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPSECI object
    :type token: u16

    :param cfg:
        congestion notification configuration
    :type cfg: const struct dpseci_congestion_notification_cfg \*

.. _`dpseci_set_congestion_notification.return`:

Return
------

'0' on success, error code otherwise

.. _`dpseci_get_congestion_notification`:

dpseci_get_congestion_notification
==================================

.. c:function:: int dpseci_get_congestion_notification(struct fsl_mc_io *mc_io, u32 cmd_flags, u16 token, struct dpseci_congestion_notification_cfg *cfg)

    Get congestion group notification configuration

    :param mc_io:
        Pointer to MC portal's I/O object
    :type mc_io: struct fsl_mc_io \*

    :param cmd_flags:
        Command flags; one or more of 'MC_CMD_FLAG_'
    :type cmd_flags: u32

    :param token:
        Token of DPSECI object
    :type token: u16

    :param cfg:
        congestion notification configuration
    :type cfg: struct dpseci_congestion_notification_cfg \*

.. _`dpseci_get_congestion_notification.return`:

Return
------

'0' on success, error code otherwise

.. This file was automatic generated / don't edit.

