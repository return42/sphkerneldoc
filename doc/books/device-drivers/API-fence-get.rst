.. -*- coding: utf-8; mode: rst -*-

.. _API-fence-get:

=========
fence_get
=========

*man fence_get(9)*

*4.6.0-rc5*

increases refcount of the fence


Synopsis
========

.. c:function:: struct fence * fence_get( struct fence * fence )

Arguments
=========

``fence``
    [in] fence to increase refcount of


Description
===========

Returns the same fence, with refcount increased by 1.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
