.. -*- coding: utf-8; mode: rst -*-

======
main.c
======


.. _`lbtf_setup_firmware`:

lbtf_setup_firmware
===================

.. c:function:: int lbtf_setup_firmware (struct lbtf_private *priv)

    :param struct lbtf_private \*priv:

        *undescribed*



.. _`lbtf_setup_firmware.description`:

Description
-----------


``priv``    A pointer to struct lbtf_private structure



.. _`lbtf_setup_firmware.returns`:

Returns
-------

0 on success.



.. _`command_timer_fn`:

command_timer_fn
================

.. c:function:: void command_timer_fn (unsigned long data)

    :param unsigned long data:

        *undescribed*



.. _`command_timer_fn.description`:

Description
-----------

It will re-send the same command again.



.. _`lbtf_add_card`:

lbtf_add_card
=============

.. c:function:: struct lbtf_private *lbtf_add_card (void *card, struct device *dmdev)

    :param void \*card:

        *undescribed*

    :param struct device \*dmdev:

        *undescribed*



.. _`lbtf_add_card.description`:

Description
-----------


``card``    A pointer to card



.. _`lbtf_add_card.returns`:

Returns
-------

pointer to struct lbtf_priv.

