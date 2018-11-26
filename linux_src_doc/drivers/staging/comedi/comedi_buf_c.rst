.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/comedi_buf.c

.. _`comedi_buf_write_alloc`:

comedi_buf_write_alloc
======================

.. c:function:: unsigned int comedi_buf_write_alloc(struct comedi_subdevice *s, unsigned int nbytes)

    Reserve buffer space for writing

    :param s:
        COMEDI subdevice.
    :type s: struct comedi_subdevice \*

    :param nbytes:
        Maximum space to reserve in bytes.
    :type nbytes: unsigned int

.. _`comedi_buf_write_alloc.description`:

Description
-----------

Reserve up to \ ``nbytes``\  bytes of space to be written in the COMEDI acquisition
data buffer associated with the subdevice.  The amount reserved is limited
by the space available.

.. _`comedi_buf_write_alloc.return`:

Return
------

The amount of space reserved in bytes.

.. _`comedi_buf_write_free`:

comedi_buf_write_free
=====================

.. c:function:: unsigned int comedi_buf_write_free(struct comedi_subdevice *s, unsigned int nbytes)

    Free buffer space after it is written

    :param s:
        COMEDI subdevice.
    :type s: struct comedi_subdevice \*

    :param nbytes:
        Maximum space to free in bytes.
    :type nbytes: unsigned int

.. _`comedi_buf_write_free.description`:

Description
-----------

Free up to \ ``nbytes``\  bytes of space previously reserved for writing in the
COMEDI acquisition data buffer associated with the subdevice.  The amount of
space freed is limited to the amount that was reserved.  The freed space is
assumed to have been filled with sample data by the writer.

If the samples in the freed space need to be "munged", do so here.  The
freed space becomes available for allocation by the reader.

.. _`comedi_buf_write_free.return`:

Return
------

The amount of space freed in bytes.

.. _`comedi_buf_read_n_available`:

comedi_buf_read_n_available
===========================

.. c:function:: unsigned int comedi_buf_read_n_available(struct comedi_subdevice *s)

    Determine amount of readable buffer space

    :param s:
        COMEDI subdevice.
    :type s: struct comedi_subdevice \*

.. _`comedi_buf_read_n_available.description`:

Description
-----------

Determine the amount of readable buffer space in the COMEDI acquisition data
buffer associated with the subdevice.  The readable buffer space is that
which has been freed by the writer and "munged" to the sample data format
expected by COMEDI if necessary.

.. _`comedi_buf_read_n_available.return`:

Return
------

The amount of readable buffer space.

.. _`comedi_buf_read_alloc`:

comedi_buf_read_alloc
=====================

.. c:function:: unsigned int comedi_buf_read_alloc(struct comedi_subdevice *s, unsigned int nbytes)

    Reserve buffer space for reading

    :param s:
        COMEDI subdevice.
    :type s: struct comedi_subdevice \*

    :param nbytes:
        Maximum space to reserve in bytes.
    :type nbytes: unsigned int

.. _`comedi_buf_read_alloc.description`:

Description
-----------

Reserve up to \ ``nbytes``\  bytes of previously written and "munged" buffer space
for reading in the COMEDI acquisition data buffer associated with the
subdevice.  The amount reserved is limited to the space available.  The
reader can read from the reserved space and then free it.  A reader is also
allowed to read from the space before reserving it as long as it determines
the amount of readable data available, but the space needs to be marked as
reserved before it can be freed.

.. _`comedi_buf_read_alloc.return`:

Return
------

The amount of space reserved in bytes.

.. _`comedi_buf_read_free`:

comedi_buf_read_free
====================

.. c:function:: unsigned int comedi_buf_read_free(struct comedi_subdevice *s, unsigned int nbytes)

    Free buffer space after it has been read

    :param s:
        COMEDI subdevice.
    :type s: struct comedi_subdevice \*

    :param nbytes:
        Maximum space to free in bytes.
    :type nbytes: unsigned int

.. _`comedi_buf_read_free.description`:

Description
-----------

Free up to \ ``nbytes``\  bytes of buffer space previously reserved for reading in
the COMEDI acquisition data buffer associated with the subdevice.  The
amount of space freed is limited to the amount that was reserved.

The freed space becomes available for allocation by the writer.

.. _`comedi_buf_read_free.return`:

Return
------

The amount of space freed in bytes.

.. _`comedi_buf_write_samples`:

comedi_buf_write_samples
========================

.. c:function:: unsigned int comedi_buf_write_samples(struct comedi_subdevice *s, const void *data, unsigned int nsamples)

    Write sample data to COMEDI buffer

    :param s:
        COMEDI subdevice.
    :type s: struct comedi_subdevice \*

    :param data:
        Pointer to source samples.
    :type data: const void \*

    :param nsamples:
        Number of samples to write.
    :type nsamples: unsigned int

.. _`comedi_buf_write_samples.description`:

Description
-----------

Write up to \ ``nsamples``\  samples to the COMEDI acquisition data buffer
associated with the subdevice, mark it as written and update the
acquisition scan progress.  If there is not enough room for the specified
number of samples, the number of samples written is limited to the number
that will fit and the \ ``COMEDI_CB_OVERFLOW``\  event flag is set to cause the
acquisition to terminate with an overrun error.  Set the \ ``COMEDI_CB_BLOCK``\ 
event flag if any samples are written to cause waiting tasks to be woken
when the event flags are processed.

.. _`comedi_buf_write_samples.return`:

Return
------

The amount of data written in bytes.

.. _`comedi_buf_read_samples`:

comedi_buf_read_samples
=======================

.. c:function:: unsigned int comedi_buf_read_samples(struct comedi_subdevice *s, void *data, unsigned int nsamples)

    Read sample data from COMEDI buffer

    :param s:
        COMEDI subdevice.
    :type s: struct comedi_subdevice \*

    :param data:
        Pointer to destination.
    :type data: void \*

    :param nsamples:
        Maximum number of samples to read.
    :type nsamples: unsigned int

.. _`comedi_buf_read_samples.description`:

Description
-----------

Read up to \ ``nsamples``\  samples from the COMEDI acquisition data buffer
associated with the subdevice, mark it as read and update the acquisition
scan progress.  Limit the number of samples read to the number available.
Set the \ ``COMEDI_CB_BLOCK``\  event flag if any samples are read to cause waiting
tasks to be woken when the event flags are processed.

.. _`comedi_buf_read_samples.return`:

Return
------

The amount of data read in bytes.

.. This file was automatic generated / don't edit.

