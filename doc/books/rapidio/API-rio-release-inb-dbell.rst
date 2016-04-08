
.. _API-rio-release-inb-dbell:

=====================
rio_release_inb_dbell
=====================

*man rio_release_inb_dbell(9)*

*4.6.0-rc1*

release inbound doorbell message service


Synopsis
========

.. c:function:: int rio_release_inb_dbell( struct rio_mport * mport, u16 start, u16 end )

Arguments
=========

``mport``
    RIO master port from which to release the doorbell resource

``start``
    Doorbell info range start

``end``
    Doorbell info range end


Description
===========

Releases ownership of an inbound doorbell resource and removes callback from the doorbell event list. Returns 0 if the request has been satisfied.
