.. -*- coding: utf-8; mode: rst -*-

.. _API-ccw-dev-id-is-equal:

===================
ccw_dev_id_is_equal
===================

*man ccw_dev_id_is_equal(9)*

*4.6.0-rc5*

compare two ccw_dev_ids


Synopsis
========

.. c:function:: int ccw_dev_id_is_equal( struct ccw_dev_id * dev_id1, struct ccw_dev_id * dev_id2 )

Arguments
=========

``dev_id1``
    a ccw_dev_id

``dev_id2``
    another ccw_dev_id


Returns
=======

``1`` if the two structures are equal field-by-field, ``0`` if not.


Context
=======

any


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
