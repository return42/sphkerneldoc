.. -*- coding: utf-8; mode: rst -*-

=====
elm.h
=====


.. _`elm_errorvec`:

struct elm_errorvec
===================

.. c:type:: elm_errorvec

    error vector for elm


.. _`elm_errorvec.definition`:

Definition
----------

.. code-block:: c

  struct elm_errorvec {
    bool error_reported;
    bool error_uncorrectable;
    int error_count;
    int error_loc[16];
  };


.. _`elm_errorvec.members`:

Members
-------

:``error_reported``:
    set true for vectors error is reported

:``error_uncorrectable``:
    number of uncorrectable errors

:``error_count``:
    number of correctable errors in the sector

:``error_loc[16]``:
    buffer for error location


