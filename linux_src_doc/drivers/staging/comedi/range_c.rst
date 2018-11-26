.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/range.c

.. _`comedi_check_chanlist`:

comedi_check_chanlist
=====================

.. c:function:: int comedi_check_chanlist(struct comedi_subdevice *s, int n, unsigned int *chanlist)

    Validate each element in a chanlist.

    :param s:
        comedi_subdevice struct
    :type s: struct comedi_subdevice \*

    :param n:
        number of elements in the chanlist
    :type n: int

    :param chanlist:
        the chanlist to validate
    :type chanlist: unsigned int \*

.. _`comedi_check_chanlist.description`:

Description
-----------

Each element consists of a channel number, a range index, an analog
reference type and some flags, all packed into an unsigned int.

This checks that the channel number and range index are supported by
the comedi subdevice.  It does not check whether the analog reference
type and the flags are supported.  Drivers that care should check those
themselves.

.. _`comedi_check_chanlist.return`:

Return
------

\ ``0``\  if all \ ``chanlist``\  elements are valid (success),
\ ``-EINVAL``\  if one or more elements are invalid.

.. This file was automatic generated / don't edit.

