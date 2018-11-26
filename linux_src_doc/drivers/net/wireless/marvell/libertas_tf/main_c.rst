.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/marvell/libertas_tf/main.c

.. _`lbtf_setup_firmware`:

lbtf_setup_firmware
===================

.. c:function:: int lbtf_setup_firmware(struct lbtf_private *priv)

    initialize firmware.

    :param priv:
        *undescribed*
    :type priv: struct lbtf_private \*

.. _`lbtf_setup_firmware.description`:

Description
-----------

\ ``priv``\     A pointer to struct lbtf_private structure

.. _`lbtf_setup_firmware.return`:

Return
------

0 on success.

.. _`command_timer_fn`:

command_timer_fn
================

.. c:function:: void command_timer_fn(struct timer_list *t)

    It will re-send the same command again.

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`lbtf_add_card`:

lbtf_add_card
=============

.. c:function:: struct lbtf_private *lbtf_add_card(void *card, struct device *dmdev)

    Add and initialize the card, no fw upload yet.

    :param card:
        *undescribed*
    :type card: void \*

    :param dmdev:
        *undescribed*
    :type dmdev: struct device \*

.. _`lbtf_add_card.description`:

Description
-----------

\ ``card``\     A pointer to card

.. _`lbtf_add_card.return`:

Return
------

pointer to struct lbtf_priv.

.. This file was automatic generated / don't edit.

