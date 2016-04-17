.. -*- coding: utf-8; mode: rst -*-

=======
namei.h
=======


.. _`retry_estale`:

retry_estale
============

.. c:function:: bool retry_estale (const long error, const unsigned int flags)

    determine whether the caller should retry an operation

    :param const long error:
        the error that would currently be returned

    :param const unsigned int flags:
        flags being used for next lookup attempt



.. _`retry_estale.description`:

Description
-----------

Check to see if the error code was -ESTALE, and then determine whether
to retry the call based on whether "flags" already has LOOKUP_REVAL set.

Returns true if the caller should try the operation again.

