
.. _API-pnp-request-card-device:

=======================
pnp_request_card_device
=======================

*man pnp_request_card_device(9)*

*4.6.0-rc1*

Searches for a PnP device under the specified card


Synopsis
========

.. c:function:: struct pnp_dev ⋆ pnp_request_card_device( struct pnp_card_link * clink, const char * id, struct pnp_dev * from )

Arguments
=========

``clink``
    pointer to the card link, cannot be NULL

``id``
    pointer to a PnP ID structure that explains the rules for finding the device

``from``
    Starting place to search from. If NULL it will start from the beginning.
