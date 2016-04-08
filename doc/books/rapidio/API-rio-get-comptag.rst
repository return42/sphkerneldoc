
.. _API-rio-get-comptag:

===============
rio_get_comptag
===============

*man rio_get_comptag(9)*

*4.6.0-rc1*

Begin or continue searching for a RIO device by component tag


Synopsis
========

.. c:function:: struct rio_dev ⋆ rio_get_comptag( u32 comp_tag, struct rio_dev * from )

Arguments
=========

``comp_tag``
    RIO component tag to match

``from``
    Previous RIO device found in search, or ``NULL`` for new search


Description
===========

Iterates through the list of known RIO devices. If a RIO device is found with a matching ``comp_tag``, a pointer to its device structure is returned. Otherwise, ``NULL`` is
returned. A new search is initiated by passing ``NULL`` to the ``from`` argument. Otherwise, if ``from`` is not ``NULL``, searches continue from next device on the global list.
