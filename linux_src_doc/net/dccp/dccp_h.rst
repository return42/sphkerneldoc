.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/dccp.h

.. _`dccp_loss_count`:

dccp_loss_count
===============

.. c:function:: u64 dccp_loss_count(const u64 s1, const u64 s2, const u64 ndp)

    Approximate the number of lost data packets in a burst loss

    :param const u64 s1:
        last known sequence number before the loss ('hole')

    :param const u64 s2:
        first sequence number seen after the 'hole'

    :param const u64 ndp:
        NDP count on packet with sequence number \ ``s2``\ 

.. _`dccp_loss_free`:

dccp_loss_free
==============

.. c:function:: bool dccp_loss_free(const u64 s1, const u64 s2, const u64 ndp)

    Evaluate condition for data loss from RFC 4340, 7.7.1

    :param const u64 s1:
        *undescribed*

    :param const u64 s2:
        *undescribed*

    :param const u64 ndp:
        *undescribed*

.. This file was automatic generated / don't edit.

