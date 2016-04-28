.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2--journal-start:

===================
jbd2__journal_start
===================

*man jbd2__journal_start(9)*

*4.6.0-rc5*

Obtain a new handle.


Synopsis
========

.. c:function:: handle_t * jbd2__journal_start( journal_t * journal, int nblocks, int rsv_blocks, gfp_t gfp_mask, unsigned int type, unsigned int line_no )

Arguments
=========

``journal``
    Journal to start transaction on.

``nblocks``
    number of block buffer we might modify

``rsv_blocks``
    -- undescribed --

``gfp_mask``
    -- undescribed --

``type``
    -- undescribed --

``line_no``
    -- undescribed --


Description
===========

We make sure that the transaction can guarantee at least nblocks of
modified buffers in the log. We block until the log can guarantee that
much space. Additionally, if rsv_blocks > 0, we also create another
handle with rsv_blocks reserved blocks in the journal. This handle is
is stored in h_rsv_handle. It is not attached to any particular
transaction and thus doesn't block transaction commit. If the caller
uses this reserved handle, it has to set h_rsv_handle to NULL as
otherwise ``jbd2_journal_stop`` on the parent handle will dispose the
reserved one. Reserved handle has to be converted to a normal handle
using ``jbd2_journal_start_reserved`` before it can be used.

Return a pointer to a newly allocated handle, or an ``ERR_PTR`` value on
failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
