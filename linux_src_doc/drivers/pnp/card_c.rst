.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pnp/card.c

.. _`pnp_add_card_id`:

pnp_add_card_id
===============

.. c:function:: struct pnp_id *pnp_add_card_id(struct pnp_card *card, char *id)

    adds an EISA id to the specified card

    :param card:
        pointer to the desired card
    :type card: struct pnp_card \*

    :param id:
        pointer to a pnp_id structure
    :type id: char \*

.. _`pnp_add_card`:

pnp_add_card
============

.. c:function:: int pnp_add_card(struct pnp_card *card)

    adds a PnP card to the PnP Layer

    :param card:
        pointer to the card to add
    :type card: struct pnp_card \*

.. _`pnp_remove_card`:

pnp_remove_card
===============

.. c:function:: void pnp_remove_card(struct pnp_card *card)

    removes a PnP card from the PnP Layer

    :param card:
        pointer to the card to remove
    :type card: struct pnp_card \*

.. _`pnp_add_card_device`:

pnp_add_card_device
===================

.. c:function:: int pnp_add_card_device(struct pnp_card *card, struct pnp_dev *dev)

    adds a device to the specified card

    :param card:
        pointer to the card to add to
    :type card: struct pnp_card \*

    :param dev:
        pointer to the device to add
    :type dev: struct pnp_dev \*

.. _`pnp_remove_card_device`:

pnp_remove_card_device
======================

.. c:function:: void pnp_remove_card_device(struct pnp_dev *dev)

    removes a device from the specified card

    :param dev:
        pointer to the device to remove
    :type dev: struct pnp_dev \*

.. _`pnp_request_card_device`:

pnp_request_card_device
=======================

.. c:function:: struct pnp_dev *pnp_request_card_device(struct pnp_card_link *clink, const char *id, struct pnp_dev *from)

    Searches for a PnP device under the specified card

    :param clink:
        pointer to the card link, cannot be NULL
    :type clink: struct pnp_card_link \*

    :param id:
        pointer to a PnP ID structure that explains the rules for finding the device
    :type id: const char \*

    :param from:
        Starting place to search from. If NULL it will start from the beginning.
    :type from: struct pnp_dev \*

.. _`pnp_release_card_device`:

pnp_release_card_device
=======================

.. c:function:: void pnp_release_card_device(struct pnp_dev *dev)

    call this when the driver no longer needs the device

    :param dev:
        pointer to the PnP device structure
    :type dev: struct pnp_dev \*

.. _`pnp_register_card_driver`:

pnp_register_card_driver
========================

.. c:function:: int pnp_register_card_driver(struct pnp_card_driver *drv)

    registers a PnP card driver with the PnP Layer

    :param drv:
        pointer to the driver to register
    :type drv: struct pnp_card_driver \*

.. _`pnp_unregister_card_driver`:

pnp_unregister_card_driver
==========================

.. c:function:: void pnp_unregister_card_driver(struct pnp_card_driver *drv)

    unregisters a PnP card driver from the PnP Layer

    :param drv:
        pointer to the driver to unregister
    :type drv: struct pnp_card_driver \*

.. This file was automatic generated / don't edit.

