.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-get-asm:

===========
rio_get_asm
===========

*man rio_get_asm(9)*

*4.6.0-rc5*

Begin or continue searching for a RIO device by
vid/did/asm_vid/asm_did


Synopsis
========

.. c:function:: struct rio_dev * rio_get_asm( u16 vid, u16 did, u16 asm_vid, u16 asm_did, struct rio_dev * from )

Arguments
=========

``vid``
    RIO vid to match or ``RIO_ANY_ID`` to match all vids

``did``
    RIO did to match or ``RIO_ANY_ID`` to match all dids

``asm_vid``
    RIO asm_vid to match or ``RIO_ANY_ID`` to match all asm_vids

``asm_did``
    RIO asm_did to match or ``RIO_ANY_ID`` to match all asm_dids

``from``
    Previous RIO device found in search, or ``NULL`` for new search


Description
===========

Iterates through the list of known RIO devices. If a RIO device is found
with a matching ``vid``, ``did``, ``asm_vid``, ``asm_did``, the
reference count to the device is incrememted and a pointer to its device
structure is returned. Otherwise, ``NULL`` is returned. A new search is
initiated by passing ``NULL`` to the ``from`` argument. Otherwise, if
``from`` is not ``NULL``, searches continue from next device on the
global list. The reference count for ``from`` is always decremented if
it is not ``NULL``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
