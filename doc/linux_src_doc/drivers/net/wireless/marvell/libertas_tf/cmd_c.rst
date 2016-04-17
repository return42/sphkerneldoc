.. -*- coding: utf-8; mode: rst -*-

=====
cmd.c
=====


.. _`lbtf_cmd_copyback`:

lbtf_cmd_copyback
=================

.. c:function:: int lbtf_cmd_copyback (struct lbtf_private *priv, unsigned long extra, struct cmd_header *resp)

    Simple callback that copies response back into command

    :param struct lbtf_private \*priv:

        *undescribed*

    :param unsigned long extra:

        *undescribed*

    :param struct cmd_header \*resp:

        *undescribed*



.. _`lbtf_cmd_copyback.description`:

Description
-----------


``priv``        A pointer to struct lbtf_private structure
``extra``        A pointer to the original command structure for which
'resp' is a response

``resp``        A pointer to the command response



.. _`lbtf_cmd_copyback.returns`:

Returns
-------

0 on success, error on failure



.. _`lbtf_update_hw_spec`:

lbtf_update_hw_spec
===================

.. c:function:: int lbtf_update_hw_spec (struct lbtf_private *priv)

    :param struct lbtf_private \*priv:

        *undescribed*



.. _`lbtf_update_hw_spec.description`:

Description
-----------


``priv``            A pointer to struct lbtf_private structure



.. _`lbtf_update_hw_spec.returns`:

Returns
-------

0 on success, error on failure



.. _`lbtf_set_channel`:

lbtf_set_channel
================

.. c:function:: int lbtf_set_channel (struct lbtf_private *priv, u8 channel)

    :param struct lbtf_private \*priv:

        *undescribed*

    :param u8 channel:

        *undescribed*



.. _`lbtf_set_channel.description`:

Description
-----------


``priv``        A pointer to struct lbtf_private structure
``channel``        The desired channel, or 0 to clear a locked channel



.. _`lbtf_set_channel.returns`:

Returns
-------

0 on success, error on failure



.. _`__lbtf_cleanup_and_insert_cmd`:

__lbtf_cleanup_and_insert_cmd
=============================

.. c:function:: void __lbtf_cleanup_and_insert_cmd (struct lbtf_private *priv, struct cmd_ctrl_node *cmdnode)

    :param struct lbtf_private \*priv:

        *undescribed*

    :param struct cmd_ctrl_node \*cmdnode:

        *undescribed*



.. _`__lbtf_cleanup_and_insert_cmd.description`:

Description
-----------

after cleans it. Requires priv->driver_lock held.



.. _`lbtf_allocate_cmd_buffer`:

lbtf_allocate_cmd_buffer
========================

.. c:function:: int lbtf_allocate_cmd_buffer (struct lbtf_private *priv)

    Allocates cmd buffer, links it to free cmd queue

    :param struct lbtf_private \*priv:

        *undescribed*



.. _`lbtf_allocate_cmd_buffer.description`:

Description
-----------


``priv``        A pointer to struct lbtf_private structure



.. _`lbtf_allocate_cmd_buffer.returns`:

Returns
-------

0 on success.



.. _`lbtf_free_cmd_buffer`:

lbtf_free_cmd_buffer
====================

.. c:function:: int lbtf_free_cmd_buffer (struct lbtf_private *priv)

    Frees the cmd buffer.

    :param struct lbtf_private \*priv:

        *undescribed*



.. _`lbtf_free_cmd_buffer.description`:

Description
-----------


``priv``        A pointer to struct lbtf_private structure



.. _`lbtf_free_cmd_buffer.returns`:

Returns
-------





.. _`lbtf_get_cmd_ctrl_node`:

lbtf_get_cmd_ctrl_node
======================

.. c:function:: struct cmd_ctrl_node *lbtf_get_cmd_ctrl_node (struct lbtf_private *priv)

    Gets free cmd node from free cmd queue.

    :param struct lbtf_private \*priv:

        *undescribed*



.. _`lbtf_get_cmd_ctrl_node.description`:

Description
-----------


``priv``                A pointer to struct lbtf_private structure



.. _`lbtf_get_cmd_ctrl_node.returns`:

Returns
-------

pointer to a struct cmd_ctrl_node or NULL if none available.



.. _`lbtf_execute_next_command`:

lbtf_execute_next_command
=========================

.. c:function:: int lbtf_execute_next_command (struct lbtf_private *priv)

    :param struct lbtf_private \*priv:

        *undescribed*



.. _`lbtf_execute_next_command.description`:

Description
-----------


``priv``     A pointer to struct lbtf_private structure



.. _`lbtf_execute_next_command.returns`:

Returns
-------

0 on success.

