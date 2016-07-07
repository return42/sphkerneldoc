.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/broadcom/bnx2x/bnx2x_sp.h

.. _`bnx2x_config_rx_mode`:

bnx2x_config_rx_mode
====================

.. c:function:: int bnx2x_config_rx_mode(struct bnx2x *bp, struct bnx2x_rx_mode_ramrod_params *p)

    Send and RX_MODE ramrod according to the provided parameters.

    :param struct bnx2x \*bp:
        *undescribed*

    :param struct bnx2x_rx_mode_ramrod_params \*p:
        Command parameters

.. _`bnx2x_config_rx_mode.return`:

Return
------

0 - if operation was successful and there is no pending completions,
positive number - if there are pending completions,
negative - if there were errors

.. _`bnx2x_config_mcast`:

bnx2x_config_mcast
==================

.. c:function:: int bnx2x_config_mcast(struct bnx2x *bp, struct bnx2x_mcast_ramrod_params *p, enum bnx2x_mcast_cmd cmd)

    Configure multicast MACs list.

    :param struct bnx2x \*bp:
        *undescribed*

    :param struct bnx2x_mcast_ramrod_params \*p:
        *undescribed*

    :param enum bnx2x_mcast_cmd cmd:
        command to execute: BNX2X_MCAST_CMD_X

.. _`bnx2x_config_mcast.description`:

Description
-----------

May configure a new list
provided in p->mcast_list (BNX2X_MCAST_CMD_ADD), clean up
(BNX2X_MCAST_CMD_DEL) or restore (BNX2X_MCAST_CMD_RESTORE) a current
configuration, continue to execute the pending commands
(BNX2X_MCAST_CMD_CONT).

If previous command is still pending or if number of MACs to
configure is more that maximum number of MACs in one command,
the current command will be enqueued to the tail of the
pending commands list.

.. _`bnx2x_config_mcast.return`:

Return
------

0 is operation was successful and there are no pending completions,
negative if there were errors, positive if there are pending
completions.

.. _`bnx2x_config_rss`:

bnx2x_config_rss
================

.. c:function:: int bnx2x_config_rss(struct bnx2x *bp, struct bnx2x_config_rss_params *p)

    Updates RSS configuration according to provided parameters

    :param struct bnx2x \*bp:
        *undescribed*

    :param struct bnx2x_config_rss_params \*p:
        *undescribed*

.. _`bnx2x_config_rss.return`:

Return
------

0 in case of success

.. _`bnx2x_get_rss_ind_table`:

bnx2x_get_rss_ind_table
=======================

.. c:function:: void bnx2x_get_rss_ind_table(struct bnx2x_rss_config_obj *rss_obj, u8 *ind_table)

    Return the current ind_table configuration.

    :param struct bnx2x_rss_config_obj \*rss_obj:
        *undescribed*

    :param u8 \*ind_table:
        buffer to fill with the current indirection
        table content. Should be at least
        T_ETH_INDIRECTION_TABLE_SIZE bytes long.

.. This file was automatic generated / don't edit.

