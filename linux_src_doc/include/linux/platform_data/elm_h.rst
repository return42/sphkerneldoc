.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/elm.h

.. _`elm_errorvec`:

struct elm_errorvec
===================

.. c:type:: struct elm_errorvec

    error vector for elm

.. _`elm_errorvec.definition`:

Definition
----------

.. code-block:: c

    struct elm_errorvec {
        bool error_reported;
        bool error_uncorrectable;
        int error_count;
        int error_loc;
    }

.. _`elm_errorvec.members`:

Members
-------

error_reported
    set true for vectors error is reported

error_uncorrectable
    number of uncorrectable errors

error_count
    number of correctable errors in the sector

error_loc
    buffer for error location

.. This file was automatic generated / don't edit.

