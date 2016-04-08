
.. _API-wiphy-dev:

=========
wiphy_dev
=========

*man wiphy_dev(9)*

*4.6.0-rc1*

get wiphy dev pointer


Synopsis
========

.. c:function:: struct device ⋆ wiphy_dev( struct wiphy * wiphy )

Arguments
=========

``wiphy``
    The wiphy whose device struct to look up


Return
======

The dev of ``wiphy``.
