.. -*- coding: utf-8; mode: rst -*-

.. _API-wiphy-priv:

==========
wiphy_priv
==========

*man wiphy_priv(9)*

*4.6.0-rc5*

return priv from wiphy


Synopsis
========

.. c:function:: void * wiphy_priv( struct wiphy * wiphy )

Arguments
=========

``wiphy``
    the wiphy whose priv pointer to return


Return
======

The priv of ``wiphy``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
