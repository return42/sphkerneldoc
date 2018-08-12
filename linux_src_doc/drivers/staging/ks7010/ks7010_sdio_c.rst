.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/ks7010/ks7010_sdio.c

.. _`ks_sdio_card`:

struct ks_sdio_card
===================

.. c:type:: struct ks_sdio_card

    SDIO device data.

.. _`ks_sdio_card.definition`:

Definition
----------

.. code-block:: c

    struct ks_sdio_card {
        struct sdio_func *func;
        struct ks_wlan_private *priv;
    }

.. _`ks_sdio_card.members`:

Members
-------

func
    Pointer to the SDIO function device.

priv
    Pointer to the \ :c:type:`struct net_device <net_device>`\  private data.

.. _`ks_sdio_card.description`:

Description
-----------

Structure is used as the \ :c:type:`struct sdio_func <sdio_func>`\  private data.

.. This file was automatic generated / don't edit.

