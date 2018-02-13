.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/blk_types.h

.. _`blk_path_error`:

blk_path_error
==============

.. c:function:: bool blk_path_error(blk_status_t error)

    returns true if error may be path related

    :param blk_status_t error:
        status the request was completed with

.. _`blk_path_error.description`:

Description
-----------

This classifies block error status into non-retryable errors and ones
that may be successful if retried on a failover path.

.. _`blk_path_error.return`:

Return
------

\ ``false``\  - retrying failover path will not help
\ ``true``\   - may succeed if retried

.. This file was automatic generated / don't edit.

