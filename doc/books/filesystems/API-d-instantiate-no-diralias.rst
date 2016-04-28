.. -*- coding: utf-8; mode: rst -*-

.. _API-d-instantiate-no-diralias:

=========================
d_instantiate_no_diralias
=========================

*man d_instantiate_no_diralias(9)*

*4.6.0-rc5*

instantiate a non-aliased dentry


Synopsis
========

.. c:function:: int d_instantiate_no_diralias( struct dentry * entry, struct inode * inode )

Arguments
=========

``entry``
    dentry to complete

``inode``
    inode to attach to this dentry


Description
===========

Fill in inode information in the entry. If a directory alias is found,
then return an error (and drop inode). Together with
``d_materialise_unique`` this guarantees that a directory inode may
never have more than one alias.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
