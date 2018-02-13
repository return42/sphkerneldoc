.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/log.c

.. _`batadv_debug_log`:

batadv_debug_log
================

.. c:function:: int batadv_debug_log(struct batadv_priv *bat_priv, const char *fmt,  ...)

    Add debug log entry

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param const char \*fmt:
        format string

    :param ellipsis ellipsis:
        variable arguments

.. _`batadv_debug_log.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_debug_log_setup`:

batadv_debug_log_setup
======================

.. c:function:: int batadv_debug_log_setup(struct batadv_priv *bat_priv)

    Initialize debug log

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_debug_log_setup.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_debug_log_cleanup`:

batadv_debug_log_cleanup
========================

.. c:function:: void batadv_debug_log_cleanup(struct batadv_priv *bat_priv)

    Destroy debug log

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

.. This file was automatic generated / don't edit.

