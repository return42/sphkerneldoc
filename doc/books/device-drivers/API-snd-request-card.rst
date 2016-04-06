
.. _API-snd-request-card:

================
snd_request_card
================

*man snd_request_card(9)*

*4.6.0-rc1*

try to load the card module


Synopsis
========

.. c:function:: void snd_request_card( int card )

Arguments
=========

``card``
    the card number


Description
===========

Tries to load the module “snd-card-X” for the given card number via request_module. Returns immediately if already loaded.
