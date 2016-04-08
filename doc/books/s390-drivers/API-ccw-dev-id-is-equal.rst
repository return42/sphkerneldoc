
.. _API-ccw-dev-id-is-equal:

===================
ccw_dev_id_is_equal
===================

*man ccw_dev_id_is_equal(9)*

*4.6.0-rc1*

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
