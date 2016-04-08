
.. _API-rio-get-device:

==============
rio_get_device
==============

*man rio_get_device(9)*

*4.6.0-rc1*

Begin or continue searching for a RIO device by vid/did


Synopsis
========

.. c:function:: struct rio_dev ⋆ rio_get_device( u16 vid, u16 did, struct rio_dev * from )

Arguments
=========

``vid``
    RIO vid to match or ``RIO_ANY_ID`` to match all vids

``did``
    RIO did to match or ``RIO_ANY_ID`` to match all dids

``from``
    Previous RIO device found in search, or ``NULL`` for new search


Description
===========

Iterates through the list of known RIO devices. If a RIO device is found with a matching ``vid`` and ``did``, the reference count to the device is incrememted and a pointer to its
device structure is returned. Otherwise, ``NULL`` is returned. A new search is initiated by passing ``NULL`` to the ``from`` argument. Otherwise, if ``from`` is not ``NULL``,
searches continue from next device on the global list. The reference count for ``from`` is always decremented if it is not ``NULL``.
