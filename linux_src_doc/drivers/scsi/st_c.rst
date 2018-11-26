.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/st.c

.. _`scsi_tape_release`:

scsi_tape_release
=================

.. c:function:: void scsi_tape_release(struct kref *kref)

    Called to free the Scsi_Tape structure

    :param kref:
        pointer to embedded kref
    :type kref: struct kref \*

.. _`scsi_tape_release.description`:

Description
-----------

st_ref_mutex must be held entering this routine.  Because it is
called on last put, you should always use the \ :c:func:`scsi_tape_get`\ 
\ :c:func:`scsi_tape_put`\  helpers which manipulate the semaphore directly
and never do a direct \ :c:func:`kref_put`\ .

.. _`read_cnt_show`:

read_cnt_show
=============

.. c:function:: ssize_t read_cnt_show(struct device *dev, struct device_attribute *attr, char *buf)

    return read count - count of reads made from tape drive

    :param dev:
        struct device
    :type dev: struct device \*

    :param attr:
        attribute structure
    :type attr: struct device_attribute \*

    :param buf:
        buffer to return formatted data in
    :type buf: char \*

.. _`read_byte_cnt_show`:

read_byte_cnt_show
==================

.. c:function:: ssize_t read_byte_cnt_show(struct device *dev, struct device_attribute *attr, char *buf)

    return read byte count - tape drives may use blocks less than 512 bytes this gives the raw byte count of of data read from the tape drive.

    :param dev:
        struct device
    :type dev: struct device \*

    :param attr:
        attribute structure
    :type attr: struct device_attribute \*

    :param buf:
        buffer to return formatted data in
    :type buf: char \*

.. _`read_ns_show`:

read_ns_show
============

.. c:function:: ssize_t read_ns_show(struct device *dev, struct device_attribute *attr, char *buf)

    return read ns - overall time spent waiting on reads in ns.

    :param dev:
        struct device
    :type dev: struct device \*

    :param attr:
        attribute structure
    :type attr: struct device_attribute \*

    :param buf:
        buffer to return formatted data in
    :type buf: char \*

.. _`write_cnt_show`:

write_cnt_show
==============

.. c:function:: ssize_t write_cnt_show(struct device *dev, struct device_attribute *attr, char *buf)

    write count - number of user calls to write(2) that have written data to tape.

    :param dev:
        struct device
    :type dev: struct device \*

    :param attr:
        attribute structure
    :type attr: struct device_attribute \*

    :param buf:
        buffer to return formatted data in
    :type buf: char \*

.. _`write_byte_cnt_show`:

write_byte_cnt_show
===================

.. c:function:: ssize_t write_byte_cnt_show(struct device *dev, struct device_attribute *attr, char *buf)

    write byte count - raw count of bytes written to tape.

    :param dev:
        struct device
    :type dev: struct device \*

    :param attr:
        attribute structure
    :type attr: struct device_attribute \*

    :param buf:
        buffer to return formatted data in
    :type buf: char \*

.. _`write_ns_show`:

write_ns_show
=============

.. c:function:: ssize_t write_ns_show(struct device *dev, struct device_attribute *attr, char *buf)

    write ns - number of nanoseconds waiting on write requests to complete.

    :param dev:
        struct device
    :type dev: struct device \*

    :param attr:
        attribute structure
    :type attr: struct device_attribute \*

    :param buf:
        buffer to return formatted data in
    :type buf: char \*

.. _`in_flight_show`:

in_flight_show
==============

.. c:function:: ssize_t in_flight_show(struct device *dev, struct device_attribute *attr, char *buf)

    number of I/Os currently in flight - in most cases this will be either 0 or 1. It may be higher if someone has also issued other SCSI commands such as via an ioctl.

    :param dev:
        struct device
    :type dev: struct device \*

    :param attr:
        attribute structure
    :type attr: struct device_attribute \*

    :param buf:
        buffer to return formatted data in
    :type buf: char \*

.. _`io_ns_show`:

io_ns_show
==========

.. c:function:: ssize_t io_ns_show(struct device *dev, struct device_attribute *attr, char *buf)

    io wait ns - this is the number of ns spent waiting on all I/O to complete. This includes tape movement commands such as rewinding, seeking to end of file or tape, it also includes read and write. To determine the time spent on tape movement subtract the read and write ns from this value.

    :param dev:
        struct device
    :type dev: struct device \*

    :param attr:
        attribute structure
    :type attr: struct device_attribute \*

    :param buf:
        buffer to return formatted data in
    :type buf: char \*

.. _`other_cnt_show`:

other_cnt_show
==============

.. c:function:: ssize_t other_cnt_show(struct device *dev, struct device_attribute *attr, char *buf)

    other io count - this is the number of I/O requests other than read and write requests. Typically these are tape movement requests but will include driver tape movement. This includes only requests issued by the st driver.

    :param dev:
        struct device
    :type dev: struct device \*

    :param attr:
        attribute structure
    :type attr: struct device_attribute \*

    :param buf:
        buffer to return formatted data in
    :type buf: char \*

.. _`resid_cnt_show`:

resid_cnt_show
==============

.. c:function:: ssize_t resid_cnt_show(struct device *dev, struct device_attribute *attr, char *buf)

    A count of the number of times we get a residual count - this should indicate someone issuing reads larger than the block size on tape.

    :param dev:
        struct device
    :type dev: struct device \*

    :param attr:
        attribute structure
    :type attr: struct device_attribute \*

    :param buf:
        buffer to return formatted data in
    :type buf: char \*

.. This file was automatic generated / don't edit.

