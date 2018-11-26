.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/bitfield.h

.. _`field_fit`:

FIELD_FIT
=========

.. c:function::  FIELD_FIT( _mask,  _val)

    check if value fits in the field

    :param _mask:
        shifted mask defining the field's length and position
    :type _mask: 

    :param _val:
        value to test against the field
    :type _val: 

.. _`field_fit.return`:

Return
------

true if \ ``_val``\  can fit inside \ ``_mask``\ , false if \ ``_val``\  is too big.

.. _`field_prep`:

FIELD_PREP
==========

.. c:function::  FIELD_PREP( _mask,  _val)

    prepare a bitfield element

    :param _mask:
        shifted mask defining the field's length and position
    :type _mask: 

    :param _val:
        value to put in the field
    :type _val: 

.. _`field_prep.description`:

Description
-----------

\ :c:func:`FIELD_PREP`\  masks and shifts up the value.  The result should
be combined with other fields of the bitfield using logical OR.

.. _`field_get`:

FIELD_GET
=========

.. c:function::  FIELD_GET( _mask,  _reg)

    extract a bitfield element

    :param _mask:
        shifted mask defining the field's length and position
    :type _mask: 

    :param _reg:
        value of entire bitfield
    :type _reg: 

.. _`field_get.description`:

Description
-----------

\ :c:func:`FIELD_GET`\  extracts the field specified by \ ``_mask``\  from the
bitfield passed in as \ ``_reg``\  by masking and shifting it down.

.. This file was automatic generated / don't edit.

