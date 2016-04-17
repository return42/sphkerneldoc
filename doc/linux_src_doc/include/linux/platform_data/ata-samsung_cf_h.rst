.. -*- coding: utf-8; mode: rst -*-

================
ata-samsung_cf.h
================


.. _`s3c_ide_platdata`:

struct s3c_ide_platdata
=======================

.. c:type:: s3c_ide_platdata

    S3C IDE driver platform data.


.. _`s3c_ide_platdata.definition`:

Definition
----------

.. code-block:: c

  struct s3c_ide_platdata {
    void (* setup_gpio) (void);
  };


.. _`s3c_ide_platdata.members`:

Members
-------

:``setup_gpio``:
    Setup the external GPIO pins to the right state for data
    transfer in true-ide mode.


