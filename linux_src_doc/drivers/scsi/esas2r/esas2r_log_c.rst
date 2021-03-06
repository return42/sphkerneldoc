.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/esas2r/esas2r_log.c

.. _`translate_esas2r_event_level_to_kernel`:

translate_esas2r_event_level_to_kernel
======================================

.. c:function:: const char *translate_esas2r_event_level_to_kernel(const long level)

    defined logging event level to a kernel logging level.

    :param level:
        *undescribed*
    :type level: const long

.. _`translate_esas2r_event_level_to_kernel.description`:

Description
-----------

\ ``param``\  [in] level the esas2r-defined logging event level to translate

\ ``return``\  the corresponding kernel logging level.

.. _`esas2r_log_master`:

esas2r_log_master
=================

.. c:function:: int esas2r_log_master(const long level, const struct device *dev, const char *format, va_list args)

    outlined by the formatting string, the input device information and the substitution arguments and output the resulting string to the system log.

    :param level:
        *undescribed*
    :type level: const long

    :param dev:
        *undescribed*
    :type dev: const struct device \*

    :param format:
        *undescribed*
    :type format: const char \*

    :param args:
        *undescribed*
    :type args: va_list

.. _`esas2r_log_master.description`:

Description
-----------

\ ``param``\  [in] level  the event log level of the message
\ ``param``\  [in] dev    the device information
\ ``param``\  [in] format the formatting string for the message
\ ``param``\  [in] args   the substition arguments to the formatting string

\ ``return``\  0 on success, or -1 if an error occurred.

.. _`esas2r_log`:

esas2r_log
==========

.. c:function:: int esas2r_log(const long level, const char *format,  ...)

    :param level:
        *undescribed*
    :type level: const long

    :param format:
        *undescribed*
    :type format: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`esas2r_log.description`:

Description
-----------

\ ``param``\  [in] level  the event level of the message
\ ``param``\  [in] format the formating string for the message
\ ``param``\  [in] ...    the substitution arguments to the formatting string

\ ``return``\  0 on success, or -1 if an error occurred.

.. _`esas2r_log_dev`:

esas2r_log_dev
==============

.. c:function:: int esas2r_log_dev(const long level, const struct device *dev, const char *format,  ...)

    device information.

    :param level:
        *undescribed*
    :type level: const long

    :param dev:
        *undescribed*
    :type dev: const struct device \*

    :param format:
        *undescribed*
    :type format: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`esas2r_log_dev.description`:

Description
-----------

\ ``param``\  [in] level   the event level of the message
\ ``param``\  [in] dev     the device information
\ ``param``\  [in] format  the formatting string for the message
\ ``param``\  [in] ...     the substitution arguments to the formatting string

\ ``return``\  0 on success, or -1 if an error occurred.

.. _`esas2r_log_hexdump`:

esas2r_log_hexdump
==================

.. c:function:: int esas2r_log_hexdump(const long level, const void *buf, size_t len)

    device information.

    :param level:
        *undescribed*
    :type level: const long

    :param buf:
        *undescribed*
    :type buf: const void \*

    :param len:
        *undescribed*
    :type len: size_t

.. _`esas2r_log_hexdump.description`:

Description
-----------

\ ``param``\  [in] level   the event level of the message
\ ``param``\  [in] buf
\ ``param``\  [in] len

\ ``return``\  0 on success, or -1 if an error occurred.

.. This file was automatic generated / don't edit.

