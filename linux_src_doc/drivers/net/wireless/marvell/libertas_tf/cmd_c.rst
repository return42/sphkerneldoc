.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/marvell/libertas_tf/cmd.c

.. _`lbtf_cmd_copyback`:

lbtf_cmd_copyback
=================

.. c:function:: int lbtf_cmd_copyback(struct lbtf_private *priv, unsigned long extra, struct cmd_header *resp)

    Simple callback that copies response back into command

    :param priv:
        *undescribed*
    :type priv: struct lbtf_private \*

    :param extra:
        *undescribed*
    :type extra: unsigned long

    :param resp:
        *undescribed*
    :type resp: struct cmd_header \*

.. _`lbtf_cmd_copyback.description`:

Description
-----------

\ ``priv``\        A pointer to struct lbtf_private structure
\ ``extra``\       A pointer to the original command structure for which
'resp' is a response
\ ``resp``\        A pointer to the command response

.. _`lbtf_cmd_copyback.return`:

Return
------

0 on success, error on failure

.. _`lbtf_update_hw_spec`:

lbtf_update_hw_spec
===================

.. c:function:: int lbtf_update_hw_spec(struct lbtf_private *priv)

    Updates the hardware details.

    :param priv:
        *undescribed*
    :type priv: struct lbtf_private \*

.. _`lbtf_update_hw_spec.description`:

Description
-----------

\ ``priv``\        A pointer to struct lbtf_private structure

.. _`lbtf_update_hw_spec.return`:

Return
------

0 on success, error on failure

.. _`lbtf_set_channel`:

lbtf_set_channel
================

.. c:function:: int lbtf_set_channel(struct lbtf_private *priv, u8 channel)

    Set the radio channel

    :param priv:
        *undescribed*
    :type priv: struct lbtf_private \*

    :param channel:
        *undescribed*
    :type channel: u8

.. _`lbtf_set_channel.description`:

Description
-----------

\ ``priv``\        A pointer to struct lbtf_private structure
\ ``channel``\     The desired channel, or 0 to clear a locked channel

.. _`lbtf_set_channel.return`:

Return
------

0 on success, error on failure

.. _`__lbtf_cleanup_and_insert_cmd`:

\__lbtf_cleanup_and_insert_cmd
==============================

.. c:function:: void __lbtf_cleanup_and_insert_cmd(struct lbtf_private *priv, struct cmd_ctrl_node *cmdnode)

    after cleans it. Requires priv->driver_lock held.

    :param priv:
        *undescribed*
    :type priv: struct lbtf_private \*

    :param cmdnode:
        *undescribed*
    :type cmdnode: struct cmd_ctrl_node \*

.. _`lbtf_allocate_cmd_buffer`:

lbtf_allocate_cmd_buffer
========================

.. c:function:: int lbtf_allocate_cmd_buffer(struct lbtf_private *priv)

    Allocates cmd buffer, links it to free cmd queue

    :param priv:
        *undescribed*
    :type priv: struct lbtf_private \*

.. _`lbtf_allocate_cmd_buffer.description`:

Description
-----------

\ ``priv``\        A pointer to struct lbtf_private structure

.. _`lbtf_allocate_cmd_buffer.return`:

Return
------

0 on success.

.. _`lbtf_free_cmd_buffer`:

lbtf_free_cmd_buffer
====================

.. c:function:: int lbtf_free_cmd_buffer(struct lbtf_private *priv)

    Frees the cmd buffer.

    :param priv:
        *undescribed*
    :type priv: struct lbtf_private \*

.. _`lbtf_free_cmd_buffer.description`:

Description
-----------

\ ``priv``\        A pointer to struct lbtf_private structure

.. _`lbtf_free_cmd_buffer.return`:

Return
------

0

.. _`lbtf_get_cmd_ctrl_node`:

lbtf_get_cmd_ctrl_node
======================

.. c:function:: struct cmd_ctrl_node *lbtf_get_cmd_ctrl_node(struct lbtf_private *priv)

    Gets free cmd node from free cmd queue.

    :param priv:
        *undescribed*
    :type priv: struct lbtf_private \*

.. _`lbtf_get_cmd_ctrl_node.description`:

Description
-----------

\ ``priv``\                A pointer to struct lbtf_private structure

.. _`lbtf_get_cmd_ctrl_node.return`:

Return
------

pointer to a struct cmd_ctrl_node or NULL if none available.

.. _`lbtf_execute_next_command`:

lbtf_execute_next_command
=========================

.. c:function:: int lbtf_execute_next_command(struct lbtf_private *priv)

    execute next command in cmd pending queue.

    :param priv:
        *undescribed*
    :type priv: struct lbtf_private \*

.. _`lbtf_execute_next_command.description`:

Description
-----------

\ ``priv``\      A pointer to struct lbtf_private structure

.. _`lbtf_execute_next_command.return`:

Return
------

0 on success.

.. This file was automatic generated / don't edit.

