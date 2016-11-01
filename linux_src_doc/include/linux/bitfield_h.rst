.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/bitfield.h

.. _`field_prep`:

FIELD_PREP
==========

.. c:function::  FIELD_PREP( _mask,  _val)

    prepare a bitfield element

    :param  _mask:
        shifted mask defining the field's length and position

    :param  _val:
        value to put in the field

.. _`field_prep.description`:

Description
-----------

FIELD_PREP() masks and shifts up the value.  The result should
be combined with other fields of the bitfield using logical OR.

.. _`field_get`:

FIELD_GET
=========

.. c:function::  FIELD_GET( _mask,  _reg)

    extract a bitfield element

    :param  _mask:
        shifted mask defining the field's length and position

    :param  _reg:
        32bit value of entire bitfield

.. _`field_get.description`:

Description
-----------

FIELD_GET() extracts the field specified by \ ``_mask``\  from the
bitfield passed in as \ ``_reg``\  by masking and shifting it down.

.. This file was automatic generated / don't edit.

